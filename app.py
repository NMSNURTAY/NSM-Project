from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Получение случайных данных
    stats = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    employees = requests.get('https://jsonplaceholder.typicode.com/users').json()
    profile = requests.get('https://jsonplaceholder.typicode.com/users/1').json()
    return render_template('index.html', stats=stats, employees=employees, profile=profile)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

