import os
from google import genai
from dotenv import load_dotenv

# 1. Load the hidden .env file
load_dotenv()

# 2. Grab the key and initialize the Client (New Syntax)
gemini_api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)

def aiProcess(command):
    """
    This function replaces the OpenAI logic. 
    You import this into main.py, pass it the voice command, and it returns the text.
    """
    # Giving Nova a personality prompt so it answers correctly
    prompt = f"You are a virtual assistant named Nova. Answer concisely using minimum one to two sentences. User says: {command}"
    
    try:
        # 3. Generate content using the new client syntax
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        # Strip out markdown stars so your text-to-speech engine doesn't read them out loud
        return response.text.replace("*", "")
        
    except Exception as e:
        print(f"Actual Error: {e}")
        return "Sorry, I am having trouble connecting to the network right now."

# --- Quick Test (Runs only if you run client.py directly) ---
if __name__ == "__main__":
    test_command = "Who is Narendra Modi?"
    print("Sending to Gemini...")
    print(aiProcess(test_command))