from datetime import datetime

def get_days_from_today(date):
    try:
        income_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        diff_date = today - income_date
        return diff_date.days
    except ValueError:
        return "Невірний формат дати. Використовуйте формат 'YYYY-MM-DD'."

user_date = input("Введіть дату у форматі YYYY-MM-DD: ")
result = get_days_from_today(user_date)

print(f"Різниця в днях: {result}")