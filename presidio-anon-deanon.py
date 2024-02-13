"""
Author: Christophe Le Dorze
Email:  Christophe.ledorze@gmail.com
Description: This script processes text through Presidio for anonymization, sends it to OpenAI's GPT for further processing, and then deanonymizes the output. It is designed to handle sensitive information securely by anonymizing identifiable details before AI processing.
"""

import os
import requests
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
import argparse

def analyze_text(text, analyzer_url, language):
    response = requests.post(analyzer_url, json={"text": text, "language": language})
    return response.json()

def anonymize_text(text, analyzer_results, anonymizer_url):
    # Initialize a mapping dictionary to keep track of original entities and their placeholders
    anonymization_mapping = {}
    anonymized_text = text

    for entity in analyzer_results:
        # Extract entity information
        start, end = entity['start'], entity['end']
        entity_type = entity['entity_type']
        original_text = text[start:end]

        # Generate a unique placeholder
        placeholder = f"<{entity_type}_{start}_{end}>"

        # Replace the original text with the placeholder
        anonymized_text = anonymized_text.replace(original_text, placeholder, 1)

        # Store the mapping
        anonymization_mapping[placeholder] = original_text

    return anonymized_text, anonymization_mapping

def deanonymize_text(anonymized_text, anonymization_mapping):
    deanonymized_text = anonymized_text
    for placeholder, original_text in anonymization_mapping.items():
        deanonymized_text = deanonymized_text.replace(placeholder, original_text)
    return deanonymized_text

def process_with_openai(prompt, messages):
    response = client.chat.completions.create(model="gpt-4",  # Adjust based on the model you have access to
    messages=messages)
    return response.choices[0].message.content

def main(file_path, language, openai_api_key, prompt):
      # Set the OpenAI API key directly

    analyzer_url = "http://localhost:5001/analyze"
    anonymizer_url = "http://localhost:5002/anonymize"
    deanonymizer_url = "http://localhost:5002/deanonymize"

    with open(file_path, 'r') as file:
        text = file.read()
    print("Original Text:\n", text)  # Print the original text

    analysis_results = analyze_text(text, analyzer_url, language)
    anonymized_text, anonymization_mapping = anonymize_text(text, analysis_results, anonymizer_url)

    print("Anonymized Text:\n", anonymized_text)  # Print the anonymized text
    messages = [
        {
            "role": "system",
            "content": "Always reinterpret the text entered as input into English, imitating the style of a highly proficient French speaker carrying out English communication, with a focus on Information Technology and Operational Technology. Utilize technical terminology related to operating systems and container orchestration, catering to specialists, managers, and engineers. Maintain a 50-50 blend of English and French linguistic styles, keeping a semi-formal tone without complex UK-specific terms."
        },
        {
            "role": "user",
            "content": anonymized_text  # Insert anonymized text directly, assuming it needs processing according to the system's instructions
        }
    ]

    processed_text = process_with_openai(prompt, messages)
    print("Response from OpenAI GPT:\n", processed_text)  # Print the response from OpenAI GPT

    # Right before the deanonymization step:
    print("Verifying analysis results integrity for deanonymization:")
    print(analysis_results)  # This should match the initial analysis_results used for anonymization

    deanonymized_text = deanonymize_text(processed_text, anonymization_mapping)

    print("Final Text:\n", deanonymized_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process text through Presidio and OpenAI GPT, then deanonymize the output.')
    parser.add_argument('file_path', type=str, help='Path to the text file to be processed.')
    parser.add_argument('--language', type=str, default='en', help='Language of the text. Defaults to English (en).')
    parser.add_argument('--openai_api_key', type=str, required=True, help='OpenAI API key for processing.')
    parser.add_argument('--prompt', type=str, default='', help='Prompt to prepend to the text for GPT processing.')
    args = parser.parse_args()

    main(args.file_path, args.language, args.openai_api_key, args.prompt)

