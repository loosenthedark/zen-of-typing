# -*- coding: utf-8 -*-

# Write your code to expect a terminal of 80 characters wide and 24 rows high

from __future__ import print_function, unicode_literals

import textwrap

import random

import pyjokes

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


print('')
print('Welcome to The Zen of Typing!')
print('')
print('The only place you can improve your typing speed and')
print('brush up on some programming principles at the same time...')
print('')

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
    '''
    Retrieve typing text content based on selection made by user from multiple-choice menu options.
    Since files are being loaded from disc/API request, which has the potential for problems
     that might trigger an exception, code here should be wrapped in a try/except block
    '''
    try: # load content from file/API
        if text == 'jokes':
            jokes = pyjokes.get_jokes()
            random.shuffle(jokes)
            jokes = jokes[:10]
            file = '\n'.join(jokes)
        else:
            file = open(f'texts/{text}.txt').read()
    except Exception as ex:
        # use a default/fallback quote in case there's
        # a problem with loading content from file/API
        file = ('The first 90 percent of the code accounts for'
        ' the first 90 percent of the development time. '
        'The remaining 10 percent of the code accounts for'
        ' the other 90 percent of the development time.')

    return file

def get_lines_for_typing(text, lines):
    '''
    Customise length of typing text content based on user's preference:
     return either 1, 3 or 5 lines; or else the entire body of stored text.
    '''
    try:
        lines_for_typing = text.split('\n')
        if lines == 'give me the whole thing!':
            return lines_for_typing
        return lines_for_typing[:int(lines)]
    except Exception as ex:
        print(ex)

class TypingText:

    def __init__(self):
        self.reset = True
        self.started = self.finished = self.running = False
        self.text_typed = self.text_to_be_typed = ''
        self.start_time = self.total_time = self.typing_accuracy = self.wpm = 0
        self.score = f'Time: {self.total_time} | Accuracy: {self.typing_accuracy}% | WordsPerMinute: {self.wpm}'

    def activate(self):
        answers = prompt(questions)
        chosen_text = answers['text']
        num_of_lines = answers['lines']
        print('')
        print('You have chosen to type:')
        print('')
        print(f"{num_of_lines} lines from {chosen_text}...")
        print('')
        # test exception handling functionality within choose_text fn
        # print(choose_text(text=None))
        text_for_typing = choose_text(chosen_text)
        # test exception handling functionality within get_lines_for_typing fn
        # print(get_lines_for_typing(chosen_text, 'abc'))
        text_for_typing = get_lines_for_typing(text_for_typing, num_of_lines)
        stringified_text_for_typing = '\n'.join(text_for_typing)
        print(len(stringified_text_for_typing))
        # for char in stringified_text_for_typing:
        #     print(char)
        for line in text_for_typing:
            print(textwrap.fill(line, width=80))
        # self.reset_game()
        self.running = True
        while self.running:
            print('Off you go!')
            for i in range(int(num_of_lines)):
                self.text_typed += (input() + ' ')
            print(self.text_typed[:-1])
            print(len(self.text_typed[:-1]))

if __name__ == '__main__':
    TypingText().activate()
