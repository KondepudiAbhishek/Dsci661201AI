# dqn/memory.py
import random
from collections import deque
import numpy as np
import torch

class ReplayMemory:
    def __init__(self, capacity=100_000):
        self.memory = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        batch = random.sample(self.memory, batch_size)

        states, actions, rewards, next_states, dones = zip(*batch)

        return (
            torch.tensor(np.array(states), dtype=torch.float),
            torch.tensor(actions, dtype=torch.long),
            torch.tensor(rewards, dtype=torch.float),
            torch.tensor(np.array(next_states), dtype=torch.float),
            torch.tensor(dones, dtype=torch.bool)
        )

    def __len__(self):
        return len(self.memory)
