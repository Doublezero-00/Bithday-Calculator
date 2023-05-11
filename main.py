import datetime

# function for validating user input
def validate(nic: str) -> bool:
    nic_length = len(nic)
    if nic_length != 12:
        return False
    else :
        nic_digit = nic.isdigit()
        return nic_digit

#Function for identify the born year
def get_born_year(nic: str) ->int:
    born_year = nic[0:4]
    return int(born_year)

#Function for calculate born date
def get_born_day(nic: str) -> datetime.date:
    born_day = int(nic[4:7])
    if born_day > 500:
        born_day = born_day - 500
    b_year = get_born_year(nic_number)
    jan_first = datetime.date(b_year,1,1)
    date = jan_first + datetime.timedelta(days=born_day-1)
    return date

#Get a user input
nic_number = input('\033[32m'"Enter your NIC number : ")

#Validating user input
nic_validate = validate(nic_number)
if not nic_validate :
    print('\033[31m'"Invalid NIC! please check and enter again")
    exit(0)

#Identify the born year
year = get_born_year(nic_number)

#Calculate born date
born_date = get_born_day(nic_number)

#Print the output
iso_format = born_date.isoformat()
print('\033[33m''Your birthday : ',iso_format)

day = born_date.strftime("%A")
print('\033[33m''Born day : ',day)
