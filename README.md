# Image Segmentation Robot System

This application, which implements a image semantic segmentation on ARC IoT board, is designed to show how to use camera and Machine Learning in embARC.

* [Introduction](#introduction)
	* [Function](#function)
	* [System Architecture](#system-architecture)
* [Hardware and Software Setup](#hardware-and-software-setup)
	* [Required Hardware](#required-hardware)
	* [Required Software](#required-software)
	* [Hardware Connection](#hardware-connection)
* [User Manual](#user-manual)
	* [Before Running This Application](#before-running-this-application)
	* [Run This Application](#run-this-application)

## Introduction
This project was successful in achieving a two-wheeled autonomous robot based on the inverted pendulum model.EMSK works as controller, it will deal with sensor datas and interact with user via bluetooth. We can view all data on serial terminal, and sent instructions to the robot to change its motion mode.

### Function

### System Architecture
![system architecture][4]

## Hardware and Software Setup
### Required Hardware
- 1 [DesignWare ARC EM Starter Kit(EMSK V2.3)][5]
- 2 [BLE module(HC-05)][6]
- 1 [USB To TTL module(CP2102)][7]
- 1 [IMU module(MPU6050)][8]
- 1 [Motor Driver][9]
- 1 [Voltage Conversion module(7805)][10]
- 1 NiCd Battery
- 1 SD Card
- 1 SPI to QEI AND PWM Expanding-board
- 1 Robot Platform
	![Robot Platform][11]
### Required Software
- ARC GNU Toolset 2017.03
- Serial port terminal, such as putty, tera-term or minicom
- 

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

## User Manual

