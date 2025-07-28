from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    error = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = os.environ.get("OPENWEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return render_template('index.html', weather=response.json())
            else:
                error = "City not found. Try again!"
        except:
            error = "Connection error. Try later!"
    return render_template('index.html', error=error)

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    app.run(debug=True)