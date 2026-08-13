

def report_to_duty(name):
    if not isinstance(name, str):
        return "Only string is allowed"

    name = name.strip()
    if not name:
        return "Name cannot be empty"
    
    return f"Recruit {name} reporting for duty"

print(report_to_duty("    James    "))
print(report_to_duty(["a","b"]))
print(report_to_duty(" 65"))