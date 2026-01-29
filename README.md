
# World-Centric Agency Game

Research prototype accompanying the paper:
'Playing Without Moving: World-Centric Agency in Embodied Camera-Based Games'

## Requirements
- Python 3.9+
- OpenCV
- MediaPipe
- NumPy

## Run
python main.py

## Modes
Change mode in main.py:
neutral | heavy | distorted
Research prototype for the paper **"Playing Without Moving: World-Centric Agency in Embodied Camera-Based Games"**.

## 📋 Overview
This study investigates how manipulating the virtual environment (rather than player input) affects perceived agency in camera-based games.

## 🚀 Quick Start
1.  **Clone & Install:**
    ```bash
    git clone https://github.com/Giantpixeel/world-centric-agency-game.git
    cd world-centric-agency-game
    pip install -r requirements.txt
    ```
2.  **Run the Prototype:**
    ```bash
    # Neutral world (1:1 mapping)
    python main.py --mode neutral
    # Heavy world (simulated resistance)
    python main.py --mode heavy
    # Distorted world (non-linear response)
    python main.py --mode distorted
