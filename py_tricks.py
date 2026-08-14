attendance = {
    "Emma": ["P","P","A","P","P"],
    "James": ["A","P","P","P","P"],
    "Joel": ["P","A","A","P","P"],
    "Desire": ["P","P","P","P","P"]
}

# refactor into a function
for student, record in attendance.items():
    present = record.count("P")
    percentage = present / len(record) * 100


    status = (
        "Eligible"
        if percentage >= 75
        else "Not Eligible"
        )

    print(student)
    print(f"Attendance: {percentage:.0f}%")
    print(status)
    print("-" * 20)
