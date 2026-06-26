# How to Upload This Project to GitHub (Step-by-Step)

---

## Step 1 – Create a GitHub account
Go to https://github.com and sign up (free).

---

## Step 2 – Create a new repository

1. Click the **+** icon → **New repository**
2. Repository name: `PasswordAnalyzer`
3. Description: `Password Strength Analyzer + Custom Wordlist Generator – BCA Cyber Security`
4. Visibility: **Public**
5. ✅ Add a README: **NO** (we already have one)
6. Click **Create repository**

---

## Step 3 – Install Git (if not already installed)

Download from https://git-scm.com/downloads  
Verify: `git --version`

---

## Step 4 – Configure Git (first time only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

## Step 5 – Initialize and push from your project folder

```bash
# Navigate into the project folder
cd path/to/PasswordAnalyzer

# Initialize a local git repository
git init

# Stage all files
git add .

# Create the first commit
git commit -m "Initial commit – Password Analyzer project"

# Link to your GitHub repo (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/PasswordAnalyzer.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 6 – Verify on GitHub

Open `https://github.com/YOUR_USERNAME/PasswordAnalyzer` in your browser.  
You should see all your files listed there.

---

## Step 7 – Add a topic / description (optional but looks professional)

1. On your repo page click **⚙ Settings** (top right of repo, not account settings)  
   Or click the ⚙ gear icon next to "About" on the repo homepage.
2. Add topics: `python`, `cybersecurity`, `password-security`, `bca-project`
3. Save changes.

---

## Uploading large files (screenshots, demo.mp4)

If `demo.mp4` is larger than 100 MB, use **Git LFS**:

```bash
git lfs install
git lfs track "*.mp4"
git add .gitattributes
git add demo.mp4
git commit -m "Add demo video"
git push
```

Alternatively, upload the video to YouTube (unlisted) and link it in your README.

---

## Updating the repo after changes

```bash
git add .
git commit -m "Describe what you changed"
git push
```
