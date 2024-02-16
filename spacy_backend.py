import spacy

# Creating that spacy object to work with.
nlp = spacy.load("en_core_web_sm")


def check_ans(ans):
    """
    Checking the user's answer and match with the actual answer

    :param ans: user's input that represent the answer to a question
    :return: boolean value that reflects the result to a certain question
    """

    # For now, we'll use a static answer
    # TODO: fetch answers from csv file
    actual_answer = "