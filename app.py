
import streamlit as st
import pandas as pd

st.title("Pushbutton LED Monitoring System")

st.write("Monitor the LED using a pushbutton with INPUT_PULLUP.")

pressed = st.checkbox("Pushbutton Pressed")

if pressed:
    button_state = "LOW"
    led_status = "OFF"
    st.warning("BUTTON PRESSED")
    st.write("LED Status: OFF")
else:
    button_state = "HIGH"
    led_status = "ON"
    st.success("BUTTON RELEASED")
    st.write("LED Status: ON")

st.subheader("System Monitoring")

col1, col2 = st.columns(2)

with col1:
    st.metric("Button Input (D2)", button_state)

with col2:
    st.metric("LED Output (D8)", led_status)

data = pd.DataFrame({
    "Button State": ["Pressed", "Released"],
    "Digital Input": ["LOW", "HIGH"],
    "LED Status": ["OFF", "ON"]
})

st.subheader("Button State Comparison")
st.dataframe(data, use_container_width=True)
