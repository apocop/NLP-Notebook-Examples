from grammar import rules
from tokenizer import Tokenizer

tokenizer_rules = rules
tokenizer = Tokenizer()

# Test rule regexes.
def test_inital_punctuation_regex():
    tokenizer_rules['INITIAL_PUNCTUATION_TOKEN'].pattern == """^([\'"])([A-Z]+[\',!?":.]*)$"""

def test_final_punctuation_regex():
    assert tokenizer_rules['FINAL_PUNCTUATION_TOKEN'].pattern == """^([A-Z]+)([',!?":.]+)$"""

def test_all_punctuation_regex():
    assert tokenizer_rules['ALL_PUNCTUATION_TOKEN'].pattern == """^([',!?":.])([',!?":.]+)$"""

def test_currency_amount_regex():
    assert tokenizer_rules['CURRENCY_AMOUNT_TOKEN'].pattern == r"""^([$£¥€])([0-9]+\.?[0-9]{,2})$"""


# Test rules.

def test_inital_punctuation_rule():
    inital_punctuation_testdata = {
        '"Hi' : ['"', 'Hi'],
        '\'Hi' : ['\'', 'Hi'],
        '-Hi' : ['-Hi'],
        '""hi' : ['""hi'],
    }

    for test, answer in inital_punctuation_testdata.items():
        assert tokenizer.tokenize(test) == answer

def test_final_punctuation_rule():
    inital_punctuation_testdata = {
        'Say,' : ["Say", ','],
        'Hi...' : ['Hi', '.', '.', '.'],
        'Like this:' : ['Like', 'this', ':'],
        'E.T.' : ['E.T.'],
        'etc.' : ['etc', '.'],
    }

    for test, answer in inital_punctuation_testdata.items():
        assert tokenizer.tokenize(test) == answer


def test_all_punctuation_rule():
    inital_punctuation_testdata = {
        '",' : ["\"", ','],
        '\',' : ["\'", ','],
    }

    for test, answer in inital_punctuation_testdata.items():
        assert tokenizer.tokenize(test) == answer


def test_currency_amount_rule():
    inital_punctuation_testdata = {
        '$5.00' : ['$', '5.00'],
        '¥32' : ['¥', '32'],
        '¥35.00' : ['¥', '35.00'],
        '€23.00' : ['€', '23.00'],
        '€1.23,' : ['€1.23,'],
    }

    for test, answer in inital_punctuation_testdata.items():
        assert tokenizer.tokenize(test) == answer