# -*- coding: utf-8 -*-

# Write your code to expect a terminal of 80 characters wide and 24 rows high

from __future__ import print_function, unicode_literals

import textwrap

import random

import time

import pyjokes

from pprint import pprint

from prompt_toolkit.validation import Validator, ValidationError

from PyInquirer import prompt

from examples import custom_style_2

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

texts = {
    "dry": "Don't Repeat Yourself (DRY)",
    "oop": "Object-Oriented Programming (OOP)",
    "python": "The History of Python: Version 3",
    "sunscreen": "Everybody’s Free (To Wear Sunscreen)",
    "zen": "The Zen of Python",
    "jokes": 'pyjokes: "programmer jokes as a service"'
}

colours = {
    'CEND': '\33[0m',
    'CBOLD': '\33[1m',
    'CITALIC': '\33[3m',
    'CURL': '\33[4m',
    'CBLINK': '\33[5m',
    'CBLINK2': '\33[6m',
    'CSELECTED': '\33[7m',
    'CURL2': '\33[21m',
    'CNORMAL': '\33[22m',
    'CURLSTOP': '\33[24m',
    'CBLINKSTOP': '\33[25m',
    'CBLACK': '\33[30m',
    'CRED': '\33[31m',
    'CGREEN': '\33[32m',
    'CYELLOW': '\33[33m',
    'CBLUE': '\33[34m',
    'CVIOLET': '\33[35m',
    'CVIOLETBLINK': '\33[35;5m',
    'CBEIGE': '\33[36m',
    'CWHITE': '\33[37m',
    'CBLACKBG': '\33[40m',
    'CREDBG': '\33[41m',
    'CGREENBG': '\33[42m',
    'CYELLOWBG': '\33[43m',
    'CBLUEBG': '\33[44m',
    'CVIOLETBG': '\33[45m',
    'CBEIGEBG': '\33[46m',
    'CWHITEBG': '\33[47m',
    'CGREY': '\33[90m',
    'CRED2': '\33[91m',
    'CGREEN2': '\33[92m',
    'CYELLOW2': '\33[93m',
    'CBLUE2': '\33[94m',
    'CVIOLET2': '\33[95m',
    'CBEIGE2': '\33[96m',
    'CWHITE2': '\33[97m',
    'CGREYBG': '\33[100m',
    'CREDBG2': '\33[101m',
    'CGREENBG2': '\33[102m',
    'CYELLOWBG2': '\33[103m',
    'CBLUEBG2': '\33[104m',
    'CVIOLETBG2': '\33[105m',
    'CBEIGEBG2': '\33[106m',
    'CWHITEBG2': '\33[107m'
}

ascii_art = open('images/ascii-art.txt').read()
print(
    f"{colours['CBOLD']}{ascii_art}{colours['CEND']}")

print('')
print(
    f"{colours['CBOLD']}{colours['CBLUE']}Welcome to {colours['CBLINK']}The Zen of Typing!{colours['CBLINKSTOP']}{colours['CEND']}")
print('')
print(
    f"{colours['CYELLOW']}The only place you can improve your typing speed and{colours['CEND']}")
print(
    f"{colours['CYELLOW']}brush up on some programming principles at the same time...{colours['CEND']}")
print('')

