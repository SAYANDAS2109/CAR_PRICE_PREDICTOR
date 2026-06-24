import pickle as pkl
import streamlit as st
import numpy as np
lin_reg = pkl.load(open("car_price_model.pkl","rb"))

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon= "🚗"
)

st.title("CAR PRICE PREDICTION SYSTEM🚗")
st.write("Enter the car details below and click predict")

year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2026,
    value=2020)

present_prices = st.number_input(
    "Present Price(Lakhs)",
    min_value=0.0,
    value=5.0


)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0.0,
    value=10000.0


)

fuel_type = st.selectbox(
    "Fuel_Type",
    ["Petrol","Diesel","CNG"]
)

Seller_Type = st.selectbox(
    "Seller Type",
    ["Dealer","Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual","Automatic"]
)

owner = st.selectbox(
    "Number of Previous Owners",
    [0,1,2,3]
)

fuel_dict = {
    "Petrol":0,
    "Diesel":1,
    "CNG":2
}

Seller_dict = {
    "Dealer" :0,
    "Individual" : 1
}

transmission_dict = {
    "Manual":0,
    "Automatic":1
}

if st.button("Predict Price"):

    features = np.array([[
        year,
        present_prices,
        kms_driven,
        Seller_dict[Seller_Type],

        fuel_dict[fuel_type],
        transmission_dict[transmission],
        owner
    ]])

    prediction = lin_reg.predict(features)

    st.success(
        f"Estimated car price: ₹{prediction[0]:.2f} Lakhs"
    )


