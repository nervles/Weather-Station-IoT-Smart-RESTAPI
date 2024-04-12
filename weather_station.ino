#include <RCSwitch.h>
#include <DHT.h>

#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

RCSwitch mySwitch = RCSwitch();

void setup() {
  Serial.begin(9600);
  mySwitch.enableTransmit(10);  // Transmitter is connected to Arduino Pin #10
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  long data = (long(t) * 100) + long(h); // Combining temperature and humidity
  mySwitch.send(data, 32); // Sending the combined data
  delay(5000); // Wait for 1 second before sending again
}
