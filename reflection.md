\# Lab 5: Static Code Analysis — Reflection



\## 1. Which issues were the easiest to fix, and which were the hardest? Why?



Formatting issues, unused variables, and missing documentation were relatively easy to fix. Security issues such as unsafe expression evaluation, weak hashing, and shell command execution required more careful changes to maintain correct program behaviour.



\## 2. Did the static analysis tools report any false positives? If so, describe one example.



The tools reported potential problems that needed to be reviewed. I did not classify any finding as a false positive without evidence. The original MD5 warning was relevant because MD5 is a weak hashing algorithm.



\## 3. How would you integrate static analysis tools into your software development workflow?



I would run Pylint, Bandit, and Flake8 during development and before submitting or committing code. I would also integrate these tools into a continuous integration workflow to identify quality and security issues early.



\## 4. What improvements did you observe after applying the fixes?



The program now uses safer fee calculation, SHA-256 hashing, secure PIN generation, input validation, clearer function names, documentation, and safer file handling. The final Pylint score improved from 4.10/10 to 9.87/10. Flake8 reports no findings, and Bandit reports no identified issues.

