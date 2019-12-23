import re
from exceptions import exceptions
from grammar import rules

class Tokenizer(object):
    def __init__(self, rules = rules, exceptions = exceptions):
        self.tokens = []
        self.rules = rules
        self.exceptions = exceptions

    def add_token(self, approved_token):
        self.tokens.append(approved_token)

    def add_exception(self, exception):
        for exception in self.exceptions.get(exception):
            self.add_exception(exception)

    def tokenize_pipline(self, token):
        if token in self.exceptions:
            self.add_exception(token)
        else:
            for rule in list(self.rules):
                match = re.match(self.rules.get(rule), token)
                if match:
                    for group in match.groups():
                        if group != '':
                            self.tokenize_pipline(group)
                    break
                else:
                    if rule == list(self.rules)[-1]:
                        self.add_token(token)

    def tokenize(self, string):
        for token in string.split():
            self.tokenize_pipline(token)

        accepted_tokens = self.tokens.copy()
        self.tokens.clear()

        return accepted_tokens