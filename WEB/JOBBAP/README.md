# Job Application Web App

A simple and efficient web application for collecting job applications within a local community. Built with Python Flask backend and vanilla JavaScript frontend, storing data in PostgreSQL.

## 🚀 Features

- **Simple Form**: Clean 5-field application form with real-time validation
- **Position Dropdown**: Pre-defined job positions (Manager, Supervisor, Teller, etc.)
- **Input Validation**: Email format checking, phone number validation, required field checking
- **Visual Feedback**: Green/red borders indicating field validity
- **Admin Dashboard**: View all submitted applications in a clean interface
- **PostgreSQL Storage**: All data securely stored in database
- **Network Accessible**: Can be accessed from any device on the same network

## 📋 Application Fields

1. **Full Name** - Text input
2. **Phone Number** - Validated 10-digit minimum
3. **Email Address** - Format validation
4. **Position** - Dropdown selection:
   - Manager
   - Ass. Manager  
   - Supervisor
   - Teller
   - Attendants
   - Cleaner
   - Gate Man
5. **Work Experience** - Textarea for experience details

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Validation**: Client-side + server-side validation
- **Hosting**: Termux (Android) or any Python environment

## 🌐 Access Points

- **Application Form**: `http://your-ip:5000/`
- **Admin Dashboard**: `http://your-ip:5000/admin`

## 💾 Database Schema

```sql
applications (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    position TEXT NOT NULL,
    experience TEXT NOT NULL,
    submitted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)