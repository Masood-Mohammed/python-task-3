import random
import string

def generate_password(length):
    # Define the character sets to use in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choices (available in Python 3.6+)
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    print("----------------------------------")
    
    try:
        length = int(input("Enter the desired length of your password: "))
        
        if length <= 0:
            print("Length should be greater than zero.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
