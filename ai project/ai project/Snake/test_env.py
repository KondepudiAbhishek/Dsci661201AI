# test_env.py
from env import SnakeEnv
import time

env = SnakeEnv()
state = env.reset()
done = False
total_reward = 0

while not done:
    action = 0  # Try UP as default for now
    state, reward, done, _ = env.step(action)
    total_reward += reward
    time.sleep(0.05)

print("Finished one episode, total reward:", total_reward)
