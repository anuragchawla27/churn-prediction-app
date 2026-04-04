import streamlit as st
import requests

st.title("Customer Churn Prediction")

# Inputs
tenure = st.number_input("Tenure", min_value=0)
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

gender = st.selectbox("Gender", ["Female", "Male"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

# Encoding
gender_val = 1 if gender == "Male" else 0

contract_one = 1 if contract == "One year" else 0
contract_two = 1 if contract == "Two year" else 0


# Predict button
if st.button("Predict"):
    try:
        response = requests.post(
           "https://churn-api-xa9z.onrender.com/predict",
            json={
                "tenure": tenure,
                "monthly_charges": monthly,
                "total_charges": total,
                "gender_male": gender_val,
                "contract_one_year": contract_one,
                "contract_two_year": contract_two
            }
        )

        result = response.json()

        # Handle error from API
        if "error" in result:
            st.error(f"Backend Error: {result['error']}")
        else:
            pred = result["churn_prediction"]
            prob = result["probability"]

            # Risk level
            if prob < 0.3:
                risk = "Low Risk"
            elif prob < 0.7 and prob>0.3:
                risk = "Medium Risk"
            else:
                risk = "High Risk"

            # Prediction display
            if pred == 1:
                st.error("⚠️ Prediction: Churn")
            else:
                st.success("✅ Prediction: No Churn")

            # Probability
            st.info(f"📌 Churn Probability: {round(prob, 2)}")

            # Risk level
            if risk == "High Risk":
                st.error(f"🚨 Risk Level: {risk}")
            elif risk == "Medium Risk":
                st.warning(f"⚠️ Risk Level: {risk}")
            else:
                st.success(f"🟢 Risk Level: {risk}")

    except Exception as e:
        st.error(f"Connection Error: {e}")