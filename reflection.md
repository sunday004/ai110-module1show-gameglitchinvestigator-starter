# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

  - The History lags by 1, instead of updating immediately
  - The hint is flipped: it says lower when it should say higher
  - The number of attempts does not update on the first submit.     Both history and attempts do not update unless you click a button (example toggle btw show hint). Attempts left should start counting from 8. (Check line 95 for app.py)
  - Scoring is unpredictable. I should be able to tell if I am making progress or not
  - Difficulty levels: Hard and Normal tend to be reversed in number of potential guesses


---

## 2. How did you use AI as a teammate?

- I used github copilot powered by Claude Sonnet 4.5, both for validating my thoughts, brainstorming fixes, and as an agent to implemented fixes. I also used it to understand the rationale behind certain logic and bugs and compare with the expected case.
- I specifically used it to explain the purpose of the logic_utils file
- It gave a correct suggestion to switch the responses on the hint section of the code, and also deduct point always for wrong guess.
- Almost all the AI suggestions were correct, I tried to be cautious. An example of a wrong response was with the Difficulty response, but I figured to inspire my attempts using binary search.

---

## 3. Debugging and testing your fixes

- I practically tested and made sure the app now behaves as expected, and the issue identified and observed was fixed.
- I tested various higher and lower values to see the effect on the score and ensure they all subtracted 5. I also ensured the final result after a correct answer is as expected, especially after a first correct guess (I'd expect a score of 100).
- I used AI to generate tests for the bugs we fixed, and I already understood them with my python background knowledge

---

## 4. What did you learn about Streamlit and state?

- The secret number kept changing because Streamlit reruns the script from top to bottom on almost every interaction. In the original version, a new random secret was being generated during those reruns, so clicks and input changes could silently replace the target number mid-game.
- the session state and reruns is a means to keep track and update variables in your app, this could be numbers, text, or even visual components like buttons, colors, etc.
- I moved the secret number into session state and only re-generated it when the New Game button is pressed, instead of creating a new random value during normal reruns.



---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- I definitely want to imbibe the habit of intentionally using AI as a teammate to understand bugs and develop efficient fixes for them.
- One thing I could do differently is to have a workflow or flow to automate the process in a more structured way
- It made me collaborate more with AI, without letting it do all the work.
