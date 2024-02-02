from datetime import datetime
d_o_b = input('enter year of birth(yyyy): ')
try:
          dob_date = datetime.strptime(d_o_b, "%Y")
except ValueError:
          print("Enter only the year of birth (yyyy)")

name = input('enter your name: ')
current_year = datetime.now().year
