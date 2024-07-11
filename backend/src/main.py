from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello World!"

# calculating some numbers to then deploy to backend
def perform_calculation():
    # Example calculation: sum of first 10 natural numbers
    result = sum(range(1, 4))
    return result

@app.route('/calculate')
def calculate():
    result = perform_calculation()
    return str(result)


if __name__ == '__main__':
    app.run()