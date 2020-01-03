"""
A grammar defining illegal tokens and groups to break them down.
"""
import re

def compile_rule(rule):
    """Return a case insensitive rule matching and entire string."""
    return re.compile(BOS + rule + EOS, re.IGNORECASE)

def create_group(expression):
    """ Returns regular expression groups."""
    return '(' + expression + ')'

# Basic characters and sets.
ALPHA = '[A-Z]+'
DIGITS = '[0-9]'
BOS = '^'
EOS = '$'
PLUS = '+'
STAR = "*"
PERIOD = r'\.'
INITIAL_PUNCTUATION = '[\'"]'
FINAL_PUNCTUATION = '[\',!?":.]'
CURRENCY_SYMBOL = '[$£¥€]'
QUESTION_MARK = '?'

# Regular expression groups.
ALPHA_GROUP = create_group(ALPHA)
INITIAL_PUNCTUATION_GROUP = create_group(INITIAL_PUNCTUATION)
FINAL_PUNCTUATION_GROUP = create_group(FINAL_PUNCTUATION + PLUS)
FINAL_PUNCTUATION_STAR_GROUP = create_group(FINAL_PUNCTUATION + STAR)
CURRENCY_SYMBOL_GROUP = create_group(CURRENCY_SYMBOL)
CURRENCY_GROUP = create_group(DIGITS + PLUS + PERIOD + QUESTION_MARK + DIGITS + '{,2}')
ALPHA_PUNCTUATION_GROUP = create_group(ALPHA + FINAL_PUNCTUATION + STAR)

# Grammar rules.
INITIAL_PUNCTUATION_TOKEN = INITIAL_PUNCTUATION_GROUP + ALPHA_PUNCTUATION_GROUP
FINAL_PUNCTUATION_TOKEN = ALPHA_GROUP + FINAL_PUNCTUATION_GROUP
PUNCTUATION_TOKEN = create_group(FINAL_PUNCTUATION) + FINAL_PUNCTUATION_GROUP
CURRENCY_TOKEN = CURRENCY_SYMBOL_GROUP + CURRENCY_GROUP + FINAL_PUNCTUATION_STAR_GROUP

RULES_TO_EXPORT = {
    'initial_punctuation_token' : INITIAL_PUNCTUATION_TOKEN,
    'final_punctuation_token' : FINAL_PUNCTUATION_TOKEN,
    'punctuation_token' : PUNCTUATION_TOKEN,
    'currency_token' : CURRENCY_TOKEN,
}

# Compiled rules with word boundaries.
RULES = {key:compile_rule(value) for (key, value) in RULES_TO_EXPORT.items()}
