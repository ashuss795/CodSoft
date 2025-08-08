import random
import tkinter as tk
from tkinter import messagebox

OPTIONS = ['rock', 'paper', 'scissors']
EMOJIS = {
    'rock': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}
BTN_COLORS = {
    'rock': '#FFD580',       # Light orange
    'paper': '#A5D8FF',      # Light blue
    'scissors': '#FFABAB'    # Light pink
}

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.user_points = 0
        self.cpu_points = 0

        # Title
        tk.Label(root, text="Rock • Paper • Scissors", font=("Verdana", 18, "bold")).pack(pady=10)
        tk.Label(root, text="Pick one to start playing!", font=("Verdana", 12)).pack()

        # Buttons for user choice
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)

        self.buttons = {}
        for idx, choice in enumerate(OPTIONS):
            btn = tk.Button(
                btn_frame,
                text=f"{EMOJIS[choice]} {choice.title()}",
                width=14,
                font=("Verdana", 13, "bold"),
                bg=BTN_COLORS[choice],
                relief=tk.RAISED,
                command=lambda c=choice: self.play_round(c)
            )
            btn.grid(row=0, column=idx, padx=6)
            self.buttons[choice] = btn

        # Bind hover effect
        for btn in self.buttons.values():
            btn.bind("<Enter>", lambda e: e.widget.config(relief=tk.SUNKEN, bd=3))
            btn.bind("<Leave>", lambda e: e.widget.config(relief=tk.RAISED, bd=2))

        # Labels to display choices & results
        self.user_label = tk.Label(root, text="You chose: —", font=("Verdana", 11))
        self.user_label.pack()

        self.cpu_label = tk.Label(root, text="Computer chose: —", font=("Verdana", 11))
        self.cpu_label.pack()

        self.result_label = tk.Label(root, text="", font=("Verdana", 13, "bold"))
        self.result_label.pack(pady=5)

        self.score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Verdana", 12))
        self.score_label.pack(pady=10)

        # Exit button
        tk.Button(root, text="Quit Game", font=("Verdana", 11, "bold"), bg="#E0E0E0", command=self.end_game).pack(pady=5)

    def decide_winner(self, player, cpu):
        if player == cpu:
            return "draw"
        elif (player == 'rock' and cpu == 'scissors') or \
             (player == 'paper' and cpu == 'rock') or \
             (player == 'scissors' and cpu == 'paper'):
            return "player"
        else:
            return "cpu"

    def play_round(self, player_choice):
        cpu_choice = random.choice(OPTIONS)

        self.user_label.config(text=f"You chose: {EMOJIS[player_choice]} {player_choice.title()}")
        self.cpu_label.config(text=f"Computer chose: {EMOJIS[cpu_choice]} {cpu_choice.title()}")

        outcome = self.decide_winner(player_choice, cpu_choice)

        if outcome == "draw":
            self.result_label.config(text="It's a draw!", fg="blue")
        elif outcome == "player":
            self.result_label.config(text="You win this round!", fg="green")
            self.user_points += 1
        else:
            self.result_label.config(text="Computer wins this round!", fg="red")
            self.cpu_points += 1

        self.score_label.config(
            text=f"Score → You: {self.user_points} | Computer: {self.cpu_points}"
        )

    def end_game(self):
        summary = f"Final Score:\nYou: {self.user_points} | Computer: {self.cpu_points}\nThanks for playing!"
        messagebox.showinfo("Game Over", summary)
        self.root.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    game = RPSGame(window)
    window.mainloop()
