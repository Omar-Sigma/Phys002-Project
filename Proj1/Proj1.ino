#include <LiquidCrystal.h>
/* Water Level Meter

Measuring water level with ultrasonic sensor.

Arduino IDE 1.5.8
*/
LiquidCrystal lcd = LiquidCrystal(2, 3, 4, 5, 6, 7);
int trig = 12;
int echo = 11;

void setup()
{
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT); 
  lcd.begin(16, 2);
}

void loop()
{

  lcd.clear();
  long t = 0, h = 0, hp = 0;
  
  // Transmitting pulse
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  
  // Waiting for pulse
  t = pulseIn(echo, HIGH);
  
  // Calculating distance 
  h = t * 0.034/ 2; 
 
 //h = h - 6;  // offset correction
  //h = 30 - h;  // water height, 0 - 50 cm
    
  // Sending to computer
  Serial.print(h);
  // Serial.print(" cm\n");
  Serial.print("\n");

    lcd.setCursor(2, 0);
  // Print the string 'Hello World!':
    lcd.print("Hello World!");
  // Set the cursor on the third column and the second row:
  char strl[5];
  
  lcd.setCursor(2, 1);
  lcd.print("Distance: ");
  lcd.setCursor(13, 1);
  // Print the string 'LCD tutorial':
  //sprintf(strl, "%d", h);
  lcd.print(h);
  
  //Serial.print(strl);
  delay(2500);
}
