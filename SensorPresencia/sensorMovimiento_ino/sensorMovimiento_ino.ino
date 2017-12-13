//Variables
int pinPIRinput = 2;
int pinLED = 13;

void setup() {
  pinMode(pinLED, OUTPUT); //Pin del led como salida
  pinMode(pinPIRinput, INPUT); //Pin del sensor como entrada
}

void loop() {
  int valorSensor = digitalRead(pinPIRinput);
  
  if (valorSensor == HIGH){ //Lo que hacemos cuando el sensor da señal: hay movimiento
    digitalWrite(pinLED, HIGH);
    delay(5000);
    digitalWrite(pinLED, LOW);
  } else { //No da señal: el sistema se para
    digitalWrite(pinLED, LOW);
  }
}
