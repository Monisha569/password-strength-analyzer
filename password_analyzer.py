import re
import secrets
import string


def analyze_password(password):

    if not password:
        return {
            "strength": "-",
            "score": 0,
            "color": "gray",
            "checks": [],
            "suggestions": [
                "Enter a password to check its security."
            ]
        }

    checks = []

    # Password length
    length_ok = len(password) >= 8
    checks.append({
        "name": "At least 8 characters",
        "passed": length_ok
    })

    # Uppercase
    uppercase_ok = bool(re.search(r"[A-Z]", password))
    checks.append({
        "name": "Contains uppercase letter (A-Z)",
        "passed": uppercase_ok
    })

    # Lowercase
    lowercase_ok = bool(re.search(r"[a-z]", password))
    checks.append({
        "name": "Contains lowercase letter (a-z)",
        "passed": lowercase_ok
    })

    # Number
    number_ok = bool(re.search(r"\d", password))
    checks.append({
        "name": "Contains a number (0-9)",
        "passed": number_ok
    })

    # Special character
    special_ok = bool(re.search(r"[^A-Za-z0-9]", password))
    checks.append({
        "name": "Contains special character (!@#$%)",
        "passed": special_ok
    })

    # Length score
    score = 0

    if len(password) >= 8:
        score += 20

    if len(password) >= 12:
        score += 10

    if len(password) >= 16:
        score += 10

    if uppercase_ok:
        score += 15

    if lowercase_ok:
        score += 15

    if number_ok:
        score += 15

    if special_ok:
        score += 15

    # Repeated characters
    if re.search(r"(.)\1\1", password):
        score -= 10

    # Common weak passwords
    common_passwords = [
        "password",
        "password123",
        "123456",
        "12345678",
        "qwerty",
        "qwerty123",
        "admin",
        "welcome",
        "letmein",
        "abc123"
    ]

    if password.lower() in common_passwords:
        score = min(score, 20)

    score = max(0, min(score, 100))

    # Strength
    if score < 30:
        strength = "Very Weak"
        color = "red"

    elif score < 50:
        strength = "Weak"
        color = "orange"

    elif score < 70:
        strength = "Medium"
        color = "yellow"

    elif score < 90:
        strength = "Strong"
        color = "lightgreen"

    else:
        strength = "Very Strong"
        color = "green"

    # Suggestions
    suggestions = []

    if len(password) < 8:
        suggestions.append(
            "Use at least 8 characters."
        )

    if len(password) < 12:
        suggestions.append(
            "For better security, use 12 or more characters."
        )

    if not uppercase_ok:
        suggestions.append(
            "Add at least one uppercase letter."
        )

    if not lowercase_ok:
        suggestions.append(
            "Add at least one lowercase letter."
        )

    if not number_ok:
        suggestions.append(
            "Add at least one number."
        )

    if not special_ok:
        suggestions.append(
            "Add a special character such as !, @, # or $."
        )

    if re.search(r"(.)\1\1", password):
        suggestions.append(
            "Avoid repeating the same character multiple times."
        )

    if password.lower() in common_passwords:
        suggestions.append(
            "Avoid commonly used passwords."
        )

    if not suggestions:
        suggestions.append(
            "Excellent! Your password satisfies the recommended security checks."
        )

    return {
        "strength": strength,
        "score": score,
        "color": color,
        "checks": checks,
        "suggestions": suggestions
    }


def generate_password(length=16):

    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*"
    )

    while True:

        password = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        if (
            re.search(r"[A-Z]", password)
            and re.search(r"[a-z]", password)
            and re.search(r"\d", password)
            and re.search(r"[^A-Za-z0-9]", password)
        ):
            return password