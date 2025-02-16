from datetime import datetime, timedelta

current_date = datetime.now()
subtract_five_days = current_date - timedelta(days=5)
print("Current date:", current_date)
print("Date five days ago:", subtract_five_days)