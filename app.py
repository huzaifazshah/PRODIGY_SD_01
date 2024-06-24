from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_temperature():
    data = request.json
    temperature = float(data['temperature'])
    unit = data['unit'].upper()

    result = {}
    if unit == 'C':
        result['fahrenheit'] = celsius_to_fahrenheit(temperature)
        result['kelvin'] = celsius_to_kelvin(temperature)
    elif unit == 'F':
        result['celsius'] = fahrenheit_to_celsius(temperature)
        result['kelvin'] = fahrenheit_to_kelvin(temperature)
    elif unit == 'K':
        result['celsius'] = kelvin_to_celsius(temperature)
        result['fahrenheit'] = kelvin_to_fahrenheit(temperature)
    else:
        return jsonify({"error": "Invalid unit of measurement"}), 400

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True,port =5000)
