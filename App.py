#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import gradio as gr
import pandas as pd
import joblib


model = joblib.load("covid_19_predictor_2025.joblib")

def predict_covid(age, gender, location, temperature, humidity, aqi, vaccinated, recent_travel, smoker,
                  fever, cough, fatigue, sore_throat, nasal_congestion, headache,
                  sneezing, nausea, loss_smell, breathlessness):


    input_dict = {
        "Age": age,
        "Gender": gender,
        "Location": location,
        "Temperature": temperature,
        "Humidity": humidity,
        "Air_Quality_Index": aqi,
        "Vaccinated": int(vaccinated),
        "Recent_Travel": int(recent_travel),
        "Smoker": int(smoker),
        "Fever": int(fever),
        "Cough": int(cough),
        "Fatigue": int(fatigue),
        "Sore_Throat": int(sore_throat),
        "Nasal_Congestion": int(nasal_congestion),
        "Headache": int(headache),
        "Sneezing": int(sneezing),
        "Nausea": int(nausea),
        "Loss_Smell": int(loss_smell),
        "Breathlessness": int(breathlessness)
    }


    input_df = pd.DataFrame([input_dict])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

    probability = model.predict_proba(input_df)[0][1]  
    return f"Your possibility of getting Covid 19 new variant is : {probability:.2%}"

inputs = [
    gr.Number(label="Age", value=30),
    gr.Dropdown(choices=["Female", "Male", "Other(Cannot Specify)"], label="Gender"),
    gr.Dropdown(choices=["Pune", "Mumbai", "Delhi"], label="Location"),
    gr.Number(label="Temperature (°C)", value=30),
    gr.Number(label="Humidity (%)", value=50),
    gr.Number(label="Air Quality Index", value=100),
    gr.Checkbox(label="Vaccinated", value=True),
    gr.Checkbox(label="Recent Travel", value=False),
    gr.Checkbox(label="Smoker", value=False),
    gr.Checkbox(label="Fever", value=False),
    gr.Checkbox(label="Cough", value=False),
    gr.Checkbox(label="Fatigue", value=False),
    gr.Checkbox(label="Sore Throat", value=False),
    gr.Checkbox(label="Nasal Congestion", value=False),
    gr.Checkbox(label="Headache", value=False),
    gr.Checkbox(label="Sneezing", value=False),
    gr.Checkbox(label="Nausea", value=False),
    gr.Checkbox(label="Loss of Smell", value=False),
    gr.Checkbox(label="Breathlessness", value=False)
]

iface = gr.Interface(
    fn=predict_covid,
    inputs=inputs,
    outputs="text",
    title="COVID-19 Variant NB 1.8.1 Prediction"
)

iface.launch(inline = False, share = True, debug = True)


# In[ ]:




