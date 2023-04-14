from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 3
for stack in range (5):
    robotArm.moveRight()
    for box in range (6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if stack < 4:
        robotArm.moveRight()
robotArm.wait()