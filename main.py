import random
from typing import Counter 

def random_day():
    a = random.randrange(1, 365)
    return int(a)

def what_month(day):
    days = [31,31,31,31,31,31,30,30,30,30,30,29]
    count = 0
    for i in days:
        day -= i
        if day <= 0 :
            return count
        else:
            count += 1

    

def what_month_word(month):
    months = ['farvardin' , 'ordibehesht' , 'khordad' , 'tir' , 'mordad' , 'shahrivar' , 'mehr' , 'aban' , 'azar' , 'day' , 'bahman' , 'esfand']
    return months[month]

def question_maker(month):
    months = ['farvardin' , 'ordibehesht' , 'khordad' , 'tir' , 'mordad' , 'shahrivar' , 'mehr' , 'aban' , 'azar' , 'day' , 'bahman' , 'esfand']
    final = []
    final = random.choices(months, k=4)
    if not month in final:
        final[random.randrange(0, len(final))] = month
    return final



test = random_day()
print(test)
print(question_maker(what_month_word(what_month(test))))
