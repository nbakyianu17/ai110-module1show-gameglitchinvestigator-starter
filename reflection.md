# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
  The first time I ran the game using Streamlit, the interface loaded correctly, but the gameplay behaved strangely. The game allowed me to enter guesses, but the hints were giving the wrong direction, which made it impossible to actually find the secret number by following the feedback. It felt like the logic controlling the hints was flipped somewhere in the code.

One bug I noticed was that the hint directions were backwards. For example, when I guessed a number that was higher than the secret number, the game told me to go higher instead of lower, which sent me in the completely wrong direction. The second bug was that the game accepted decimal inputs like "12.7" without any error, silently converting them to whole numbers instead of prompting the user to enter a valid whole number. Both bugs were inside the core logic functions in app.py, which is what made them hard to spot at first glance.
---

## 2. How did you use AI as a teammate?

I used GitHub Copilot as my main AI tool throughout this project, both in the Chat view and in Agent mode. For the hint direction bug, I asked Copilot to refactor `check_guess` into `logic_utils.py` and fix the reversed logic — it correctly identified that the `>` comparison was there but the messages were swapped, and it moved the function over with the right fix. I verified this by running the game manually and confirming that guessing above the secret now told me to go lower. One misleading suggestion came when I asked Copilot to fix the decimal input bug — it initially suggested keeping the `float()` conversion and just rounding the result, which would have still silently accepted decimal input instead of rejecting it. I caught this by re-reading the suggestion carefully and realizing it didn't actually show an error to the user, so I prompted Copilot again to reject the input entirely and return an error message instead.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when both the manual game behavior matched what I expected and a pytest test confirmed the logic in isolation. For the hint direction fix, I wrote a test that calls `check_guess(60, 50)` and asserts the outcome is `"Too High"` and the message contains `"LOWER"` — this test initially failed, which confirmed the bug was real, and passed after the fix. For the decimal bug, I wrote a test that passes `"12.7"` to `parse_guess` and asserts `ok == False` and an error message is returned. When I first ran pytest, the tests failed with a `ModuleNotFoundError` because pytest couldn't find `logic_utils` — I fixed this by adding a `conftest.py` at the project root, and after that all 5 tests passed. Copilot helped me understand the structure of pytest assertions and suggested using tuple unpacking to check both the outcome and message from `check_guess` at the same time.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the entire Python script from top to bottom every single time a user interacts with the app — clicking a button, typing in a field, or changing a dropdown all trigger a full rerun. This means that regular Python variables reset to their initial values on every rerun, so you can't use them to remember things like the secret number or the attempt count between interactions. That's what `st.session_state` is for — it's a dictionary that persists across reruns, so values stored there survive each rerun. If I were explaining it to a friend, I'd say: imagine every button click restarts the script, but `session_state` is like a notepad that the script checks at the top each time so it can pick up where it left off.

---

## 5. Looking ahead: your developer habits

One habit I want to carry forward is writing tests that target the specific behavior a bug broke, not just general passing tests — having a test that checks the message says "LOWER" (not just that the outcome label is "Too High") meant the test would have caught the original bug before the fix. Next time I work with AI on a coding task, I would be more careful about reading the AI's suggestion fully before accepting it, especially for input validation logic where the AI sometimes takes a shortcut that looks correct but doesn't fully handle the edge case. This project changed how I think about AI-generated code because I came in expecting it to be mostly right, but I found that the original app.py was confidently written with real logical bugs in it — which means AI code always needs to be tested, not just read.
