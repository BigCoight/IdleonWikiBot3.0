# IdleonWikiBot3.0

The third iteration of the bot that uploads all gamedata to idleon.info

This project relies heavily on Pydantic base models to validate and parse the spaghetti coming out of the stencyl
converter.

To define a new model, create a new class that inherits from IdleonModel with its details, add a new section to the code
reader that the data is stored, and create a repository that then parses the data into the class. After running you will
then fine the repo exporred as a JSON file under the exported tab

## Getting started

It's generally recommended to use [venv](https://docs.python.org/3/library/venv.html) to create an isolated environment.

To make sure you have all the required dependancies installed, execute:

```
pip install -r requirements.txt
```

## Preparing the file

To prepare the file for the bot to read, edit the `ver` variable inside of `pre_parsing.py` to the latest current
version, paste the `N.js` file in from the `.asar` folder into the root directory and finally run `pre_parsing.py`.
This should create a new text file inside the `codefiles` directory for the bot to read.

## Running the tool

To run the tool, simply execute the following command in the main directory:

```
python -m main
```

If successful, you should get an output that looks similar to this:

> {'NothingERROR', 'aError', 'aRecipe', 'dExpOrb', 'aTalentBook'}