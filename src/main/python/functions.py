import random
import string

SPECIALS = '!$%^&*@#'        # Well, could use string.punctuation, but only needs these really...

############################################
def generate_random_password(length = 8, useUpper = False, useNumbers = False, useSpecial = False):
    '''
    Generates a random password from a set of letters, numbers and special characters.

    Parameters:
        length (int) - Number of characters to use for the password.
        useUpper (bool) - Flag to indicate use of uppercase letters.
        useNumbers (bool) - Flag to indicate use of numerical characters.
        useSpecial (bool) - Flag to indicate use of special characters.
    Return:
        A passwords with randomly selected characters.
    '''
    ichar = 0       # Start counting how many character are filled

    # By default, start with lowercase letters...
    feed = string.ascii_lowercase
    password = random.SystemRandom().choice(string.ascii_lowercase)
    ichar += 1

    if useUpper:
        # Add uppercase (at least one and add to the pool)
        feed += string.ascii_uppercase
        password += random.SystemRandom().choice(string.ascii_uppercase)
        ichar += 1
    
    if useNumbers:
        # Add digits (at least one and add to the pool)
        feed += string.digits
        password += random.SystemRandom().choice(string.digits)
        ichar += 1

    if useSpecial:
        # Add special characters (at least one and add to the pool)
        feed += SPECIALS
        password += random.SystemRandom().choice(SPECIALS)
        ichar += 1

    if ichar < length:
        for i in range(length - ichar):
            password += random.SystemRandom().choice(feed)

    # OK, strictly speaking, I may exceed the max length...
    # could do something funcy to create a smaller one?
        
    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    return ''.join(password_list)

############################################
def meetsCriteria(password, charset, mincount=1):
    '''
    Checks if the password meets certain criteria.

    Parameters:
        password (str) - Password string to be checked.
        charset (str) - Characters' set to compare with.
        mincount (int) - Minimum number of characters from charset to be found in password.
    Return:
        The result of the test. True if it passes, false otherwise.
    '''
    count = 0
    for c in password:
        if c in charset:
            count += 1
    return count >= mincount


if __name__ == "__main__":
    print(f" 8 lowercase letters only          :: {generate_random_password()}")
    print(f" 8 lower+uppercase letters         :: {generate_random_password(useUpper=True)}")
    print(f"12 lower+uppercase+digits          :: {generate_random_password(length=12, useUpper=True, useNumbers=True)}")
    print(f"20 lower+uppercase+digits+specials :: {generate_random_password(length=20, useUpper=True, useNumbers=True, useSpecial=True)}")
    print(f"15 lower+uppercase+specials        :: {generate_random_password(length=15, useUpper=True, useSpecial=True)}")
