from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search_attractions():
    # Print a message to indicate the microservice is listening
    print("Microservice is listening...")

    # Get the location from the request payload
    location = request.json.get('location')

    # Make the request to the BookingCOM API
    url = "https://booking-com15.p.rapidapi.com/api/v1/attraction/searchLocation"
    querystring = {"query": location, "languagecode": "en-us"}
    headers = {
        "X-RapidAPI-Key": "f7c41bb0f7mshd4a73c764d26d56p1f372bjsna43950002797",
        "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    # Return the response from the BookingCOM API
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)
