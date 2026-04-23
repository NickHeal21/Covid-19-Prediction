---
title: Covid 19 Prediction
app_file: app.py
sdk: gradio
sdk_version: 5.31.0
---
🦠 COVID-19 Variant NB 1.8.1 Predictor – 2025 Edition
A machine learning-powered web app to predict the probability of COVID-19 positivity using user symptoms and environmental data.
Deployed using Gradio on Hugging Face Spaces – fully open-source, interactive, and demo-ready!

🔗 Live App: https://huggingface.co/spaces/Nikhildev21/Covid_19_Prediction_2025

📌 Features
✅ Real-time COVID-19 prediction with a user-friendly form interface
🧠 Powered by Random Forest Classifier
📈 Based on real-world features:
Demographics (age, gender, location)
Environmental data (temperature, humidity, air quality)
Symptoms (fever, cough, breathlessness, etc.)
Risk factors (recent travel, smoker status, vaccination)
💡 Intuitive Gradio front-end
📦 Ready-to-deploy with Hugging Face Spaces and pip requirements
🧠 Model Info

Trained on a synthetic dataset with 20+ real-world features
Used Random Forest Classifier for balanced accuracy and interpretability
Model file: covid_19_predictor_2025.joblib
Feature importance includes:
Fever, Loss of Smell, Breathlessness, Travel History, AQI, etc.

💻 Tech Stack
Python
Scikit-learn
Gradio
Hugging Face Spaces
Jupyter Notebook
Joblib (for model serialization)

🚀 Run Locally
git clone https://huggingface.co/spaces/Nikhildev21/Covid_19_Prediction_2025
cd Covid_19_Prediction_2025
pip install -r requirements.txt
python app.py

📂 Project Structure
Covid_19_Prediction_2025/
│
├── App1.ipynb                 # Notebook with preprocessing + training
├── app.py                     # Gradio interface (main app file)
├── covid_19_predictor_2025.joblib  # Trained model
├── requirements.txt           # Required packages
└── README.md                  # Project readme (you're reading it!)
📹 Demo (Optional)


📣 About the Author
👨‍💻 Developed by Nikhil,
Aspiring AI Engineer, ML enthusiast, and proud creator of this health-tech tool.
Feel free to connect and drop feedback!

📬 Feedback & Contributions
Pull requests welcome!
Open issues for bug reports or feature requests
