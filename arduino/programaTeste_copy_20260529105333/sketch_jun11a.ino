#include <FastLED.h>

#define LED_PIN 6
#define NUM_LEDS 10

CRGB leds[NUM_LEDS];

void setup() {
  FastLED.addLeds<WS2811, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(20);
}

void loop() {
  fill_solid(leds, NUM_LEDS, CRGB::Blue);
  FastLED.show();
}
