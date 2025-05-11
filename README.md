
# 🐍 Snake Game AI Using Deep Q-Learning — User Documentation

## 📌 Table of Contents
- [Introduction](#-introduction)
- [Features](#-features)
- [System Requirements](#-system-requirements)
- [Installation Guide](#-installation-guide)
- [Project Structure](#-project-structure)
- [How to Play](#-how-to-play)
- [AI Training Workflow](#-ai-training-workflow)
- [Testing the Trained Model](#-testing-the-trained-model)
- [Results](#-results)
- [Contributors](#-contributors)

## 🔍 Introduction
This project is a combination of classic game development and modern AI. We built a customizable Snake Game using Python and Pygame, and trained an AI agent to play it autonomously using Deep Q-Learning (DQN). The agent learns to make optimal decisions over time by interacting with the environment, collecting rewards, and avoiding penalties.

## ✨ Features
- Smooth and interactive gameplay using Pygame
- Sound effects and custom visuals
- AI agent using Deep Q-Network (DQN)
- Experience Replay and Neural Network-based training
- Visual tracking of training performance
- Autonomous gameplay using a trained model

## 🖥️ System Requirements
- Python 3.7+
- Pygame
- NumPy
- Matplotlib
- PyTorch

## ⚙️ Installation Guide

**Clone the repository:**
```bash
git clone https://github.com/KondepudiAbhishek/Dsci661201AI
cd Dsci661201AI
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

| File/Folder         | Description |
|---------------------|-------------|
| `snake_game.py`     | Manual Snake Game with GUI |
| `board_fast.py`     | Fast version used during AI training (no visuals) |
| `dqn.py`            | Neural network model (DQN) |
| `memory.py`         | Replay Memory buffer |
| `trainer.py`        | DQN trainer for updating the model |
| `train.py`          | Main script to train the agent |
| `env.py`            | Game environment logic for agent |
| `test_env.py`       | Test the environment independently |
| `test_model.py`     | Run evaluation of the trained model |
| `play_trained.py`   | Play using the trained agent |
| `dqn_snake_model.pth` | Saved trained model |
| `training_rewards.png` | Training performance visualization |

## 🎮 How to Play

### Manual Gameplay:
Run `snake_game.py` to play manually using arrow keys.

### Objective:
Eat apples 🟥, avoid walls and self-collision. The more apples eaten, the higher your score!

## 🧠 AI Training Workflow

- **Environment Setup:** `env.py` and `board_fast.py` define how the snake interacts and receives rewards.
- **Model Initialization:** `dqn.py` defines the neural network that predicts Q-values for moves.
- **Training Loop:** `train.py` runs multiple episodes to let the agent learn.
- **Memory Replay:** `memory.py` stores past experiences and feeds them during training.
- **Trainer Logic:** `trainer.py` updates model weights based on rewards.
- **Checkpointing:** Saves the trained model as `dqn_snake_model.pth`.

## ✅ Testing the Trained Model

Run:
```bash
python play_trained.py
```

This lets the trained snake play on its own. You’ll observe it:
- Move toward apples
- Avoid collisions
- Survive longer with smarter decisions

## 📈 Results

- The `training_rewards.png` graph shows improved performance over time.
- The agent learns complex behaviors by training over thousands of episodes.
- Demonstrates real-world reinforcement learning in a controlled game environment.

## 👨‍💻 Contributors
- Varun Yadav D
- Sai Abhishek
