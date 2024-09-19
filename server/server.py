from flask import Flask, request, jsonify
import util
from flask_cors import CORS  # Import CORS

app=Flask(__name__)
CORS(app)
@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Debugging to check the incoming request content type
        print("Request Content-Type:", request.content_type)

        # Checking if the request contains JSON data
        if request.is_json:
            data = request.get_json()  # Parse JSON data
            print("Received Data:", data)  # Debugging to print the received JSON

            # Extract required fields
            total_sqft = float(data['total_sqft'])
            location = data['location']
            bhk = int(data['bhk'])
            bath = int(data['bath'])

            # Perform prediction
            response = jsonify({
                'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
            })
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            return jsonify({"error": "Expected JSON data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()