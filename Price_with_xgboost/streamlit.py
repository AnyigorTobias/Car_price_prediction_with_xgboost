import pickle
import streamlit as st
import json
import pandas as pd
import numpy as np

model_file = r'C:\Users\anuel\OneDrive\Desktop\Price_with_xgboost\Car_price_prediction_model.pickle'
with open(model_file,'rb') as f_in:
    dv,model = pickle.load(f_in)

with open('brands.json', 'r') as f:
    Car_brands = json.load(f)

def main():
    st.title ('Car Prediction Application')

    #input variables
    car_make = st.selectbox('Make:', Car_brands)
    year = st.number_input('What is the year?:')
    condition = st.selectbox(' What is the condition of the car:', ['Foreign Used', 'Foreign Used', 'Brand New'])
    mileage = st.number_input('What is the mileage of the car?:')
    Engine_size = st.number_input('Enter the engine size in cc:', min_value = 1000, max_value = 1000000, value = 0)
    Fuel = st.selectbox('Specify the choice fuel option:', ['Petrol', 'Diesel', 'Hybrid', 'Electric'])
    Transmission = st.selectbox('What is the preferred gear transmission?:', ['Automatic', 'Manual', 'AMT', 'CVT'])

    input_dict = {
        'make': car_make,
        'year': year,
        'condition': condition,
        'mileage': mileage,
        'Engine_Size': Engine_size,
        'Fuel': Fuel,
        'Transmission': Transmission
    }

    #prediction
    if st.button ('Predict'):
        check2 = np.delete(dv.transform([input_dict]), -6, axis=1)
        make_predict =  model.predict(check2)[0]
        output = round(make_predict, 2)
        st.success ('You can sell your car for {}'.format(output))

    if __name__ == '__main__':
        main()





