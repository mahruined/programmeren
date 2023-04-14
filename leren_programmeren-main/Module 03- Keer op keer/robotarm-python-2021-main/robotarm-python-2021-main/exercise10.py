from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
moves = 8
robotArm.grab()
for i in range(4):
    for x in range(moves):
        robotArm.moveRight()   
    robotArm.drop()
    moves = moves - 1
    for x in range(moves):
        robotArm.moveLeft()
    if i < 3:
        robotArm.grab()
    moves = moves - 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()