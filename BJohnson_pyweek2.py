# Example: Grad# Example: Grading system using if, elif, else
#
# score = 85  # Change this number to test (0–100)
# print(f"Your score is: {score}")
#
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")
#
# print("Keep studying!")ing system using if, elif, else

score = 85  # Change this number to test (0–100)
print(f"Your score is: {score}")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print("Keep studying!")

# Example: Simple login using if, elif, else

username = "admin"     # correct username
password = "1234"      # correct password

# Try different combinations below
entered_username = "admin"
entered_password = "0000"

print(f"Trying login for: {entered_username}")

if entered_username == username and entered_password == password:
    print("Access granted.")
elif entered_username == username:
    print("Wrong password!")
else:
    print("User not found.")

# Example: Temperature check using if, elif, else

temperature = 32  # Change this number to test (in degrees Celsius)
print(f"The temperature is: {temperature}°C")

if temperature >= 30:
    print("It's hot outside.")
elif temperature >= 20:
    print("It's warm outside.")
elif temperature >= 10:
    print("It's cool outside.")
else:
    print("It's cold outside.")

print("Check the weather before going out!")

