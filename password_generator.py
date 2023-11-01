import random
import string

def generate_password(min_len, numbers=True, spec_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if spec_char:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if spec_char:
            meets_criteria = meets_criteria and has_special
        
    return pwd

def main():
  min_len = int(input("Enter the minimum length: "))
  has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
  has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
  pwd = generate_password(min_len, has_number, has_special)
  print("The generated password is: ", pwd)

if __name__ == "__main__":
    main()
