# 🔐 Password Strength Analyzer + Custom Wordlist Generator

A beginner-friendly Python CLI tool for BCA Cyber Security students that:

- **Analyzes password strength** using `zxcvbn` (or built-in entropy scoring as fallback)
- **Generates a custom password wordlist** from personal information
- **Applies real-world mutations** — leetspeak, capitalization, year appending, symbols
- **Exports the wordlist** to a `.txt` file

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 Password Analysis | Strength score (0–4), crack time estimate, actionable tips |
| 🧠 zxcvbn Integration | Industry-standard realistic strength estimation |
| 📋 Fallback Scorer | Built-in entropy scorer if zxcvbn is unavailable |
| 🗂️ Wordlist Generator | Builds candidates from name, username, pet, birth year, etc. |
| 🔀 Mutation Engine | Leetspeak, case variants, year suffixes, symbols, combos |
| 💾 TXT Export | One-click export of the full wordlist |
| 🛡️ Input Validation | Empty-password guard, path checking, graceful error messages |
| 🎨 Colour CLI | ANSI-coloured strength bars and icons |

---

## 🛠️ Technologies Used

- **Python 3.8+** — core language
- **zxcvbn** — realistic password strength estimation
- **argparse** — clean CLI argument handling
- **itertools** — efficient combination generation
- **os / sys / datetime** — standard library utilities

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/PasswordAnalyzer.git
cd PasswordAnalyzer

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### Interactive mode (default)
```bash
python app.py
```
You will be prompted to:
1. Enter a password to analyze
2. Optionally generate a custom wordlist

### Analyze a specific password
```bash
python app.py --analyze "MySecretP@ss2024"
```

### Generate a wordlist only
```bash
python app.py --wordlist
```

### Custom output file
```bash
python app.py --output my_wordlist.txt
```

### Combine flags
```bash
python app.py --wordlist --output custom.txt
```

### Help
```bash
python app.py --help
```

---

## 📸 Screenshots

| Screen | Description |
|---|---|
| `screenshots/01_main_menu.png` | Banner and password input prompt |
| `screenshots/02_strong_password.png` | Analysis of a strong password (score 4) |
| `screenshots/03_weak_password.png` | Analysis of a weak password with suggestions |
| `screenshots/04_wordlist_input.png` | Collecting personal info for wordlist |
| `screenshots/05_wordlist_saved.png` | Success message after export |
| `screenshots/06_cli_flags.png` | Using `--analyze` and `--wordlist` flags |

> See **How to Take Screenshots** in the project report for step-by-step instructions.

---

## 🔮 Future Improvements

- GUI version using Tkinter
- MD5 / SHA hash generation alongside each wordlist entry
- Integration with `Have I Been Pwned` API
- Rule-based mutations file (user-configurable)
- Password policy checker (minimum length, required character types)

---

## 👤 Author

**BCA Cyber Security Student**  
Course: Bachelor of Computer Applications – Cyber Security  
Tool built for educational purposes only. Do not use for unauthorized access.

---

## ⚠️ Disclaimer

This tool is intended **strictly for educational and ethical security research**.  
Always get explicit permission before testing passwords on any system you do not own.
