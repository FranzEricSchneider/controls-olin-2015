/* 
For use with the Adafruit Motor Shield v2 
---->   http://www.adafruit.com/products/1438
*/


#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"


// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield();

// Select which 'port' M1, M2, M3 or M4. In this case, M4
Adafruit_DCMotor *myMotor = AFMS.getMotor(4);


void setup() {
    Serial.begin(9600);
    Serial.println("Adafruit Motorshield v2 - DC Motor test");

    AFMS.begin();           // create with the default frequency 1.6KHz
    //AFMS.begin(1000);     // OR with a different frequency, say 1KHz
    
    // Set the speed to start, from 0 (off) to 255 (max speed)
    myMotor->setSpeed(50);
    myMotor->run(FORWARD);
    
    // turn on motor
    myMotor->run(RELEASE);
}

void loop() {
    uint8_t i;
    
    Serial.print("tick");

    myMotor->run(FORWARD);
    for (i=0; i<255; i++) {
        myMotor->setSpeed(i);  
        delay(10);
    }
    for (i=255; i!=0; i--) {
        myMotor->setSpeed(i);  
        delay(10);
    }
    
    Serial.print("tock");

    myMotor->run(BACKWARD);
    for (i=0; i<255; i++) {
        myMotor->setSpeed(i);  
        delay(10);
    }
    for (i=255; i!=0; i--) {
        myMotor->setSpeed(i);  
        delay(10);
    }

    Serial.print("tech");
    myMotor->run(RELEASE);
    delay(1000);
}