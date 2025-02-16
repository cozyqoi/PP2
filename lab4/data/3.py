from datetime import datetime, timedelta

now = datetime.now()
new_now = now.replace(microsecond=0)
print("Time without microsecond = ", new_now)