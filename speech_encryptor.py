import argparse

def encrypt_text(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + 3) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_text(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - 3) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("SX-king")
    parser = argparse.ArgumentParser(description="Encrypt and decrypt text using a simple substitution cipher.")
    parser.add_argument("-e", "--encrypt", help="Encrypt the provided text")
    parser.add_argument("-d", "--decrypt", help="Decrypt the provided text")
    parser.add_argument("-i", "--input-file", help="Read input from a file")
    parser.add_argument("-o", "--output-file", help="Write output to a file")
    args = parser.parse_args()

    if args.encrypt:
        encrypted_text = encrypt_text(args.encrypt)
        if args.output_file:
            try:
                with open(args.output_file, "w") as file:
                    file.write(encrypted_text)
                print(f"Encrypted text written to {args.output_file}")
            except IOError:
                print(f"Error: Unable to write to {args.output_file}")
        else:
            print("Encrypted text:", encrypted_text)
    elif args.decrypt:
        decrypted_text = decrypt_text(args.decrypt)
        if args.output_file:
            try:
                with open(args.output_file, "w") as file:
                    file.write(decrypted_text)
                print(f"Decrypted text written to {args.output_file}")
            except IOError:
                print(f"Error: Unable to write to {args.output_file}")
        else:
            print("Decrypted text:", decrypted_text)
    elif args.input_file:
        try:
            with open(args.input_file, "r") as file:
                input_text = file.read()
            encrypted_text = encrypt_text(input_text)
            decrypted_text = decrypt_text(encrypted_text)
            if args.output_file:
                try:
                    with open(args.output_file, "w") as file:
                        file.write(decrypted_text)
                    print(f"Decrypted text written to {args.output_file}")
                except IOError:
                    print(f"Error: Unable to write to {args.output_file}")
            else:
                print("Encrypted text:", encrypted_text)
                print("Decrypted text:", decrypted_text)
        except FileNotFoundError:
            print(f"Error: File {args.input_file} not found")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
