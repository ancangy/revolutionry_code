import hashlib

def reduction_function_dynamic(hash_str, length=5):
    # Use the first portion of the hash, scaled by length
    portion_of_hash = int(hash_str[:8], 16)  # Convert the first 8 hex characters to an integer
    dynamic_value = portion_of_hash % (26**length)
    
    # Convert dynamic value to a string of the desired length
    reduced_password = ''
    for _ in range(length):
        dynamic_value, remainder = divmod(dynamic_value, 26)
        reduced_password += chr(97 + remainder)  # Map to a-z
    
    return reduced_password

# Hashing function using SHA-256
def hash_function(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create the rainbow table
def create_rainbow_table(start_passwords, chain_length,pass_length):
    rainbow_table = {}
    for password in start_passwords:
        current_password = password
        start_hashed = hash_function(current_password) 
        end_hashed =  start_hashed
        for i in range(chain_length):
            current_password = reduction_function_dynamic(end_hashed, pass_length)   
            end_hashed = hash_function(current_password)
        if password not in rainbow_table:  # Only store if not already stored
            bound = dict()
            bound['start'] = start_hashed
            bound['end'] = end_hashed
            rainbow_table[password] =bound  # Store the final hash with the initial password
            print(f"Stored in Rainbow Table: {bound} -> {password}")  # Print each entry
    return rainbow_table

# Function to crack a hash using the rainbow table
def crack_password(in_hash_to_crack, rainbow_table, pass_length=5):
    
    for key in rainbow_table: 
        hashed = hash_function(key) 
        if in_hash_to_crack == rainbow_table[key]['start']:
            return key
        while hashed != rainbow_table[key]['end']:
            current_password = reduction_function_dynamic(hashed,pass_length)   
            hashed = hash_function(current_password)
            if hashed == in_hash_to_crack:
                return current_password



# Example usage
start_passwords = ['aaaaa', 'bbbbb', 'ccccc']
chain_length = 100  # Reduce the chain length to minimize collision chances
pass_length = 5

# Create the rainbow table
rainbow_table = create_rainbow_table(start_passwords, chain_length, pass_length)
print(rainbow_table)


print(crack_password('ed968e840d10d2d313a870bc131a4e2c311d7ad09bdf32b3418147221f51a6e2', rainbow_table)) #result aaaaa
print(crack_password('bca245dc935703c4a690c27aa4345e12de428b31012f17602f21681fdc551d5a', rainbow_table)) #result nfupc
print(crack_password('4cbe90354066ecc761dbea96a5d8e69279216b2c6715b97cc5053fe0cbccfddb', rainbow_table)) #result tjdaa
print(crack_password('631a4571fc09d78d894400f508d6c30243afb99a13d00d816dc547fbe7af8ae8', rainbow_table)) #result cjckt
