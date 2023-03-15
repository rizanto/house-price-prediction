import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image
import xgboost



# loading the saved model
loaded_model = pickle.load(open("./model/housepricemodel.sav", 'rb'))

# function for currency formatting
def currency(price):
    seperator_of_thousand = "."
    seperator_of_fraction = ","
    my_currency = "Rp {:,.2f}".format(price)
    if seperator_of_thousand == ".":
        main_currency, fractional_currency = my_currency.split(".")[0], my_currency.split(".")[1]
        new_main_currency = main_currency.replace(",", ".")
        currency = new_main_currency + seperator_of_fraction + fractional_currency
    return(currency)


# creating a function for Prediction
def houseprice(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # print(input_data_as_numpy_array)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    prediction = round(float(prediction[0])*1_000_000, 0)
    prediction = currency(prediction)
    return f"Harganya INSYAALLAH sekitar {prediction}" 

    
  
def main():
    
    st.set_page_config(layout='centered', page_title="House Price Prediction", page_icon="🤣")

    # giving a title
    header = Image.open('./images/header.jpg')
  
    st.image(header)
    st.title('House Price Prediction')
    
    # getting the input data from the user
    city = st.selectbox('CITY', (
      'Bekasi',
      'Bogor',
      'Depok',
      'Jakarta Barat',
      'Jakarta Pusat',
      'Jakarta Selatan',
      'Jakarta Timur',
      'Jakarta Utara',
      'Tangerang'
    ))
    land_size_m2 = st.text_input('LAND SIZE M2', 20)
    building_size_m2 = st.text_input('BUILDING SIZE M2', 20)
    floors = st.slider('FLOORS', min_value=1, max_value=4, value=1, step=1)
    bedrooms = st.slider('BEDROOMS', min_value=1, max_value=9, value=2, step=1)
    bathrooms = st.slider('BATHROOMS', min_value=1, max_value=9, value=2, step=1)
    electricity = st.text_input('ELECTRICITY', 900)
    carports = st.selectbox('CARPORTS', ('Yes','No'))
    garages = st.selectbox('GARAGES', ('Yes','No'))




        
    # km_driven = st.text_input("KM Driven",0)
    # mileage = st.slider('Mile Age (Kilometres per Litre)', min_value=10, max_value=40,value=13,step=1)
    # engine = st.slider('Engine (CC)', min_value=800, max_value=2700,value=1200,step=100)
    # max_power = st.slider('Max Power (Brake Horse Power)', min_value=45, max_value=180,value=80,step=5)
    # seats = st.select_slider("Seats", [2,4,5,6,7,8,9,10,14], value=5)
    # year = st.slider('Year', min_value=1997, max_value=2022,value=2007,step=1)
    # fuel = st.selectbox('Fuel', ('Diesel','LPG','Petrol','CNG'))
    # seller_type = st.selectbox("Type of Seller",('Dealer', 'Individual'))
    # transmission = st.selectbox("Transmission",("Automatic","Manual"))
    # owner = st.selectbox("Type Owner",("First Owner","Second Owner","Third Owner","Fourth and Above Owner"))

    
    # code for Prediction
    price = f'Baca Bismillah Dulu... \n\n -Ubed 2023'
    
    # transforming data

    city_Bogor = 0
    city_Depok = 0
    city_Jakarta_Barat = 0
    city_Jakarta_Pusat = 0
    city_Jakarta_Selatan = 0
    city_Jakarta_Timur = 0
    city_Jakarta_Utara = 0
    city_Tangerang = 0

    if city=='Bogor':
      city_Bogor = 1
    elif city=="Depok":
      city_Depok = 1
    elif city=="Jakarta Barat":
      city_Jakarta_Barat = 1
    elif city == "Jakarta Pusat":
      city_Jakarta_Pusat = 1
    elif city=="Jakarta Selatan":
      city_Jakarta_Selatan = 1
    elif city=="Jakarta Barat":
      city_Jakarta_Barat = 1
    elif city == "Jakarta Timur":
      city_Jakarta_Timur = 1
    elif city=="Jakarta Utara":
      city_Jakarta_Utara = 1
    elif city == "Tangerang":
      city_Tangerang = 1

    
    if carports == 'Yes':
       carports = 1
    else:
       carports = 0

    if garages == 'Yes':
       garages = 1
    else:
       garages = 0

    # creating a button for Prediction
    
    if st.button('Price Prediction'):
        price = houseprice([
          bedrooms,
          bathrooms,
          land_size_m2,
          building_size_m2,
          carports,
          electricity,
          floors,
          garages,
          city_Bogor,
          city_Depok,
          city_Jakarta_Barat,
          city_Jakarta_Pusat,
          city_Jakarta_Selatan,
          city_Jakarta_Timur,
          city_Jakarta_Utara,
          city_Tangerang,
        ])
        
    st.success(price)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  