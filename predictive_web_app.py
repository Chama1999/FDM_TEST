# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/sadini/Desktop/FDM/trained_model.sav', 'rb'))

# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Resort Hotel'
    else:
      return 'City Hotel'
  
    
  
def main():
    
    
    # giving a title
    st.title('Hotel Prediction Web App')
    
    
    # getting the input data from the user
    
    form = st.form("Form 1")
    meal_list = ['Select...','BB','FB','HB','SC','Undefined']
    meal = form.selectbox('Select Meal',meal_list)
    
    market_segment = ['Select...','Direct','Corporate','Online TA','Offline TA/TO','Complementary','Groups','Aviation']
    market_segment = form.selectbox('Select Marcket Segment',market_segment)
    
    reserved_room_type_list = ['Select...','C','A','D','E','G','F','H','L','B']
    #reserved_room_type_list = ['',1,2,3,4,5,6,7,8,9]
    reserved_room_type_list = form.selectbox('Select Room Type',reserved_room_type_list)
    
    col1,col2 = form.columns(2)
    stays_in_weekend_nights = col1.text_input('Weekend Nights')
    stays_in_week_nights = col2.text_input('Weekday Nights')
    
    col3,col4,col5 = form.columns(3)
    adults = col3.text_input('No of Adults')
    children = col4.text_input('No of Childrens')
    babies = col5.text_input('No of Babies')
    adr= form.text_input('adr')
    required_car_parking_spaces = form.text_input('required_car_parking_spaces')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if form.form_submit_button('Hotel Result'):
        diagnosis = diabetes_prediction([meal, market_segment, reserved_room_type_list, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, adr, required_car_parking_spaces])
        
        
    form.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()