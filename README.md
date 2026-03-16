# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game purpose:**
This is a number guessing game built with Streamlit. The player picks a difficulty level, then tries to guess a randomly generated secret number within a limited number of attempts. After each guess, the game gives a hint telling the player whether to guess higher or lower.

**Bugs found:**
1. **Reversed hint directions** — when a player guessed a number higher than the secret, the game told them to go higher instead of lower. The comparison logic was correct (`guess > secret`) but the feedback messages were swapped.
2. **Decimal inputs silently accepted** — entering a value like `12.7` would not trigger any error. The original code used `int(float(raw))` which quietly truncated the decimal and treated it as a valid integer guess.

**Fixes applied:**
1. Moved `check_guess` and `parse_guess` into `logic_utils.py` and corrected the hint messages so "Too High" maps to "Try LOWER!" and "Too Low" maps to "Try HIGHER!".
2. Updated `parse_guess` in `logic_utils.py` to use `int(raw)` directly, which raises a `ValueError` on any decimal string, and returns a user-facing error message instead of silently accepting the input.
3. Updated `app.py` to import all game logic from `logic_utils.py` instead of using its own local copies.
4. Added `conftest.py` at the project root so pytest can locate `logic_utils` when running tests from the `tests/` folder.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
- [ ] [Insert a screenshot of your pytest results showing all 5 tests passing]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
