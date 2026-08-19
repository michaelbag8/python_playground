# group two task
def report_to_duty(name):
    #type check
    if not isinstance(name, str):
        return "Only string is allowed"

    #removing trailing and leading space 
    name = name.strip()
    #checking for empty value
    if not name:
        return "Name cannot be empty"
    #checking for only letters
    if not name.replace(" ", "").isalpha():
        return "Only letters are allowed"
        
    return f"Recruit {name} reporting for duty"

print(report_to_duty("    James    "))
print(report_to_duty(["a","b"]))
print(report_to_duty(" 65"))
