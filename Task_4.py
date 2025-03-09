from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()  
    upcoming_birthdays = []  

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        else:
            birthday = birthday.replace(year=today.year)

        if today <= birthday <= today + timedelta(days=7):
            
            if birthday.weekday() == 5:  
                birthday += timedelta(days=2) 
            elif birthday.weekday() == 6: 
                birthday += timedelta(days=1)  

           
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.03.12"},
    {"name": "Jane Smith", "birthday": "1990.03.15"},
    {"name": "Bill Gates", "birthday": "1955.03.19"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)