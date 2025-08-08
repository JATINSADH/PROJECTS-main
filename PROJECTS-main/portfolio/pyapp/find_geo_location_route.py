from flask import render_template,flash 
import geocoder

def find_geo_location_route():
    try:
        g = geocoder.ip('me')
        location_info = f"Your current location: {g.city}, {g.state}, {g.country}. Coordinates: {g.latlng}"
        return render_template('find_geo_location_success.html', location_info=location_info)
    except Exception as e:
        flash(f"Failed to get geo coordinates: {e}")
        return render_template('index1.html')