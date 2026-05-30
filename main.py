import json
from datetime import datetime
# Load data from JSON file
with open("tips.json", "r") as file:
    data = json.load(file)
# Ask user name
name = input("Enter your name: ")
print(f"\nHello, {name}! Welcome to Smart Student Assistant")
print("\nMenu:")
print("1. Generate Study Tip")
print("2. Generate Motivation Quote")
print("3. Display Current Date & Time")
choice = input("\nEnter your choice (1-3): ")
if choice == "1":
    result = data["study_tips"][0]
elif choice == "2":
    result = data["quotes"][0]
elif choice == "3":
    result = str(datetime.now())
else:
    result = "Invalid choice"
print("\nResult:")
print(result)
# Save to output file
with open("output.txt", "a") as file:
    file.write(result + "\n")
print("\nResult saved to output.txt")