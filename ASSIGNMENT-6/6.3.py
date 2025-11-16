def classify_age(age):
    if age < 0:
        return "Invalid age"
    else:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        elif age <= 64:
            return "Adult"
        else:
            return "Senior"

print(classify_age(10))
print(classify_age(16))
print(classify_age(35))
print(classify_age(80))