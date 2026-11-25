def is_palindrome(s):
    clean = s.replace(" ", "").lower()
    return clean == clean[::-1]

s = "Madam"
print("Palindrome" if is_palindrome(s) else "Not palindrome")
