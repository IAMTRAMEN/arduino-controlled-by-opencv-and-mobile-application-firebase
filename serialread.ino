#include <Servo.h>
int servoPin=11;
Servo servo1;
void setup() {
  Serial.begin(9600);
servo1.attach(servoPin);
  // put your setup code here, to run once:

}
char data;
void loop() {
  if (Serial.available()){
char data = Serial.read();
if (data=='1')
servo1.write(0);
if (data=='0')
servo1.write(180);
  }
  // put your main code here, to run repeatedly:

}
