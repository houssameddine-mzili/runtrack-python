def caesar_cipher(message, shift):

    encrypted_message = ""

    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + shift) % 26
            encrypted_char = chr(start + offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char

    return encrypted_message

message_to_cipher = "LaPlateforme"
shift_amount = 3  
encrypted_message = caesar_cipher(message_to_cipher, shift_amount)
print(encrypted_message)
