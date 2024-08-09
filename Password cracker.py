from passlib.hash import sha256_crypt

# Load shadow file and password list
shadow_file = 'new_shadow.txt'
password_list = 'new_passwords.txt'

def crack_passwords(shadow_file, password_list):
    with open(shadow_file, 'r') as sf, open(password_list, 'r') as pl:
        shadow_lines = sf.readlines()
        passwords = pl.readlines()

        for shadow_line in shadow_lines:
            username, hashed_password = shadow_line.split(':')[0], shadow_line.split(':')[1].strip()
            print(f"Checking for user: {username}")
            for password in passwords:
                password = password.strip()
                print(f"Trying password: {password}")
                if sha256_crypt.verify(password, hashed_password):
                    print(f"Password for {username} found: {password}")
                    break

# Call the function
crack_passwords(shadow_file, password_list)

