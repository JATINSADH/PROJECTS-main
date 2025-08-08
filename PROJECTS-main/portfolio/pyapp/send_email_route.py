from flask import request
import smtplib

def send_email_route():  
    to_email = request.form['email']  # This should now match the name in your HTML  
    subject = request.form['subject']  
    message = request.form['message']  

    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        from_email = "ajaysadh15@gmail.com"  # replace with your email
        password = "vhmqakiobcgxbzhu"         # replace with your app-specific password

        # Create the email message
        email_message = f'Subject: {subject}\n\n{message}'

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, email_message)
            
        return True, None
    except Exception as e:
        return False, str(e)
    #     return render_template('success.html')
    # except Exception as e:
    #     return f"Failed to send email: {e}"