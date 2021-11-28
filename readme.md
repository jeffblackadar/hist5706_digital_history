# Mesa model of charcoal production

Agent based modeling of the manufacturing of charcoal in forested areas of the eastern United States. There will be two models:

+ Mill model, a simple model of a saw mill that is a prototype.
+ Charcoal production model

## Documentation

[Documentation](https://jeffblackadar.github.io/hist5706_digital_history/)

## Installation

### 0. Requirements

This simulation requires Python to be installed on a machine that can launch a local http server. This does not work on Google Colaboratory, unfortunately.

### 1. Install Mesa

See the Installation section in this [tutorial](https://mesa.readthedocs.io/en/stable/tutorials/intro_tutorial.html#installation).

### 2. Clone this repository

+ Make a directory
+ git init .
+ git pull https://github.com/jeffblackadar/hist5706_digital_history.git

# Models

There are two models, mill and charcoal production.

## Mill model

This is a prototype model meant try out Mesa and build a basic model of consumption of wood in a forested area.

[Class diagram](https://jeffblackadar.github.io/hist5706_digital_history/doc_mill.html)

### Running the Mill model

python run_mill.py

## CharoalProduction model
This is a model of chacoal production for an iron furnace in the Eastern United States during the 18th to mid-19th centuries.

[Class diagram](https://jeffblackadar.github.io/hist5706_digital_history/doc_charcoalproduction.html)

### Running the CharoalProduction model

+ change directory to /charcoalproduction
+ python run_charcoalproduction.py

### Other programs

+ server.py - Instantiates the model and sets its size. Change the size of the model here.
+ For model.py, furnace.py, landcell.py, charcoalhearth.py see the [model class documentation](https://jeffblackadar.github.io/hist5706_digital_history/doc_charcoalproduction.html)
+ portrayal.py - Contains information to render the classes in the html visualization.

#### Mesa Class addition
+ HexGridMulti.py - HexGridMulti is an additional class added to the Mesa grid classes so that cells in a Hexagon grid may contain more than 1 agemt at time.

#### Utilities
 
+ run_iron_p.py, + server_image.py - Run a simple image based simulation. This is a prototype that was abandoned.
+ documenter_charcoalproduction.py - Creates an html page of documentation of the classes using Mermaid.
+ model_init_image.py - A prototype of logic to add agents in order from the center of a grid outwards.
+ workbook.ipynb - Contains calculations to inform the model's paradata.
+ charcoalhearth_paradata_workbook - Also contains calculations to inform the model's paradata. (These two will be merged.)





