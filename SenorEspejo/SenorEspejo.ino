#include "DHT.h"
#include <Ultrasonic.h>


#define DHTPIN 2     // what digital pin we're connected to

#define DHTTYPE DHT11   // DHT 11


// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);
Ultrasonic ultrasonic(12, 13);

#define cepilloPin 7
#define aguaPin 8

int cepilloState = 0;
int aguaState = 0;

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(cepilloPin, INPUT);
  pinMode(aguaPin, INPUT);
}

void loop() {
  // Wait a few seconds between measurements.
  delay(1000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);
  int dist;
  boolean esta = false;

  //Read values from ultrasonic sensors and compute presence
  dist = ultrasonic.distanceRead();
  if (dist <= 50){
      esta = true;
    }else{
      esta = false;  
    }

  //Read values from water and brush sensors
  cepilloState = digitalRead(cepilloPin);
  aguaState = digitalRead(aguaPin);
  
  Serial.print(h);
  Serial.print(",");
  Serial.print(t);
  Serial.print(",");
  Serial.print(f);
  Serial.print(",");
  Serial.print(esta);
  Serial.print("\n");
}
