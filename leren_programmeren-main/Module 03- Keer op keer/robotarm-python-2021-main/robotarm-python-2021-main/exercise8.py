from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.speed = 3
robotArm.moveRight()
for block in range (7):
    robotArm.grab()
    for move in range(8):
        robotArm.moveRight()
    robotArm.drop()
    if block <6:
        for move in range (8):
            robotArm.moveLeft()
robotArm.wait()