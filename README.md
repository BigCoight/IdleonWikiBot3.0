# IdleonWikiBot3.0
The third iteration of the bot that uploads all gamedata to idleon.info

This project relies heavily on Pydantic base models to validate and parse the spaghetti coming out of the stencyl converter.

To define a new model, create a new class that inherits from IdleonModel with its details, add a new section to the code reader that the data is stored, and create a repository that then parses the data into the class. After running you will then fine the repo exporred as a JSON file under the exported tab
