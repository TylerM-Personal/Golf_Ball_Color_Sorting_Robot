# Smart Thermostat Fan

Bare-metal C and Assembly project for the TI LP-MSPM0G3507 LaunchPad and CSC202 expansion board. The controller reads a TMP61 thermistor and target-temperature potentiometer, calculates fan duty, and updates the displays and alarm.

![Smart thermostat fan architecture](../../assets/thermostat-fan-architecture.svg)

## Behavior

- PB2 starts or stops the fan controller. PB1 switches between the thermistor and potentiometer demo input.
- ADC channel 5 reads the thermistor, and channel 7 reads the target-temperature potentiometer.
- A 100 ms control period updates fan output. PB22 carries software PWM at 4 kHz; the code turns the buzzer on when the measured temperature is at least 10 °F above target.
- The LCD shows actual temperature, target temperature, and mode. The SPI LED bar and two-digit seven-segment display show fan duty. UART diagnostics run at 115200 baud.

## Source files

- `final_project_main.c` contains input processing, fan control, display updates, interrupt handlers, and alarm logic.
- `adc.*`, `clock.*`, `LaunchPad.*`, `lcd1602.*`, `spi.*`, and `uart.*` provide the local peripheral support files used by the application.
- `mspm0g3507.cmd` is the device linker command file.

The application header credits Tyler Mulvehill and Hakan Demirtas. Peripheral support files retain their original attribution to Bruce Link and their copyright notices. The linker command file retains Texas Instruments' redistribution terms. Building requires Code Composer Studio, the MSPM0 SDK, and the course expansion board definitions. Generated build directories and IDE caches are omitted.
