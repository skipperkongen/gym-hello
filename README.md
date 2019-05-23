A minimal template for OpenAI Gym environments.

## Installation

Install the [OpenAI gym](https://gym.openai.com/docs/).

Then install this package via

```
pip install -e .
```

## Usage

```
import gym
import gym_hello

env = gym.make('Hello-v0')
env.reset()

done = False
while not done:
    action = env.action_space.sample()
    state, reward, done, _ = env.step(action)
    print(state, reward, done)
```


## The Environment

The environment just implements the right interface with the minimal amount of code possible (well almost).
- the environment terminates after three steps
- the state is the number of steps left before termination
- there are two possible actions: 0 and 1.
- the reward is -1 per step, except for the last step where it is 100. The action makes no difference.
