import re


def validate_email(email: str) -> bool:
    """
    Validate email format.
    """
    if not email:
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(re.match(pattern, str(email)))


def validate_phone(phone: str) -> bool:
    """
    Validate Ghanaian phone numbers.
    """

    if not phone:
        return False

    phone = str(phone).strip()

    pattern = r"^(\+233\d{9}|233\d{9}|0\d{9})$"

    return bool(re.match(pattern, phone))