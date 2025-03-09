from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()  # Текущая дата
    upcoming_birthdays = []  # Список предстоящих дней рождения

    for user in users:
        # Преобразуем дату рождения в объект datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Если день рождения уже прошел в этом году, устанавливаем дату на следующий год
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        else:
            birthday = birthday.replace(year=today.year)

        # Проверяем, попадает ли день рождения в диапазон 7 дней с сегодняшнего дня
        if today <= birthday <= today + timedelta(days=7):
            # Если день рождения выпадает на выходные (суббота или воскресенье), переносим на понедельник
            if birthday.weekday() == 5:  # Суббота
                birthday += timedelta(days=2)  # Перенос на понедельник
            elif birthday.weekday() == 6:  # Воскресенье
                birthday += timedelta(days=1)  # Перенос на понедельник

            # Добавляем в список словарь с именем пользователя и датой привітання
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Пример пользователей
users = [
    {"name": "John Doe", "birthday": "1985.03.12"},
    {"name": "Jane Smith", "birthday": "1990.03.15"},
    {"name": "Bill Gates", "birthday": "1955.03.19"}
]

# Получаем список предстоящих дней рождений
upcoming_birthdays = get_upcoming_birthdays(users)

# Выводим результат
print("Список привітань на цьому тижні:", upcoming_birthdays)