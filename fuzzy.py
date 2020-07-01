from fuzzywuzzy import process
from fuzzywuzzy.fuzz import ratio


def get_fuzzy_similarity(token=None, dictionary=None):
    """Returns similar words ans similary scores for a given token
    from a provided dictonary of words.

    Keywords Arguements:
        token {str} -- the reference word (default : {None})
        dictionary {list} -- the list fo target words (default : {None})


    Returns:
        [list] -- a list of tuples in the form '(matched_word, similarity score)'
    """

    if token in dictionary:
        return process.extractBests(token, dictionary, scorer=ratio, score_cutoff=70)
    else:
        return []


if __name__ == "__main__":
    # toy doctionary of words will be query our mispelt input against
    word_dictionary = ["medium", "Twitter", "Google", "LiknedIn", "Facebook"]

    # print the result of the fuzzy match search

    print(get_fuzzy_similarity("mediaum", word_dictionary))
