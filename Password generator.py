from passlib.hash import sha256_crypt

# Creating a new shadow file with known passwords
passwords = {
    "user0": "password123",  # Password to hash
    "user1": "123456",
    "user2": "qwerty"
}

# Generate the corresponding shadow file content
shadow_content = ""
for user, password in passwords.items():
    hashed_password = sha256_crypt.hash(password)
    shadow_content += f"{user}:{hashed_password}\n"

# Write the shadow.txt file with the hashed passwords
with open('new_shadow.txt', 'w') as shadow_file:
    shadow_file.write(shadow_content)

# Create a passwords.txt file that includes the correct passwords and some wrong guesses
password_list_content = """password123
123456
qwerty
password
abc123
letmein
monkey
dragon
111111
123456789
sunshine
"""

with open('new_passwords.txt', 'w') as password_list_file:
    password_list_file.write(password_list_content)
