
import tkinter as tk
import random

# ---------------- GAME VARIABLES ----------------
cs = 0
hs = 0

choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissor"
}


# ---------------- GAME LOGIC ----------------
def play(user_choice):

    global cs, hs

    # If game is already over
    if hs == 5 or cs == 5:
        return

    comp = random.randint(1, 3)

    user_text = choices[user_choice]
    comp_text = choices[comp]

    # Display choices
    user_choice_label.config(text=f"You chose: {user_text}")
    computer_choice_label.config(text=f"Computer chose: {comp_text}")

    # Decide winner
    if user_choice == 1 and comp == 3:
        hs += 1
        result_label.config(text="🎉 You Win!", fg="green")

    elif user_choice == 2 and comp == 1:
        hs += 1
        result_label.config(text="🎉 You Win!", fg="green")

    elif user_choice == 3 and comp == 2:
        hs += 1
        result_label.config(text="🎉 You Win!", fg="green")

    elif user_choice == comp:
        result_label.config(text="🤝 Draw!", fg="orange")

    else:
        cs += 1
        result_label.config(text="💻 Computer Wins!", fg="red")

    # Update score
    score_label.config(
        text=f"You: {hs}       Computer: {cs}"
    )

    # Check overall winner
    if hs == 5:
        result_label.config(
            text="🏆 YOU ARE THE OVERALL WINNER!",
            fg="green"
        )
        disable_buttons()

    elif cs == 5:
        result_label.config(
            text="💻 COMPUTER IS THE OVERALL WINNER!",
            fg="red"
        )
        disable_buttons()


# ---------------- DISABLE BUTTONS ----------------
def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissor_button.config(state="disabled")


# ---------------- RESTART GAME ----------------
def restart_game():

    global cs, hs

    cs = 0
    hs = 0

    score_label.config(text="You: 0       Computer: 0")
    user_choice_label.config(text="You chose: -")
    computer_choice_label.config(text="Computer chose: -")
    result_label.config(text="Choose your move!", fg="white")

    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")


# ---------------- WINDOW ----------------
root = tk.Tk()

root.title("Rock Paper Scissor")
root.geometry("600x650")
root.configure(bg="#121212")
root.resizable(False, False)


# ---------------- TITLE ----------------
title_label = tk.Label(
    root,
    text="ROCK PAPER SCISSOR",
    font=("Arial", 28, "bold"),
    bg="#121212",
    fg="white"
)

title_label.pack(pady=(30, 10))


# ---------------- SUBTITLE ----------------
subtitle_label = tk.Label(
    root,
    text="First to 5 wins!",
    font=("Arial", 14),
    bg="#121212",
    fg="#aaaaaa"
)

subtitle_label.pack(pady=5)


# ---------------- SCORE ----------------
score_label = tk.Label(
    root,
    text="You: 0       Computer: 0",
    font=("Arial", 20, "bold"),
    bg="#121212",
    fg="white"
)

score_label.pack(pady=25)


# ---------------- CHOICES ----------------
user_choice_label = tk.Label(
    root,
    text="You chose: -",
    font=("Arial", 15),
    bg="#121212",
    fg="#dddddd"
)

user_choice_label.pack(pady=5)


computer_choice_label = tk.Label(
    root,
    text="Computer chose: -",
    font=("Arial", 15),
    bg="#121212",
    fg="#dddddd"
)

computer_choice_label.pack(pady=5)


# ---------------- RESULT ----------------
result_label = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 20, "bold"),
    bg="#121212",
    fg="white"
)

result_label.pack(pady=30)


# ---------------- BUTTON FRAME ----------------
button_frame = tk.Frame(
    root,
    bg="#121212"
)

button_frame.pack(pady=10)


# ---------------- ROCK BUTTON ----------------
rock_button = tk.Button(
    button_frame,
    text="🪨\nRock",
    font=("Arial", 16, "bold"),
    width=10,
    height=3,
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=lambda: play(1)
)

rock_button.grid(row=0, column=0, padx=10)


# ---------------- PAPER BUTTON ----------------
paper_button = tk.Button(
    button_frame,
    text="📄\nPaper",
    font=("Arial", 16, "bold"),
    width=10,
    height=3,
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=lambda: play(2)
)

paper_button.grid(row=0, column=1, padx=10)


# ---------------- SCISSORS BUTTON ----------------
scissor_button = tk.Button(
    button_frame,
    text="✂️\nScissor",
    font=("Arial", 16, "bold"),
    width=10,
    height=3,
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=lambda: play(3)
)

scissor_button.grid(row=0, column=2, padx=10)


# ---------------- RESTART BUTTON ----------------
restart_button = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Arial", 14, "bold"),
    width=20,
    height=2,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    command=restart_game
)

restart_button.pack(pady=35)


# ---------------- START APPLICATION ----------------
root.mainloop()



#RPSGame is run through the Terminal