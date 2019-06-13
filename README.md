# CareBaby -- Baby Caretaking Micro-Robot System

This application, which implements a image semantic segmentation on ARC IoT board, is designed to show how to use camera and Machine Learning in embARC to save your baby from entering dangerous section in your home, such as kitchen.

* [Introduction](#introduction)
	* [System Architecture](#system-architecture)
* [Hardware and Software Setup](#hardware-and-software-setup)
	* [Required Hardware](#required-hardware)
	* [Required Software](#required-software)
	* [Hardware Connection](#hardware-connection)
* [User Manual](#user-manual)
	* [Before Running This Application](#before-running-this-application)
	* [Run This Application](#run-this-application)

## Introduction
A hazard detection system to prevent the baby creeping to dangerous section in your house by utilizing image segmentation. We could track location of the baby in the home precisely
and later alarm parents when the baby enters dangerous scenes.


### System Architecture
![][3]

## Hardware and Software Setup
### Required Hardware
- [ARC IoT Development Kit][1]
- [OV7670 Camera Module][2]
- [Arduino]
- [HC-05]
- [1.8" TFT LCD Screen]
- [Micro-Robot Car]

### Required Software
- ARC GNU Toolset 2019
- Serial port terminal, such as putty, tera-term or minicom
- embARC MLI

### Hardware Connection
1. Connect OV7670 camera module to ARC following below instructions

        # ARC: 2x18 Pin Extension Header
        SIOC   ->    I2C0_SCL (need pull-up 10K resistor)
        SIOD   ->    I2C0_SDA (need pull-up 10K resistor)

        # ARC: Arduino PIN
        VSYBC  ->    arduino IO0
        PCLK   ->    arduino IO1
        XCLK   ->    arduino IO3
        D7~D0  ->    arduino IO4~IO11

        3V3    -> +3.3V
        RESET  -> +3.3V
        GND    -> GND
        PWDN   -> GND

2. Connect 1.8" TFT LCD screen to ARC spi interface

3. Connect HC-05 to arduino and prepared the necessary micro-robot car

## User Manual
[1]: https://embarc.org/embarc_osp/doc/build/html/board/iotdk.html "ARC IoT Development Kit"
[2]: https://www.voti.nl/docs/OV7670.pdf "OV7670 Camera Module"
[3]: ./doc/system.png "System Architecture"
