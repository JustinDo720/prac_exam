from build_questions import initialize_questions, add_question, transfer_to_csv


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # First we build our question dataframe in order to add questions.
    question_df = initialize_questions()

    # Building a list of questions
    question_bank = []
    question_switch = True

    while question_switch:
        # Retrieving the question and the answer to that question
        new_question = input("Question or 'q' to cancel: ")
        new_answer = input("Answer or 'q' to cancel: ")
        print()

        # Inserting our objects into the question back.
        question_object = {"question": new_question, "correct_answer": new_answer}
        question_bank.append(question_object)

        # Checking for another loop
        if new_question.lower() == 'q' or new_answer.lower() == 'q':
            question_switch = False

    # Adding the questions to a dataframe
    for question_object in question_bank:
        question_df = add_question(question_df, question=question_object['question'], correct_answer=question_object['correct_answer'])

    # Transferring data to a csv file
    transfer_to_csv(question_df)