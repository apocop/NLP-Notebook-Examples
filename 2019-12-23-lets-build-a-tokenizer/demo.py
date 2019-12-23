from tokenizer import Tokenizer

lines = [
    "Hi, how are you?",
    "What's up, John?",
    "I hear that Google's looking to purchase #yourcompany for $10 million!",
    "I'm really starting to dig this NLP Notebook blog.",
    "What's your E.T.A.? I really have to know.",
    "I have $43, while you have €3.32.",
]

tokenizer = Tokenizer()

tokenized_lines = [tokenizer.tokenize(line) for line in lines]
for line in tokenized_lines:
    print(line)
