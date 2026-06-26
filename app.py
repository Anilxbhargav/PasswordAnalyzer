"""
Password Strength Analyzer with Custom Wordlist Generator
=========================================================
Author  : BCA Cyber Security Student
Purpose : Educational – analyze password strength and generate custom wordlists
Usage   : python app.py
"""

import os
import sys
import argparse
import itertools
import datetime

# ── Try to import zxcvbn (graceful fallback if missing) ──────────────────────
try:
    from zxcvbn import zxcvbn
    ZXCVBN_AVAILABLE = True
except ImportError:
    ZXCVBN_AVAILABLE = False


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 – CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

# Leetspeak substitution map
LEET_MAP = {
    'a': '@', 'e': '3', 'o': '0',
    'i': '1', 's': '$', 't': '7',
    'l': '1', 'g': '9',
}

# Common symbols and years to append
COMMON_SYMBOLS = ['!', '@', '#', '$', '*', '123', '1234']
YEAR_RANGE     = range(1970, datetime.datetime.now().year + 2)

# Strength labels (used in fallback entropy mode)
STRENGTH_LABELS = {
    0: "Very Weak",
    1: "Weak",
    2: "Fair",
    3: "Strong",
    4: "Very Strong",
}

# ANSI colour codes for pretty CLI output
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 – PASSWORD STRENGTH ANALYSIS
# ─────────────────────────────────────────────────────────────────────────────

def analyze_with_zxcvbn(password: str) -> dict:
    """Use the zxcvbn library for realistic strength estimation."""
    result = zxcvbn(password)
    score  = result['score']          # 0–4
    crack  = result['crack_times_display']['offline_slow_hashing_1e4_per_second']
    suggestions = result['feedback']['suggestions']
    warning     = result['feedback'].get('warning', '')

    return {
        "score":       score,
        "label":       STRENGTH_LABELS[score],
        "crack_time":  crack,
        "suggestions": suggestions,
        "warning":     warning,
    }


def entropy_score(password: str) -> int:
    """
    Fallback entropy-based scorer (used when zxcvbn is not installed).
    Returns a score 0–4 based on character variety and length.
    """
    import math
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(not c.isalnum() for c in password): pool += 32

    entropy = len(password) * math.log2(pool) if pool else 0

    if entropy < 28:   return 0
    elif entropy < 36: return 1
    elif entropy < 60: return 2
    elif entropy < 80: return 3
    else:              return 4


def analyze_password(password: str) -> dict:
    """
    Dispatcher: use zxcvbn if available, else fall back to entropy scoring.
    Always returns the same dict shape.
    """
    if ZXCVBN_AVAILABLE:
        return analyze_with_zxcvbn(password)

    # ── Fallback path ──
    score = entropy_score(password)
    suggestions = []

    if len(password) < 12:
        suggestions.append("Use at least 12 characters.")
    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Add numbers.")
    if not any(not c.isalnum() for c in password):
        suggestions.append("Add special characters (!, @, #, …).")

    return {
        "score":       score,
        "label":       STRENGTH_LABELS[score],
        "crack_time":  "unknown (install zxcvbn for accurate estimate)",
        "suggestions": suggestions,
        "warning":     "",
    }


def print_analysis(password: str, result: dict) -> None:
    """Pretty-print the password analysis to the terminal."""
    score = result['score']

    # Pick a colour based on score
    colour = [RED, RED, YELLOW, GREEN, GREEN][score]

    bar_filled = "█" * (score + 1)
    bar_empty  = "░" * (4 - score)
    bar        = colour + bar_filled + RESET + bar_empty

    print(f"\n{BOLD}{'─'*50}{RESET}")
    print(f"  Password : {CYAN}{password}{RESET}")
    print(f"  Strength : {colour}{result['label']}{RESET}  [{bar}] {score}/4")
    print(f"  Est. crack time: {result['crack_time']}")

    if result.get('warning'):
        print(f"\n  {YELLOW}⚠  {result['warning']}{RESET}")

    if result['suggestions']:
        print(f"\n  {BOLD}Suggestions:{RESET}")
        for tip in result['suggestions']:
            print(f"    • {tip}")

    print(f"{BOLD}{'─'*50}{RESET}\n")


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3 – WORDLIST GENERATION & MUTATIONS
# ─────────────────────────────────────────────────────────────────────────────

def collect_user_info() -> dict:
    """
    Interactively ask the user for personal details.
    Returns a dict of raw word tokens.
    """
    print(f"\n{BOLD}{CYAN}═══ Custom Wordlist Generator ═══{RESET}")
    print("Enter details below (press Enter to skip any field).\n")

    fields = {
        "name":       "Full name",
        "username":   "Username / nickname",
        "pet":        "Pet name",
        "birth_year": "Birth year (e.g. 1998)",
        "fav_word":   "Favourite word / hobby",
        "partner":    "Partner / best friend name",
        "company":    "Company / college name",
        "city":       "City / hometown",
    }

    info = {}
    for key, label in fields.items():
        value = input(f"  {label}: ").strip()
        if value:
            info[key] = value

    return info


def apply_leet(word: str) -> str:
    """Replace characters using the LEET_MAP substitutions."""
    return ''.join(LEET_MAP.get(c.lower(), c) for c in word)


