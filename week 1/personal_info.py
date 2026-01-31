# Name: Giriprasath K
# Project: Personal Information Manager
# Description: A simple Python program that stores, collects, and displays
#              personal information using variables, input/output, and
#              string formatting with basic validation.

# -------------------------
# Welcome Message
# -------------------------
print("=" * 50)
print("Welcome to the Personal Information Manager!")
print("=" * 50)

# -------------------------
# Static Information
# -------------------------

# Store basic personal details using appropriate data types
name = "Giriprasath K"          # String to store name
age = 20                    # Integer to store age
city = "Ratnagiri"          # String to store city
hobby = "Reading"           # String to store hobby

# Calculate age in months
age_in_months = age * 12

# -------------------------
# User Input with Validation
# -------------------------

# Get user's favorite food
favorite_food = input("Enter your favorite food: ").strip()
if not favorite_food:
    favorite_food = "Not specified"

# Get user's favorite color
favorite_color = input("Enter your favorite color: ").strip()
if not favorite_color:
    favorite_color = "Not specified"

# -------------------------
# Display Formatted Output
# -------------------------

print("\n" + "-" * 50)
print("PERSONAL INFORMATION SUMMARY")
print("-" * 50)

print(f"Name              : {name.title()}")
print(f"Age               : {age} years")
print(f"Age in Months     : {age_in_months} months")
print(f"City              : {city.title()}")
print(f"Hobby             : {hobby.capitalize()}")

print("\n" + "-" * 50)
print("USER PREFERENCES")
print("-" * 50)

print(f"Favorite Food     : {favorite_food.capitalize()}")
print(f"Favorite Color    : {favorite_color.capitalize()}")

# -------------------------
# Goodbye Message
# -------------------------
print("\nThank you for using the Personal Information Manager!")
print("Have a great day! 😊")
