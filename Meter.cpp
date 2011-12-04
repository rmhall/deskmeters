#include "Meter.h"

#include "WProgram.h"

#define ANALOG_MAX		255.0

Meter::Meter(int outputPin, float analogFullScale) :
	pin(outputPin),
	analogFullScale(constrain(analogFullScale, 0.0, 1.0))
{
}

void Meter::setup() {
	pinMode(pin, OUTPUT);
	digitalWrite(pin, LOW);
}

void Meter::setValue(float value) {
	int analogValue = int(ANALOG_MAX *
		analogFullScale * constrain(value, 0.0, 1.0));
	analogWrite(pin, analogValue);
}

