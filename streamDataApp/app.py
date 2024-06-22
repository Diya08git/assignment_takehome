from flask import Flask, request,jsonify
from data_stream import DataStream
from fuel_station import FuelStation

app = Flask(__name__)
data_stream = DataStream()
fuel_station = FuelStation(diesel=2, petrol=2, electric=2)

@app.route('/stream', methods=['POST'])
def stream():
    data = request.get_json()
    timestamp = data.get('timestamp')
    data_str = data.get('data_str')
    result = data_stream.output_data_str(timestamp, data_str)
    return jsonify({"output":result})

@app.route('/fuel_vehicle', methods=['POST'])
def fuel_vehicle():
    data = request.get_json()
    fuel_type = data.get('fuel_type')
    result = fuel_station.fuel_vehicle(fuel_type)
    return jsonify({"success":result})

@app.route('/open_fuel_slot', methods=['POST'])
def open_fuel_slot():
    data = request.get_json()
    fuel_type = data.get('fuel_type')
    result = fuel_station.open_fuel_slot(fuel_type)
    return jsonify({"success":result})

if __name__ == '__main__':
    app.run(debug=True)
