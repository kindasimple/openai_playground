# openai_playground

Use the OpenAI api and ChatGPT to write small python utilities
## Quickstart
```
# Set the variable `OPENAI_API_KEY` to your api key, and run one of the following scripts
export OPENAI_API_KEY=...

python -m venv venv
. venv/bin/activate && pip3 install -r requirements.txt

# pipe a function prompt using the docstring example
echo -e "# Python 3.7\n \ndef tasty_cake(name: str, cost: decimal):\n    print(f'The {name} cake costs \${cost:.2f}')" | python play.py --example="docstring"

python play.py --example="qa" --prompt="What is the largest country in the world?"
```

## --example=docstring

Create a python docstring for a function

Examples

```
# run the script to prompt for input
python play.py --example="docstring" --prompt "# Python 3.7\n \ndef tasty_cake(name: str, cost: decimal):\n    print(f'The {name} cake costs \${cost:.2f}')"

# output from OpenAI API
Prints the name and cost of a cake.

Parameters
----------
name : str
    The name of the cake.
cost : decimal
    The cost of the cake.

Returns
-------
None

Examples
--------
>>> tasty_cake('chocolate', 10.5)
The chocolate cake costs $10.50
```

## --example=qa

echo -e "Who is the president" | python play.py --example="qa"

Enter a python function to produce a python docstring
Received the following input:
Who is the president

Docstring Option #1 using text-davinci-003:

Joe Biden is the current President of the United States.

## --example=grammar

echo -e "Why can i not write correct sentences" | python play.py --example="grammar"