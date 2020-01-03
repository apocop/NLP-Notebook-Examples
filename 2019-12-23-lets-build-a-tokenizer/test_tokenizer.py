"""
Test the tokenizer, grammar and exceptions.
"""
import tokenizer
import grammar


TOKENIZER = tokenizer.Tokenizer()
RULES = grammar.RULES

# Test rule regexes.
def test_inital_punctuation_regex():
    """Test the grammar generated regex."""
    test_regex = RULES['initial_punctuation_token'].pattern
    assert test_regex == """^([\'"])([A-Z]+[\',!?":.]*)$"""

def test_final_punctuation_regex():
    """Test the grammar generated regex."""
    test_regex = RULES['final_punctuation_token'].pattern
    assert test_regex == """^([A-Z]+)([',!?":.]+)$"""

def test_all_punctuation_regex():
    """Test the grammar generated regex."""
    test_regex = RULES['punctuation_token'].pattern
    assert test_regex == """^([',!?":.])([',!?":.]+)$"""

def test_currency_regex():
    """Test the grammar generated regex."""
    test_regex = RULES['currency_token'].pattern
    assert test_regex == r"""^([$£¥€])([0-9]+\.?[0-9]{,2})([',!?":.]*)$"""


# Test rules.
def test_inital_punctuation_rule():
    """Test the tokenizer pipeline is tokenizing initial punctuation."""
    inital_punctuation_testdata = {
        '"Hi' : ['"', 'Hi'],
        '\'Hi' : ['\'', 'Hi'],
        '-Hi' : ['-Hi'],
        '""hi' : ['""hi'],
    }

    for test, answer in inital_punctuation_testdata.items():
        assert TOKENIZER.tokenize(test) == answer

def test_final_punctuation_rule():
    """Test the tokenizer pipeline is tokenizing final punctuation."""
    final_punctuation_testdata = {
        'Say,' : ["Say", ','],
        'Hi...' : ['Hi', '.', '.', '.'],
        'Like this:' : ['Like', 'this', ':'],
        'E.T.' : ['E.T.'],
        'etc.' : ['etc', '.'],
    }

    for test, answer in final_punctuation_testdata.items():
        assert TOKENIZER.tokenize(test) == answer


def test_all_punctuation_rule():
    """Test the tokenizer pipeline is tokenizing all punctuation."""
    all_punctuation_testdata = {
        '",' : ["\"", ','],
        '\',' : ["\'", ','],
    }

    for test, answer in all_punctuation_testdata.items():
        assert TOKENIZER.tokenize(test) == answer


def test_currency_amount_rule():
    """Test the tokenizer pipeline is tokenizing currency amount."""
    currency_amount_testdata = {
        '$5.00' : ['$', '5.00'],
        '¥32' : ['¥', '32'],
        '¥35.00' : ['¥', '35.00'],
        '€23.00' : ['€', '23.00'],
        '€1.23,' : ['€', '1.23', ','],
    }

    for test, answer in currency_amount_testdata.items():
        assert TOKENIZER.tokenize(test) == answer

def test_exceptions():
    """Test the tokenizer pipeline using exceptions."""
    exceptions_testdata = {
        "don't" : ["do", "n't"],
        "isn't" : ["is", "n't"],
        "What's" : ["What", "'s"],
        "what's" : ["what's"],
        "I'm" : ["I", "'m"],
    }
    for test, answer in exceptions_testdata.items():
        assert TOKENIZER.tokenize(test) == answer
