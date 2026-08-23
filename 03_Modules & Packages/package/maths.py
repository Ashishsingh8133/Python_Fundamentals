
## I have created Addition Function
def addition(a,b):
    return a+b

##Substraction Function
def substraction(a,b):
    return a-b 

##Function to check whether the password is strong or not 
def is_strong(password):
    if len(password)<8:
        print(f" password should be more tha 8 words")
        return False
    if not any(char.isdigit() for char in password):
        print(f"password contains all digits")
        return False
    if not any(char.islower() for char in password):
        print(f"password contains all lower case letters")
        return False
    if not any(char.isupper() for char in password):
        print(f"password contains all upper case letters")
        return False
    if not any(char in '!@#?.,' for char in password):
        return False
    
    print(f"it's a strong password")
    return True