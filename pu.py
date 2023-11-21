from datetime import datetime, timedelta
from operator import itemgetter

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

USERS = [
    {"name": "Bill", "birthday": datetime(year=2023, month=11, day=24).date()},
    {"name": "Andrew", "birthday": datetime(year=2023, month=11, day=23).date()},
    {"name": "Jill", "birthday": datetime(year=2023, month=11, day=26).date()},
    {"name": "Till", "birthday": datetime(year=2023, month=11, day=27).date()},
    {"name": "Jan", "birthday": datetime(year=2023, month=11, day=28).date()},
]

def close_birthday_users(users, start, end):
    return [user for user in users if start <= user['birthday'] <= end]

def get_birthdays_per_week(users):
    now = datetime.today().date()
    current_week_day = now.weekday()

    if current_week_day == 0:
        start_date = now - timedelta(days=1)
    else:
        start_date = now - timedelta(days=current_week_day)

    end_date = start_date + timedelta(days=4)
    
    birthday_users = close_birthday_users(users, start=start_date, end=end_date)

    if not birthday_users:
        print("No colleagues with birthdays this week.")
        return

    birthday_users.sort(key=itemgetter('birthday'))

    for user in birthday_users:
        user_birthday = user['birthday'].weekday()
        user_happy_day = WEEKDAYS[user_birthday]
        print(f"{user['name']} - {user_happy_day}")

get_birthdays_per_week(USERS)
