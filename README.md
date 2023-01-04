# openai_playground

Use the OpenAI api and ChatGPT to write small python utilities
## Quickstart
```
# Set the variable `OPENAI_API_KEY` to your api key, and run one of the following scripts
export OPENAI_API_KEY=...

python -m venv venv
. venv/bin/activate && pip3 install -r requirements.txt

# run pydocs
python ./pydocs.py

# paste a function followed by `ctrl-d`
```

## pydocs.py

Create a python docstring for a function

Examples

```
# run the script to prompt for input
python ./pydocs.py

Enter a python function to produce a python docstring

# paste the function body
def tasty_cake(name: str, cost: decimal):
    print(f'The {name} cake costs \${cost:.2f}')

# use ctrl-d to send an input terminator

# Alternatively, pipe the function as a string
echo -e "# Python 3.7\n \ndef tasty_cake(name: str, cost: decimal):\n    print(f'The {name} cake costs \${cost:.2f}')" | python pydocs.py

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