# Gomoku AI 🎯

An AI system designed to play the classic board game **Gomoku**, developed as part of an AI semester project. The system is evaluated against a Minimax baseline player to demonstrate its strategic decision-making capabilities.

## 📘 About the Game
**Gomoku** is a strategy board game where players alternate placing pieces on a square grid. The goal is to form an unbroken line of **five** pieces horizontally, vertically, or diagonally.

## 💡 Project Overview
This project implements a heuristic-based AI player that competes against a baseline **Minimax** player. It uses board evaluation techniques to make intelligent move decisions and block the opponent's winning paths.


## ⚙️ How It Works
### Key Methods:
- `Evaluate_Potential` – Calculates the score for each position based on possible future wins for both players.
- `Count_Consecutive` – Counts consecutive marks in all directions to identify potential winning opportunities.

The heuristic AI uses these scores to choose optimal moves, maximizing its chances to win while minimizing the opponent’s.

## 📊 Performance Evaluation
- The AI agent (from `submission.py`) competes with the Minimax agent in 30 rounds.
- Scores and execution time are recorded.
- A lower (more negative) score indicates stronger AI performance over Minimax.

