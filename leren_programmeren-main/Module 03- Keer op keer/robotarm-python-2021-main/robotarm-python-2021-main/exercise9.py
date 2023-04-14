from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 3
for stack in range(1,5):
    for box in range(stack):
        robotArm.grab()
        for move in range (5):
            robotArm.moveRight()
        robotArm.drop()
        for move in range (5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()