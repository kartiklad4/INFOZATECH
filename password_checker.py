import re

def check_password(password):
    # Simple blocklist of common words
    blocklist = ["password", "password123", "qwerty", "12345678", "admin"]
    if password.lower() in blocklist:
        return "Weak (Common/Guessed Password)", "Change this immediately! It is in the blocklist."
    
    score = 0
    feedback = []
    
    if len(password) >= 8: score += 1
    else: feedback.append("Make it at least 8 characters long.")
        
    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("Add uppercase letters.")
        
    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("Add lowercase letters.")
        
    if re.search(r"\d", password): score += 1
    else: feedback.append("Add numbers.")
        
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password): score += 1
    else: feedback.append("Add special symbols.")

    # Rating logic
    if score <= 2: rating = "Weak"
    elif score <= 4: rating = "Medium"
    else: rating = "Strong"
        
    return rating, " ".join(feedback) if feedback else "Great job! Secure password."

pwd = input("Enter a password to test: ")
strength, advice = check_password(pwd)
print(f"\nRating: {strength}\nFeedback: {advice}")
