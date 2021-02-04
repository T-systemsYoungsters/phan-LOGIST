#include <Arduino.h>
#include <LiquidCrystal.h>                // Die Bibliothek für deinen Display
#include <Wire.h>

 

int RS = 6;                              //

int E = 7;                               //

int D4 = 11;                               //

int D5 = 10;                               //

int D6 = 9;                               //Variablen für die Arduino Pins

int D7 = 8;                               //

int Spalte = 16;                          //

int Zeile = 2;                            //

 

LiquidCrystal lcd(RS, E, D4, D5, D6, D7); // Hier wird das Objekt lcd vom Typ 

                                          // LiquidCrystal erzeugt

 

void setup() {

  

   lcd.begin(Spalte,Zeile);               // Leg die LCD mit 16 Spalten und 2 Zeilen fest

   lcd.print(" hello ");         // Der Text für die erste Zeile

   lcd.setCursor(0,1);                    // Springe in die nächste Zeile

   lcd.print("  world ");           // Schreibe den Text in die zweite Zeile

 

}

 

void loop() {

 

   // Deine loop- Methode bleibt leer.

 

}