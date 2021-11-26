from mesa.visualization.modules import CanvasHexGrid

# for set up as a rectangular grid
# from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from mesa.visualization.UserParam import UserSettableParameter

#from charcoalproduction.portrayal import portrayAgent
#from charcoalproduction.model import CharcoalProductionMap
from portrayal import portrayAgent
from model import CharcoalProductionMap


#from .portrayal import portrayCell
#from .model import CharcoalProductionMap

width, height = 3, 3

# Make a map on a 500x500 display.
canvas_element = CanvasHexGrid(portrayAgent, width, height, 90, 90)

# for set up as a rectangular grid
#canvas_element = CanvasGrid(portrayAgent, width, height, 600, 600)

chart = ChartModule([{"Label": "Cut",
                      "Color": "Black"},
                      {"Label": "Age",
                      "Color": "Green"}
                      ],
                    data_collector_name='datacollector')

model_params = {
    "height": height,
    "width": width,
    "required_charcoal_loads_per_year": UserSettableParameter("slider", "Required number of loads of charcoal to run furnace each year", 20, 1, 40),
    "cells_cut_for_charcoal_hearth": UserSettableParameter("slider", "Acres cut to supply a charcoal hearth for a season", 4, 1, 5),
    "collection_radius": UserSettableParameter("slider", "Radius from charcoal hearth of cut area", 3, 1, 5),
    "forest_age_maturity": UserSettableParameter("slider", "Age the forest becomes mature", 20, 20, 100),
}
#default, min_value, max_value
server = ModularServer(
   CharcoalProductionMap, [canvas_element, chart], "Charcoal Production Map", model_params
)

server.launch()
