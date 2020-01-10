"""
Tokenizer class which uses a regex grammar to break down tokens.
"""
import re
import exceptions
import grammar

class Tokenizer:
    """Tokenizer class."""
    def __init__(self):
        self.rules = grammar.RULES
        self.rule_list = list(grammar.RULES)
        self.exception_lexicon = exceptions.LEXICON
        self.accepted_tokens = None

    def __tokenize_pipeline(self, token):
        """Validate tokens."""
        if token in self.exception_lexicon:
            self.accepted_tokens += self.exception_lexicon[token]
        else:
            continue_matching = True
            rule_index = 0

            while continue_matching:
                rule = self.rule_list[rule_index]
                match = re.match(self.rules[rule], token)
                if match:
                    for group in match.groups():
                        if group:
                            self.__tokenize_pipeline(group)
                            continue_matching = False
                else:
                    if rule == self.rule_list[-1]:
                        self.accepted_tokens.append(token)
                        continue_matching = False
                    else:
                        rule_index += 1

    def tokenize(self, string):
        """Return list of tokenized strings."""
        self.accepted_tokens = []
        tokens = (token for token in string.split())
        for token in tokens:
            self.__tokenize_pipeline(token)

        return self.accepted_tokens
