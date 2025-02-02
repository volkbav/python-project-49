# import function find randint and gcd
from math import gcd
from random import randint

QUESTION = 'Find the greatest common divisor of given numbers.'


def logic_game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    correct_answer = str(gcd(number1, number2))
    print(f'Question: {number1} {number2}')
    answer = input('Your answer: ')
    return (answer, correct_answer)        

