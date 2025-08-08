from flask import request, redirect, flash, url_for  
import pyttsx3

def text_to_speech_route():  
    try:  
        text = request.form['text']  
        if not text.strip():  
            flash("Please enter some text to convert to speech.")  
            return redirect(url_for('index1'))  

        # Initialize the text-to-speech engine  
        engine = pyttsx3.init()  
        engine.say(text)  
        engine.runAndWait()  

        flash("Successfully converted text to speech!")  
        return redirect(url_for('text_to_speech'))  # Redirect back to the same page  

    except Exception as e:  
        flash(f"Failed to convert text to speech: {e}")  
        return redirect(url_for('index1'))