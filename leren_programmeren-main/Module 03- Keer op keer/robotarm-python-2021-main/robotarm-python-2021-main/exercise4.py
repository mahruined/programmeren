from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
for x in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    if x < 4:
        robotArm.moveLeft()
        robotArm.moveLeft() 
for x in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
   
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()