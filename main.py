email = input("Enter your email: ")
is_valid = True

# Length check
if len(email) >= 6:
    # Check if the first character is alphabetic
    if email[0].isalpha():
        # Check for exactly one "@" character
        if email.count("@") == 1:
            # Check if the email ends with a dot in the last three or four characters
            if email[-4] == '.' or email[-3] == '.':
                # Check for uppercase letters
                if not any(char.isupper() for char in email):
                    # Check for spaces
                    if ' ' not in email:
                        print("Valid email")
                    else:
                        print("Invalid email: No spaces allowed.")
                else:
                    print("Invalid email: Must contain at least one uppercase letter.")
            else:
                print("Invalid email: Must contain a dot in the last three or four characters.")
        else:
            print("Invalid email: Must contain exactly one '@' symbol.")
    else:
        print("Invalid email: First character must be an alphabet.")
else:
    print("Invalid email: Must be at least 6 characters long.")
