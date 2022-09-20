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
    data = request.get_json()
    location = "./assets/test_logit.pkl"
    #vect = load_model("./vectorizer.bin")
    model = load_model(location)
    #data = vect.transform(data)
    data = data["data"]
    avg_price = model.predict(data)
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
