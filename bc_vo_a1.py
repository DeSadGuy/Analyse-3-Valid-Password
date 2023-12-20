'''
Problem Statement:
In an application a valid password must be a combination of digits, uppercase and lowercase letters and only four symbols {*,@,!,?}.
Implement a Python program that asks the password of the user and checks if it is a valid password.

Criteria:
- The length of the password must not be less than 8 characters and must not be more than 20 characters.
- In case the password is not valid, the user can try maximum three times to validate the password.
- Print Valid on a validated password and Invalid on a invalidated password.
- Use sets and set operations to solve this problem.
- Do not use extra messages or text in the interactions.

Input example:
Password: B4s3c4p

Output example:
Invalid

Input example:
Password: B4s3c*4p

Output example:
Valid
'''
def checkdigit(value:str)->bool:
    for letter in value:
        if letter.isdigit():
            return True
    return False

def checklower(value:str)->bool:
    for letter in value:
        if letter.islower():
            return True
    return False
    
def checkupper(value:str)->bool:
    for letter in value:
        if letter.isupper():
            return True
    return False
    
def checksymbol(value:str)->bool:
    for letter in value:
        if letter in ["*","@","!","?"]:
            return True
    return False

def checklength(value:str)->bool:
    
    if len(value) >= 8 and len(value) <= 20:
        return True
    else:
        return False
    
def validate_password(password:str)->bool:
    # TODO: implement the body of the function
    if checkdigit(password) and checklower(password) and checkupper(password) and checksymbol(password) and checklength(password):
        return True
    else:
        return False


def main():
    # TODO: implement the body of the function
    attempts = 0 
    while attempts < 3:
        password = input("Password: ")
        if validate_password(password):
            print("Valid")
            break
        else:
            print("Invalid")
            attempts += 1

def test_validate_password():
    print("password: 12345678 - expected: False - actual:", validate_password("12345678"))
    print("password: 12345678a - expected: False - actual:", validate_password("12345678a"))
    print("password: 12345678A - expected: False - actual:", validate_password("12345678A"))
    print("password: Password123 - expected: False - actual:", validate_password("Password123"))
    print("password: Password*123 - expected: True - actual:", validate_password("Password*123"))
    

if __name__ == "__main__":
    main()
    #test_validate_password()

