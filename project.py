import json


class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        self.activities = []
        self.goals = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def set_goal(self, goal):
        self.goals.append(goal)

    @staticmethod
    def validate_user_data(username, email):
        # Перевірка унікальності email або username
        return True  # Поки що просто повертаємо True


class Activity:
    def __init__(self, activity_type, duration, distance, calories):
        self.activity_type = activity_type
        self.duration = duration
        self.distance = distance
        self.calories = calories

    @staticmethod
    def validate_activity(activity_type):
        allowed_activities = ["run", "walk", "exercise"]
        return activity_type.lower() in allowed_activities


class Goal:
    def __init__(self, goal_type, target):
        self.goal_type = goal_type
        self.target = target


class ProgressTracker:
    def __init__(self, user):
        self.user = user

    class ProgressTracker:
        def __init__(self, user):
            self.user = user

        def track_progress(self):
            total_duration = sum(activity.duration for activity in self.user.activities)
            total_distance = sum(activity.distance for activity in self.user.activities)
            total_calories = sum(activity.calories for activity in self.user.activities)

            print("Прогрес користувача:")
            print(f"Загальна тривалість активностей: {total_duration} хвилин")
            print(f"Загальна пройдена відстань: {total_distance} км")
            print(f"Загальна кількість спалених калорій: {total_calories}")

def save_user_data(users):
    with open("users.json", "w") as f:
        json.dump(users, f, default=lambda o: o.__dict__, indent=4)


def load_user_data():
    try:
        with open("users.json", "r") as f:
            users_data = json.load(f)
            users = [User(**user_data) for user_data in users_data]
            return users
    except FileNotFoundError:
        return []


def register_user(users):
    username = input("Введіть ім'я користувача: ")
    email = input("Введіть електронну пошту: ")
    age = int(input("Введіть вік: "))

    if User.validate_user_data(username, email):
        user = User(username, email, age)
        users.append(user)
        save_user_data(users)
        return user
    else:
        print("Дані користувача недійсні.")
        return None


def create_activity(user):
    print("Оберіть тип активності:")
    print("1. Біг")
    print("2. Прогулянка")
    print("3. Вправи")
    activity_type_choice = input("Введіть ваш вибір: ")

    if activity_type_choice == "1":
        activity_type = "run"
    elif activity_type_choice == "2":
        activity_type = "walk"
    elif activity_type_choice == "3":
        activity_type = "exercise"
    else:
        print("Недійсний вибір.")
        return

    duration = float(input("Введіть тривалість (у хвилинах): "))
    if activity_type != "exercise":
        distance = float(input("Введіть відстань (у кілометрах): "))
    else:
        distance = 0
    calories = float(input("Введіть кількість спалених калорій: "))

    if Activity.validate_activity(activity_type):
        activity = Activity(activity_type, duration, distance, calories)
        user.add_activity(activity)
        save_user_data(users)
    else:
        print("Недійсний тип активності.")


def set_goal(user):
    print("Оберіть тип цілі:")
    print("1. Щоденна кількість кроків")
    print("2. Кількість хвилин тренувань")
    print("3. Пройдена відстань")
    goal_type_choice = input("Введіть ваш вибір: ")

    if goal_type_choice == "1":
        goal_type = "Щоденна кількість кроків"
    elif goal_type_choice == "2":
        goal_type = "Кількість хвилин тренувань"
    elif goal_type_choice == "3":
        goal_type = "Пройдена відстань"
    else:
        print("Недійсний вибір.")
        return

    target = float(input("Введіть ціль: "))

    goal = Goal(goal_type, target)
    user.set_goal(goal)
    save_user_data(users)


def main_menu():
    print("1. Зареєструвати нового користувача")
    print("2. Додати активність")
    print("3. Встановити ціль")
    print("4. Відстежити прогрес")
    print("5. Вийти")


users = load_user_data()

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            user = register_user(users)
        elif choice == "2":
            if users:
                create_activity(user)
            else:
                print("Будь ласка, спочатку зареєструйтесь.")
        elif choice == "3":
            if users:
                set_goal(user)
            else:
                print("Будь ласка, спочатку зареєструйтесь.")
        elif choice == "4":
            if users:
                tracker = ProgressTracker(user)
                tracker.track_progress()
            else:
                print("Будь ласка, спочатку зареєструйтесь.")
        elif choice == "5":
            print("Вихід з програми...")
            break
        else:
            print("Недійсний вибір. Будь ласка, спробуйте знову.")
