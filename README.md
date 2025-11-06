# Console RPG: Turn-Based Boss Battle with Timing System

A Python-based console RPG that combines **turn-based combat** with **real-time quick-time events (QTEs)** for attacking and blocking.  
Featuring dynamic color-coded timing bars, player mana management, and boss AI turns — all playable directly in your terminal.

---

## Project Structure

project_root/
│
├── main.py
│
├── characters/
│ ├── init.py
│ ├── base_character.py
│ ├── player_team.py
│ └── boss.py
│
├── combat/
│ ├── init.py
│ ├── battle.py
│ └── timing_bar.py
│
└── data/
├── players.json
└── bosses.json


---

## Setup Instructions

1. **Clone or Download** the repository.

2. Ensure you have **Python 3.10+** installed.  
   (The game uses threading and ANSI color sequences compatible with most modern terminals.)

3. **Run the game:**
   ```bash
   python main.py
