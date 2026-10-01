# Group two task


def validate_name(name):
    """Validate a candidate name before assigning duty."""
    if not isinstance(name, str):
        raise TypeError("Only string is allowed")

    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Only letters are allowed")

    return name


def report_to_duty(name):
    """Return a duty report message for a valid name."""
    try:
        valid_name = validate_name(name)
    except (TypeError, ValueError) as error:
        return str(error)

    return f"Recruit {valid_name} reporting for duty"


if __name__ == "__main__":
    print(report_to_duty("    James    "))
    print(report_to_duty(["a", "b"]))
    print(report_to_duty(" 65"))
