# Hangman_Game
Hangman is a guessing game where one player chooses a word or phrase and the other players try to guess it by suggesting letters or numbers

# Hangman Game Code Explanation

This Python program implements a **GUI-based Hangman game** using `tkinter`. The game allows players to guess letters of a hidden word with visual feedback, difficulty levels, and win/lose conditions.

---

## **1. Modules Used**
- `tkinter`: For creating the graphical user interface (GUI).  
- `random`: For selecting random words from the word list.

---

## **2. Hangman ASCII Art (HANGMAN_STAGES)**
```python
HANGMAN_STAGES = [...]
```
- They dipict the players performance
  
---

## **3. Word List (WORDS)**
- A list of strings representing the hangman figure at each stage of incorrect guesses.
- As the player makes wrong guesses, the next stage of the hangman is displayed.
  
---

## **4. Difficulty Filter Function**
```python
def get_words_by_mode(mode):
```
- Filters words based on length according to difficulty:
  <ul>
    <li>Easy - 4-5 letter words</li>
    <li>Medium - 6-8 letter words</li>
    <li>Hard - 9-10 letter words</li>
    <li>Expert - 12-14 letter words</li>
  </ul>
- Returns a list of words suitable for the selected difficulty.
  
---

## **5. Main Game Class: `HangmanGame`**
```python
class HangmanGame:
```
- Encapsulates the entire game logic and GUI.
- Key attributes:
  <ul>
      <li>`self.word`: The randomly selected word.</li>
      <li>`self.guessed_letters`: List of letters guessed by the player.</li>
      <li>`self.wrong_guesses`: Counter for incorrect guesses.</li>
      <li>`self.MAX_WRONG`: Maximum allowed wrong guesses (based on hangman stages).</li>
    </ul>

### **5.1 `__init__(self, master)`**
- Initializes the game window, sets the title, size, background color.
- Calls `create_difficulty_screen()` to show difficulty options.
  
### **5.2 Difficulty Selection Screen**
```python
def create_difficulty_screen(self):
```
- Clears any existing widgets.
- Displays buttons for difficulty levels: Easy, Medium, Hard, Expert.
- Clicking a button starts the game with `self.start_game(level)`.

### **5.3 Start Game**
```python
def start_game(self, difficulty):
```
- Selects a random word from the filtered list based on difficulty.
- Resets `guessed_letters` and `wrong_guesses`.
- Sets up the GUI for gameplay:
  <ul>
      <li>Hangman ASCII display (`self.hangman_label`)</li>
      <li>Word display with underscores (`self.word_label`)</li>
      <li>Entry box and button for guesses (`self.guess_entry` and `self.guess_button`)</li>
      <li>Labels for messages, guessed letters, and wrong guess count.</li>
    </ul>
  
### **5.4 Display Word**
```python
def display_word(self):
```
- Returns a string showing the current word with guessed letters revealed and unknown letters as underscores.
= Example: For word "PYTHON" and guessed letters `['P', 'O']` → `"P _ _ _ O _"`
  

### **5.5 Check Guessed Letter**
```python
def check_guess(self):
```
- Reads the player's input from the entry box.
- Validates input:
  <ul>
    <li>Must be a single alphabetical character.</li>
    <li>Not previously guessed.</li>
  </ul>
- Updates `guessed_letters` or increments `wrong_guesses`.
- Provides feedback via `self.message_label`.
- Updates the GUI display (`update_display()`) and checks win/lose status (`check_game_status()`).

### **5.6 Update Display**
```python
def update_display(self):
```
- Updates:
  <ul>
      <li>Current word display with guessed letters.</li>
      <li>List of guessed letters.</li>
      <li>Hangman ASCII art according to `wrong_guesses`.</li>
      <li>Wrong guess counter.</li>
    </ul>
  
---

## **6. Running the Game**
```python
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
```
- Creates the Tkinter root window.
- Initializes the HangmanGame object.
- Starts the Tkinter event loop with mainloop().
  
---

## **7. How to run the code on your system**
- Copy and paste the entire code on NotePad with `.py` (to run using cmd) or `.pyw` (to run even without cmd) extension, file type: `All Files`
- In the Command Promt `cmd`:
 ```cmd
cd folder\name\where\file\is\saved
``` 
if saved as `.py`:
 ```cmd
python file_name
```
if saved as `.pyw`:
 ```cmd
pythonw file_name
``` 
---

## **Summary**
- Purpose: Provides an interactive Hangman game with GUI.
- Features:
  <ul>
      <li>Difficulty levels with filtered word lengths.</li>
      <li>Hangman ASCII art visual feedback.</li>
      <li>Input validation and feedback messages.</li>
      <li>Win and loss detection.</li>
      <li>Real-time GUI updates for guesses, hangman drawing, and status.</li>
    </ul>
  
- Key Functions:
  <ul>
      <li>get_words_by_mode(): Filters words based on difficulty.</li>
      <li>display_word(): Shows word progress with guessed letters.</li>
      <li>check_guess(): Processes player input and updates game state.</li>
      <li>update_display(): Refreshes GUI after each guess.</li>
      <li>check_game_status(): Detects win or loss and updates messages.</li>
    </ul>



<img width="807" height="902" alt="hmg3" src="https://github.com/user-attachments/assets/60813a34-bc09-4569-878a-46583e32ab43" />
<img width="798" height="911" alt="hmg2" src="https://github.com/user-attachments/assets/d0ab8271-5ebd-45a9-9ddc-1964795a3f69" />
<img width="802" height="901" alt="hmg 1" src="https://github.com/user-attachments/assets/642cf843-4a39-446e-a117-82cd35490c90" />







