import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from nes_py.wrappers import JoypadSpace

env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env,SIMPLE_MOVEMENT)

done = True
for step in range(100000):
    if done:
        env.reset()
    state , reward , done , info = env.step(env.action_space.sample())
    env.render()
env.close()