import re

phone_number = ["    +38(050)123-32-34",
                "     0503451234",
                "(050)8889900",
                "38050-111-22-22",
                "38050 111 22 11   "]


def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    pattern = r"[^\d+]"
    replacement = ""
    phone_number = re.sub(pattern, replacement, phone_number)

    if re.search(r"^\+380", phone_number):
        return phone_number
    if re.search(r"^380", phone_number):
        return "+" + phone_number
    return "+38" + phone_number


sanitized_numbers = [normalize_phone(num) for num in phone_number]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)