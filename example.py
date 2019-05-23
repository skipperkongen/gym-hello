import gym
import gym_hello

env = gym.make('Hello-v0')
env.reset()

done = False
while not done:
    action = env.action_space.sample()
    state, reward, done, _ = env.step(action)
    print(state, reward, done)
