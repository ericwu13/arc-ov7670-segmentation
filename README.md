# ov7670-segmentation

## ov7670 pin connection

OV7670

ARC: 2x18 Pin Extension Header
         
SIOC   ->    I2C0_SCL (need pull-up 10K resistor)

SIOD   ->    I2C0_SDA (need pull-up 10K resistor)

ARC: Arduino PIN

VSYBC  ->    arduino IO0

PCLK   ->    arduino IO1

XCLK   ->    arduino IO3

D7\~D0  ->    arduino IO4\~IO11


3V3    -> +3.3V

RESET  -> +3.3V

GND    -> GND

PWDN   -> GND

