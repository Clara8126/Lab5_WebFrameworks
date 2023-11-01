from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load the pickled model
    with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    # Get input from the form
    feature_1 = float(request.form['feature_1'])
    # Add more lines to get other feature values

    # Perform prediction using the loaded model
    prediction = loaded_model.predict([[feature_1]])  # Adjust input format as needed

    return f"Predicted Car Price: {prediction[0]}"

if __name__ == '__main__':
    app.run(debug=True)
