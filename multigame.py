import tkinter as tk
import os

def launch_snake_game():
    os.system("python main.py")  

def launch_turtle_race():
    os.system("python turtle_race.py")  


def open_game_selection():
    game_selection_window = tk.Toplevel(root)
    game_selection_window.title("Select a Game")

    snake_game_button = tk.Button(game_selection_window, text="Snake Game", command=launch_snake_game)
    turtle_race_button = tk.Button(game_selection_window, text="Turtle Race", command=launch_turtle_race)

    snake_game_button.pack(pady=10)
    turtle_race_button.pack(pady=10)


root = tk.Tk()
root.title("Game Launcher")


root.geometry("400x400")

select_game_button = tk.Button(root, text="Select a Game", command=open_game_selection)
select_game_button.pack(pady=10)


root.mainloop()
