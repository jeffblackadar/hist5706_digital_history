from mesa.visualization.modules import CanvasHexGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from mesa.visualization.UserParam import UserSettableParameter

from mill.portrayal import portrayCell
from mill.model import MillMap

width, height = 19, 19

# Make a map on a 500x500 display.
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
    "max_cut": UserSettableParameter("slider", "Cells cut per year by mill", 5, 1, 20),
    "mill_radius": UserSettableParameter("slider", "Radius from mill of cut area", 6 , 1, 8),
    "forest_age_maturity": UserSettableParameter("slider", "Age the forest becomes mature", 40, 20, 100),
}

server = ModularServer(
   MillMap, [canvas_element, chart], "Mill Map", model_params
)


