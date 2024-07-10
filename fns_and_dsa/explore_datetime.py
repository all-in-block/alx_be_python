from datetime import datetime, timedelta
def display_current_datetime():
   current_date = datetime.now()
   formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
   print(f"Current date and time: {formatted_date}")

def calculate_future_date(day_number):
   days_to_add = timedelta(days=day_number)
   current_time = datetime.now()
   future_date = current_time + days_to_add
   formatted_future_date = future_date.strftime("%Y-%m-%d")
   print(f"Future date: {formatted_future_date}")

def main():
   display_current_datetime()
   day_number = int(input("Enter the number of days to add to the current date: "))
   calculate_future_date(day_number)
main()