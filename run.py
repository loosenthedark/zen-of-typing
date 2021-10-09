# -*- coding: utf-8 -*-
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from __future__ import print_function, unicode_literals

from pprint import pprint

import regex

from prompt_toolkit.validation import Validator, ValidationError

from PyInquirer import prompt


# class PhoneNumberValidator(Validator):
#     def validate(self, document):
#         ok = regex.match(r"^\d{10}$", document.text)
#         if not ok:
#             raise ValidationError(
#                 message='Please enter a valid phone number',
#                 cursor_position=len(document.text))  # Move cursor to end


class InputValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


print('Hi, welcome to Python Pizza')

questions = [
    {
        'type': 'list',
        'name': 'text',
        'message': 'Choose a text:',
        'choices': ['dry', 'jokes', 'oop', 'python', 'sunscreen', 'zen'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'text',
        'message': 'How many lines do you want?',
        'choices': ['1', '3', '5', 'The whole thing!'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'input',
        'name': 'comments',
        'message': 'Any comments on your purchase experience?',
        'default': 'Nope, all good!'
    },
    {
        'type': 'list',
        'name': 'prize',
        'message': 'For leaving a comment, you get a freebie',
        'choices': ['cake', 'fries'],
        'when': lambda answers: answers['comments'] != 'Nope, all good!'
    }
]

# def choose_text(self):
#     pass

if __name__ == '__main__':
    answers = prompt(questions)
    print('Order receipt:')
    pprint(answers)  # use the answers as input for your app
