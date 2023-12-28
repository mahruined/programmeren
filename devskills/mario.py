import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from nes_py.wrappers import JoypadSpace
# from gym.wrappers import frame_stack, gray_scale_observation
# from stable_baseline3.common.ver_env import vecframestack, dummyvecenv
# from matplotlib import pyplot as plt
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env,SIMPLE_MOVEMENT)


#restart or not
done = True
for step in range(100000):
    if done:
        # start the game
        env.reset()
        # does random actions
    state, reward, done, info = env.step(env.action_space.sample())
    #shows the game
    env.render()
    #closes the game
env.close()

