import re
import exceptions
import grammar

class Tokenizer():
    def __init__(self, rules=grammar.rules, exceptions=exceptions.lexicon):
        self.rules = rules
        self.lexicon = exceptions
        self.accepted_tokens = None

    def add_exception(self, exception):
        for token in self.lexicon.get(exception):
            self.accepted_tokens.append(token)

    def tokenize_pipeline(self, token):
        if token in self.lexicon:
            self.add_exception(token)
        else:
            for rule in list(self.rules):
                match = re.match(self.rules.get(rule), token)
                if match:
                    for group in match.groups():
                        if group:
                            self.tokenize_pipeline(group)
                    break
                else:
                    if rule == list(self.rules)[-1]:
                        self.accepted_tokens.append(token)

    def tokenize(self, string):
        self.accepted_tokens = []
        tokens = (token for token in string.split())
        for token in tokens:
            self.tokenize_pipeline(token)

        return self.accepted_tokens
