from flask import send_from_directory

def download_resume():
    # Path to the directory containing the resume file
    directory = 'static/resume'  # Adjust if needed
    filename = 'RESUME_JATIN.pdf'
    return send_from_directory(directory, filename, as_attachment=True)