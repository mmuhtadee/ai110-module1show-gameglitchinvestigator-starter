# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Difficulty level at hard is easier than medium
- List at least two concrete bugs you noticed at the start  
1. at level easy, secret number is 78, when it's supposed to be between 1-20
2. After each guess, the hints lie to the player by directing them to the opposite direction.
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | | Correct hints      Incorrect Hints     "Go lower" even when guess was below actual
| | | | | Score > 0          Score < 0          
| | | | | 1 number to win     No way to win

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude code identified the if-statement that provided the wrong hints to the player after each guess.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I couldn't identify any statement made by claude code that are supposedly wrong.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran the app, ran some pytests, and made sure the code passed them all.
- Describe at least one test you ran (manual or using pytest)  
One test I ran was guessing numbers, and noting whether the hints are actually leading to the secret.
  and what it showed you about your code.
It showed me that the code performs better than it was, and actually makes the game playable
- Did AI help you design or understand any tests? How?
Yes, AI helped me to decide where the backend coverage of my code belongs, and generated pytests to validate the game.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- I'd describe streamlit reruns as the "mannequin challenge" game that restarts as long as u do something, in this case if you click something. Session state is something to record your activity, to remember what you did in the last turn.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
