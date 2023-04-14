from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 3
for x in range(0, 8):
    robotArm.moveRight()
for box in range(0, 9):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        if box <8:
            robotArm.moveLeft()
robotArm.wait()