# Demo Video Script
## Password Strength Analyzer – 3-Minute Walkthrough

---

### [0:00 – 0:20] Introduction (face-cam or voice-over)

> "Hi! Today I'll demo my BCA Cyber Security project –
> a Password Strength Analyzer with a Custom Wordlist Generator.
> This tool shows why weak passwords are dangerous and how attackers
> build targeted password lists. Let's get started."

---

### [0:20 – 0:40] Installation

**Screen: terminal**

```
pip install -r requirements.txt
```

> "Installation is simple – just one command."

---

### [0:40 – 1:10] Analyzing a WEAK password

**Screen: terminal**

```
python app.py
```

- When prompted, type: `fluffy123`

> "I'll enter a common weak password. Notice the score is 1 out of 4 –
> Weak – and the tool tells us exactly why and how to improve it."

📸 **Screenshot here**: `screenshots/03_weak_password.png`

---

### [1:10 – 1:40] Analyzing a STRONG password

**Screen: terminal**

```
python app.py --analyze "Tr0ub4dor&3_Sky!"
```

> "Now let's try a strong password directly from the command line.
> Score 4 – Very Strong – with an estimated crack time in the centuries."

📸 **Screenshot here**: `screenshots/02_strong_password.png`

---

### [1:40 – 2:30] Generating a custom wordlist

**Screen: terminal**

```
python app.py --wordlist --output demo_wordlist.txt
```

Fill in the prompts:
- Name: `John`
- Username: `j0hn`
- Pet: `Fluffy`
- Birth year: `1998`
- Favourite word: `cricket`

> "I'll fill in some personal details. The tool combines these,
> applies leetspeak, symbols, and year suffixes, then exports
> thousands of candidates to a text file."

📸 **Screenshot here**: `screenshots/05_wordlist_saved.png`

---

### [2:30 – 2:50] Showing the exported wordlist

**Screen: text editor or `head demo_wordlist.txt`**

```bash
head -20 demo_wordlist.txt
```

> "Here's a sample of the wordlist. Notice how 'fluffy' becomes
> 'Fluffy1998!', 'flu##y', 'fl0##y@', and hundreds of other variants –
> this is exactly what attackers generate against targets they've researched."

📸 **Screenshot here**: `screenshots/06_cli_flags.png`

---

### [2:50 – 3:00] Closing

> "That's the project! It covers password analysis, mutation-based
> wordlist generation, and export – all in clean Python.
> Code and documentation are on GitHub. Thanks for watching!"

---

### Recording Tips

- Use **OBS Studio** (free) to record the screen.
- Set resolution to **1920×1080**, 30 fps.
- Use a dark terminal theme (e.g. **Dracula** or **Monokai**) for contrast.
- Font size: **16–18 pt** so text is readable in the video.
- Pause ~1 second after each command before speaking, so edits are easy.
- Export as **MP4** (H.264) and name it `demo.mp4`.
