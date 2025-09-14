from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from modules.models import db, Memoir, Audio, Picture, Video
from datetime import datetime
from sqlalchemy.orm import session

from werkzeug.utils import secure_filename


import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ememoira.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'


db.init_app(app)


@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        
        
def make_directory_if_not_exists(dir_path):
    nomedia_file = os.path.join(dir_path, ".nomedia") # Hidden .nomedia file. This prevents file from showing in the android gallery
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        
        with open(nomedia_file, "w") as f:
            pass # This will create empty .nomedia file
                 # Files in the respective folders will not show in gallery
                 # Android will skip scanning files when it encounters that file


def save_files(files, dir):
    upload_dir = os.path.join(app.config['UPLOAD_FOLDER'], dir)
    make_directory_if_not_exists(upload_dir)
    saved_files = []
    
    for file in files:
        filename = secure_filename(file.filename)
        
        if filename:
            filepath = os.path.join(upload_dir, filename)
            file.save(filepath)
            saved_files.append(filepath)
            
    return saved_files


@app.route("/")
def home():
    memoirs = Memoir.query.order_by(Memoir.date_of_reference.desc()).all()
    return render_template("ememoira.html", memoirs=memoirs)


@app.route("/memoirs/<int:memoirid>")
def view_memoir(memoirid):
    return render_template("ememoira_entry.html", memoirid=memoirid)


@app.route("/memoirs/add", methods=["GET","POST"])  
def add_memoir():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        date_of_reference = format_and_clean_date_for_server_input(request.form["refdate"])
        
        new_memoir = Memoir(title=title, body=body, date_of_reference=date_of_reference)
        
        # Save the memoir so that we can get its id
        # The id will help in creating a directory where files will be saved
        # Files will be saved in the respective entry with folder name being its ID
        db.session.add(new_memoir)
        db.session.commit()
        
        memoir_folder = f".Media {str(new_memoir.id).zfill(6)}"
        
        # Get files the user has uploaded
        audios = request.files.getlist("audio")
        pictures = request.files.getlist("picture")
        videos = request.files.getlist("video")
        
        # Save files in the folder named after the memoir id
        aud_files = save_files(audios, os.path.join(memoir_folder, "audios"))
        pic_files = save_files(pictures, os.path.join(memoir_folder, "pictures"))
        vid_files = save_files(videos, os.path.join(memoir_folder, "videos"))
        
        # Link the files in the database
        for fpath in aud_files:
            new_aud = Audio(filepath=fpath, memoir=new_memoir)
            db.session.add(new_aud)
            
        for fpath in pic_files:
            new_pic = Picture(filepath=fpath, memoir=new_memoir)
            db.session.add(new_pic)
            
        for fpath in vid_files:
            new_vid = Video(filepath=fpath, memoir=new_memoir)
            db.session.add(new_vid)
            
        db.session.add(new_memoir)
        db.session.commit()
        
        return redirect(url_for("home"))
        
    return render_template("ememoira_entry_add.html")


