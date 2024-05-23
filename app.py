# Load packages
from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse

# fetch environmental variables
load_dotenv()


# initiate the OpenAI client
client = OpenAI()


# helper function to process one line of text
def process_question(new_question, chat_history):
    '''
    process_question() functions takes in a single question 
    for LLM as an argument and the previous chat history and 
    returns Chat Completion API response
    
    Parameters: 
        new_question (str): New question from the user
        chat_history (list): list of tuples where each tuple contains 
            a previous question and Chat Completion API answer
            
    Returns:
        (str) The response text
    '''

    print(f"processing question {new_question}")

    # build messages
    system_prompt = {
    "role": "system", 
    "content" : "You are a distinguished scientist and an expert in the biomedical domain. You are answering questions in the biomedical domain only.  If you are asked a question that is not related to biomedical domain you response will be 'The question is not relevant to the biomedical domain'."
    }

    user_question = {
        "role": "user", 
        "content": f"Only give me answers if the question is related to biomedical domain. If a question is not from biomedical domain, respond with 'The question is not relevant to the biomedical domain'.  Here is the user's question: {new_question}"
    }

    messages = [system_prompt]
    
    # add the chat history
    for question, answer in chat_history:
        messages.append({"role": "user", "content": question})
        messages.append({"role": "assistant", "content": answer})
        
    # append the latest user question    
    messages.append(user_question)
        
    # run the model to generate chat completion object
    chat_completion = client.chat.completions.create(
    model = 'gpt-4-turbo-preview',
    messages = messages,
    temperature = 0.5,
    max_tokens = 800,
    top_p = 0.95,
    frequency_penalty = 0,
    presence_penalty = 0,
    stop = None
    )
    
    return chat_completion.choices[0].message.content


# main app funtion
def main(text_file):
    '''
    main() function takes the text file as an argument.  
    The input text file may have several questions, one question per line. 
    Some of these questions may be follow up questions.
    Main() function uses process_question() helper function to process
    each line and as an output, it prints out the answer to each 
    question in the corresponding order in the following format: 
    Answer to question 1: 
    The body of the answer.
    
    Parameters:
        text_file (str): path to the input text file
    
    Returns:
        printed output with the GPT answer to each question
    '''
    # keep the history of previous questions and answers
    chat_history = []

    print("#######################################################")
    
    # process the text file line by line
    with open(text_file, 'r') as file:
        question_counter = 0
        for line in file:
            question_counter += 1
            # Process each line
            new_user_question = line
            response = process_question(new_question = new_user_question, chat_history = chat_history)
            
            # add new question and response to the chat_history
            chat_history.append((new_user_question, response))
            
            # print the response
            print(f"Answer to question {question_counter}: \n")
            print(response, "\n")
            
            
if __name__ == "__main__":
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description = "Biomedical domain chatbot application.")
    parser.add_argument("--input", help = "Input text file", required = True)

    # Parse command line arguments
    args = parser.parse_args()

    # Call the main function with the input file
    main(text_file = args.input)
