attendance = {
    "Emma": ["P","P","A","P","P"],
    "James": ["A","P","P","P","P"],
    "Joel": ["P","A","A","P","P"],
    "Desire": ["P","P","P","P","P"]
}

# refactor into a function
def student_record(attendance):
    lines = []
    for student, record in attendance.items():
        present = record.count("P")
        percentage = present / len(record) * 100
        status = "Eligible" if percentage >= 75 else "Not Eligible"

        lines.append(
            f"{student}\n"
            f"Attendance: {percentage:.0f}%\n"
            f"{status}\n"
            f"{'*' * 20}"
        )
    return "\n".join(lines)

record = student_record(attendance)
print(record)
