from flask import render_template, request, redirect, flash, url_for
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL, CoInitialize
from ctypes import cast, POINTER

def control_volume_route():
    try:
        # Initialize COM library
        CoInitialize()

        # Get the volume level from the form
        volume_level = int(request.form['volume'])
        print(f"Volume level received: {volume_level}")  # Debugging line
        
        if 0 <= volume_level <= 100:
            # Get audio devices
            devices = AudioUtilities.GetSpeakers()
            print("Devices:", devices)  # Debugging line

            # Activate volume interface
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            print("Volume interface:", volume)  # Debugging line

            # Get the current volume level
            current_volume = volume.GetMasterVolumeLevelScalar()
            print(f"Current system volume: {current_volume * 100}%")  # Convert scalar to percentage

            # Set the new volume
            level_normalized = volume_level / 100.0
            volume.SetMasterVolumeLevelScalar(level_normalized, None)

            # Verify the new volume
            new_volume = volume.GetMasterVolumeLevelScalar()
            print(f"New system volume: {new_volume * 100}%")  # Convert scalar to percentage

            flash(f"Volume successfully set to {volume_level}%.")
            return render_template('success.html', volume_level=volume_level)
        else:
            flash("Volume must be between 0 and 100.")
    except ValueError:
        flash("Invalid input. Please enter a number between 0 and 100.")
    except Exception as e:
        print(f"Error: {e}")  # Debugging line
        flash(f"Error: {e}")

    return redirect(url_for('index1'))
