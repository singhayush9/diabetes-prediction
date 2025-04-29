from flask import Flask, render_template, request
import joblib  # use joblib instead of pickle
import numpy as np

# Load the model using joblib (recommended for sklearn)
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = joblib.load(filename)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract features from the form
        try:
            preg = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            bp = int(request.form['bloodpressure'])
            st = int(request.form['skinthickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = int(request.form['age'])

            # Prepare input array
            data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
            prediction = classifier.predict(data)[0]

            return render_template('result.html', prediction=prediction)
        except Exception as e:
            return f"Error in prediction: {e}"

# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
