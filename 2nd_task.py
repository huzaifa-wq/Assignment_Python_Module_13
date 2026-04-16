from flask import Flask, Response
import json

app = Flask(__name__)

airport_db = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Location": "London"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Location": "New York"},
    "OMDB": {"Name": "Dubai International Airport", "Location": "Dubai"}
}

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    icao = icao.upper()
    airport_info = airport_db.get(icao)

    if airport_info:
        result = {
            "ICAO": icao,
            "Name": airport_info["Name"],
            "Location": airport_info["Location"]
        }
    else:
        result = {
            "ICAO": icao,
            "Error": "Airport not found"
        }

    return Response(json.dumps(result), mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
