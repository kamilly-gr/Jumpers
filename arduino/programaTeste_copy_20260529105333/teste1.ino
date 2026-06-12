#include <FastLED.h>

#define LED_PIN 6
#define NUM_LEDS 60

CRGB leds[NUM_LEDS];

void setup() {
  FastLED.addLeds<WS2811, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(80);
}

void loop() {

  preencher(CRGB::Red);
  delay(1500);

  preencher(CRGB::Green);
  delay(1500);

  preencher(CRGB::Blue);
  delay(1500);
}

void preencher(CRGB cor) {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = cor;
  }
  FastLED.show();
}