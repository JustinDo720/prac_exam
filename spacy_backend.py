import spacy

# Creating that spacy object to work with.
nlp = spacy.load("en_core_web_lg")


def check_ans(ans):
    """
    Checking the user's answer and match with the actual answer

    :param ans: user's input that represent the answer to a question
    :return: boolean value that reflects the result to a certain question
    """

    # For now, we'll use a static answer
    # TODO: fetch answers from csv file
    actual_answer = "Composition allows a class to be projected as a container of different classes."

    # Checking the similarity between our user's response vs the correct answer
    ans = nlp(ans)
    similarity_percentage = ans.similarity(nlp(actual_answer))

    # Returning a value based on our percentage
    print(similarity_percentage)
    return (similarity_percentage * 100) > 77.0




