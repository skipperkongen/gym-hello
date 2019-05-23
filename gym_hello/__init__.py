from gym.envs.registration import register

register(
    id='Hello-v0',
    entry_point='gym_hello.envs:HelloEnv',
)
