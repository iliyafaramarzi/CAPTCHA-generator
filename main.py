import random
from sympy.solvers import solve
from sympy import Symbol

class date():

    def __init__(self) -> None:
        pass

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

class math():

    def __init__(self) -> None:
        pass

    def question_maker():
        operations = ['+', '-', '/', '*']
        return f'{random.randrange(0, 11)} {random.choice(operations)} {random.randrange(0, 11)}'
    
    def answer(question):
        x = Symbol('x')
        return solve(f'{question} - x', x)
    
    def options(answer):
        options = [answer]
        for i in range(3):
            options.append(math.answer(math.question_maker()))

        return options