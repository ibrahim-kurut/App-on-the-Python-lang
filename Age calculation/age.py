import datetime



name = input("enter your name : ")
birht_day = input("enter your birthday : ")
current_year = datetime.datetime.now()
age = current_year.year - int(birht_day)

print(f"hello {name} your age {age}")
