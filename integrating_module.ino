#include <RCSwitch.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <Arduino_JSON.h>


const char* ssid = "Weather";
const char* password = "vddb2152";


const char* url1 = "http://nervles.pythonanywhere.com/add/mes";

const int device_id = 1;

RCSwitch mySwitch = RCSwitch();

void setup() {
  Serial.begin(9600);
  mySwitch.enableReceive(4);  // Receiver on interrupt 0 => GPIO 4
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  if (mySwitch.available()) {
    long receivedValue = mySwitch.getReceivedValue();

    if (receivedValue == 0) {
      Serial.println("Unknown encoding");
    } else {
      float temperature = receivedValue / 100;
      float humidity = receivedValue % 100;
      Serial.print("Received Temperature: ");
      Serial.print(temperature);
      Serial.print(" C, Humidity: ");
      Serial.print(humidity);
      Serial.println(" %");

      if(WiFi.status() == WL_CONNECTED){
        postRequest(url1, device_id, temperature, humidity);
      }

      delay(10000);
    }

    mySwitch.resetAvailable();
  }
}


void postRequest(const char* serverName, const int device_id, float temperature, float humidity){
  WiFiClient client;
  HTTPClient http;

  http.begin(client, serverName);

  http.addHeader("Content-Type", "application/json");

  String jsonPayload = "{\"device_id\":\"" + String(device_id) + "\",\"temperature\":\"" + String(temperature) + "\",\"humidity\":\"" + String(humidity) + "\"}";
  Serial.println(jsonPayload);

  int httpResponseCode = http.POST(jsonPayload);

  if(httpResponseCode > 0) {
    String response = http.getString();
    Serial.println(response);
  } else {
    Serial.print("Error on sending POST: ");
    Serial.println(httpResponseCode);
  }

  http.end();
}
