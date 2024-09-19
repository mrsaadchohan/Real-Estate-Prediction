import os
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

def get_estimated_price(location, sqft, bhk, bath):
    
        # Debugging to check the function input
        # print(f"Inputs - location: {location}, sqft: {sqft}, bhk: {bhk}, bath: {bath}")

        # Checking if location exists in the data columns
        loc_index = __data_columns.index(location.lower()) if location.lower() in __data_columns else -1

        # Debugging location index
        # print(f"Location Index: {loc_index}")

        # Create input array for prediction
        x = np.zeros(len(__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk

        # Set location one-hot encoding
        if loc_index >= 0:
            x[loc_index] = 1

        # Debugging input array
        print(f"Input Array for Prediction: {x}")

        # Make the prediction
        predicted_price = __model.predict([x])[0]
        return round(predicted_price, 2)

    

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    # global __model

    # Get the current directory where the script is located
    script_dir = os.path.dirname(__file__)

    # Load columns.json file
    columns_path = os.path.join(script_dir, "artifacts", "columns.json")
    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    # Load Real-Estate.pickle file
    model_path = os.path.join(script_dir, "artifacts", "Real-Estate.pickle")
    with open(model_path, 'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts done...")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location

