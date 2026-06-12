#include <FastLED.h>

#define LED_PIN 6
#define NUM_LEDS 60

CRGB leds[NUM_LEDS];

void setup() {
  Serial.begin(9600);

  FastLED.addLeds<WS2811, LED_PIN, GBR>(leds, NUM_LEDS);
  FastLED.setBrightness(100);
}

void loop() {

  if (Serial.available()) {

    String cor = Serial.readStringUntil('\n');
    cor.trim();

    if (cor == "AZUL") {
      fill_solid(leds, NUM_LEDS, CRGB(0,255,0));
    }

    else if (cor == "ROXO") {
      fill_solid(leds, NUM_LEDS, CRGB(0,155,155));
    }

    else if (cor == "AMARELO") {
      fill_solid(leds, NUM_LEDS, CRGB(100, 0, 255));
    }

    else if (cor == "LARANJA") {
      fill_solid(leds, NUM_LEDS, CRGB(40, 0, 255));
    }

    FastLED.show();
  }
}
