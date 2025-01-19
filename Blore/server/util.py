import pickle
import json
import numpy as np

locations = None
data_cols = None
model = None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global data_cols
    global locations

    with open(r".\server\artifacts\columns.json", "r") as f:
        data_cols = json.load(f)['data_columns']
        locations = data_cols[3:]  # first 3 columns are sqft, bath, bhk

    global model
    if model is None:
        with open(r"server\artifacts\banglore_home_prices_pred.pickle", 'rb') as f:
            model = pickle.load(f) #loading the model
    print("loading saved artifacts...done")

def get_estimated_price(location,sqft,bath,bhk):
    try:
        loc_index = data_cols.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_cols))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(model.predict([x])[0],2)

def get_location_names():
    print("locations: ")
    return locations

def get_data_columns():
    print("\ncols \n")
    return data_cols

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    print(get_location_names())
    print(f"predicted price: {get_estimated_price('1st Phase JP Nagar',1000, 3, 3)}")