# automated_response.py

import openai

# Replace with your actual OpenAI API key
API_KEY = 'sk-exampleapikey1234567890abcdefghijklmnopqrstuvwxyz'
openai.api_key = API_KEY

# Function to generate a response to a customer query
def generate_response(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Example query
    query = "What is the return policy for your products?"
    
    # Generate and print the response
    response = generate_response(query)
    print(f"Customer Query: {query}\nAI Response: {response}")
