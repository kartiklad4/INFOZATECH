def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

print("--- Classical Caesar Cipher Toolkit ---")
mode = input("Type 'encrypt' or 'decrypt': ").strip().lower()
message = input("Enter your message: ")
shift_key = int(input("Enter shift key number (1-25): "))

processed_text = caesar_cipher(message, shift_key, mode)
print(f"\nResult Text: {processed_text}")
