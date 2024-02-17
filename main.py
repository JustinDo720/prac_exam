from build_questions import initialize_questions, add_question, transfer_to_csv
from spacy_backend import check_ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # First we build our question dataframe in order to add or retrieve questions
    question_df = initialize_questions()

    # Figure out which mode we are in "Answering" or "Adding question mode"
    # TODO: Consider using tkinter and switching tabs
    mode = "a"

    if mode.lower() == "a":
        # Loop over all questions and answers to that question
        for q_a in question_df.index:
            # Showing the question to our users
            print(question_df['question'][q_a])
            user_ans = input("Your Answer: ")

            # Checking the result of our user's response.
            result = check_ans(user_ans)
            if result:
                print("That is Correct!")
            else:
                print("That is Incorrect!")

            print()
            print("The correct answer is: ", question_df['correct answer'][q_a])
            print()

    else:

        # Building a list of questions
        question_bank = []
        question_switch = True

        while question_switch:
            # Retrieving the question and the answer to that question
            new_question = input("Question or 'q' to cancel: ")
            new_answer = input("Answer or 'q' to cancel: ")
            print()

            # Checking for another loop
            if new_question.lower() == 'q' or new_answer.lower() == 'q':
                question_switch = False
            else:
                # Inserting our objects into the question back.
                question_object = {"question": new_question, "correct_answer": new_answer}
                question_bank.append(question_object)

        # Adding the questions to a dataframe
        for question_object in question_bank:
            question_df = add_question(question_df, question=question_object['question'], correct_answer=question_object['correct_answer'])

        # Transferring data to a csv file
        transfer_to_csv(question_df)