questions = [
    {
        'type': 'confirm',
        'name': 'practice',
        'message': 'Would you like some (more) practice before you begin?',
        'default': False
    },
    {
        'type': 'list',
        'name': 'text',
        'message': "Okay, I hope you're ready! Please choose a text:",
        'choices': ['DRY', 'Jokes', 'OOP', 'Python', 'Sunscreen', 'Zen', "Can't decide. Choose one for me!"],
        'when': lambda answers: not answers['practice'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'lines',
        'message': 'How many lines would you like?',
        'choices': ['1', '3', '5', 'Give me the whole thing!'],
        'when': lambda answers: not answers['practice'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'confirm',
        'name': 'secret_password',
        'message': 'Do you know the secret password?',
        'when': lambda answers: not answers['practice'],
        'default': False
    },
    {
        'type': 'input',
        'name': 'enter_password',
        'message': 'Please enter the secret password:',
        'when': lambda answers: not answers['practice'] and answers['secret_password']
    },
    {
        'type': 'list',
        'name': 'mode',
        'message': 'Please select a game mode:',
        'choices': ['normal mode', 'BEAST MODE'],
        'when': lambda answers: not answers['practice'] and answers['secret_password'] and answers['enter_password'] == 'PEP8'
    }
]

question_restart = [{
        'type': 'confirm',
        'name': 'restart_game',
        'message': 'Would you like another go?',
        'default': False
    }]

PW_COUNT = 0

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

def get_lines_for_typing(text, lines, mode):
    '''
    Customise length of typing text content based on user's preference:
     return either 1, 3 or 5 lines; or else the entire body of stored text.
    '''
    try:
        lines_for_typing = text.split('\n')
        reversed_lines = [line[::-1] for line in lines_for_typing]
        if lines == 'all':
            if mode:
                return reversed_lines
            else:
                return lines_for_typing
        if mode:
            return reversed_lines[:int(lines)]
        else:
            return lines_for_typing[:int(lines)]
    except Exception as ex:
        print(ex)

class TypingText:

    def __init__(self):
        self.practiced = False
        self.reset = True
        self.beast = False
        self.started = self.finished = self.running = False
        self.text_typed = self.text_to_be_typed = ''
        self.start_time = self.total_time = self.typing_accuracy = self.wpm = 0
        self.score = f'Time: {self.total_time} | Accuracy: {self.typing_accuracy}% | WordsPerMinute: {self.wpm}'

    def calculate_results(self, text_a, text_b):
        if not self.finished:
            # Work out time spent typing...
            self.total_time = time.time() - self.start_time
            # Work out typing accuracy...
            score = 0
            for i, char in enumerate(text_a):
                try:
                    # print(char)
                    if text_b[i] == char:
                        score += 1
                except:
                    pass
            self.typing_accuracy = score / len(text_b) * 100
            # Work out WPM...
            self.wpm = len(text_b) * 60 / (5 * self.total_time)
            print('')
            print(f"{colours['CBOLD']}{colours['CGREEN']}Not bad!{colours['CEND']}")
            print(f"{colours['CBOLD']}{colours['CGREEN']}That took you {str(round(self.total_time, 2))} seconds to type, and you were {str(round(self.typing_accuracy))}% accurate.{colours['CEND']}")
            print(f"{colours['CBOLD']}{colours['CGREEN']}Your average typing speed was {str(round(self.wpm))} words per minute.{colours['CEND']}")
            if self.wpm > 10:
                global PW_COUNT
                PW_COUNT = PW_COUNT + 1
                print('')
                print(f"{colours['CBOLD']}{colours['CBLINK']}{colours['CYELLOW']}The first character in the secret password is: P{colours['CEND']}" if PW_COUNT == 1 else f"{colours['CBOLD']}{colours['CBLINK']}{colours['CYELLOW']}The second character in the secret password is: E{colours['CEND']}" if PW_COUNT == 2 else f"{colours['CBOLD']}{colours['CBLINK']}{colours['CYELLOW']}The third character in the secret password is: P{colours['CEND']}" if PW_COUNT == 3 else f"{colours['CBOLD']}{colours['CBLINK']}{colours['CYELLOW']}The fourth and {colours['CURL']}final{colours['CURLSTOP']} character in the secret password is: 8{colours['CEND']}" if PW_COUNT == 4 else f"{colours['CBOLD']}{colours['CBLINK']}{colours['CYELLOW']}You should now know all four characters of the secret password...{colours['CEND']}" if PW_COUNT >= 5 else "")
                print(f"{colours['CBOLD']}{colours['CBLINK']}{colours['CYELLOW']}Be sure to make a note of it somewhere!{colours['CEND']}" if 1 <= PW_COUNT <= 4 else f"{colours['CBOLD']}{colours['CBLINK']}{colours['CYELLOW']}Don't forget to use it in order to unlock BEAST MODE!{colours['CEND']}" if PW_COUNT >= 5 else "")
            print('')
            answer = prompt(question_restart, style=custom_style_2)
            if answer['restart_game']:
                print('')
                self.activate()

    def activate(self):
        self.game_restart()
        self.running = True
        answers = prompt(questions, style=custom_style_2)
        if answers['practice']:
            answers['secret_password'] = False
            chosen_text = None
            num_of_lines = 'all'
            print('')
            print(f"{colours['CBOLD']}{colours['CBLUE']}You can warm up by typing the following. Hit enter when you're done!{colours['CEND']}")
        else:
            chosen_text = random.choice(['dry', 'jokes', 'oop', 'python', 'sunscreen', 'zen']) if answers['text'] == "can't decide. choose one for me!" else answers['text']
            num_of_lines = 'all' if answers['lines'] == 'give me the whole thing!' else answers['lines']
            print('')
            if answers['secret_password'] and answers['enter_password'] != 'PEP8':
                (f"{colours['CBOLD']}{colours['CGREEN']}Not bad!{colours['CEND']}")
                print(f"{colours['CBOLD']}{colours['CRED']}Sorry, that password is incorrect.{colours['CEND']}")
                print('')
            if answers['text'] != "can't decide. choose one for me!":
                print(f"{colours['CBOLD']}{colours['CBLUE']}You have chosen to type:{colours['CEND']}")
            print(f"{colours['CBOLD']}{colours['CBLUE']}{colours['CURL']}{num_of_lines} line(s){colours['CURLSTOP']} from {colours['CURL']}{texts[chosen_text]}{colours['CURLSTOP']}{colours['CEND']}")
            if answers['text'] == "can't decide. choose one for me!":
                print(f"{colours['CBOLD']}{colours['CBLUE']}have been chosen for you:{colours['CEND']}")
        print('')
        # test exception handling functionality within choose_text fn
        # print(choose_text(text=None))
        text_for_typing = choose_text(chosen_text)
        # test exception handling functionality within get_lines_for_typing fn
        # print(get_lines_for_typing(chosen_text, 'abc'))
        self.beast = True if answers['secret_password'] and not answers['practice'] and answers['mode'] == 'BEAST MODE' else False
        text_for_typing = get_lines_for_typing(text_for_typing, num_of_lines, self.beast)
        stringified_text_for_typing = '\n'.join(text_for_typing)
        # stringified_text_for_typing = stringified_text_for_typing[::-1]
        # print(len(stringified_text_for_typing))
        for line in text_for_typing:
            print(f"{colours['CITALIC']}{textwrap.fill(line, width=80)}{colours['CEND']}")
        if answers['practice']:
            print('')
            input()
            print('')
            answers['practice'] = 'practiced'
            self.activate()
        while self.running:
            print('')
            print(f"{colours['CBOLD']}{colours['CBLINK']}{colours['CYELLOW']}Off you go!!!{colours['CEND']}")
            print('')
            self.started = True
            self.start_time = time.time()
            if self.started and not self.finished:
                if num_of_lines != 'all':
                    for i in range(int(num_of_lines)):
                        self.text_typed += (input() + '\n')
                else:
                    for i in range(13):
                        self.text_typed += (input() + '\n')
            # print(len(self.text_typed[:-1]))
            self.calculate_results(stringified_text_for_typing, self.text_typed[:-1])
            self.finished = True
            self.running = False
            self.practiced = True

    def game_restart(self):
        self.reset = False
        self.finished = False
        self.text_typed = self.text_to_be_typed = ''
        self.start_time = self.total_time = self.wpm = 0

if __name__ == '__main__':
    TypingText().activate()
