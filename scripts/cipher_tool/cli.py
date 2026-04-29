# cli.py

import argparse
from caesar_cipher import caesar, brute_force


def main():
    parser = argparse.ArgumentParser(
        description="🔐 Caesar Cipher Tool (Encrypt, Decrypt, Brute Force)"
    )

    parser.add_argument("-t", "--text", required=True, help="Input text")
    parser.add_argument("-s", "--shift", type=int, help="Shift value (1-25)")
    parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt", "brute"], required=True)

    args = parser.parse_args()

    if args.mode in ["encrypt", "decrypt"]:
        if args.shift is None:
            print("❌ Shift is required for encrypt/decrypt")
            return

        result = caesar(args.text, args.shift, encrypt=(args.mode == "encrypt"))
        print(f"\n✅ Result:\n{result}")

    elif args.mode == "brute":
        print("\n🔍 Brute Force Results:\n")
        results = brute_force(args.text)
        for shift, output in results:
            print(f"[Shift {shift}] {output}")


if __name__ == "__main__":
    main()