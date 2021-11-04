from mesa.visualization.modules import CanvasHexGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from mesa.visualization.UserParam import UserSettableParameter

from charcoal.portrayal import portrayCell
from charcoal.model import CharcoalMap

width, height = 19, 19

# Make a world that is 19x19, on a 500x500 display.
canvas_element = CanvasHexGrid(portrayCell, width, height, 500, 500)

chart = ChartModule([{"Label": "Cut",
                      "Color": "Black"},
                      {"Label": "Age",
                      "Color": "Green"}
                      ],
                    data_collector_name='datacollector')

model_params = {
    "height": height,
    "width": width,
    "max_cut": UserSettableParameter("slider", "Cells cut per year", 5, 1, 20),
    "mill_radius": UserSettableParameter("slider", "Radius of cut area", 6 , 1, 9),
    "forest_age_maturity": UserSettableParameter("slider", "Age the forest becomes mature", 40, 20, 100),
}

server = ModularServer(
   CharcoalMap, [canvas_element, chart], "Charcoal Map", model_params
)


