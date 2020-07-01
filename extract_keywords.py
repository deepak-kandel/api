import spacy
import subprocess
from string import punctuation


def extract_keywords(nlp, sequence, special_tags: list = None):
    """Takes a Spacy core language model,
    string sequence of text and optional
    list of special tags as arguements.

    If any of the words in the string are
    in the list of special tags they are immediately
    added to the result.

    Arguements:
        sequence {str} -- string sequence to have keywords added (default :{None})

    Keyword Arguements:
        {list} -- list of tags to be automatically added (default : {None})

    Returns:
        {list} -- list of unique keywords extracted from a string 
    """
    result = []

    # custom list of part of speech tags we are interested in
    # we are interested in proper nouns, nouns, ans adjectives
    # edit this list of POS tags according to your needs.
    pos_tag = ["PROPN", "NOUN", "ADJ"]

    # create a spacy doc object by calling the nlp object on the input sequence
    doc = nlp(sequence.lower())

    # if special tags are given and exits in the input sequence
    # add them to results by default

    if special_tags:
        tags = [tags.lower() for tag in special_tags]
        for token in doc:
            if token.text in tags:
                result.append(token.text)

    for chunk in doc.noun_chunks:
        final_chunk = ""
        for token in chunk:
            if token.pos_ in pos_tag:
                final_chunk = final_chunk + token.text + " "
        if final_chunk:
            result.append(final_chunk.strip())

    for token in doc:
        if token.text in token.text in punctuation:
            continue
        if token.pos_ in pos_tag:
            result.append(token.text)
    return list(set(result))


if __name__ == "__main__":
    """install the language model using the subprocess package
    useful whrn hosting the service in the cloud as it prevents against
    us forgetting to do this via the CLI
    """
    subprocess.call("python -m spacy download en_core_web_sm", shell=True)
    nlp = spacy.load("en_core_web_sm")

    print("Loaded language vacabulary")

    print(
        extract_keywords(
            nlp,
            """Learninig how to use Natural Language Processing
                                in Python and build Flask's API is easy when you have
                                packages like spacy anc fuzzywuzzy""",
        )
    )
