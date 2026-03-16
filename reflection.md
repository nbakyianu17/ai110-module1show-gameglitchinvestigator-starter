# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
  The first time I ran the game using Streamlit, the interface loaded correctly, but the gameplay behaved strangely. The game allowed me to enter guesses, but the hints did not always match the guess I made, and sometimes the game continued running even after the correct number was guessed. It felt like the logic controlling the hints and game state was inconsistent.

One bug I noticed was that the hints seemed backwards in some situations. For example, when I guessed a number that was higher than the secret number, the hint sometimes indicated that the guess was too low. Another issue was that the game did not always end properly after the correct guess, which made it seem like the win condition was not being handled correctly. I also noticed that the score or state sometimes behaved oddly between guesses, which made me suspect there was a problem with how the logic was structured.
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
