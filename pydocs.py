#!/usr/bin/env python
"""
Use ChatGPT to write a python program that uses the OpenAI api to create
docstrings for python functions

See OpenAI docs at: https://beta.openai.com/examples/default-python-docstring

Usage:
    >>> python ./pydocs.py
    Enter a python function to produce a python docstring
    >>> def tasty_cake(name: str, cost: decimal):
    print(f'The {name} cake costs \${cost:.2f}')
    # use ctrl-d to send an input terminator
"""
import sys
import openai
import os


def main():
    # Print the instructions
    print("Enter a python function to produce a python docstring")

    # Read the input string
    input_str = sys.stdin.read()

    # Do something with the input string
    print(f"Received the following input:\n{input_str}")

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=f"{input_str}\n\n# An elaborate, high quality docstring for the above function:\n\"\"\"",
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", "\"\"\""]
    )

    for num, choice in enumerate(response["choices"], start=1):
        print(f"Docstring Option #{num}:")
        print(choice["text"])


if __name__ == '__main__':
  main()