#include <Arduino.h>
#include "DHT.h"
#include <Servo.h>
#define DHTPIN 2          // Hier die Pin Nummer eintragen wo der Sensor angeschlossen ist
#define DHTTYPE DHT11     // Hier wird definiert was für ein Sensor ausgelesen wird. In 
                          // unserem Beispiel möchten wir einen DHT11 auslesen, falls du 
                          // ein DHT22 hast einfach DHT22 eintragen

/**( Definieren der Objekte )**/
DHT dht(DHTPIN, DHTTYPE);
Servo servoMain; // Define our Servo


void setup() {
  Serial.begin(9600);
  Serial.println("DHT11 Testprogramm");
  dht.begin();
  
  servoMain.attach(10); // servo on digital pin 10
  // Serial.begin(9600);                      // Die serielle Kommunikation starten
}
void loop() {
  // Wait a few seconds between measurements.
  delay(5000);                     // Hier definieren wir die Verweilzeit die gewartet wird
                                   // bis der Sensor wieder ausgelesen wird. Da der DHT11
                                   // auch ca. 2 Sekunden hat um seine Werte zuaktualisieren
                                   // macht es keinen sinn ihn schneller auszulesen!

  float h = dht.readHumidity();    // Lesen der Luftfeuchtigkeit und speichern in die Variable h
  float t = dht.readTemperature(); // Lesen der Temperatur in °C und speichern in die Variable t

/**( Überprüfen ob alles richtig Ausgelesen wurde )**/ 
  if (isnan(h) || isnan(t)) {
    Serial.println("Fehler beim auslesen des Sensors!");
    return;
  }

  // Nun senden wir die gemessenen Werte an den PC dise werden wir im Seriellem Monitor sehen
  Serial.print("Luftfeuchtigkeit: ");
  Serial.print(h);                  // Ausgeben der Luftfeuchtigkeit
  Serial.print("%\t");              // Tabulator
  Serial.print("Temperatur: ");
  Serial.print(t);                  // Ausgeben der Temperatur
  Serial.write("°");                // Schreiben des ° Zeichen
  Serial.println("C");
  float zeiger = 180 - ((t-26)*90*1);
  servoMain.write(90); // Turn Servo back to center position (90 degrees)
  delay(3000); // Wait 1 second
  servoMain.write(zeiger); // Turn Servo Right to 180 degrees
  delay(1000); // Wait 1 second
 
  
}