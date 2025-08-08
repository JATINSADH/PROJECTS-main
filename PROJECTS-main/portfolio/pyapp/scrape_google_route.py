from flask import render_template, request
from bs4 import BeautifulSoup
import requests

def scrape_google_route():  
    query = request.form['query']  
    try:  
        url = f"https://www.google.com/search?q={query}"  
        headers = {"User-Agent": "Mozilla/5.0"}  
        response = requests.get(url, headers=headers)  
        soup = BeautifulSoup(response.text, 'html.parser')  

        results = soup.find_all('h3', limit=5)  
        results_list = [result.text for result in results]  

        return render_template('scrape_google_success.html', results=results_list)  

    except Exception as e:  
        print(f"Failed to scrape Google search results: {e}")  
        return "An error occurred while scraping." 