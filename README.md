# Space War

A two-player space battle game built with Python's `turtle` graphics library. Both players pilot ships on a shared battlefield, shooting at each other and navigating hazards to outscore their opponent.

## Gameplay

Two players compete head-to-head on a black space arena with a space-themed background:

- **Player 1** (yellow turtle, starts at the bottom) uses arrow keys to move and `Space` to fire.
- **Player 2** (green turtle, starts at the top) uses `Q`/`D` to turn, `Z`/`S` to accelerate/decelerate, and `K` to fire.

Each player has **3 lives** and starts with a score of 0. The game ends when a player loses all their lives.

### Scoring
| Event | Player 1 | Player 2 |
|---|---|---|
| Shoot an enemy (red circle) | +100 | — |
| Shoot an ally (blue square) | -50 | — |
| Shoot Player 2 | +100 | — |
| Shoot Player 1 | — | +100 |
| Shoot an enemy | — | -50 |
| Shoot an ally (blue square) | — | +100 |
| Hit by an enemy / ally | -100 | -100 |
| Players collide | -50 each | -50 each |

### Hazards
- **Red enemies** bounce around the arena — avoid them or shoot them.
- **Blue allies** bounce around too — Player 1 should avoid them; Player 2 should shoot them for points.

Explosions and sound effects play on every collision.

## Controls

| Key | Player 1 | Player 2 |
|---|---|---|
| Turn left | `←` | `Q` |
| Turn right | `→` | `D` |
| Accelerate | `↑` | `Z` |
| Decelerate | `↓` | `S` |
| Fire | `Space` | `K` |

## Getting Started

### Prerequisites
- Python 3.8 or higher
- macOS (sound effects use `afplay`)

### Setup
1. Clone or download this repository.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install any required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game
```bash
python main.py
```

## Project Structure
- [main.py](main.py) — Main entry point; contains all game logic and classes.
- `anti.gif` — Space background image.
- `laser.mp3` — Player 1 shoot sound.
- `boomerang.mp3` — Player 2 shoot sound.
- `explosion.mp3` — Collision/explosion sound.

## License
This project is licensed under the MIT License.
