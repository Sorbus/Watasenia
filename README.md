# Watasenia
DIY RGB Caselighting

Watasenia scintillans is the firefly squid, a bioluminescent squid mostly found in the Wester Pacific ocean.

The software that shares its name is used to control a DIY RGB Caselighting solution using WS2812b LEDs.

# Usage

## Configuration

Minimum part list:

* WS2812b RGB LED string
* Molex power plug (or SATA power to 4-pin molex adapter)
* Arduino (a Nano is recommended)
* USB Cable (Mini-B required for Arduino Nano, USB 2.0 Header Adapter recommended to keep all components inside the case)

![Hardware Schematic](https://raw.githubusercontent.com/Sorbus/Watasenia/master/Schematic.png)

As illustrated in the schematic above, the string of WS2812b RGB LEDs is powered using the 4-pin molex plug's +5V line and grounded to one of the two grounds. This allows the LED string to be powered from the computer's power supply. Optionally the Arduino can also be powered from the 4-pin molex plug, but since it can also be powered by its USB connection this is not essential.

One of the Arduino's digital output pins is then connected to the LED string's digital input (DIN), and the Arduino is connected to the host computer via USB.

> For ease of use, we recommend using 3-pin molex plugs to separate segments which may need to be disconnected or to accomodate bends in the case. Since most LED strings can be easily cut, it is a simple matter to add these breaks.

The Arduino program in arduino/ledControl is uploaded to the Arduino after two modifications: DATA_PIN must be set to match the actual configuration, and NUM_LEDS must be set to match the number of LEDs in the strand.

## Usage


# Notes and Caveats

* At the current time, the software is Windows-only. This is primarily due to the temperature monitoring module. Since temperature monitoring on Linux is much easier than on Windows, it would be quite easy to add support for other operating systems.
* On Windows, OpenHardwareMonitor must be running for temperating monitoring to work properly. It may be possible to work around this limitation, but at the present time this feature has not been added.
* Currently, the ledControl program only supports an LED strand on a single pin. It would be easy to add support for additional strands, but at present it seems best to do this on a case-by-case basis.
