import zxcvbn  # Correct import statement

def check_password_strength(password):
    # Analyze the password strength
    result = zxcvbn.zxcvbn(password)

    # Extract the score and feedback
    score = result['score']  # Score is from 0 (weak) to 4 (very strong)
    feedback = result['feedback']

    return score, feedback

def evaluate_password(password):
    special_characters = "!@#$%^&*()-_+=<>?/{}~`|[]\\:;\"'"
    requirements = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "digits": any(char.isdigit() for char in password),
        "special_characters": any(char in special_characters for char in password),
        "non_continuous": not any(
            ord(password[i]) == ord(password[i - 1]) + 1 for i in range(1, len(password))
        ),
    }

    missing_requirements = [req for req, met in requirements.items() if not met]
    return requirements, missing_requirements

def main():
    print("Password Complexity Checker")
    print("A strong password should include:")
    print("- At least 8 characters")
    print("- Both uppercase and lowercase letters")
    print("- Numbers")
    print("- Special characters (e.g., !@#$%^&*)")
    print("- No continuous sequences of letters or numbers")

    while True:
        password = input("\nEnter a password to check (or 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Exiting the Password Complexity Checker. Goodbye!")
            break

        requirements, missing_requirements = evaluate_password(password)
        if not missing_requirements:
            print("\nPassword meets all requirements.")
        else:
            print("\nPassword is missing the following requirements:")
            for req in missing_requirements:
                print(f"  - {req.replace('_', ' ').capitalize()}")

        score, feedback = check_password_strength(password)
        print(f"\nPassword complexity score: {score} (0=Very Weak, 1=Weak, 2=Fair, 3=Good, 4=Very Strong)")
        if feedback['warning']:
            print(f"Warning: {feedback['warning']}")
        if feedback['suggestions']:
            print("Suggestions to improve your password:")
            for suggestion in feedback['suggestions']:
                print(f"  - {suggestion}")
        print("\n")

if __name__ == "__main__":  # Correct main block check
    main()
