import re

def compile_rule(rule):
    return re.compile(bos + rule + eos, re.IGNORECASE)

def group(group):
    # Returns regular expression groups.
    return open_group + group + close_group

# Basic characters and sets.
alpha = '[A-Z]+'
digits = '[0-9]'
bos = '^'
eos = '$'
plus = '+'
star = "*"
period = r'\.'
open_group = '('
close_group = ')'
initial_punctuation = '[\'"]'
final_punctuation = '[\',!?":.]'
currency_symbol = '[$£¥€]'
zero_or_one = '?'

# Regular expression groups.
alpha_group = group(alpha)
initial_punctuation_group = group(initial_punctuation)
final_punctuation_group = group(final_punctuation + plus)
final_punctuation_star_group = group(final_punctuation + star)
currency_symbol_group = group(currency_symbol)
currency_group = group(digits + plus + period + zero_or_one + digits + '{,2}')
alpha_punctuation_group = group(alpha + final_punctuation + star)

# Grammar rules.
initial_punctuation_token = initial_punctuation_group + alpha_punctuation_group
final_punctuation_token = alpha_group + final_punctuation_group
all_punctuation_token = open_group + final_punctuation + close_group + final_punctuation_group
currency_amount_token = currency_symbol_group + currency_group + final_punctuation_star_group

rules_to_export = {
    'initial_punctuation_token' : initial_punctuation_token,
    'final_punctuation_token' : final_punctuation_token,
    'all_punctuation_token' : all_punctuation_token,
    'currency_amount_token' : currency_amount_token,
}

# Compiled rules with word boundaries.
rules = {k:compile_rule(v) for (k,v) in rules_to_export.items()}