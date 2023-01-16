#!/usr/bin/env python3
"""
Use ChatGPT to write a python program that uses the OpenAI api to create
docstrings for python functions

See OpenAI docs at: https://beta.openai.com/examples/default-qa

Usage:
    >>> echo -e "Who is the president" | python play.py --example="qa"
"""
import sys
import openai
import os
import random
import click

DEFAULT_KWARGS = {
    "temperature": 0,
    "max_tokens": 150,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
}

MODELS = [
    "text-davinci-003",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001",
    "code-davinci-002",
    "code-cushman-001",
]

MODEL_DEFAULTS = {
    "docstring": "code-davinci-002",
    "qa": "text-davinci-003",
    "grammar": "text-davinci-003",
}

QA_PROMPT = """
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

Q: What is human life expectancy in the United States?
A: Human life expectancy in the United States is 78 years.

Q: {prompt}
A:
"""

PYTHON_EXPLAIN = """
# Python 3
{prompt}

# Explanation of what the code does

#
"""

TLDR = """
{prompt}

Tl;dr
"""

SENTIMENT = """
Classify the sentiment in this tweet:
{prompt}
"""

GRAMMAR_PROMPT = "Correct this to standard English:\n\n{prompt}"

@click.command()
@click.option('--example', default="docstring", help='The type of prompt')
@click.option('--prompt', default="", help='A text prompt')
@click.option('--model', default="", help='The model to use')
def main(example: str, prompt: str, model: str):
    # save the prompt fragment for later reporting since we need to tweak it
    kwargs = DEFAULT_KWARGS.copy()

    # Read the input string
    if not prompt:
        prompt = sys.stdin.read()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    # tweak the prompt or parameters
    if example == "docstring":
        prompt += "\n\n# An elaborate, high quality docstring for the above function:\n\"\"\""
        kwargs["stop"] = ["#", "\"\"\""]
    elif example == "qa":
        prompt = QA_PROMPT.format(prompt=prompt)
    elif example == "grammar":
        prompt = GRAMMAR_PROMPT.format(prompt=prompt)
    elif example == "py-explain":
        prompt = PYTHON_EXPLAIN.format(prompt=prompt)
    elif example == "tldr":
        prompt = TLDR.format(prompt=prompt)
        kwargs = { "presence_penalty": 1, "max_tokens": 60, }
    elif example == "twitter-sentiment":
        prompt = SENTIMENT.format(prompt=prompt)

    if not model:
        model = MODEL_DEFAULTS.get(example, random.choice(MODELS))

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        **DEFAULT_KWARGS
    )

    for num, choice in enumerate(response["choices"], start=1):
        print(f"Example {example.upper()} Result Option #{num} using {model}:")
        print(choice["text"])


if __name__ == '__main__':
  main()