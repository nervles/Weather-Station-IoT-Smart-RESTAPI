# Weather-Station-IoT-Smart-RESTAPI
Welcome to the Weather Station IoT Smart REST API repository! This project comprises a comprehensive system for gathering weather data from a weather station, transmitting it wirelessly to an integrating module, and visualizing it on a web interface via REST API routes.

## Project Overview

The Weather Station IoT Smart REST API project aims to create a fully functional weather monitoring system. Here's a breakdown of its components:

### Weather Station
The weather station collects weather data using an Arduino Uno and sensors. It consists of:
- Arduino Uno
- DHT11 Temperature and Humidity Sensor
- FS1000A 433MHz RF Transmitter

<img src="https://github.com/nervles/Weather-Station-IoT-Smart-RESTAPI/assets/130153131/11db2c48-978f-4326-8dc2-ddb22589e30e" width=500 height=400>

The weather station is powered by a cable from a computer. I encourage you to change the power source that will allow this station to be portable as it will make more sense. I simply wanted to focus on other parts of this project and had very limited budget. The collected data is radio transmitted wirelessly to the integrating module.

### Integrating Module
The integrating module receives data from the weather station and sends it to a server via REST API. It comprises:
- ESP32
- MX-RM-5V 433MHz RF Receiver
- MP2636 Power Booster & Charger Module
- Lithium Polymer AKYGA Battery 3.7V, 750mAh

![pcb_schema](https://github.com/nervles/Weather-Station-IoT-Smart-RESTAPI/assets/130153131/2e7ebeff-6988-48ee-828c-2f5032820475)

The integrating module is powered by a battery, and its output is boosted by the charging module to 5V to power the ESP32 and receiver.

### How does it work? - brief description
The weather station radio transmits the data to integrating module. Integrating module receives the data, processes it to json and sends it to the server. The data is displayed on website in real time. Server is hosted on [pythonanywhere.com](pythonanywhere.com). It allows its services for free - you just have to sign in. Then you have to set it up and upload the database. (I won't delve deeper into that, because there are surely some tutorials on how to do it)

<img src="https://github.com/nervles/Weather-Station-IoT-Smart-RESTAPI/assets/130153131/a8da6115-4cc9-4c3c-a8c8-6bb0f1128410" width=500 height=150>


### Printed Circuit Board (PCB)
A PCB was designed to provide stability to the wiring connections. However, there was a challenge during its creation as it was ordered one-sided, causing difficulty in soldering the components.

![pcb_sciezki](https://github.com/nervles/Weather-Station-IoT-Smart-RESTAPI/assets/130153131/9cdbfa2f-6886-48a7-847d-6285f3ceb2c3) <img src="https://github.com/nervles/Weather-Station-IoT-Smart-RESTAPI/assets/130153131/56095a07-3a78-49b8-93af-15633b7b8cc3" width=300 height=300>

### ESP should be mirrored in eagle. My mistake makes assembly/soldering problematic. ESP should be on the same side as rest of the components.

### 3D Printed Container
A small container was 3D printed to house the integrating module. The container's dimensions are 100x65x50 [mm] and lid's are 107x72x8 [mm]. I used Siemens NX for this so i don't know if you will be able to make changes but stl files will be fine to print right away. I haven't made proper case as i wanted to focus on programming side but i encorage tou to do so if you have spare time!

<img src="https://github.com/nervles/Weather-Station-IoT-Smart-RESTAPI/assets/130153131/f8efacde-7a2d-423d-845a-f3d6d8cb7a48" width=500 height=400>

### Assembled integrating module

<img src="https://github.com/nervles/Weather-Station-IoT-Smart-RESTAPI/assets/130153131/1b7542c4-69b7-40cb-a59d-efc38acc7a04" width=400 height=500>

<img src="https://github.com/nervles/Weather-Station-IoT-Smart-RESTAPI/assets/130153131/3f9744e3-d6c8-4a82-82c3-36c0c08019c5" width=400 height=500>

## Repository Contents

### Diagrams and Photos
- Wiring diagram for the weather station (Fritzing)
- Wiring diagram for the integrating module (Eagle)
- PCB diagram for the integrating module (Eagle)
- Photos of the assembled weather station and integrating module
- 3D model photo of the printed container

### Code
- Code for the weather station (Arduino/C)
- Code for the integrating module (Arduino/C)
- Flask application for server-side implementation (Python)
- Database creation code (SQL)
- Website code for visualizing data (HTML)

## Setup Instructions

1. Connect the components according to the provided wiring diagrams.
2. Upload the Arduino code to the weather station and integrating module.
3. Set up the Flask application on a server (e.g., PythonAnywhere).
4. Create the database using the provided SQL code and deploy it on server.
5. Deploy the website code to visualize the data.

![baza](https://github.com/nervles/Weather-Station-IoT-Smart-RESTAPI/assets/130153131/38502eed-e096-4185-9974-f735f3190816)

## Usage

- The weather station collects data and transmits it wirelessly to the integrating module.
- The integrating module sends the data to the server using REST API routes.
- Users can access the visualized data on the website hosted on the server.

Feel free to explore the code and make your own improvements!
