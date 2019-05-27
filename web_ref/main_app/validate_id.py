"""
  #This code is a transtalation of a JavaScript code which can be found here http://jsfiddle.net/chridam/VSKNx/
"""
from datetime import datetime
from django.shortcuts import redirect


def validate(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d')
    except ValueError:
        return False
    return True 


def check_gender(id_number):
    gender_code = id_number[6:10]
    male = 'Male'
    female = 'Female'
    gender = None

    if int(gender_code) < 5000:
        gender = female
    else:
        gender = male
    return gender

def sa_citizen(id_number):
    citizen_digit = id_number[10:11]
    sa_citizen = False

    if int(citizen_digit) == 0:
        sa_citizen = True
    else:
        sa_citizen = False
    return sa_citizen

def check_digits(id_number):
    tempTotal = 0
    checkSum = 0
    multiplier = 1
    valid = True

    for i in range(len(id_number)):
        tempTotal = int(id_number[i]) * multiplier

        if tempTotal > 9:
            st = str(tempTotal)
            x = st[0]
            y = st[1]
            tempTotal = int(x) + int(y)

        checkSum = checkSum + tempTotal
        if multiplier % 2 == 0:
            multiplier = 1
        else:
            multiplier = 2

    if checkSum % 10 != 0:
        valid = False

    return valid




def valid_id(id_number):
    correct = True
    error_thrown = 'All good!'

    id_number = str(id_number)
    
    if len(id_number) != 13 or id_number.isdigit() == False:
        correct = False
        error_thrown = 'Your ID number should be a number of 13 digits'
        date_of_birth = ''
    else:

        year = id_number[:2]
        month = id_number[2:4]
        day = id_number[4:6]

        n = datetime.now()
        t = n.timetuple()
        y, m, d, h, min, sec, wd, yd, i = t

        current_year = y % 100
        prefix = '19'

        if int(year) < current_year:
            prefix = '20'
        year_of_birth = str(prefix) + str(year)
        date_of_birth = year_of_birth + '-' + str(month) + '-' + str(day)
        # do = str(month) + '/' + str(day) + '/' + year_of_birth

        if validate(date_of_birth) == False:
            correct = False
            error_thrown = 'Your ID number is incorrect'

        if check_digits(id_number) == False:
            correct = False
            error_thrown = 'Your ID number is incorrect'

        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        # return print(Gender(id_number))
    return correct, error_thrown, date_of_birth

    