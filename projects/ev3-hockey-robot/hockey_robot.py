#!/usr/bin/env pybricks-micropython
# general navigation

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.nxtdevices import UltrasonicSensor, TouchSensor, LightSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

# Objects to Build
left = Motor(Port.C)
right = Motor(Port.B)
driver = DriveBase(left, right, 43.2, 120)
current = StopWatch()
colorsensor = ColorSensor(Port.S4)
linefollowing = ColorSensor(Port.S4)
ultrasonic = UltrasonicSensor(Port.S2)
Arm = Motor(Port.d)

def line_following(x):
    BLACK = 30
    WHITE = 70
    PROPORTIONAL_GAIN = 0.8
    DRIVE_SPEED = 120
    threshold = (BLACK + WHITE) / 2

    while driver.distance() < x:
        deviation = linefollowing.reflection() - threshold
        turn_rate = PROPORTIONAL_GAIN * deviation
        driver.drive(DRIVE_SPEED, turn_rate)
        wait(10)


driver.settings(350,350,300,300)

# First black line navigation and turn
count = 0
for count in range(0,50000000):
    if colorsensor.reflection() <= 9:
        driver.stop()
        break
    else:
        driver.drive(200,0)
        wait(10)
        count +=1

driver.reset()
driver.straight(-10)
driver.turn(-90)
driver.reset()


# Follow black line to blue line & center in front of goal from there
while driver.distance() < 700:
    BLACK = 30
    WHITE = 70
    PROPORTIONAL_GAIN = 0.8
    DRIVE_SPEED = 130
    threshold = (BLACK + WHITE) / 2
    deviation = linefollowing.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    driver.drive(DRIVE_SPEED, turn_rate)
    wait(10)


driver.turn(-90)
driver.straight(390)
driver.turn(-90)

count = 0
for count in range(0,50000000):
    if colorsensor.reflection() <= 9:
        driver.stop()
        break
    else:
        driver.drive(200,0)
        wait(10)
        count +=1

driver.straight(200)
driver.reset()
wait(10)
#infront of goal


# Use ultrasonic to shoot blue puck number one
count = 0
for count in range(0,200):
    if ultrasonic.distance() >= 21:
        Arm.run_angle(10000, 100, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, 100, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        break
    else:
        wait(400)
        count +=1


# Navigate backwards onto blue line and turn to follow
driver.reset()
driver.straight(-520)
driver.turn(90)
driver.reset()

# Navigate up the blue line then stop at the black
while True:
    BLACK = 40
    WHITE = 70
    PROPORTIONAL_GAIN = 0.6
    DRIVE_SPEED = 140
    threshold = (BLACK + WHITE) / 2
    deviation = linefollowing.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    driver.drive(DRIVE_SPEED, turn_rate)

    if colorsensor.reflection() <=9:
        driver.stop()
        break

driver.reset()

#line follow for distance and turn to grab second blue puck

left.run_angle(500, 380, then=Stop.HOLD, wait=True)
driver.reset()

while driver.distance() <= 1850:
    BLACK = 30
    WHITE = 70
    PROPORTIONAL_GAIN = .75
    DRIVE_SPEED = 140
    threshold = (BLACK + WHITE) / 2
    deviation = linefollowing.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    driver.drive(DRIVE_SPEED, turn_rate)
    wait(10)
driver.reset()
#should pick up second blue puck and stop in front of blue goal for orientation
#turn and start navigating to other side of board
driver.turn(90)
driver.straight(30)
driver.reset()

#go straight until blue line is detected
count = 0
for count in range(0,50000000):
    if colorsensor.reflection() <= 15:
        driver.stop()
        break
    else:
        driver.drive(200,0)
        wait(10)
        count +=1

driver.straight(150)
driver.turn(-90)
driver.reset()

#turn and continue to follow blue line and stop at black to follow
while True:
    BLACK = 40
    WHITE = 70
    PROPORTIONAL_GAIN = 0.6
    DRIVE_SPEED = 140
    threshold = (BLACK + WHITE) / 2
    deviation = linefollowing.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    driver.drive(DRIVE_SPEED, turn_rate)

    if colorsensor.reflection() <=10:
        driver.stop()
        break
driver.reset()

#turn and follow black line
driver.straight(15)
driver.turn(90)
driver.reset()
wait(10)

#detect second blue line and stop plz
driver.straight(805)

driver.reset()
driver.turn(90)
driver.straight(390)
driver.turn(-90)
driver.straight(30)

count = 0
for count in range(0,50000000):
    if colorsensor.reflection() <= 9:
        driver.stop()
        break
    else:
        driver.drive(200,0)
        wait(10)
        count +=1

driver.straight(200)
driver.reset()
wait(10)

#should be infront of goal with second blue puck

#second shot of blue puck acquired pew pew
count = 0
for count in range(0,200):
    if ultrasonic.distance() >= 200:
        Arm.run_angle(10000, 100, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, 100, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        break
    else:
        wait(400)
        count +=1


#back up to  black line to follow and pick up first red puck and naviagte to first blue line
driver.straight(-100)
driver.turn(80)

while True:
    BLACK = 30
    WHITE = 70
    PROPORTIONAL_GAIN = 0.8
    DRIVE_SPEED = 120
    threshold = (BLACK + WHITE) / 2
    deviation = linefollowing.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    driver.drive(DRIVE_SPEED, turn_rate)

    if colorsensor.reflection() > 13 and colorsensor.reflection() <=15:
        driver.stop()
        break

wait(10)
driver.reset()
driver.straight(805)
driver.reset()

#use this point to line follow for distance and navigate to front of goal
while driver.distance() <= 700:
    BLACK = 30
    WHITE = 70
    PROPORTIONAL_GAIN = 1
    DRIVE_SPEED = 120
    threshold = (BLACK + WHITE) / 2
    deviation = linefollowing.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    driver.drive(DRIVE_SPEED, turn_rate)
    wait(10)

driver.reset()
driver.turn(-90)


#shoot in first red puck into goal
count = 0
for count in range(0,200):
    if ultrasonic.distance() >= 200:
        Arm.run_angle(10000, 90, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, 90, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        break
    else:
        wait(400)
        count +=1


#start to turn and find second red puck
driver.turn(90)

#line follow until blue line is detected and stop
while True:
    BLACK = 30
    WHITE = 70
    PROPORTIONAL_GAIN = 0.8
    DRIVE_SPEED = 120
    threshold = (BLACK + WHITE) / 2
    deviation = linefollowing.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    driver.drive(DRIVE_SPEED, turn_rate)

    if colorsensor.reflection() > 12 and colorsensor.reflection() <=14:
        driver.stop()
        break


#navigate infront of goal from blue line
wait(10)
driver.reset()
driver.turn(90)
driver.straight(390)
driver.turn(90)
driver.straight(520)

#shoot second red puck
count = 0
for count in range(0,200):
    if ultrasonic.distance() >= 200:
        Arm.run_angle(10000, 100, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, 100, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        break
    else:
        wait(400)
        count +=1



#black pucks time to shine (THESE VALUES ARE GUESSTIMATES)
driver.straight(-200)
driver.turn(180)
driver.straight(1300)

#shoot in final black puck!
count = 0
for count in range(0,200):
    if ultrasonic.distance() >= 200:
        Arm.run_angle(10000, 90, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, 90, then=Stop.HOLD, wait=True)
        wait(50)
        Arm.run_angle(10000, -80, then=Stop.HOLD, wait=True)
        break
    else:
        wait(400)
        count +=1

#voila
