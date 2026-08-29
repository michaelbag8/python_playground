import random
import string

def password_generator():

characters = string.ascii_letters + string.digits + string.punctuation

length = 16
password = "".join(
    random.choice(characters) for _ in range(length)
)
return password 


def build_report(students):
    
report = {}

    for name, marks in students.items():
    average = sum(marks) / len(marks)

        report[name] = {
        "average": round(average,2),
        "grade": (
            "A" if average >= 90 else
            "B" if average >= 80 else
            "C" if average >= 70 else
            "D"
        )
    }

    for name , info in sorted(
    report.items(),
    key=lambda item: item[1]["average"],
    reverse=True
):
    print(
        f"{name:<8} | "
        f"{info["average"]:>5} | "
        f"Grade: {info["grade"]}"
    )
return report 

students = {
    "Emma": [67,89,90],
    "James": [100,78,92],
    "Joel": [54,71,98],
    "Desire": [53,22,89]
}

report = build_report(students)
print(report)


print("\033[32mGenerated Password\033[0m")
print("\033[33m" + password + "\033[0m")
