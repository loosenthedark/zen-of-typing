# -*- coding: utf-8 -*-
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from __future__ import print_function, unicode_literals

import sys

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


print('Welcome to The Zen of Typing - the only place you can improve your typing speed and brush up on some programming essentials at the same time!')

questions = [
    {
        'type': 'list',
        'name': 'text',
        'message': 'Please choose a text:',
        'choices': ['dry', 'jokes', 'oop', 'python', 'sunscreen', 'zen'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'lines',
        'message': 'How many lines would you like?',
        'choices': ['1', '3', '5', 'Give me the whole thing!'],
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

def choose_text(text):
    file = open(f'texts/{text}.txt').read()
    return file

def get_lines_for_typing(text, lines):
    lines_for_typing = text.split('\n')
    if lines == 'give me the whole thing!':
        return '\n'.join(lines_for_typing)
    print(lines)
    return '\n'.join(lines_for_typing[:int(lines)])

if __name__ == '__main__':
    answers = prompt(questions)
    chosen_text = answers['text']
    num_of_lines = answers['lines']
    print('You have chosen to type:')
    print(f"{num_of_lines} lines from {chosen_text}...")
    TEXT_FOR_TYPING = choose_text(chosen_text)
    TEXT_FOR_TYPING = get_lines_for_typing(TEXT_FOR_TYPING, num_of_lines)
    print(TEXT_FOR_TYPING)
