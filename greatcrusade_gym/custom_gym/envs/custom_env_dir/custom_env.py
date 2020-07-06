import gym


class CustomEnv(gym.Env):
    def __init__(self):
        print('Environment initialized')
        print('f')

    def step(self, **kwargs):
        print('Step successful!')

    def reset(self):
        print('Environment reset')
