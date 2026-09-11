code = input("Enter a code: ").strip()

if len(code) == 0 or code[0] == "A":
    print("Invalid code.")
else:
    print("Valid code.")