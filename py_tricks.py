attendance = {
    "Emma": ["P","P","A","P","P"],
    "James": ["A","P","P","P","P"],
    "Joel": ["P","A","A","P","P"],
    "Desire": ["P","P","P","P","P"]
}

# refactor into a function
def student_record(attendance):
    for student, record in attendance.items():
        present = record.count("P")
        percentage = present / len(record) * 100
    
        status = (
        "Eligible"
        if percentage >= 75
        else "Not Eligible"
        )
    return """
    {student}
    Attendance: {percentage:.0f}%
    {status}
    '*' * 20
    """
    
record= student_record(attendance)
print(record)
