# 🗺️ U.S. States Geography Game

An interactive Python game where the user is challenged to name all 50 U.S. states. Each correct guess appears on a U.S. map using Turtle graphics, and missed states are saved to a CSV file for review.

---

## 📌 Project Overview

This project was created as a fun and educational way to practice Python while reinforcing U.S. geography knowledge. It uses the `turtle` module to display a blank map and `pandas` to handle data from a CSV file containing state names and their x/y coordinates.

If the player gives up by entering `Exit`, the program generates a new file—`states_to_learn.csv`—listing all the states they missed.

---

## 🛠️ Techniques Used

- Python 3
- [Turtle Graphics](https://docs.python.org/3/library/turtle.html)
- Pandas
- CSV for data storage

---

## 🎮 How It Works

1. A blank map of the United States is displayed using a `.gif` image.
2. The user is prompted to guess the name of a state.
3. If the guess is correct, the state name is written at the correct position on the map.
4. The game continues until all 50 states are guessed or the user types `"Exit"`.
5. Upon exiting, the game creates `states_to_learn.csv` with the states the user missed.

---

## 📂 Files Included

- `main.py` – The main game script
- `50_states.csv` – Contains the list of all U.S. states with their corresponding x/y coordinates
- `blank_states_img.gif` – The U.S. map image used in the game
- `states_to_learn.csv` – Generated file containing missed states (created after exiting the game)

---

## ✅ Skills Practiced

- Data manipulation with pandas
- GUI and coordinate plotting with turtle graphics
- Real-time user input and control flow
- File input/output using CSVs
