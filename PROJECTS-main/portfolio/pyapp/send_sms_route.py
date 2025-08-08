from flask import render_template, request
import pywhatkit as pwk

def send_sms_route():
    phone_number = request.form['phone']
    message = request.form['message']
    
    try:
        # Assuming pwk is a module for sending WhatsApp messages
        pwk.sendwhatmsg_instantly(phone_number, message)
        return render_template('success.html')
    except Exception as e:
        print(f"Failed to send SMS: {e}")
        return f"Failed to send SMS: {e}"