#!/usr/bin/env python3

import argparse
import os
import sys
import spacy
import re
nlp = spacy.load('en_core_web_sm')

help_mutations = '''
    U : To uppercase,
    L : To lowercase,
    T : To title,
    C : Add curly brackets,
    P : Add parentheses,
    S : Add square brackets
'''

def lower(s):
    return s.lower()


def upper(s):
    return s.upper()


def title(s):
    return s.title()


def append_sides(s, l, r):
    return l + s + r


def curly_brackets(s):
    return append_sides(s, '{', '}')


def square_brackets(s):
    return append_sides(s, '[', ']')


def parentheses(s):
    return append_sides(s, '(', ')')


def mutate(references, pos, field, command):
    """Mutate certain POS to adjust their form"""

    references = references.splitlines()

    mutations = {
        'L' : lower,
        'U' : upper,
        'T' : title,
        'C' : curly_brackets,
        'S' : square_brackets,
        'P' : parentheses
    }

    result = []
    regex = field + r'\s*=\s*\{(.*?)\}'

    for i, line in enumerate(references):
        matches = re.finditer(regex, line)
        for m in matches:
            content = m.group(1)
            new_content = content
            doc = nlp(content)
            for token in doc:
                if token.pos_ == pos:
                    temp = token.text
                    for cmd in command:
                        temp = mutations[cmd](temp)

                    new_content = re.sub(token.text, temp, content)


            references[i] = re.sub(content, new_content, line)

    return '\n'.join(references)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--pos', help='Part of speech to mutate (e.g. NOUN)', default='NOUN')
    argparser.add_argument('--field', help='Field to mutate (e.g. title)', default='title')
    argparser.add_argument('-c', help='Command to mutate\n' + help_mutations, default='T')

    args = argparser.parse_args()

    references = sys.stdin.read()

    result = mutate(references, args.pos, args.field, args.c)

    print(result)
