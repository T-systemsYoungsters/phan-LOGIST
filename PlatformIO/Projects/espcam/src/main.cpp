#include <WiFi.h>
#include <Arduino.h>
 
const char* ssid = "AndroidAPA2C4";
const char* password =  "phyk8666";
 
void setup() {
 
   Serial.begin(115200);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
 
}
 
void loop() {
  Serial.println("Hello");
  delay(1000);
}