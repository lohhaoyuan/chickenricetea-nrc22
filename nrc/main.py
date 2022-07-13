#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import *
from statistics import * 
# Create your objects here.
ev3 = EV3Brick()
MotorLeft = Motor(Port.A)
MotorRight = Motor(Port.B)
MotorWater= Motor(Port.C)
MotorBlocks = Motor(Port.D)
left_color = ColorSensor(Port.S1)
right_color = ColorSensor(Port.S2)
bottom_color = ColorSensor(Port.S4)
gyro_sensor = GyroSensor(Port.S3)

robot = DriveBase(MotorLeft, MotorRight, wheel_diameter=55.5, axle_track=104)

# Write your program here.
ev3.speaker.beep()
ev3.speaker.beep()

ev3.speaker.beep()

ev3.speaker.beep()

ev3.speaker.beep()

ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()

# PID General Controller
def PID_Gyro(threshold, target, actual):
    robot.straight(500)
    kp = 1
    ki = 1
    kd = 1
    integral = 0
    derivative   = 0 
    output = 0
    error = target - actual
    previous = error
    while abs(error) > threshold:
        error = target - actual
        integral += error
        derivative = error - previous
        output = (kp * error) + (ki * integral) + (kd * derivative)
        MotorLeft.run(output)
        MotorRight.run(output * -1) 
    
        
# def PID_Colour(threshold, left_rgb, right_rgb, actual_rgb): # look yuzhe you arent dead
#     kp = 1
#     ki = 1
#     kd = 1
#     integral = 0 
#     derivative = 0
#     output = 0
#     error = (target_rgb(1)-actual_rgb(1),target_rgb(2)-actual_rgb(2),target_rgb(0)-actual_rgb(0))
#     previous = error
#     while abs(mean(error)) > threshold:
#         error = (target_rgb(1)-actual_rgb(1),target_rgb(2)-actual_rgb(2),target_rgb(0)-actual_rgb(0))
#         integral += mean(error)
#         derivative = (error(1)-previous(1),error(2)-previous(2),error(0)-previous(0))
# actual program
# Testing
# PID_Gyro(2,0,gyro_sensor.angle())
#while True:
 #   PID_Gyro(2,0,gyro_sensor.angle())
#
while True:
    if gyro_sensor.angle() >= 360:
        gyro_sensor.reset_angle(0)
    if gyro_sensor.angle() > 0:
        MotorLeft.run(1000)
    
# the picking stuff up FUNCTION


# the savepeopleandpickstuffup algorithm