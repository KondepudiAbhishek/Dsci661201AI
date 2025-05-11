import torch
from dqn.dqn import DQN
from env import SnakeEnv

def test_trained_model(model_path="dqn_snake_model.pth"):
    env = SnakeEnv()
    state = env.reset()

    model = DQN()
    model.load_state_dict(torch.load(model_path))
    model.eval()

    with torch.no_grad():
        state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
        q_values = model(state_tensor)

    print("Q-values:", q_values)

if __name__ == "__main__":
    test_trained_model()
