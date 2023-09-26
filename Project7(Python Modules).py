import math
import json
import datetime

# Use the math module for Square root operation
result = math.sqrt(64)
print("The square root of 64 is: ", result)

# Use the datetime function to print the date
current_date = datetime.datetime.now()
print(current_date)

# Use son module to convert  python dict into json
my_dict = {
    "name": "faith",
    "language": "python",
    "city": "nairobi"
}

json_data = json.dumps(my_dict)
print(json_data)



