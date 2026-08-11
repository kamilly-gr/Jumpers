#include <FastLED.h>

#define LED_PIN 6
#define NUM_LEDS 60

CRGB leds[NUM_LEDS];

void setup() {
  FastLED.addLeds<WS2811, LED_PIN, GBR>(leds, NUM_LEDS);

  FastLED.setBrightness(60);

  fill_solid(leds, NUM_LEDS, CRGB(255, 0, 255));
  FastLED.show();
}

void loop() {
}