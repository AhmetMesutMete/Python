import string
import secrets


def contains_upper(password: str) -> bool:
    """Check if password contains an uppercase letter."""
    return any(char.isupper() for char in password)
    

def contains_symbols(password: str) -> bool:
    """Check if password contains symbols."""
    return any(char in string.punctuation for char in password)


def generate_password(length: int = 15, symbols: bool = False, uppercase: bool= True) -> str:
    """Generate a secure random password according to your preferences."""
    if length < (symbols + uppercase):
        raise ValueError('The length is not long enough to include required elements.')
    
    combination: str = string.ascii_lowercase + string.digits
    new_password = []

    if symbols:
        new_password.append(secrets.choice(string.punctuation))
        combination += string.punctuation

    if uppercase:
        new_password.append(secrets.choice(string.ascii_uppercase))
        combination += string.ascii_uppercase

    while len(new_password) < length:
        new_password.append(secrets.choice(combination))

    secrets.SystemRandom().shuffle(new_password)

    return ''.join(new_password)


if __name__ == "__main__":

    try:
        num_of_passwords = int(input('How many passwords would you like to generate? '))
        length_pref = int(input('Please state the length of the passwords you\'d like generate: '))
        symbols_pref = input('Would you like your password to contain symbols? (Yes/No) ').lower() == 'yes' 
        uppercase_pref = input('Would you like your password to contain uppercase characters? (Yes/No) ').lower() == 'yes'
        
        for i in range(1,num_of_passwords+1):
            new_pass: str = generate_password(length_pref, symbols_pref, uppercase_pref)
            
            if symbols_pref != contains_symbols(new_pass):
                raise 'Symbol pref not met in {i}. try!'
            
            if uppercase_pref != contains_upper(new_pass):
                raise 'Uppercase pref not met in {i}. try!'
            
            specs: str = f'U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}'
            print(f'{i} -> {new_pass}: ({specs})')

    except ValueError as e:
        print(f"Error: {e}")
