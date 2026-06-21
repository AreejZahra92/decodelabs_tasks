"""
Password Strength Checker
DecodeLabs Industrial Training Kit - Cyber Security - Project 1

Goal:
    Check whether a password is Weak, Medium, or Strong based on:
    - Length
    - Use of uppercase letters
    - Use of lowercase letters
    - Use of numbers
    - Use of symbols
"""

# A small sample list of common/leaked passwords (optional extra from the brief)
COMMON_PASSWORDS = {
    "password", "password123", "123456", "123456789", "qwerty",
    "abc123", "letmein", "monkey", "111111", "iloveyou",
    "admin", "welcome", "qwerty123", "12345678", "football"
}

SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"


def check_password(password: str) -> dict:
    """
    Runs all checks on the password and returns a dictionary
    with the individual results, the score, and the final strength.
    """
    results = {
        "length_ok": len(password) >= 8,
        "has_upper": any(char.isupper() for char in password),
        "has_lower": any(char.islower() for char in password),
        "has_digit": any(char.isdigit() for char in password),
        "has_symbol": any(char in SYMBOLS for char in password),
        "is_common": password.lower() in COMMON_PASSWORDS,
    }

    # Score = number of conditions met (length, upper, lower, digit, symbol)
    score = sum([
        results["length_ok"],
        results["has_upper"],
        results["has_lower"],
        results["has_digit"],
        results["has_symbol"],
    ])

    # Decide strength
    if results["is_common"]:
        strength = "Weak"  # Known leaked/common password overrides everything
    elif not results["length_ok"]:
        strength = "Weak"  # Page 7: < 8 chars = immediate fail
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    results["score"] = score
    results["strength"] = strength
    return results


def print_feedback(password: str, results: dict) -> None:
    """Prints the strength result and tips on what to improve."""
    print("\n" + "-" * 40)
    print(f"Password: {'*' * len(password)}")
    print(f"Strength: {results['strength']}")
    print("-" * 40)

    if results["is_common"]:
        print("⚠  This password is in a list of commonly leaked passwords.")
        print("   Avoid using it under any circumstances.")

    tips = []
    if not results["length_ok"]:
        tips.append("Use at least 8 characters.")
    if not results["has_upper"]:
        tips.append("Add at least one uppercase letter (A-Z).")
    if not results["has_lower"]:
        tips.append("Add at least one lowercase letter (a-z).")
    if not results["has_digit"]:
        tips.append("Add at least one number (0-9).")
    if not results["has_symbol"]:
        tips.append("Add at least one symbol (e.g. ! @ # $ %).")

    if tips:
        print("\nSuggestions to improve your password:")
        for tip in tips:
            print(f"  - {tip}")
    else:
        print("\nGreat job! Your password meets all the criteria.")


def main():
    print("=" * 40)
    print("   PASSWORD STRENGTH CHECKER")
    print("=" * 40)
    print("Type 'exit' at any time to quit.\n")

    while True:
        password = input("Enter a password to check: ")

        if password.lower() == "exit":
            print("Goodbye!")
            break

        if password == "":
            print("Please enter a non-empty password.\n")
            continue

        results = check_password(password)
        print_feedback(password, results)
        print()  # blank line for spacing


if __name__ == "__main__":
    main()