import torch
import random
import numpy as np
from env import SnakeEnv
from dqn.dqn import DQN
from dqn.memory import ReplayMemory
from dqn.trainer import DQNTrainer
import matplotlib.pyplot as plt

MAX_EPISODES = 1000
BATCH_SIZE = 1000
MEMORY_CAPACITY = 100_000 
EPSILON_START = 1.0
EPSILON_END = 0.01
EPSILON_DECAY = 0.999

def train():
    env = SnakeEnv()
    model = DQN()
    target_model = DQN()
    target_model.load_state_dict(model.state_dict())
    trainer = DQNTrainer(model, target_model)
    memory = ReplayMemory(MEMORY_CAPACITY)

    epsilon = EPSILON_START
    all_rewards = []

    for episode in range(1, MAX_EPISODES + 1):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            if random.random() < epsilon:
                action = random.randint(0, 3)
            else:
                with torch.no_grad():
                    state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
                    q_values = model(state_tensor)
                    action = torch.argmax(q_values).item()

            next_state, reward, done, _ = env.step(action)
            memory.push(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward

            if len(memory) > BATCH_SIZE:
                batch = memory.sample(BATCH_SIZE)
                trainer.train_step(*batch)

        if episode % 10 == 0:
            target_model.load_state_dict(model.state_dict())

        all_rewards.append(total_reward)
        epsilon = max(EPSILON_END, epsilon * EPSILON_DECAY)

        print(f"Episode {episode} - Reward: {total_reward:.2f} - Epsilon: {epsilon:.3f}")

    torch.save(model.state_dict(), "dqn_snake_model.pth")
    plt.plot(all_rewards)
    plt.title("Episode Rewards")
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.grid()
    plt.savefig("training_rewards.png")

if __name__ == "__main__":
    train()
