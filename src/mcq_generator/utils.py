import json
from mcq_generator.logger import logging
from PyPDF2 import PdfReader
from mcq_generator.mcq_generator import seq_quiz_chain


def generate_mcq_from_text(text,no_of_mcqs,subject,tone):
    with open("response.json",'r') as json_file:
        RESPONSE_JSON = json.load(json_file)
        
    response = seq_quiz_chain.invoke(input={"text":text,
                             "number":no_of_mcqs,
                             "subject":subject,
                             "tone":tone,
                             "response_json":RESPONSE_JSON})
    return response

def extract_text_from_pdf(uploaded_pdf,pdf_name):
    try:
        reader = PdfReader(uploaded_pdf)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        logging.info(f"Extracting text from {pdf_name} is successfully completed.")
        return text
    except Exception as e:
        logging.error(f"Failed to extract text from {pdf_name}. Error : {e}")
        raise e
    
def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        cleaned_quiz_string = quiz_str.replace('```json\n', '').replace('```', '')
        cleaned_quiz_string = cleaned_quiz_string.split('### RESPONSE_JSON')[1].strip().replace("'", '"')
        
        print("Cleaned quiz string : ",cleaned_quiz_string)
            
        cleaned_quiz_json = json.loads(cleaned_quiz_string)
        quiz_table_data=[]
        
        # iterate over the quiz dictionary and extract the required information
        for key,value in cleaned_quiz_json.items():
            mcq=value["mcq"] + "\n"
            options="\n".join(
                [
                    f"{option}. {option_value}" for option, option_value in value["options"].items()
                 
                 ]
            )
            correct=value["correct"]
            quiz_table_data.append({"MCQ": mcq,"Choices": options, "Correct": correct})
        
        return quiz_table_data
        
    except Exception as e:
        raise e