def mutate_word(word: str) -> list:
    """
    Generate common password mutations for a single base word.
    Returns a list of unique candidate strings.
    """
    word_lower = word.lower()
    word_upper = word.upper()
    word_title = word.title()
    word_leet  = apply_leet(word)

    variants = {
        word_lower,
        word_upper,
        word_title,
        word_leet,
        word_title + word_leet,   # e.g. FluffyFlu##y
    }

    # Append common years
    base_set = list(variants)
    for base in base_set:
        for year in YEAR_RANGE:
            variants.add(base + str(year))

    # Append common symbols / short numbers
    for base in list(variants):      # iterate over a snapshot
        for sym in COMMON_SYMBOLS:
            variants.add(base + sym)

    return list(variants)


def generate_wordlist(info: dict) -> list:
    """
    Build a full wordlist from user info by:
      1. Extracting base tokens from each field.
      2. Mutating each token.
      3. Combining pairs of tokens and mutating the combos.
    Returns a sorted, deduplicated list.
    """
    # Step 1 – collect base tokens
    base_tokens = []
    for value in info.values():
        # Split multi-word entries (e.g. "John Doe" → ["john", "doe"])
        for part in value.split():
            if part.strip():
                base_tokens.append(part.strip())

    if not base_tokens:
        print(f"{RED}No information provided – wordlist will be empty.{RESET}")
        return []

    all_words = set()

    # Step 2 – mutate each base token
    for token in base_tokens:
        all_words.update(mutate_word(token))

    # Step 3 – combine pairs of tokens (first 6 tokens to avoid combinatorial explosion)
    limited_tokens = base_tokens[:6]
    for t1, t2 in itertools.permutations(limited_tokens, 2):
        combo = t1 + t2
        all_words.update(mutate_word(combo))

    return sorted(all_words)


def export_wordlist(wordlist: list, output_path: str) -> None:
    """Write the wordlist to a plain-text file, one entry per line."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(wordlist))
        print(f"\n{GREEN}✔  Wordlist saved → {output_path}  ({len(wordlist):,} entries){RESET}")
    except OSError as e:
        print(f"{RED}Error saving file: {e}{RESET}")
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4 – INPUT VALIDATION
# ─────────────────────────────────────────────────────────────────────────────

def validate_output_path(path: str) -> str:
    """Ensure the output path ends with .txt and its directory exists."""
    if not path.endswith('.txt'):
        path += '.txt'

    directory = os.path.dirname(path) or '.'
    if not os.path.isdir(directory):
        print(f"{RED}Error: directory '{directory}' does not exist.{RESET}")
        sys.exit(1)

    return path


def validate_password(password: str) -> None:
    """Reject empty passwords early."""
    if not password or not password.strip():
        print(f"{RED}Error: password cannot be empty.{RESET}")
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5 – MAIN FLOW
# ─────────────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    """Define and parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="app.py",
        description="Password Strength Analyzer & Custom Wordlist Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python app.py                          # interactive mode (default)
  python app.py --analyze "MyP@ss123"   # analyze a single password
  python app.py --wordlist               # generate wordlist only
  python app.py --output my_words.txt   # specify output file
        """,
    )
    parser.add_argument(
        "--analyze", "-a",
        metavar="PASSWORD",
        help="Analyze a specific password directly (skip interactive prompt)",
    )
    parser.add_argument(
        "--wordlist", "-w",
        action="store_true",
        help="Generate a custom wordlist (skips password analysis)",
    )
    parser.add_argument(
        "--output", "-o",
        metavar="FILE",
        default="wordlist.txt",
        help="Output file for the wordlist (default: wordlist.txt)",
    )
    return parser.parse_args()


def banner() -> None:
    """Print a welcoming header banner."""
    print(f"""
{BOLD}{CYAN}╔══════════════════════════════════════════════════╗
║   🔐  Password Strength Analyzer + Wordlist Gen  ║
║         Educational Tool – BCA Cyber Security    ║
╚══════════════════════════════════════════════════╝{RESET}
""")

    if not ZXCVBN_AVAILABLE:
        print(f"{YELLOW}ℹ  zxcvbn not found – using built-in entropy scorer.")
        print(f"   For richer analysis: pip install zxcvbn{RESET}\n")


def interactive_mode(output_path: str) -> None:
    """
    Default interactive mode:
      1. Analyze a password typed by the user.
      2. Optionally generate a custom wordlist.
    """
    # ── Password analysis ──
    print(f"{BOLD}Step 1 – Password Analysis{RESET}")
    password = input("  Enter a password to analyze: ").strip()
    validate_password(password)

    result = analyze_password(password)
    print_analysis(password, result)

    # ── Wordlist generation (optional) ──
    gen = input("Would you like to generate a custom wordlist? [y/N]: ").strip().lower()
    if gen == 'y':
        info = collect_user_info()
        print(f"\n{CYAN}Generating wordlist…{RESET}")
        wordlist = generate_wordlist(info)
        if wordlist:
            export_wordlist(wordlist, output_path)


def main() -> None:
    banner()
    args = parse_args()
    output_path = validate_output_path(args.output)

    # ── CLI: analyze a password passed as argument ──
    if args.analyze:
        validate_password(args.analyze)
        result = analyze_password(args.analyze)
        print_analysis(args.analyze, result)
        return

    # ── CLI: wordlist only ──
    if args.wordlist:
        info = collect_user_info()
        print(f"\n{CYAN}Generating wordlist…{RESET}")
        wordlist = generate_wordlist(info)
        if wordlist:
            export_wordlist(wordlist, output_path)
        return

    # ── Default: full interactive mode ──
    interactive_mode(output_path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Interrupted. Goodbye!{RESET}")
        sys.exit(0)