@app.route("/memoirs/<int:memoirid>/edit", methods=["GET", "POST"])
def edit_memoir(memoirid):
    memoir = Memoir.query.get_or_404(memoirid)
    
    refdate = format_and_clean_date_for_client_output(memoir.date_of_reference)
    
    audios = [{"id": audio.id, "filename": os.path.basename(audio.filepath)} for audio in memoir.audios]
    pictures = [{"id": picture.id, "filename": os.path.basename(picture.filepath)} for picture in memoir.pictures]
    videos = [{"id": video.id, "filename": os.path.basename(video.filepath)} for video in memoir.videos]
    
    if request.method == "POST":
        memoir.title = request.form['title']
        memoir.body = request.form['body']
        memoir.description = (memoir.body[:195] + "...") if len(memoir.body) > 100 else memoir.body
        memoir.date_of_reference = format_and_clean_date_for_server_input(request.form['refdate'])
        
        #-----
        # Handle File updates
        memoir_folder = f".Media {str(memoir.id).zfill(6)}"
        
        # Get files the user has uploaded
        audios = request.files.getlist("audio")
        pictures = request.files.getlist("picture")
        videos = request.files.getlist("video")
   
        # Save files in the respective folders named after the memoir id
        aud_files = save_files(audios, os.path.join(memoir_folder, "audios"))
        pic_files = save_files(pictures, os.path.join(memoir_folder, "pictures"))
        vid_files = save_files(videos, os.path.join(memoir_folder, "videos"))
       
        # Link new files to the database
        for fpath in aud_files:
            new_aud = Audio(filepath=fpath, memoir=memoir)
            db.session.add(new_aud)
            
        for fpath in pic_files:
            new_pic = Picture(filepath=fpath, memoir=memoir)
            db.session.add(new_pic)
            
        for fpath in vid_files:
            new_vid = Video(filepath=fpath, memoir=memoir)
            db.session.add(new_vid)
            
        #-----
        # Handle old files (delete them). Check whether the user has selected files to delete.
        # If so, get the files to be deleted from the user. These will be the audio ids
        # as stored in the database.
        old_audios_to_delete = request.form.getlist("delete-audio")
        old_pictures_to_delete = request.form.getlist("delete-picture")
        old_videos_to_delete = request.form.getlist("delete-video")
        
        # Delete old audios
        for audio_id in old_audios_to_delete:
            audio = Audio.query.get(audio_id)
            delete_file(audio.filepath)
            db.session.delete(audio)
            
        # Delete old picture
        for picture_id in old_pictures_to_delete:
            picture = Picture.query.get(picture_id)
            delete_file(picture.filepath)
            db.session.delete(picture)
               
        # Delete old videos
        for video_id in old_videos_to_delete:
            video = Video.query.get(video_id)
            delete_file(video.filepath)
            db.session.delete(video) 
        #----
       
        # Commit the changes to the database
        db.session.commit()
        
        return redirect(url_for('view_memoir', memoirid=memoirid))
        
    return render_template("ememoira_entry_edit.html", memoir=memoir, date=refdate, audios=audios, pictures=pictures, videos=videos)


@app.route('/memoirs/<int:memoir_id>/delete', methods=['DELETE'])
def delete_memoir(memoir_id):
    try:
        memoir = Memoir.query.get_or_404(memoir_id)
        memoir_folder = os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER'], f".Media {str(memoir.id).zfill(6)}")
        
        print(memoir_folder)
        
        db.session.delete(memoir)
        db.session.commit()
        
        if os.path.exists(memoir_folder):
            try:
                os.removedirs(memoir_folder) # Does not work because directory is not empty. See on how to remove a non empty dir.
                
            except Exception as error:
                print(" Error Removing file: " + str(error))
                pass
                
        return jsonify({"message": "Memoir deleted successfully"}), 200
    
    except Exception as e:
        return jsonify({"message": "Error deleting memoir"}), 500


@app.route("/api/memoirs", methods=["GET"])
def get_memoires():
    memoirs = Memoir.query.order_by(Memoir.date_of_reference.desc()).all()
    memoirs_data = [{
            "id": memoir.id,
            "title": memoir.title,
            "body": memoir.description,
            "date_created": memoir.date_created.strftime("%Y-%m-%d"),
            "date_of_reference": memoir.date_of_reference.strftime("%Y-%m-%d")
    } for memoir in memoirs]
    
    return jsonify(memoirs_data)


@app.route("/api/memoirs/<int:memoirid>", methods=["GET"])
def get_memoir(memoirid):
    memoir = Memoir.query.get(memoirid)
    
    if memoir:
        memoir_data = {
            "id": memoir.id,
            "title": memoir.title,
            "body": memoir.body,
            "date_created": memoir.date_created.strftime("%A, %d %B %Y, %I:%M%p"),
            "date_of_reference": memoir.date_of_reference.strftime("%A, %d %B, %Y"),
            "audios": [aud.filepath for aud in memoir.audios],
            "pictures": [pic.filepath for pic in memoir.pictures],
            "videos": [vid.filepath for vid in memoir.videos]
        }
        
    else:
        memoir_data = {"error": "Data for the requested Memoir is not found"}
    
    return jsonify(memoir_data)


def format_and_clean_date_for_server_input(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    return date


def format_and_clean_date_for_client_output(date):
    date = date.strftime("%Y-%m-%d")
    return date



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
