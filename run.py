"""This is the Zen of Typing main app script"""

# Standard library imports
from __future__ import print_function, unicode_literals
import random
import sys
import textwrap
import time

# Third-party imports
import pyjokes
from PyInquirer import prompt
from examples import custom_style_2

# dictionary of target texts
texts = {
    "dry": "Don't Repeat Yourself (DRY)",
    "oop": "Object-Oriented Programming (OOP)",
    "python": "The History of Python: Version 3",
    "sunscreen": "Everybody’s Free (To Wear Sunscreen)",
    "zen": "The Zen of Python",
    "jokes": 'pyjokes: "programmer jokes as a service"'
}

# code block adapted from
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal/39452138#39452138
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

# Python logo ASCII art file copied from https://github.com/honno/ascii-art
ascii_art = open('images/ascii-art.txt').read()
print(
    f"{colours['CBOLD']}{ascii_art}{colours['CEND']}")

print('')
print(
    f"{colours['CBOLD']}{colours['CBLUE']}Welcome to "
    f"{colours['CBLINK']}The Zen of Typing!"
    f"{colours['CBLINKSTOP']}{colours['CEND']}"
)
print('')
print(
    f"{colours['CBOLD']}{colours['CYELLOW']}The only place you can "
    f"improve your typing speed and{colours['CEND']}")
print(
    f"{colours['CBOLD']}{colours['CYELLOW']}brush up on some programming "
    f"principles at the same time...{colours['CEND']}")
print('')

