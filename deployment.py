import pickle
import warnings
warnings.simplefilter("ignore")

from flask import Flask, request, jsonify


def load_model(location):
    """Loads the pickled model"""
    with open(location, "rb") as file_in:
        model = pickle.load(file_in)
        # print("Model loaded sucessfully...")
        return model

app = Flask("California_model")

@app.route("/predict", methods=["POST"])
def predict():
    # Requests get the data being sent to our API
    data = request.get_json()

    # Location to the assets (pickled model and processing function)
    location = "./assets/test_logit.pkl"
    #vect = load_model("./vectorizer.bin")

    # Loads the model and preprocessing function
    model = load_model(location)
    #data = vect.transform(data)

    # Extracts the data in the json {"data": [1, 3, ...]} sent to our api
    data = data["data"]

    # Model prediction
    avg_price = model.predict(data)

    # checks if data sent to the model is one sample or more and converts to
    # python format easily understandable by flask (the result returned by the
    # model are usually numpy arrays)
    if len(data) == 1:
        result = {
            "result": float(avg_price)
            }
    else:
        result = {
            "result": list(avg_price)
        }
    # print(f"The prediction of the data is {result}")
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1200)
