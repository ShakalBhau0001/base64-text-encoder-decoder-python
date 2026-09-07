import base64 as bs


def encode_text(text):
    encoded = bs.b64encode(text.encode("utf-8"))
    return encoded.decode("utf-8")


def decode_text(encoded_text):
    decoded = bs.b64decode(encoded_text)
    return decoded.decode("utf-8")


def main():
    print("=" * 40)
    print("        BASE64 - ENCODER | DECODER")
    print("=" * 40)
    while True:
        print("\n[1] Encode")
        print("[2] Decode")
        print("[3] Exit")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            text = input("Enter text: ")
            try:
                result = encode_text(text)
                print("\nEncoded Base64:")
                print(result)
            except Exception as error:  # noqa: BLE001
                print(f"Error: {error}")

        elif choice == "2":
            encoded_text = input("Enter Base64 text: ")
            try:
                result = decode_text(encoded_text)
                print("\nDecoded text:\n")
                print(result)
            except Exception:  # noqa: BLE001
                print("\nInvalid Base64 input.")

        elif choice == "3":
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
