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


## --example=tldr

summarize text

```
python play.py --example="tldr" --prompt "A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei."

Example TLDR Result Option #1 using text-ada-001:

A neutron star is the collapsed core of a massive supergiant star. It has a radius of 10 kilometers and a mass of 1.4 solar masses.
```

## --example=py-explain

Create a python docstring for a function

Examples

```
# run the script to prompt for input
python play.py --example="py-explain" --prompt "# Python 3.7\n \ndef tasty_cake(name: str, cost: decimal):\n    print(f'The {name} cake costs \${cost:.2f}')"

# The function tasty_cake takes two arguments: name and cost.
# The function prints the string The followed by the name of the cake and the cost of the cake.
# The cost of the cake is formatted to two decimal places.
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