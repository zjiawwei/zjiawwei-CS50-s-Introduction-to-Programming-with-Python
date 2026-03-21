from datetime import date
import inflect
import sys

class Time:
    def __init__(self,birth_date):
        self.birth_date = birth_date
        self.inflect_engine = inflect.engine()

    def calculate_minutes(self):
        today = date.today()

        if self.birth_date > today:
            raise ValueError("Invalid date")
        days_old = (today - self.birth_date).days
        minutes = days_old * 24 * 60
        return minutes
    
    def format_minutes(self,minutes):
        words = self.inflect_engine.number_to_words(minutes,andword="")
        return f"{words.capitalize()} minutes"
    
def get_time_from_input():
    birth_str = input("Date of Birth:")
    try:
        birth_date = date.fromisoformat(birth_str)
    except ValueError:
        sys.exit("Invalid date")
    return Time(birth_date)
    
def main():
    try:
        time_obj = get_time_from_input()
        minutes = time_obj.calculate_minutes()
        result = time_obj.format_minutes(minutes)
        print(result)
    except ValueError as e:
        sys.exit(str(e))

if __name__ == "__main__":
    main()