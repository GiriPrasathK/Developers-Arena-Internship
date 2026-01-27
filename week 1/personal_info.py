# Giriprasath K
# Project: Personal Information Manager
# Description: A simple Python program to store and display personal information

# ---------------- Welcome Message ----------------
print("=" * 40)
print("     Personal Information Manager")
print("=" * 40)
print()

# ---------------- Static Information ----------------
user_name = "Giriprasath K"        # User's full name
user_age = 22                      # User's age in years
user_city = "Ratnagiri"            # City of residence
user_hobbies = "Cricket, Football"  # User hobbies

# ---------------- User Input Section ----------------
print("Please tell me about yourself:")
print("-" * 40)

favorite_food = input("What's your favorite food? ").strip()
while not favorite_food:
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ").strip()

favorite_color = input("What's your favorite color? ").strip()
while not favorite_color:
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ").strip()

# ---------------- Calculations ----------------
age_in_months = user_age * 12

# ---------------- Display Information ----------------
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name           : {user_name}")
print(f"Age            : {user_age} years ({age_in_months} months)")
print(f"City           : {user_city}")
print(f"Hobbies        : {user_hobbies}")
print()
print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.title()}")
print()

# ---------------- Goodbye Message ----------------
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)
