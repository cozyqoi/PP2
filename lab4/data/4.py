from datetime import datetime, timedelta

date1 = datetime.now()
date2 = date1 + timedelta(days = 1)
difference = (date2 - date1).total_seconds()
print("Difference in seconds:", difference)