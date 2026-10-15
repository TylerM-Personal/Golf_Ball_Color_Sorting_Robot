# EV3 Hockey Puck Robo

Pybricks MicroPython program for an EV3 robot that follows a marked route, detects checkpoints, and shoots pucks toward a goal.

![EV3 hockey robot architecture](../../assets/ev3-hockey-robot-architecture.svg)

## How it works

- The color sensor on port S4 supplies reflected-light readings for line following and checkpoint detection.
- The ultrasonic sensor on port S2 checks distance near the goal.
- Motors on ports C and B drive the robot; the arm motor runs the puck launcher sequence.
- The program combines route segments, proportional line-following corrections, color thresholds, and distance checks. Its source contains five puck-shot sequences.

## Run i

Use an EV3 running Pybricks MicroPython. Transfer `hockey_robot.py` to the brick and run it with the sensors and motors connected to the ports declared at the top of the file. The course surface and sensor thresholds affect line and checkpoint detection, so verify them against the field before a run.
