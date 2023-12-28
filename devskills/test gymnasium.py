import gym
import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from rl.agents import DNQAgent
from rl.policy import Boltzmanqpolicy
from rl.memory import Sequentialmemory

env = gym.make('CartPole-v1', render_mode = 'human')
states = env.observation_space.shape[0]
actions = env.action_space.n


model = Sequential()
model.add(Flatten(input_shape=(1,states)))
model.add(Dense(24,activation="relu"))
model.add(Dense(24,activation="relu"))
model.add(Dense(actions, activation="linear"))


agent = DNQAgent(
    model = model,
    memory = Sequentialmemory(limit=50000, window_length=1),
    policy = Boltzmanqpolicy(),
    nb_actions=actions,
    nb_steps_warmup = 10,
    target_model_update=0.01
)
agent.compile(Adam(lr=0.001), metrics =["mae"])
agent.fit(env, nb_steps=100000, visualize = False, verbose=1)
result = agent.test(env, nb_episodes=10, visualize=True)
print(np.mean(result.history["episodes_reward"]))

# episodes = 10
# for episode in range (1,episodes+1):
#     state = env.reset()
#     done = False
#     score = 0
#     while not done:
#         env.render()
#         action = random.choice([0,1])
#         n_state, reward, done , info = env.step(action)
#         score+= reward
#         env.render()
#         print('Episode:{} score:{} '.format(episode,score))

env.close