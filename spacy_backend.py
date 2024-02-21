import spacy

# Creating that spacy object to work with.
nlp = spacy.load("en_core_web_lg")


def check_ans(ans, actual_answer):
    """
    Checking the user's answer and match with the actual answer

    :param ans: user's input that represent the answer to a question
    :param actual_answer: the correct answer that is used to compare with our user's answer
    :return: boolean value that reflects the result to a certain question
    """

    # Checking the similarity between our user's response vs the correct answer
    ans = nlp(ans)
    similarity_percentage = ans.similarity(nlp(actual_answer))

    # Returning a value based on our percentage
    print(similarity_percentage)
    return (similarity_percentage * 100) > 77.0




