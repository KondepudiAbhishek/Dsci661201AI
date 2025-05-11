# dqn/trainer.py
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class DQNTrainer:
    def __init__(self, model, target_model, lr=0.001, gamma=0.9):
        self.model = model
        self.target_model = target_model
        self.gamma = gamma
        self.optimizer = optim.Adam(model.parameters(), lr=lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        # No need to unsqueeze for MLP
        pred_q = self.model(state)
        target_q = pred_q.clone().detach()

        for idx in range(len(done)):
            q_next = self.target_model(next_state[idx].unsqueeze(0))
            max_q_next = torch.max(q_next).item()

            if done[idx]:
                new_q = reward[idx]
            else:
                new_q = reward[idx] + self.gamma * max_q_next

            target_q[idx][action[idx]] = new_q

        pred_q = self.model(state)
        loss = self.criterion(pred_q, target_q)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.item()
