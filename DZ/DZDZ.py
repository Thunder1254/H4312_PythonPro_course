# Labyrinth Solver using ONLY front distance sensor
# Works in VEXcode VR Python
# Author: ChatGPT

from vex import *

# Brain and drivetrain setup (default VR Robot)
brain = Brain()
drivetrain = Drivetrain()

# Variables
turn_direction = "left"
blocked_count = 0

# Settings
drive_speed = 40
turn_speed = 30
drivetrain.set_drive_velocity(drive_speed, PERCENT)
drivetrain.set_turn_velocity(turn_speed, PERCENT)

# Helper functions
def move_forward():
    drivetrain.drive(FORWARD)

def stop_moving():
    drivetrain.stop()

def turn_left():
    drivetrain.turn_for(LEFT, 90, DEGREES)

def turn_right():
    drivetrain.turn_for(RIGHT, 90, DEGREES)

def back_up():
    drivetrain.drive_for(REVERSE, 200, MM)

# Main loop
while True:
    front_distance = drivetrain.distance(DistanceUnits.MM)

    # If wall detected close ahead
    if front_distance < 100:
        stop_moving()
        blocked_count += 1

        # Too many turns = likely stuck
        if blocked_count > 3:
            brain.screen.print("Backing up to escape loop...")
            back_up()
            blocked_count = 0
            turn_right()
            wait(0.5, SECONDS)
        else:
            # Alternate turns
            if turn_direction == "left":
                turn_left()
                turn_direction = "right"
            else:
                turn_right()
                turn_direction = "left"

    else:
        # Path is clear
        move_forward()
        blocked_count = 0


if brain.down_eye.detect(Colors.RED):
    stop_moving()
    brain.screen.print("Maze completed!")
    break
