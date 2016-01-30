#include <FastLED.h>
#define NUM_LEDS 60
#define DATA_PIN 6

CRGB leds[NUM_LEDS];
int incomingByte = 0;
byte buff[NUM_LEDS * 3];

void setup() {
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    Serial.readBytes(buff, NUM_LEDS * 3);
    for(int led = 0; led < NUM_LEDS; led++){
      leds[led].r = buff[3*led];
      leds[led].g = buff[3*led+1];
      leds[led].b = buff[3*led+2];
    }
    FastLED.show();
    delay(10);
  }
  delay(5);
}