# code block adapted from
# https://github.com/CITGuru/PyInquirer/tree/master/examples
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
        'choices': ['DRY', 'Jokes', 'OOP', 'Python', 'Sunscreen', 'Zen',
                    "Can't decide. Choose one for me!"],
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
        'when': lambda answers: not answers['practice'] and
                answers['secret_password']
    },
    {
        'type': 'list',
        'name': 'mode',
        'message': 'Please select a game mode:',
        'choices': ['normal mode', 'BEAST MODE'],
        'when': lambda answers: (
                not answers['practice'] and answers['secret_password'] and
                answers['enter_password'] == 'PEP8'
                )
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
    Retrieve typing text content based on selection made by user from
    multiple-choice menu options. Since files are being loaded from
    disc/API request, which has the potential for problems that might
    trigger an exception, code here should be wrapped in a try/except block
    '''
    try:  # load content from file/API
        if text == 'jokes':
            jokes = pyjokes.get_jokes()
            random.shuffle(jokes)
            jokes = jokes[:10]
            file = '\n'.join(jokes)
        else:
            file = open(f'texts/{text}.txt').read()
    except Exception:
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
    """Class for enclosing all methods required to run the application"""

    def __init__(self):
        self.beast = self.started = self.finished = self.running = False
        self.text_typed = self.text_to_be_typed = ''
        self.start_time = self.total_time = self.typing_accuracy = self.wpm = 0

    def calculate_results(self, text_a, text_b):
        '''
        Monitor user performance on each typing task and provide feedback
        upon completion. Results breakdown includes total time taken,
        accuracy level and words per minute (wpm). A global variable is also
        used as a flag to incrementally reveal a secret password based on
        steady increases in the user's typing speed. Farewell message also
        communicated to the user should they opt to discontinue the game.
        '''
        if not self.finished:
            # Work out time spent typing...
            self.total_time = time.time() - self.start_time
            # Work out typing accuracy...
            score = 0
            for i, char in enumerate(text_a):
                try:
                    if text_b[i] == char:
                        score += 1
                except:
                    pass
            self.typing_accuracy = score / len(text_b) * 100
            # Work out WPM...
            self.wpm = len(text_b) * 60 / (5 * self.total_time)
            print('')
            print(
                f"{colours['CBOLD']}{colours['CGREEN']}Not bad!"
                f"{colours['CEND']}"
                )
            print(
                f"{colours['CBOLD']}{colours['CGREEN']}That took you "
                f"{str(round(self.total_time, 2))} seconds to type, and you "
                f"were {str(round(self.typing_accuracy))}% accurate."
                f"{colours['CEND']}"
                )
            print(
                f"{colours['CBOLD']}{colours['CGREEN']}Your average typing"
                f" speed was {str(round(self.wpm))} words per minute."
                f"{colours['CEND']}"
                )
            global PW_COUNT
            if self.wpm >= 20 and PW_COUNT == 0:
                PW_COUNT = 1
                print('')
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}The first character in"
                    f" the secret password is: P{colours['CEND']}"
                    )
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}Be sure to make a"
                    f" note of it somewhere!{colours['CEND']}"
                    )
            elif self.wpm >= 30 and PW_COUNT == 1:
                PW_COUNT = 2
                print('')
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}The second character"
                    f" in the secret password is: E{colours['CEND']}"
                    )
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}Be sure to make a"
                    f" note of it somewhere!{colours['CEND']}"
                    )
            elif self.wpm >= 40 and PW_COUNT == 2:
                PW_COUNT = 3
                print('')
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}The third character "
                    f"in the secret password is: P{colours['CEND']}"
                    )
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}Be sure to make a"
                    f" note of it somewhere!{colours['CEND']}"
                    )
            elif self.wpm >= 50 and PW_COUNT == 3:
                PW_COUNT = 4
                print('')
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}The fourth and {colours['CURL']}"
                    f"final{colours['CURLSTOP']} character in the secret "
                    f"password is: 8{colours['CEND']}"
                    )
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}Be sure to make "
                    f"a note of it somewhere!{colours['CEND']}"
                    )
            elif PW_COUNT == 4:
                print('')
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}You should now have all four "
                    f"characters of the secret password...{colours['CEND']}"
                    )
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}Don't forget to use it in "
                    f"order to unlock BEAST MODE!{colours['CEND']}"
                    )
            else:
                print('')
                print(
                    f"{colours['CBOLD']}{colours['CBLINK']}"
                    f"{colours['CYELLOW']}Keep practicing to reveal the secret"
                    f" password and unlock BEAST MODE!{colours['CEND']}"
                    )
            print('')
            answer = prompt(question_restart, style=custom_style_2)
            if answer['restart_game']:
                print('')
                self.activate()
            print('')
            print(
                f"{colours['CBOLD']}{colours['CBLUE']}Thanks for playing"
                f" The Zen of Typing!{colours['CEND']}"
                )
            print('')
            print(
                f"{colours['CBOLD']}{colours['CYELLOW']}"
                f"See you again soon ;){colours['CEND']}"
                )
            print('')
            sys.exit()

    def activate(self):
        """
        Primary in-game method for triggering various helper functions to
        configure typing activity while looping through conditional logic
        (i.e. choices based on user input). User is first of all asked if
        they'd like to practice their typing before starting the game proper.
        Following on from this, they are asked to select both a target text
        and the number of lines they wish to type. They are also asked if they
        know the secret password (which can be entered to unlock 'Beast Mode').
        """
        self.game_restart()
        self.running = True
        answers = prompt(questions, style=custom_style_2)
        if answers['practice']:
            answers['secret_password'] = False
            chosen_text = None
            num_of_lines = 'all'
            print('')
            print(
                f"{colours['CBOLD']}{colours['CBLUE']}"
                f"You can warm up by typing the following. "
                f"Hit enter when you're done!{colours['CEND']}"
                )
        else:
            chosen_text = random.choice(
                ['dry', 'jokes', 'oop', 'python', 'sunscreen', 'zen']
                ) if (
                    answers['text'] == "can't decide. choose one for me!"
                    ) else answers['text']
            num_of_lines = 'all' if (
                answers['lines'] == 'give me the whole thing!'
                ) else answers['lines']
            print('')
            if (
                answers['secret_password'] and
                answers['enter_password'] != 'PEP8'
            ):
                print(
                    f"{colours['CBOLD']}{colours['CRED']}Sorry, that "
                    f"password is incorrect!{colours['CEND']}"
                    )
                print('')
            if answers['text'] != "can't decide. choose one for me!":
                print(
                    f"{colours['CBOLD']}{colours['CBLUE']}You have chosen "
                    f"to type:{colours['CEND']}"
                    )
            print(
                f"{colours['CBOLD']}{colours['CBLUE']}{colours['CURL']}"
                f"{num_of_lines} line(s){colours['CURLSTOP']} from "
                f"{colours['CURL']}{texts[chosen_text]}{colours['CURLSTOP']}"
                f"{colours['CEND']}"
                )
            if answers['text'] == "can't decide. choose one for me!":
                print(
                    f"{colours['CBOLD']}{colours['CBLUE']}have been "
                    f"chosen for you:{colours['CEND']}"
                    )
        print('')
        text_for_typing = choose_text(chosen_text)
        self.beast = True if (
            answers['secret_password'] and
            answers['enter_password'] == 'PEP8' and
            not answers['practice'] and answers['mode'] == 'BEAST MODE'
        ) else False
        text_for_typing = get_lines_for_typing(
            text_for_typing, num_of_lines, self.beast
            )
        stringified_text_for_typing = '\n'.join(text_for_typing)
        for line in text_for_typing:
            print(
                f"{colours['CITALIC']}{textwrap.fill(line, width=76)}"
                f"{colours['CEND']}"
                )
        if answers['practice']:
            print('')
            input()
            print('')
            self.activate()
        while self.running:
            print('')
            print(
                f"{colours['CBOLD']}{colours['CBLINK']}{colours['CYELLOW']}"
                f"Off you go!!!{colours['CEND']}"
                )
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
            self.calculate_results(
                stringified_text_for_typing, self.text_typed[:-1]
                )
            self.finished = True
            self.running = False

    def game_restart(self):
        """
        Method for resetting game state by returning main properties to
        original values.
        """
        self.finished = False
        self.text_typed = self.text_to_be_typed = ''
        self.start_time = self.total_time = self.wpm = 0

if __name__ == '__main__':
    # game activation method is immediately called
    # in order to launch the application
    TypingText().activate()
