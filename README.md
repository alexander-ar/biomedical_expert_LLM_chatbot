# Biomedical Expert Chatbot Application

## Overview
This is a repo for GPT chatbot application. The application leverages GPT 3.5 model that is accessed through. OpenAI API.  The app works through a command line interface accepting a text file as an input.  This file contains a list of questions that need to be answered by the chatbot (one question per line).  For additional requirements,  the app is designed to handle multiple questions about the same topic in succession, including the follow up questions (i.e. retaining the memory of the conversation).  The app is also tailored to answer questions in the biomedical domain only. If asked about significantly unrelated topics (e.g. “Give me a recipe for a cheesecake”), the app may respond by saying "The question is not relevant to the domain of interest.".  

## How to Run This Application
The code for this application is contained in the root directory in the file `app.py`.  This application is designed to be run from command line.  Navigate to the folder where the app.py is saved and then run:
```
python3 app.py --input path_to_file/test_question_list.txt
```
where `path_to_file/test_question_list.txt` should be the location for the file with input user questions (one question per line).

## Application Dependencies
The dependencies for this application are described in the `requirements.txt` file located in the root directory.  From the same directory, run:
```
pip install -r requirements.txt
```
to install the required python libraries.

## Setting Environmental Variables
Environmental variables needed to authenticate AzureOpenAI connection are located in .env file saved in the same directory as the app.py file.  The file should have API key for the open AI API:
```
OPENAI_API_KEY="your...api...key"
```

## Example of Use
The root directory contains a sample input text file `sample_test_input.txt` with sample questions from the biomedical domain, follow up question, as well as questions unrelated to the biomedical domain:
```
What type of molecule encodes heritable genetic information for all forms of life?
What does IBD stand for?
How can I make a paper airplane?
What is the deadliest form of cancer in the United States, measured by number of deaths per year?
How is it typically diagnosed?
give me a recipe for a chocolate cake
```

Here is an example of the app use with this sample text file as an input:
```
$ python3 app.py --input sample_test_input.txt
Answer to question 1:

The molecule that encodes heritable genetic information for all forms of life is DNA (deoxyribonucleic acid).


Answer to question 2:

IBD stands for Inflammatory Bowel Disease. It is a term used to describe a group of chronic inflammatory disorders of the digestive tract, including Crohn's disease and ulcerative colitis.

Answer to question 3:

The question is not relevant to the biomedical domain.

Answer to question 4: 

The deadliest form of cancer in the United States, measured by the number of deaths per year, is lung cancer. 

Answer to question 5: 

Lung cancer is typically diagnosed through a combination of imaging tests, such as chest X-rays and computed tomography (CT) scans, as well as tissue biopsy to examine the cells for cancerous changes. Additionally, techniques like bronchoscopy and sputum cytology may be used to collect samples for analysis.

Answer to question 6: 

The question is not relevant to the biomedical domain.
```

## Author and Acknowledgments
All the code in this repo was created by the author of this repo, Alexander Arefolov.  


