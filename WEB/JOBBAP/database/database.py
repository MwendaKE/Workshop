import psycopg2
import os, sys

sys.path.append('..')

def connect_db():
    return psycopg2.connect(
        dbname='job_applications',
        user=os.getenv('USER'),
        password='',
        host='localhost',
        port='5432'
    )

def init_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id SERIAL PRIMARY KEY,
            full_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            position TEXT NOT NULL,
            experience TEXT NOT NULL,
            submitted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_application(data):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO applications (full_name, phone, email, position, experience)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['full_name'], data['phone'], data['email'], data['position'], data['experience']))
    conn.commit()
    conn.close()
    
def get_all_applications():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM applications ORDER BY submitted_date DESC")
    
    applications = []
    for row in cur.fetchall():
        applications.append({
            'id': row[0],
            'full_name': row[1],
            'phone': row[2],
            'email': row[3],
            'position': row[4],
            'experience': row[5],
            'submitted_date': row[6].isoformat() if row[6] else None
        })
    
    conn.close()
    return applications