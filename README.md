# Weather-Station-IoT-Smart-RESTAPI
Welcome to the Weather Station IoT Smart REST API repository! This project comprises a comprehensive system for gathering weather data from a weather station, transmitting it wirelessly to an integrating module, and visualizing it on a web interface via REST API routes.

## Project Overview

The Weather Station IoT Smart REST API project aims to create a fully functional weather monitoring system. Here's a breakdown of its components:

### Weather Station
The weather station collects weather data using an Arduino Uno and sensors. It consists of:
- Arduino Uno
- DHT11 Temperature and Humidity Sensor
- FS1000A 433MHz RF Transmitter

The weather station is powered by a cable from a computer. The collected data is transmitted wirelessly to the integrating module.

### Integrating Module
The integrating module receives data from the weather station and sends it to a server via REST API. It comprises:
- ESP32
- MX-RM-5V 433MHz RF Receiver
- MP2636 Power Booster & Charger Module
- Lithium Polymer AKYGA Battery 3.7V, 750mAh

The integrating module is powered by a battery, and its output is boosted by the charging module to power the ESP32 and receiver.

### Printed Circuit Board (PCB)
A PCB was designed to provide stability to the wiring connections. However, there was a challenge during its creation as it was ordered one-sided, causing difficulty in soldering the components.

### 3D Printed Container
A small container was 3D printed to house the integrating module. While a proper case was not developed, the dimensions of the container and lid are provided for reference.

## Repository Contents

### Diagrams and Photos
- Wiring diagram for the weather station (Fritzing)
- Wiring diagram for the integrating module (Eagle)
- PCB diagram for the integrating module (Eagle)
- Photos of the assembled weather station and integrating module
- 3D model files and photos of the printed container

### Code
- Code for the weather station (Arduino)
- Code for the integrating module (Arduino with ESP32)
- Flask application for server-side implementation (Python)
- Database creation code (SQL)
- Website code for visualizing data (HTML/CSS)

## Setup Instructions

1. Connect the components according to the provided wiring diagrams.
2. Upload the Arduino code to the weather station and integrating module.
3. Set up the Flask application on a server (e.g., PythonAnywhere).
4. Create the database using the provided SQL code.
5. Deploy the website code to visualize the data.

## Usage

- The weather station collects data and transmits it wirelessly to the integrating module.
- The integrating module sends the data to the server using REST API routes.
- Users can access the visualized data on the website hosted on the server.

Feel free to explore the code and contribute to further improvements!
