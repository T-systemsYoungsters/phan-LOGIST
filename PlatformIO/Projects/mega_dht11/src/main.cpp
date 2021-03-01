#include <Arduino.h>
#include "DHT.h"
#define DHTPIN 2      // Hier die Pin Nummer eintragen wo der Sensor angeschlossen ist
#define DHTTYPE DHT11 // Hier wird definiert was für ein Sensor ausgelesen wird. In  \
                      // unserem Beispiel möchten wir einen DHT11 auslesen, falls du \
                      // ein DHT22 hast einfach DHT22 eintragen
/**( Definieren der Objekte )**/
DHT dht(DHTPIN, DHTTYPE);
int trigger = 22; // Der Trigger Pin
int echo = 24; // Der Echo Pin
long dauer = 0; // Hier wird die Zeitdauer abgespeichert
// die die Ultraschallwelle braucht
// um zum Sensor zurückzukommen
long entfernung = 0; // Hier wird die Entfernung vom
// Hindernis abgespeichert
void setup()
{
  Serial.begin(9600);
  Serial.println("DHT11 Testprogramm");
  dht.begin();
  // Serial.begin(9600);                      // Die serielle Kommunikation starten
  pinMode(trigger, OUTPUT); // Trigger Pin als Ausgang definieren
  pinMode(echo, INPUT); // Echo Pin als Eingang defnieren
}
void loop()
{
  // Wait a few seconds between measurements.
  delay(5000); // Hier definieren wir die Verweilzeit die gewartet wird
               // bis der Sensor wieder ausgelesen wird. Da der DHT11
               // auch ca. 2 Sekunden hat um seine Werte zuaktualisieren
               // macht es keinen sinn ihn schneller auszulesen!
  float h = dht.readHumidity();    // Lesen der Luftfeuchtigkeit und speichern in die Variable h
  float t = dht.readTemperature(); // Lesen der Temperatur in °C und speichern in die Variable t
  /**( Überprüfen ob alles richtig Ausgelesen wurde )**/
  if (isnan(h) || isnan(t))
  {
    Serial.println("Fehler beim auslesen des Sensors!");
    return;
  }
  // Nun senden wir die gemessenen Werte an den PC dise werden wir im Seriellem Monitor sehen
  Serial.print("Luftfeuchtigkeit: ");
  Serial.print(h);     // Ausgeben der Luftfeuchtigkeit
  Serial.print("%\t"); // Tabulator
  Serial.print("Temperatur: ");
  Serial.print(t);   // Ausgeben der Temperatur
  Serial.write("°"); // Schreiben des ° Zeichen
  Serial.println("C");
  digitalWrite(trigger, LOW); // Den Trigger auf LOW setzen um
  // ein rauschfreies Signal
  // senden zu können
  delay(5); // 5 Millisekunden warten
  digitalWrite(trigger, HIGH); // Den Trigger auf HIGH setzen um eine
  // Ultraschallwelle zu senden
  delay(10); // 10 Millisekunden warten
  digitalWrite(trigger, LOW); // Trigger auf LOW setzen um das
  // Senden abzuschließen
  dauer = pulseIn(echo, HIGH); // Die Zeit messen bis die
  // Ultraschallwelle zurückkommt
  entfernung = (dauer / 2) / 29.1; // Die Zeit in den Weg in Zentimeter umrechnen
  Serial.print(entfernung); // Den Weg in Zentimeter ausgeben
  Serial.println(" cm"); //
  delay(1000); // Nach einer Sekunde wiederholen
}