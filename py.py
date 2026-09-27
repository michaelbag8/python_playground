import random
import string


def password_generator(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


def determine_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    return "D"


def build_report(students):
    report = {}

    for name, marks in students.items():
        average = sum(marks) / len(marks)
        report[name] = {
            "average": round(average, 2),
            "grade": determine_grade(average),
        }

    for name, info in sorted(
        report.items(), key=lambda item: item[1]["average"], reverse=True
    ):
        print(f"{name:<8} | {info['average']:>5} | Grade: {info['grade']}")

    return report


def main():
    students = {
        "Emma": [67, 89, 90],
        "James": [100, 78, 92],
        "Joel": [54, 71, 98],
        "Desire": [53, 22, 89],
    }

    report = build_report(students)
    print(report)

    password = password_generator()
    print("\033[32mGenerated Password\033[0m")
    print("\033[33m" + password + "\033[0m")


if __name__ == "__main__":
    main()
