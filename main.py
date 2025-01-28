"""
Ling, Za

https://github.com/zlingx1/Module-2-Lab

If...Else...While
Application asks for student information (last_name, first_name, gpa), and processes them on eligible rewards 
"""


# Const
 
EXIT = "ZZZ"

DEAN_LIST = 3.5
HONOR_ROLL = 3.25

def input_number(prompt, error): # Recurse until user inputs valid number
    value = input(prompt)

    try:
        number = float(value)
        return number
    except:
        print(error)
        return input_number(prompt, error)

def input_name(prompt, error): # Recurse until user inputs valid text
    name = input(prompt)

    if not name or not name.isalpha():
        print(error)
        return input_name(prompt, error)
    
    return name

def process_input():
    last_name = input_name("Enter last name: ", "Invalid last name...")
    
    if last_name == EXIT:  # If exit code is reached, return
        return False

    first_name = input_name("Enter first name: ", "Invalid first name...")
     
    gpa = input_number("Enter GPA: ", "Invalid GPA...")
    
    if gpa >= DEAN_LIST: 
        print(f"{last_name}, {first_name} is eligible for the Dean's list!")
    elif gpa >= HONOR_ROLL:
        print(f"{last_name}, {first_name} is eligible for the Honor Roll!")
    else:
        print(f"{last_name}, {first_name} is not eligible for an award!")

    return True

def main():
    while(process_input()):
        pass

if __name__ == "__main__":
    main()

