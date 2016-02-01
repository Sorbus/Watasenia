#include <FastLED.h>
#define NUM_LEDS 60
#define DATA_PIN 5

CRGB leds[NUM_LEDS];
int incomingByte = 0;
byte buff[NUM_LEDS * 3];

void setup() {
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  Serial.begin(57600);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read(); /* first byte is the target method */
    if(incomingByte == 'A'){ /* write *every* pixel from an array */
      Serial.readBytes(buff, NUM_LEDS * 3);
      for(int led = 0; led < NUM_LEDS; led++){
        leds[led].setRGB(buff[3*led],buff[3*led+1],buff[3*led+2]);
      }
    }
    else if(incomingByte == 'F'){ /* fill with single color
                                     byte 0-2: rgb color */
      Serial.readBytes(buff, 3);
      for(int led = 0; led < NUM_LEDS; led++){
        leds[led].setRGB(buff[0],buff[1],buff[2]);
      }
    }
    else if(incomingByte == 'P'){ /* set single pixel
                                     byte 0: target pixel
                                     byte 1-3: rgb color */
      Serial.readBytes(buff, 4);
      leds[buff[0]].setRGB(buff[1],buff[2],buff[3]);
    }
    else{
      
    }
    FastLED.show();
  }
}
