# Customer Support Automation Using Generative AI

This repository contains scripts to automate customer support interactions using the OpenAI GPT-3.5 model. The scripts can generate automated responses to common customer queries and create personalized engagement messages based on customer data.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/customer-support-automation.git
    cd customer-support-automation
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install openai
    ```

3. Set your OpenAI API key:
    - Option 1: Open each Python script (`automated_response.py` and `personalized_engagement.py`) and replace the placeholder API key (`'sk-exampleapikey1234567890abcdefghijklmnopqrstuvwxyz'`) with your actual OpenAI API key.
    - Option 2: Store your API key in an environment variable:
        ```bash
        export OPENAI_API_KEY='sk-exampleapikey1234567890abcdefghijklmnopqrstuvwxyz'
        ```

## Usage

### Automated Response Generation

1. Run the `automated_response.py` script to generate an automated response to a customer query:
    ```bash
    python automated_response.py
    ```

2. Edit the script to use your own query:
    ```python
    query = "Your customer query here"
    ```

### Personalized Customer Engagement

1. Run the `personalized_engagement.py` script to generate a personalized engagement message:
    ```bash
    python personalized_engagement.py
    ```

2. Edit the script to use your own customer data:
    ```python
    customer_data = {
        "name": "Customer Name",
        "purchase_history": ["item1", "item2"],
        "preferences": ["preference1", "preference2"]
    }
    ```

## Contributing

Feel free to submit issues or pull requests if you have any improvements or suggestions.

## License

This project is licensed under the MIT License.
