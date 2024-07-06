import hashlib

def cracker(supplied_hash, algorithm):
    if algorithm == 'md5':
        hash_function = hashlib.md5
    elif algorithm == 'sha1':
        hash_function = hashlib.sha1    
    elif algorithm == 'sha256':
        hash_function = hashlib.sha256
    elif algorithm == 'sha512':
        hash_function = hashlib.sha512
    else:
        raise ValueError(f"Unsupported algorithm '{algorithm}'")
    
    # Open the passwords.txt file for reading
    with open("passwords.txt", "r") as passwords: 
        for line in passwords:
            password = line.strip()  # Remove any leading/trailing whitespace
            encoded_text = password.encode('utf-8')  # Encode password to bytes
            calculated_hash = hash_function(encoded_text).hexdigest()  # Calculate hash
            if calculated_hash == supplied_hash:
                return password  # Return the cracked password if hash matches
            
        # If no password matches the supplied hash
        return "Password can not be cracked in this wordlist"

# Function to get user input
def user_input():
    hash = input("Enter the hashed password that you want to crack: ")

    algorithms = '''
    Please select the algorithm of the above entered hash: 
    1. MD5
    2. SHA-1
    3. SHA-256
    4. SHA-512
    '''
    print(algorithms)
    algo = input("Select 1, 2, 3, or 4: ")

    if algo == "1":
        return hash, "md5"
    elif algo == "2":
        return hash, "sha1"
    elif algo == "3":
        return hash, "sha256"
    elif algo == "4":
        return hash, "sha512"
    else: 
        return hash, "Invalid algorithm selected"

# Main function to handle other functions
def main():
    hash, algorithm = user_input()
    if algorithm != "Invalid algorithm selected":
        crack_result = cracker(hash, algorithm)
        if crack_result != "Password can not be cracked in this wordlist":
            print(f"Cracked password for hash {hash} is: {crack_result} ")
        else:
            print(crack_result)
    else: 
        print(algorithm)


if __name__=="__main__":
    main()
