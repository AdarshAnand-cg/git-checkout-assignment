import time
import random
import os

GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

os.system("cls" if os.name == "nt" else "clear")

print(CYAN + "=" * 50)
print("        ⚡ CYBER TERMINAL SIMULATOR ⚡")
print("=" * 50 + RESET)

username = input("\nEnter your name: ")

slow_print(f"\nWelcome, {username}...")
slow_print("Initializing system...")

for i in range(1, 6):
    print(f"{GREEN}[+] Loading module {i}/5...{RESET}")
    time.sleep(0.5)

print("\nSystem Status: ONLINE ✅")

while True:
    print("\n" + "-" * 40)
    print("1. Generate Random Password")
    print("2. Roll a Dice")
    print("3. Check Even/Odd")
    print("4. Exit")
    print("-" * 40)

    choice = input("Choose an option: ")

    if choice == "1":
        password = ""
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%"
        
        for _ in range(12):
            password += random.choice(characters)

        print(f"\n🔐 Generated Password: {password}")

    elif choice == "2":
        dice = random.randint(1, 6)
        print(f"\n🎲 You rolled: {dice}")

    elif choice == "3":
        number = int(input("\nEnter a number: "))

        if number % 2 == 0:
            print(f"⚡ {number} is EVEN")
        else:
            print(f"🔥 {number} is ODD")

    elif choice == "4":
        print("\n👋 Shutting down terminal...")
        time.sleep(1)
        break

    else:
        print("\n❌ Invalid choice!")

print("\nSystem terminated successfully.")
