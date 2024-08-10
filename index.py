import datetime

def get_user_birthday():
    day = int(input("Введите день рождения (1-31): "))
    month = int(input("Введите месяц рождения (1-12): "))
    year = int(input("Введите год рождения (например, 1990): "))
    return datetime.date(year, month, day)

def determine_age(birthday):
    today = datetime.date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

def display_date_as_stars(birthday):
    day_str = f"{birthday.day:02}"
    month_str = f"{birthday.month:02}"
    year_str = f"{birthday.year:04}"
    
    date_as_stars = f"{day_str} {month_str} {year_str}"
    
    star_patterns = {
        '0': [
            " ** ",
            "*  *",
            "*  *",
            "*  *",
            " ** "
        ],
        '1': [
            "   *",
            "   *",
            "   *",
            "   *",
            "   *"
        ],
        '2': [
            " ** ",
            "  * ",
            " ** ",
            "*   ",
            " ** "
        ],
        '3': [
            " ** ",
            "  * ",
            " ** ",
            "  * ",
            " ** "
        ],
        '4': [
            "*  *",
            "*  *",
            " ** ",
            "   *",
            "   *"
        ],
        '5': [
            " ** ",
            "*   ",
            " ** ",
            "  * ",
            " ** "
        ],
        '6': [
            " ** ",
            "*   ",
            " ** ",
            "*  *",
            " ** "
        ],
        '7': [
            " ** ",
            "  * ",
            "  * ",
            "  * ",
            "  * "
        ],
        '8': [
            " ** ",
            "*  *",
            " ** ",
            "*  *",
            " ** "
        ],
        '9': [
            " ** ",
            "*  *",
            " ** ",
            "  * ",
            " ** "
        ]
    }

    for row in range(5):
        line = ""
        for char in date_as_stars:
            if char == " ":
                line += "     " 
            else:
                line += star_patterns[char][row] + "  "
        print(line)

def main():
    birthday = get_user_birthday()
    age = determine_age(birthday)
    day_of_week = birthday.strftime("%A")

    print(f"\nВаш день рождения: {birthday}")
    print(f"День недели: {day_of_week}")
    print(f"Сейчас вам {age} лет.")

    print("\nВаша дата рождения в формате дд мм гггг:")
    display_date_as_stars(birthday)

if __name__ == "__main__":
    main()
