
# Pushbutton-Controlled LED System

## Project Description
This project demonstrates how an Arduino Uno reads a pushbutton input using INPUT_PULLUP and controls an LED using digital output and if/else statements.

## Components Used
1. Arduino Uno
2. Breadboard
3. Pushbutton
4. Red LED
5. 220Ω Resistor
6. Jumper Wires

## Wiring Connections

### LED Connections
1. Arduino D8 → 220Ω resistor
2. Other resistor end → LED anode (+)
3. LED cathode (-) → GND

### Pushbutton Connections
1. One switching terminal → Arduino D2
2. Opposite switching terminal → GND
3. Use terminals on opposite sides of the switch contact.

## How It Works
- INPUT_PULLUP enables the internal pull-up resistor.
- Pressed button reads LOW.
- Released button reads HIGH.
- The Arduino uses if/else statements to control the LED.
- The LED responds to the button state.

## Arduino Program
The program reads the pushbutton through digital pin 2 and controls the LED through digital pin 8.

## Files
- README.md – Project documentation.
- app.py – Streamlit monitoring dashboard.
- sketch.ino – Arduino control program.

## Technologies Used
- Arduino Uno
- C++
- Python
- Streamlit
- Pandas
- Wokwi

