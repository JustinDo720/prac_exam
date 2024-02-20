from build_questions import initialize_questions, add_question, transfer_to_csv
import tkinter as tk
from tkinter import ttk
from spacy_backend import check_ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Building a function to check our answer by obtaining the user's response
    # input that into our check_ans function from our spacy_backend module.
    def validate_user_input(result_showcase, correct_ans_showcase, user_ans_var, corr_ans):
        users_response = user_ans_var.get("1.0", tk.END).strip()
        print(users_response)
        result = check_ans(users_response)
        if result:
            result_showcase.config(text="Correct")
        else:
            result_showcase.config(text="Incorrect!")
            correct_ans_showcase.config(text=corr_ans)

    # First we build our question dataframe in order to add or retrieve questions
    question_df = initialize_questions()

    # Figure out which mode we are in "Answering" or "Adding question mode"
    # Starting that Tkinter Root and configurations
    wnd = tk.Tk()
    wnd.title = "Practice Test"
    wnd.geometry("600x600")

    # Building the tab system
    tabsys = ttk.Notebook(master=wnd)

    # Creating new tabs using Frame Widgets
    tab1 = tk.Frame(tabsys)
    tab2 = tk.Frame(tabsys)

    # Binding our Frames to the tab system
    tabsys.add(tab1, text="Quiz")
    tabsys.add(tab2, text="Add Question & Answer")
    tabsys.pack(expand=1, fill="both")

    # Working on widgets inside the first tab
    for q_a in question_df.index:
        # Showing the question to our users
        question_t1 = tk.Label(tab1, text=question_df['question'][q_a])
        print(question_t1)
        question_t1.grid(column=1, row=1, padx=25, pady=5)

        # Create text widget and specify size.
        user_ans = tk.Text(tab1, height=5,width=52)
        user_ans.grid(column=1, row=2, padx=40, pady=40)

        ans_submit_btn = tk.Button(tab1, height=2, width=20,
                                   text="Submit",
                                   command=lambda: validate_user_input(result_showcase, correct_ans_showcase,
                                                                       user_ans, question_df['correct answer'][q_a]))
        ans_submit_btn.grid(column=1, row=3)

        result_showcase = tk.Label(tab1, text="")
        result_showcase.grid(column=1, row=4)

        correct_ans_showcase = tk.Label(tab1, text="")
        correct_ans_showcase.grid(column=1, row=5)


    # mode = "a"
    #
    # if mode.lower() == "a":
    #     # Loop over all questions and answers to that question
    #
    #
    # else:
    #
    #     # Building a list of questions
    #     question_bank = []
    #     question_switch = True
    #
    #     while question_switch:
    #         # Retrieving the question and the answer to that question
    #         new_question = input("Question or 'q' to cancel: ")
    #         new_answer = input("Answer or 'q' to cancel: ")
    #         print()
    #
    #         # Checking for another loop
    #         if new_question.lower() == 'q' or new_answer.lower() == 'q':
    #             question_switch = False
    #         else:
    #             # Inserting our objects into the question back.
    #             question_object = {"question": new_question, "correct_answer": new_answer}
    #             question_bank.append(question_object)
    #
    #     # Adding the questions to a dataframe
    #     for question_object in question_bank:
    #         question_df = add_question(question_df, question=question_object['question'], correct_answer=question_object['correct_answer'])
    #
    #     # Transferring data to a csv file
    #     transfer_to_csv(question_df)

    # Ensure that our window continues until closed
    wnd.mainloop()