import random

LOWCHARS = 'abcdefghijklmnopqrstuvwxyz'
UPCHARS = ''.join([c.upper() for c in LOWCHARS])
NUMBERS = '0123456789'
SPECIAL = '!$%^&*@#'

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
    feed = LOWCHARS
    if useUpper:
        feed += UPCHARS
    
    if useNumbers:
        feed += NUMBERS

    if useSpecial:
        feed += SPECIAL
    
    return ''.join(random.sample(feed, length))

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
    print(generate_random_password())
    print(generate_random_password(useUpper=True))
    print(generate_random_password(length=12, useUpper=True, useNumbers=True))
    print(generate_random_password(length=20, useUpper=True, useNumbers=True, useSpecial=True))
    print(generate_random_password(length=15, useUpper=True, useSpecial=True))
