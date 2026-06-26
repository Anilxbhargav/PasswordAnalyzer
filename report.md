# Password Strength Analyzer with Custom Wordlist Generator
### Project Report | BCA – Cyber Security

---

## Project Name
**Password Strength Analyzer with Custom Wordlist Generator**

---

## Introduction

Passwords are the first line of defence for any digital account or system. Despite decades of security awareness campaigns, weak passwords remain one of the leading causes of data breaches worldwide. This project was created to help Cyber Security students understand *why* certain passwords are weak, *how* attackers generate candidate lists, and *what* makes a password truly strong.

By combining a real-world password-strength library (`zxcvbn`) with a mutation-based wordlist generator, the tool bridges theory and practice in a hands-on, educational way.

---

## Abstract

This Python CLI application performs two related tasks:

1. **Password Strength Analysis** – Given any password, the tool scores it from 0 (Very Weak) to 4 (Very Strong) using the `zxcvbn` library, estimates the time an attacker would need to crack it, and provides concrete improvement suggestions.

2. **Custom Wordlist Generation** – The user provides personal information (name, birth year, pet name, etc.). The tool applies common password-mutation rules (leetspeak substitutions, upper/lower case variations, year/symbol suffixes, and two-token combinations) to generate a realistic list of candidate passwords an attacker might try — demonstrating why personal information should never form the basis of a password.

The generated wordlist is exported as a `.txt` file compatible with tools like Hashcat and John the Ripper for legitimate penetration-testing labs.

---

## Tools Used

| Tool / Library | Version | Purpose |
|---|---|---|
| Python | 3.8+ | Core programming language |
| zxcvbn | ≥ 4.4.28 | Realistic password strength estimation |
| argparse | stdlib | CLI argument parsing |
| itertools | stdlib | Efficient token combination |
| os / sys / datetime | stdlib | File I/O, exit handling, year generation |

No external GUI framework is required; the application runs entirely in the terminal with ANSI colour output.

---

## Steps Involved

1. **Requirements gathering** – Identified key features: strength analysis, suggestions, wordlist generation, export, and CLI usability.
2. **Library evaluation** – Compared `zxcvbn` vs. raw entropy calculation; chose `zxcvbn` with an entropy fallback for environments without internet access.
3. **Core module design** – Split logic into four clear sections: constants, password analysis, wordlist generation/mutation, and the main CLI flow.
4. **Mutation engine** – Implemented leetspeak, case variants, year-range suffixes (1970–present+1), common symbols, and pairwise token combinations.
5. **CLI design** – Used `argparse` to support three modes: fully interactive, `--analyze`, and `--wordlist`.
6. **Input validation** – Added guards for empty passwords, missing directories, and keyboard interrupts.
7. **Testing** – Manually tested weak passwords (`123456`, `password`), strong passwords (`Tr0ub4dor&3`), and edge cases (empty input, missing directory).
8. **Documentation** – Wrote README.md, this report, and inline code comments for every non-obvious block.

---

## Conclusion

This project successfully demonstrates two core Cyber Security concepts — **password strength evaluation** and **targeted wordlist generation** — in a single, beginner-friendly Python application. By seeing how quickly personal details become guessable passwords, students gain an intuitive understanding of why password hygiene matters.

The tool is intentionally kept simple and educational. Future extensions could include a Tkinter GUI, integration with the *Have I Been Pwned* breach database, and rule-file support for custom mutation patterns.

> **Ethical note:** This tool is for learning only. Always obtain written permission before testing passwords on systems you do not own.
