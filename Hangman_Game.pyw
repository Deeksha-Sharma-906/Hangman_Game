import tkinter as tk
import random

# -----------------------------
# Hangman ASCII Art (Stages)
# -----------------------------
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# -----------------------------
# Word List (Expanded)
# -----------------------------
WORDS = [
    "able","about","acid","act","ball","bread","camera","country","danger","education",
    "flower","friend","gold","happy","important","machine","manager","monkey","mountain",
    "orange","possible","process","public","question","science","station","structure",
    "umbrella","writing","beautiful","agreement","adventure","excellence","university",
    "architecture","environment","communication","responsible",
    'python', 'java', 'kotlin', 'swift', 'programming', 'developer',
    'hangman', 'statistics', 'visualization', 'algorithm', 'function', 'variable', 'database', 
    'network', 'software', 'hardware', 'computer', 'engineer', 'project', 'innovation', 
    'performance', 'design', 'automation'
]

# -----------------------------
# 🧠 Difficulty Filter
# -----------------------------
def get_words_by_mode(mode):
    if mode == "Easy":
        return [w for w in WORDS if 4 <= len(w) <= 5]
    elif mode == "Medium":
        return [w for w in WORDS if 6 <= len(w) <= 8]
    elif mode == "Hard":
        return [w for w in WORDS if 9 <= len(w) <= 10]
    elif mode == "Expert":
        return [w for w in WORDS if 12 <= len(w) <= 14]
    else:
        return WORDS


# -----------------------------
# Main Game Class
# -----------------------------
class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game 🎯")
        self.master.geometry("650x700")
        self.master.config(bg="#9ca5ad")
        
        self.word = ""
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.MAX_WRONG = len(HANGMAN_STAGES) - 1
       
        self.create_difficulty_screen()
    
    # -----------------------------
    # Difficulty Selection Screen
    # -----------------------------
    def create_difficulty_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()


        tk.Label(self.master, text="🎯 Choose Difficulty", font=("Arial", 24, "bold"), bg="#9ca5ad").pack(pady=30)
        
        for level in ["Easy", "Medium", "Hard", "Expert"]:
            tk.Button(self.master, text=level, font=("Arial", 16, "bold"), width=15, 
                      bg="#0d6efd", fg="white", command=lambda l=level: self.start_game(l)).pack(pady=10)
    
    # -----------------------------
    # Start Game
    # -----------------------------
    def start_game(self, difficulty):
        self.word = random.choice(get_words_by_mode(difficulty)).upper()
        self.guessed_letters = []
        self.wrong_guesses = 0

        for widget in self.master.winfo_children():
            widget.destroy()

             
        tk.Label(self.master, text=f"🎯 Difficulty: {difficulty}", font=("Arial", 20, "bold"), bg="#9ca5ad").pack(pady=10)
        
        self.hangman_label = tk.Label(self.master, text=HANGMAN_STAGES[0], font=("Courier", 16), bg="#f8f9fa", justify="left")
        self.hangman_label.pack()
        
        self.word_label = tk.Label(self.master, text=self.display_word(), font=("Courier", 32, "bold"), bg="#f8f9fa", fg="#0d6efd")
        self.word_label.pack(pady=20)

        self.message_label = tk.Label(self.master, text="Welcome to Hangman! Start guessing 👇", font=("Arial", 14), bg="#f8f9fa", fg="#495057")
        self.message_label.pack(pady=10)
        
        guess_frame = tk.Frame(self.master, bg="#f8f9fa")
        guess_frame.pack(pady=10)
        
        self.guess_entry = tk.Entry(guess_frame, font=("Arial", 20), width=5, justify='center')
        self.guess_entry.grid(row=0, column=0, padx=10)
        self.guess_entry.bind("<Return>", lambda e: self.check_guess())

        self.guess_button = tk.Button(guess_frame, text="Guess", font=("Arial", 14, "bold"), bg="#198754", fg="white", command=self.check_guess)
        self.guess_button.grid(row=0, column=1)
        
        self.restart_button = tk.Button(self.master, text="🔄 Restart Game", font=("Arial", 12, "bold"), bg="#ffc107", fg="black", command=lambda: self.start_game(difficulty))
        self.restart_button.pack(pady=10)
        
        
        self.guessed_label = tk.Label(self.master, text="Guessed: ", font=("Arial", 12), bg="#f8f9fa", fg="#495057")
        self.guessed_label.pack(pady=5)
        
        self.status_label = tk.Label(self.master, text=f"Wrong: {self.wrong_guesses}/{self.MAX_WRONG}", font=("Arial", 12), bg="#f8f9fa", fg="#495057")
        self.status_label.pack(pady=5)
    
    # -----------------------------
    # Display word
    # -----------------------------
    def display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
    
    # -----------------------------
    # Check guessed letter
    # -----------------------------
    def check_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="⚠️ Enter a single letter only!")
            return
        
        if guess in self.guessed_letters:
            self.message_label.config(text=f"😅 '{guess}' already guessed.")
            return
        
        self.guessed_letters.append(guess)
        
        if guess in self.word:
            self.message_label.config(text=f"✅ Nice! '{guess}' is in the word.")
        else:
            self.wrong_guesses += 1
            self.message_label.config(text=f"❌ Nope! '{guess}' isn’t in the word.")
        
        self.update_display()
        self.check_game_status()
    
    # -----------------------------
    # Update GUI
    # -----------------------------
    def update_display(self):
        self.word_label.config(text=self.display_word())
        self.guessed_label.config(text=f"Guessed: {' '.join(sorted(self.guessed_letters))}")
        self.hangman_label.config(text=HANGMAN_STAGES[self.wrong_guesses])
        self.status_label.config(text=f"Wrong: {self.wrong_guesses}/{self.MAX_WRONG}")
    

    # -----------------------------
    # Check win/lose
    # -----------------------------
    def check_game_status(self):
      # 🎯 WIN CONDITION
      if all(letter in self.guessed_letters for letter in self.word):
        self.message_label.config(text=f"🎉 You Won! The word was '{self.word}'", fg="green")
        self.guess_button.config(state=tk.DISABLED)
        self.guess_entry.config(state=tk.DISABLED)

      # 💀 LOSS CONDITION
      elif self.wrong_guesses >= self.MAX_WRONG:
        self.message_label.config(text=f"OOPS!☹️ You Lost! The word was '{self.word}'", fg="red")
        self.guess_button.config(state=tk.DISABLED)
        self.guess_entry.config(state=tk.DISABLED)

# -----------------------------
# Run Game
# -----------------------------
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
