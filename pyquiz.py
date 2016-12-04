import random
import sys

# list of nouns, downloaded from scrapmaker.com
WORD_FILE = "nouns.txt"
WORDS = []

QUESTIONS = {
    "class %%%(%%%):":
        "Make a class named %%% that is a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has a __init__ that takes self and *** parameters",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# phrase or answer first
if len(sys.argv) == 2 and sys.argv[1] == "reverse":
    ANSWER_FIRST = True
else:
    ANSWER_FIRST = False

# load up words from file
with open(WORD_FILE) as open_file:
    for line in open_file:
        WORDS.append(line.strip())

def parse(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake params list
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until quit or CTRL-D
try:
    while True:
        snippets = list(QUESTIONS)
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = QUESTIONS[snippet]
            answer, question = parse(snippet, phrase)
            if ANSWER_FIRST:
                question, answer = answer, question

            print (question)

            input("> ")
            print("ANSWER: {}\n\n".format(answer))
except EOFError:
    print ("\nBye!")

