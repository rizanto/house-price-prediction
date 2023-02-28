import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image



# loading the saved model
loaded_model = pickle.load(open("./web-app/model/housepricemodel.sav", 'rb'))


# creating a function for Prediction

def houseprice(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    return f"The price will be around ${round(prediction[0],2)}" 
    
  
def main():
    
    st.set_page_config(layout='wide', page_title="House Price Prediction", page_icon="😘🤣")

    # giving a title
    header = Image.open('./web-app/images/header3.png')
  
    st.image(header)
    st.title('House Price Prediction')
    
    # getting the input data from the user
    bedrooms = st.slider('bedrooms', min_value=1, max_value=9,value=2,step=1)
    bathrooms = st.slider('bathrooms', min_value=1, max_value=9,value=2,step=1)
    land_size_m2 = st.text_input('land_size_m2', 0)
    building_size_m2 = st.text_input('building_size_m2', 0)
    carports = st.slider('carports', min_value=1, max_value=15,value=2,step=1)
    electricity = st.text_input('electricity', 0)
    floors = st.slider('floors', min_value=1, max_value=5,value=2,step=1)
    garages = st.slider('garages', min_value=1, max_value=15,value=2,step=1)
    city = st.selectbox('city', (
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
    price = 'In Data We Believe...'
    
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
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  