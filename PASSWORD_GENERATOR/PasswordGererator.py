import secrets
import string
from datetime import datetime

line = "-"*75
"""
def generate_password(length, uppercase, lowercase, digits, special_characters):
    Generates a secure random password based on user preferences.

    Parameters:
    length (int): Required length of the password.
    uppercase (bool): Include uppercase letters if True.
    lowercase (bool): Include lowercase letters if True.
    digits (bool): Include numeric digits if True.
    special_characters (bool): Include special symbols if True.

    Returns:
    str: Randomly generated password.

    Feature:
    - Uses secure random selection.
    - Builds character pool dynamically based on user input.
    - Ensures flexible and customizable password generation.
    """
def generate_password(length, uppercase, lowercase, digits, special_characters):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    password = ""
    for i in range(length):
        password += secrets.choice(characters)

    return password

"""
def check_strength(password):
    Evaluates the strength of a generated password.

    Parameters:
    password (str): The password to analyze.

    Functionality:
    - Calculates strength score based on:
        • Length
        • Presence of uppercase letters
        • Presence of lowercase letters
        • Presence of digits
        • Presence of special characters
    - Displays a detailed strength report.

    Purpose:
    - Helps user understand password security level.
    - Encourages strong password practices.
    """
def check_strength(password):
    upcount = lowercount = digitcount = specialcount = start_score = 0
    special_characters = "!@#$%^&*()-+{}[]|:;\"'<>,.?/~`"
    for char in password:
        if char.isupper():
            upcount += 1
        elif char.islower():
            lowercount += 1
        elif char.isdigit():
            digitcount += 1
        elif char in special_characters:
            specialcount += 1
    print(line)
    print("------------------------> Password Strength Analysis: <------------------------")
    print(f"Uppercase Letters: {upcount}")
    print(f"Lowercase Letters: {lowercount}")
    print(f"Digits: {digitcount}")
    print(f"Special Characters: {specialcount}")

    if len(password) >= 8:
        start_score += 1
    if len(password) >= 12:
        start_score += 1
    if any(char.isupper() for char in password):
        start_score += 1
    if any(char.islower() for char in password):
        start_score += 1
    if any(char.isdigit() for char in password):
        start_score += 1
    if any(char in special_characters for char in password):
        start_score += 1

    print(f"Password Strength Score: {start_score}/6")

    if start_score <= 2:
        print("Password Strength: Weak")
    elif start_score <= 4:
        print("Password Strength: Moderate")
    else:
        print("Password Strength: Strong")

"""
def Save_Password_to_File(password):
    Saves the generated password to a text file with timestamp.

    Parameters:
    password (str): The password (or hashed password) to store.

    Features:
    - Stores password in append mode (preserves history).
    - Adds current date and time for logging.
    - Ensures data persistence.

    Purpose:
    - Maintains password generation history.
    - Simulates real-world logging system.
    """
def Save_Password_to_File(password):
    with open("Generated_passwords.txt", "a") as file:
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Password: {password}\n")

    print("Password saved to Generated_passwords.txt successfully.")

def main():
    print(line)
    print("This Program Generates A Secure Password Based On Your Requirements.")
    print(line)
    
    #take length for password and validate it
    #the password must be at least 8 characters long for security reasons
    while True:
        try:
            length = int(input("Enter Required Password Length (Minimum 8 Characters): "))
            if length < 8 or length > 128:
                print("Password length must be between 8 and 128 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for password length.")

    #take user preferences for character types to include in the password
    #uppercase 
    print("Include Uppercase Letters? (y/n): ")
    uppercase = input().lower() == 'y'
    #lowercase
    print("Include Lowercase Letters? (y/n): ")
    lowercase = input().lower() == 'y'
    #digits
    print("Include Digits? (y/n): ")
    digits = input().lower() == 'y'
    #special characters
    print("Include Special Characters? (y/n): ")
    specialCharacters = input().lower() == 'y'
    
    #validate that at least one character type is selected
    if not (uppercase or lowercase or digits or specialCharacters):
        print("At least one character type must be selected.")
        return

    password = generate_password(length, uppercase, lowercase, digits, specialCharacters)
    
    print("Generated Password:")
    print(password)
    print("Do you want to check the strength of the generated password? (y/n): ")
    if input().lower() == 'y':
        check_strength(password)

    print("Do you want to save the generated password to a file? (y/n): ")
    if input().lower() == 'y':
        Save_Password_to_File(password)
    else:
        print("Password not saved.")


if __name__ == "__main__":
    main()

'''
if examiner asks:
Why did you use secrets instead of random?

You answer:
The random module is not cryptographically secure and can be predictable. 
The secrets module is designed for generating secure tokens and passwords, 
making it suitable for cybersecurity applications.
--------------------------------------------------------------------------------------------------------
Q: 
How does your system determine strength?

Answer:
The system uses a scoring-based algorithm that evaluates length and character diversity. 
Each security factor contributes to the total score, 
and the final strength classification is determined based on the score range.
--------------------------------------------------------------------------------------------------------
If asked:
How does your program prevent runtime errors?

You can say:
I implemented a try-except block to handle ValueError exceptions when converting user input to integer
The loop ensures the program continues prompting until valid input is provided.
-------------------------------------------------------------------------------------------------------
Q: 
Why did you create a separate function for file saving?

Answer:
To maintain modular design and separation of concerns. 
Each function performs a specific task, making the program easier to maintain and extend.
-------------------------------------------------------------------------------------------------------

'''