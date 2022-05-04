#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import os, sys

# This program requires LEGO EV3 MicxroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
MotorA = Motor(Port.A)
MotorB = Motor(Port.B)
MotorC= Motor(Port.C)
MotorD = Motor(Port.D)
left_color = EV3ColorSensor()
right_color = EV3ColorSensor()
bottom_color = EV3ColorSensor()
gyro_sensor = EV3GyroSensor()
# Write your program here.

# starting algorithm


# the picking stuff up FUNCTION


# the savepeopleandpickstuffup algorithm

