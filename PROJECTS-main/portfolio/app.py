from flask import Flask, render_template, request, redirect, flash, url_for,send_from_directory 
from pyapp.send_email_route import send_email_route
from pyapp.scrape_google_route import scrape_google_route
from pyapp.text_to_speech_route import text_to_speech_route
from pyapp.control_volume_route import control_volume_route
from pyapp.find_geo_location_route import find_geo_location_route
from pyapp.send_bulk_email_route import send_bulk_email_route
from pyapp.send_sms_route import send_sms_route
from pyapp.resume import download_resume


import os
from dotenv import load_dotenv

load_dotenv()  # .env file load karega

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

app = Flask(__name__)  
app.secret_key = 'e4ddd3b2a340fab8d742043d7716495c'  # Required for flash messages  

# Function to send an email  
@app.route('/', methods=['GET'])  
def index():  
    return render_template('index.html')

@app.route('/index1', methods=['GET'])  
def index1():  
    return render_template('index1.html')

@app.route('/index2', methods=['GET'])
def index2():
    return render_template('index2.html')

@app.route('/send_email', methods=['GET'])  
def send_email_page():  
    return render_template('send_email.html') 

@app.route('/send_email', methods=['POST'])
def send_email():
    success, error = send_email_route()
    if success:
        return render_template('success.html')
    else:
        return f"Failed to send email: {error}"

@app.route('/scrape_google', methods=['GET'])  
def scrape_google_page():  
    return render_template('scrape_google.html')

@app.route('/scrape_google', methods=['POST'])  
def scrape_google():  # Name the function differently to avoid conflicts with the import
    return scrape_google_route()  # Call the imported scrape_google function   
    

@app.route('/text_to_speech', methods=['GET'])  
def text_to_speech_page():  
    return render_template('text_to_speech.html')

@app.route('/text_to_speech', methods=['POST'])  
def text_to_speech():
    return text_to_speech_route()


@app.route('/control_volume', methods=['GET'])  
def control_volume_page():  
    return render_template('control_volume.html')

@app.route('/control_volume', methods=['POST'])
def control_volume():
    return control_volume_route()


@app.route('/find_geo_location', methods=['GET'])  
def find_geo_location_page():  
    return render_template('find_geo_location.html')

@app.route('/find_geo_location', methods=['POST'])
def find_geo_location():
    return find_geo_location_route()
    
    
@app.route('/send_bulk_email', methods=['GET'])  
def send_bulk_email_page():  
    return render_template('send_bulk_email.html')

@app.route('/send_bulk_email', methods=['POST']) 
def send_bulk_email(): 
    return send_bulk_email_route()

    
@app.route('/send_sms', methods=['GET'])  
def send_sms_page():  
    return render_template('send_sms.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    return send_sms_route()

@app.route('/send_sms_from_mobile', methods=['GET'])  
def send_sms_from_mobile_page():  
    return render_template('send_sms_from_mobile.html')


# Route to serve the resume file
@app.route('/download_resume',methods=['GET'])
def resume():
    return download_resume()

@app.route('/ML', methods=['GET'])
def ML():
    return "<h1>Coming Soon</h1>"


# contact section submit function
import smtplib
from email.mime.text import MIMEText

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('full_name')
    email = request.form.get('email')
    mobile = request.form.get('mobile_number')
    subject = request.form.get('email_subject')
    message = request.form.get('message')

    # Email content
    body = f"Name: {name}\nEmail: {email}\nMobile: {mobile}\nSubject: {subject}\nMessage: {message}"
    msg = MIMEText(body)
    msg['Subject'] = "New Contact Form Submission"
    msg['From'] = "yourgmail@gmail.com"
    msg['To'] = "ajaysadh15@gmail.com"  # Apna email yahan likhein

    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("ajaysadh15@gmail.com", "vhmqakiobcgxbzhu")  # Gmail app password use karein
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        server.quit()
        return render_template('thankyou.html', name=name)
    except Exception as e:
        return f"<h2>Sorry, there was an error: {e}</h2>"
    
if __name__ == '__main__':  
    app.run(debug=True, port=5000)