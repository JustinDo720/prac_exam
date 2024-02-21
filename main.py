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
        result = check_ans(users_response, corr_ans)
        if result:
            result_showcase.config(text="Correct")
        else:
            result_showcase.config(text="Incorrect!")
            correct_ans_showcase.config(text=corr_ans)


    def change_question(mode):
        global question_num
        if mode.lower().startswith('n'):
            question_num += 1
        elif mode.lower().startswith('b') and question_num > 0:
            question_num -= 1
        question_t1.config(text=question_df['question'][question_num])
        result_showcase.config(text="")
        correct_ans_showcase.config(text="")
        user_ans.delete('1.0', tk.END)


    def on_question_select():
        sel_index = question_box.curselection()
        if sel_index:
            selected_question = question_box.get(sel_index)
            show_question.config(text=selected_question)
            show_ans.config(text=question_df['correct answer'].loc[sel_index])

    def add_new_question():
        new_dataframe = add_question(question_df, question=question_entry.get(), correct_answer=answer_entry.get())
        transfer_to_csv(new_dataframe)
        question_box.insert(tk.END, question_entry.get())



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
    question_num = 0

    # Showing the question to our users
    question_t1 = tk.Label(tab1, text=question_df['question'][question_num])
    print(question_t1)
    question_t1.grid(column=1, row=1, padx=25, pady=5)

    # Create text widget and specify size.
    user_ans = tk.Text(tab1, height=5,width=52)
    user_ans.grid(column=1, row=2, padx=40, pady=40)

    ans_submit_btn = tk.Button(tab1, height=2, width=20,
                               text="Submit",
                               command=lambda: validate_user_input(result_showcase, correct_ans_showcase,
                                                                   user_ans, question_df['correct answer'][question_num]))
    ans_submit_btn.grid(column=1, row=3)

    result_showcase = tk.Label(tab1, text="")
    result_showcase.grid(column=1, row=4)

    correct_ans_showcase = tk.Label(tab1, text="")
    correct_ans_showcase.grid(column=1, row=5)

    back_question_btn = tk.Button(tab1, text="Back", command=lambda: change_question("back"))
    back_question_btn.grid(column=2, row=6)

    next_question_btn = tk.Button(tab1, text="Next", command=lambda: change_question("next"))
    next_question_btn.grid(column=2, row=5)

    # Working with adding a question tab
    question_box = tk.Listbox(tab2, width=50)
    for question in question_df['question']:
        question_box.insert(tk.END, question)

    question_box.grid(row=1, column=3, columnspan=4, rowspan=4)

    question_box_btn = tk.Button(tab2, text="Check Answer", command=on_question_select)
    question_box_btn.grid(row=5, column=3, columnspan=4)

    # Create a Scrollbar
    scrollbar = tk.Scrollbar(tab2, command=question_box.yview)
    scrollbar.grid(row=1, column=7, rowspan=4, sticky='ns')

    # Attach the Scrollbar to the Listbox
    question_box.config(yscrollcommand=scrollbar.set)

    new_question_label = tk.Label(tab2, text="New Question:")
    new_question_label.grid(row=1, column=1)

    question_entry = tk.Entry(tab2)
    question_entry.grid(row=2, column=1)

    answer_label = tk.Label(tab2, text="Correct Answer:")
    answer_label.grid(row=3, column=1)

    answer_entry = tk.Entry(tab2)
    answer_entry.grid(row=4, column=1)

    sub_new_question = tk.Button(tab2, text='Add Question', command=add_new_question)
    sub_new_question.grid(row=5, column=1)

    show_question = tk.Label(tab2, text="")
    show_question.grid(row=1, column=8)
    show_ans = tk.Label(tab2, text="")
    show_ans.grid(row=2, column=8)



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