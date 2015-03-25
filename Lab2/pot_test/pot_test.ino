/*
Test taken from Analog example
*/


const int analogInPin = A0;
int pot_v[2] = {0, 0};
int delta_pot_v = 0;


void setup() {
  Serial.begin(9600); 
}


void loop() {
  pot_v[1] = pot_v[0];
  pot_v[0] = analogRead(analogInPin);
  delta_pot_v = pot_v[0] - pot_v[1];

  // print the results to the serial monitor:
  Serial.print("pot voltage = " );
  Serial.print(pot_v[0]);
  Serial.print("\tdelta = ");
  Serial.println(delta_pot_v);

  // wait 2 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
  delay(2);
}
