import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generate a random password with given settings."""
    # Build a string of available characters based on the selected options.
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Check if at least one character set is selected.
    if not characters:
        return "Please select at least one option!"
    
    # Generate the password by randomly choosing from the characters.
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def validate_password(password, min_length=8):
    """Validate the given password against common criteria."""
    errors = []
    if len(password) < min_length:
        errors.append(f"Password must be at least {min_length} characters long.")
    if not any(c.isupper() for c in password):
        errors.append("Password must include at least one uppercase letter.")
    if not any(c.islower() for c in password):
        errors.append("Password must include at least one lowercase letter.")
    if not any(c.isdigit() for c in password):
        errors.append("Password must include at least one digit.")
    if not any(c in string.punctuation for c in password):
        errors.append("Password must include at least one special character.")
    return errors

# --- Password Generator Section ---
st.title("Password Generator & Validator")

st.header("Generate a Password")
# Slider to choose password length
length = st.slider("Select Password Length", min_value=4, max_value=32, value=12)

# Checkboxes for character set options
use_upper = st.checkbox("Include Uppercase Letters", value=True)
use_lower = st.checkbox("Include Lowercase Letters", value=True)
use_digits = st.checkbox("Include Digits", value=True)
use_special = st.checkbox("Include Special Characters", value=True)

# Button to generate the password
if st.button("Generate Password"):
    generated_password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    st.success(f"Generated Password: {generated_password}")

# --- Password Validation Section ---
st.header("Validate Your Password")
# Input field for the user to enter a password
user_password = st.text_input("Enter a password to validate:")

if st.button("Validate Password"):
    if user_password:
        validation_errors = validate_password(user_password)
        if not validation_errors:
            st.success("Your password is strong and meets all the criteria!")
        else:
            st.error("Your password did not meet the following criteria:")
            for err in validation_errors:
                st.write(f"- {err}")
    else:
        st.warning("Please enter a password to validate.")