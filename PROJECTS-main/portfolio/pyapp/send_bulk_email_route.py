from flask import render_template, request 
import smtplib

def send_bulk_email_route():  
    email_addresses = request.form['email_addresses']  # This should now match the name in your HTML  
    email_subject = request.form['email_subject']  
    email_message = request.form['email_message']  

    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        from_email = "ajaysadh15@gmail.com"  # replace with your email
        password = "vhmqakiobcgxbzhu"         # replace with your app-specific password

        # Create the email message
        email_message = f'Subject: {email_subject}\n\n{email_message}'

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, password)
            email_list = email_addresses.split(',')
            server.sendmail(from_email, email_list, email_message)


        return render_template('success.html')
    except Exception as e:
        return f"Failed to send email: {e}"
