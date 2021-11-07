from mesa.visualization.modules import CanvasHexGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from mesa.visualization.UserParam import UserSettableParameter

from charcoal_production.portrayal import portrayAgent
from charcoal_production.model import CharcoalProductionMap

#from .portrayal import portrayCell
#from .model import CharcoalProductionMap

width, height = 19, 19

# Make a map on a 500x500 display.
canvas_element = CanvasHexGrid(portrayAgent, width, height, 500, 500)

chart = ChartModule([{"Label": "Cut",
                      "Color": "Black"},
                      {"Label": "Age",
                      "Color": "Green"}
                      ],
                    data_collector_name='datacollector')

model_params = {
    "height": height,
    "width": width,
    "max_cut": UserSettableParameter("slider", "Cells cut per year for furnace", 5, 1, 20),
    "collection_radius": UserSettableParameter("slider", "Radius from furnace of cut area", 6 , 1, 8),
    "forest_age_maturity": UserSettableParameter("slider", "Age the forest becomes mature", 40, 20, 100),
}

server = ModularServer(
   CharcoalProductionMap, [canvas_element, chart], "Charcoal Production Map", model_params
)


