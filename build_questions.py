import pandas as pd
import os

# Constant file path
FILE_PATH = 'questions/pcpp_studying.csv'

def transfer_to_csv(dataframe):
    """
    Builds a csv file given a dataframe

    :param dataframe: our dataframe object that holds our questions
    """
    dataframe.to_csv(FILE_PATH, header=['question', 'correct answer'], index=False)


def add_question(old_dataframe, question, correct_answer):
    """
    Adds additional questions to our csv file

    :param old_dataframe: our dataframe object that holds our questions
    :param question: the user's input for a question
    :param correct_answer: the user's input for a correct answer to that question

    :returns: a new dataframe with the combined questions
    """

    new_dataframe = pd.DataFrame([[question, correct_answer]], columns=['question', 'correct answer'])
    new_dataframe = pd.concat([new_dataframe, old_dataframe])

    return new_dataframe


def initialize_questions():
    """
    Creating the question dataframes to hold our question and answer bank

    :return: a question dataframe
    """

    # We have to keep in mind that if the CSV file exist (we prob already have questions in there).
    # In order to preserve the questions and add new ones, we check for the csv file then create a new dataframe
    # from that csv file.

    if os.path.exists(FILE_PATH):
        old_question_df = pd.read_csv(FILE_PATH)
        return old_question_df
    else:
        question_df = pd.DataFrame(columns=['question', 'correct answer'])
        return question_df

