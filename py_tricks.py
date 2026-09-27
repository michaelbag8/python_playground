ATTENDANCE_THRESHOLD = 75
SEPARATOR = "*" * 20

attendance = {
    "Emma": ["P", "P", "A", "P", "P"],
    "James": ["A", "P", "P", "P", "P"],
    "Joel": ["P", "A", "A", "P", "P"],
    "Desire": ["P", "P", "P", "P", "P"],
}


def calculate_attendance_percentage(record):
    if not record:
        return 0.0

    present_days = record.count("P")
    return (present_days / len(record)) * 100


def determine_eligibility(percentage, threshold=ATTENDANCE_THRESHOLD):
    return "Eligible" if percentage >= threshold else "Not Eligible"


def format_student_report(student, record, threshold=ATTENDANCE_THRESHOLD):
    percentage = calculate_attendance_percentage(record)
    status = determine_eligibility(percentage, threshold)

    return (
        f"{student}\n"
        f"Attendance: {percentage:.0f}%\n"
        f"{status}\n"
        f"{SEPARATOR}"
    )


def student_record(attendance, threshold=ATTENDANCE_THRESHOLD):
    lines = [
        format_student_report(student, record, threshold)
        for student, record in sorted(attendance.items())
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    print(student_record(attendance))
