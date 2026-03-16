# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
  The first time I ran the game using Streamlit, the interface loaded correctly, but the gameplay behaved strangely. The game allowed me to enter guesses, but the hints were giving the wrong direction, which made it impossible to actually find the secret number by following the feedback. It felt like the logic controlling the hints was flipped somewhere in the code.

One bug I noticed was that the hint directions were backwards. For example, when I guessed a number that was higher than the secret number, the game told me to go higher instead of lower, which sent me in the completely wrong direction. The second bug was that the game accepted decimal inputs like "12.7" without any error, silently converting them to whole numbers instead of prompting the user to enter a valid whole number. Both bugs were inside the core logic functions in app.py, which is what made them hard to spot at first glance.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
 In one or two sentences, describe how this project changed the way you think about AI generated code.

