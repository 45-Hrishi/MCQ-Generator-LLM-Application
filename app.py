import json
import traceback
import pandas as pd
from mcq_generator.utils import extract_text_from_pdf,get_table_data,generate_mcq_from_text
import streamlit as st

#creating a title for the app
st.title("QuizChain 🦜⛓️")

#Create a form using st.form
with st.form("user_inputs"):
    #File Upload
    uploaded_file=st.file_uploader("Uplaod a PDF or txt file")
    if uploaded_file : pdf_filename = uploaded_file.name
    
    #Input Fields
    mcq_count=st.number_input("No. of MCQs", min_value=3, max_value=20)

    #Subject
    subject=st.text_input("Insert Subject",max_chars=20)

    # Quiz Tone
    tone = st.selectbox(
        "Complexity Level Of Questions",
        options=["Simple", "Intermediate", "Hard"])

    #Add Button
    button=st.form_submit_button("Create MCQs")

    # Check if the button is clicked and all fields have input
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=extract_text_from_pdf(uploaded_file,pdf_name=pdf_filename)
                response = generate_mcq_from_text(text=text,no_of_mcqs=mcq_count,subject=subject,tone=tone)
                # st.write(response)
                # print(response)
                
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")

            else:
                if isinstance(response, dict):
                    #Extract the quiz data from the response
                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.to_csv("quiz.csv")
                            df.index=df.index+1
                            st.table(df)
                            #Display the review in atext box as well
                            # st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data")

                else:
                    st.write(response)


