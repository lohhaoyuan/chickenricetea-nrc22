#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from math import *
# Create your objects here.
ev3 = EV3Brick()
MotorLeft = Motor(Port.A)
MotorRight = Motor(Port.B)
MotorWater= Motor(Port.C)
MotorBlocks = Motor(Port.D)
left_color = ColorSensor()
right_color = ColorSensor()
bottom_color = ColorSensor()
gyro_sensor = GyroSensor()
# Write your program here.

# PID General Controller
def PID_Gyro(threshold, target, actual):
    kp = 200
    ki = 1
    kd = 1
    integral = 0
    derivative = 0
    output = 0
    while abs(error) > threshold:
        error = target - actual
        integral += error
        derivative = error - previous
        output = (kp * error) + (ki * integral) + (kd * derivative)
        MotorLeft.run(output)
        MotorRight.un(output * -1)
        previous = error
        print(f"error is now {error}, output is now: {output}")

# actual program

# Testing
PID_Gyro(2,0,gyro_sensor.angle())
# the picking stuff up FUNCTION


# the savepeopleandpickstuffup algorithm