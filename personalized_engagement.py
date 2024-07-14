# personalized_engagement.py

import openai
import json

# Replace with your actual OpenAI API key
API_KEY = 'sk-exampleapikey1234567890abcdefghijklmnopqrstuvwxyz'
openai.api_key = API_KEY

# Function to generate a personalized message
def generate_personalized_message(customer_data):
    prompt = f"Generate a personalized message for a customer with the following data: {json.dumps(customer_data)}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Example customer data
    customer_data = {
        "name": "Jane Doe",
        "purchase_history": ["laptop", "mouse"],
        "preferences": ["technology", "gadgets"]
    }
    
    # Generate and print the personalized message
    message = generate_personalized_message(customer_data)
    print(f"Personalized Message: {message}")
