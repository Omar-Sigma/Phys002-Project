#include <LiquidCrystal.h>

/* Water Level Meter

Measuring water level with ultrasonic sensor.

Arduino IDE 1.5.8
*/

/*Declaring som global variables. These values will hold some user defined values*/

//Leave the comments below as they are. If you're goin to change the place of the lines below, then copy them WITH their comments.
/*conth*/ int conth = 50 ; // Depth of the container
/*sensh*/ int sensh = 5 ;  // Distance from the sensor to the tip of the container
/*maxl*/  int maxl  = 90 ;  // If this waterlevel is reached, a certain action will be done

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
  float t = 0, h = 0, hp = 0;
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

  // Calculating the water level
  float hw = h - sensh; // Subtracting the sensor's height from the total height to get the distance between the tip of the container and the water surface
  float hwf = conth - hw; // Subtracting the distance above from the container's height to get water's height
  float WaL= (hwf/conth)*100; // Getting a percentage.
  
  // These three lines are printed to the serial monitor. For debugging purposes mostly.
  Serial.print("\n");
  Serial.print(h);
  
  Serial.print("\n");
  Serial.print(hw);
  
  Serial.print("\n");
  Serial.print(hwf);
  
  Serial.print("\n");

  int WaLF = (int) (WaL + 0.5); // To round the floats to integars.
  

  // To make 100 the maximum water level
  if (WaLF >= 100){
    WaLF = 100;
    lcd.setCursor(0, 0);
    lcd.print("Status: ");
    lcd.setCursor(8, 0);
    lcd.print("Off!");
    lcd.setCursor(0, 1);
    lcd.print("Waterlevel: ");
    lcd.setCursor(12, 1);
    lcd.print(WaLF);
    lcd.setCursor(15, 1);
    lcd.print("%");
  }

  // The rest of the code which prints to the LCD at different positions.
  else{
    
  if (WaLF > maxl){
    lcd.setCursor(0, 0);
    lcd.print("Status: ");
    lcd.setCursor(8, 0);
    lcd.print("Off!");
  }
  
  else{
    lcd.setCursor(0, 0);
    lcd.print("Status: ");
    lcd.setCursor(8, 0);
    lcd.print("On!");
  }
  
  lcd.setCursor(0, 1);
  lcd.print("Waterlevel: ");
  lcd.setCursor(12, 1);
  lcd.print(WaLF);
  lcd.setCursor(14, 1);
  lcd.print("%");
  }
  delay(1000);
}
