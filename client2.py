import os
from google import genai
from dotenv import load_dotenv

# 1. Load your secret key from the .env file
load_dotenv()

# 2. Initialize the client (it automatically looks for GEMINI_API_KEY in your environment)
client = genai.Client()

# 3. Write your question
my_question = "full form of pip in python that we use to install packages? answer in four sentences and give an example of how to use it in terminal to install a package called numpy"
print("Sending question to Gemini: ", my_question)
print("Waiting for answer...\n")

# 4. Send the question using the fast flash model
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=my_question
)

# 5. Print the exact text response to the terminal
print(response.text)