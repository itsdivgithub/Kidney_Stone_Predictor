#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('my_model.h5')

# Define a function to make a prediction
def predict_target(gravity, ph, osmo, cond, urea, calc, osmo_cond_ratio, urea_calc_diff, osmo_urea_interaction, gravity_bin, ph_bin, osmo_bin, cond_bin, urea_bin, calc_bin):
    
    # Create a numpy array with the input values and reshape it for the model
    input_data = np.array([[gravity, ph, osmo, cond, urea, calc, osmo_cond_ratio, urea_calc_diff, osmo_urea_interaction, gravity_bin, ph_bin, osmo_bin, cond_bin, urea_bin, calc_bin]])
    input_data = np.reshape(input_data, (input_data.shape[0], input_data.shape[1], 1))
    
    # Make a prediction using the model
    prediction = model.predict(input_data)
    
    # Return the predicted target value
    return prediction[0][0]

    
 # Add a title
st.title("Kidney Stone Prediction App")
    
# Add input fields for the features
gravity = st.number_input("Enter gravity value")
ph = st.number_input("Enter pH value")
osmo = st.number_input("Enter osmo value")
cond = st.number_input("Enter cond value")
urea = st.number_input("Enter urea value")
calc = st.number_input("Enter calc value")
osmo_cond_ratio = st.number_input("Enter osmo_cond_ratio value")
urea_calc_diff = st.number_input("Enter urea_calc_diff value")
osmo_urea_interaction = st.number_input("Enter osmo_urea_interaction value")
gravity_bin = st.number_input("Enter gravity_bin value")
ph_bin = st.number_input("Enter ph_bin value")
osmo_bin = st.number_input("Enter osmo_bin value")
cond_bin = st.number_input("Enter cond_bin value")
urea_bin = st.number_input("Enter urea_bin value")
calc_bin = st.number_input("Enter calc_bin value")
    
# Add a button to make the prediction
if st.button("Predict"):
    prediction = predict_target(gravity, ph, osmo, cond, urea, calc, osmo_cond_ratio, urea_calc_diff, osmo_urea_interaction, gravity_bin, ph_bin, osmo_bin, cond_bin, urea_bin, calc_bin)
    st.write("Predicted Target Value: ", prediction)
    if prediction > 0.3:
        st.write("You have kidney stone.")
    else:
        st.write("You dont have kidney stone.")


# In[ ]:




