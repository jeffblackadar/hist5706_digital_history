from mesa import Model
from mesa.time import SimultaneousActivation
# changing to HexGridMulti
# from mesa.space import HexGrid
#from charcoalproduction.HexGridMulti import HexGridMulti
from HexGridMulti import HexGridMulti
from HexGridMulti import MultiGrid

from mesa.datacollection import DataCollector

"""
from charcoalproduction.landcell import LandCell
from charcoalproduction.furnace import Furnace
from charcoalproduction.charcoalhearth import CharcoalHearth
"""
from landcell import LandCell
from furnace import Furnace
from charcoalhearth import CharcoalHearth


def compute_total_cut(model):
    return model.total_cut

def compute_furnace_forest_average_age(model):
    furnace_forest = [a for a in model.furnace.neighbors_outer(model.furnace.collection_radius) if a.type == "forest"]

    avg_mfa = sum([a.forest_age for a in furnace_forest]) / len(furnace_forest)
    return avg_mfa

class CharcoalProductionMap(Model):
    """
    # Map:
    Represents the hex grid of cells. The grid is represented by a 2-dimensional array of cells with adjacency rules specific to hexagons.

    # Furnace:
    The furnace is at the center of the map.
    When colliers cut down the forest to make charcoal in a neighbouring cell, that cell's forest's age becomes 0 and is not mature.

    # land Cell:
    Each hexagon represents a single area of forest in the simulation.
    
    The land cell is most often a forest that can be mature (above the age of a mature forest and ready to cut) or young (not read to cut)
    The land cell where the furnace is located is not a forest.
    The age of the forest increases each year and is displayed in the cell. The color of the cell is determined by land cell state or forest age. 
    """
    def add_cell(self, x,y):
        print(x,y)
        land_cell = LandCell((x, y), self)
        self.grid.place_agent(land_cell, (x, y))
        self.schedule.add(land_cell)


    def __init__(self, height=50, width=50, required_charcoal_loads_per_year=2, cells_cut_for_charcoal_hearth=3,collection_radius=3, forest_age_maturity=30, hexgrid = True):
        """
        Create a new playing area of (height, width) cells.
        """

        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.
        self.schedule = SimultaneousActivation(self)
        # +object schedule 
        # Use a hexagonal grid, where edges don't wrap around (it's a map of a part of the earth's surface).
        if hexgrid == False:
            self.grid = MultiGrid(width, height, torus=False)
        else:
            self.grid = HexGridMulti(width, height, torus=False)
        # +object grid HexGrid a grid to represent the map.

        self.forest_age_maturity = forest_age_maturity
        # +int forest_age_maturity the age forest becomes mature and ready to be cut

        self.total_cut = 0
        # +int total_cut the total amount of acres cut

        # Place a land cell at each location.
        
        for (contents, x, y) in self.grid.coord_iter():
            if(not (x==width // 2 and y==height // 2)):
                land_cell = LandCell((x, y), self)
                self.grid.place_agent(land_cell, (x, y))
                self.schedule.add(land_cell)
        """
        # place agents from the center outwards 
        center_y = height // 2
        center_x = width // 2

        y_plus = center_y 
        y_minus = center_y 
        x_plus = center_x
        x_minus = center_x 

        while y_plus < height or y_minus >= 0 or x_plus < width or x_minus >= 0:

            y_plus = y_plus + 1
            y_minus = y_minus - 1
            x_plus = x_plus + 1
            x_minus = x_minus - 1
            print(y_minus, y_plus,x_minus, x_plus)
            
            if y_minus >= 0:                
                x_low = x_minus
                if x_minus < 0:
                    x_low = 0
                x_high = x_plus +1
                if x_high > width:
                    x_high = width
                for xcounter in range(x_low,x_high):
                    print(1)
                    self.add_cell(xcounter,y_minus)

            if y_plus < height:                
                x_low = x_minus
                if x_minus < 0:
                    x_low = 0
                x_high = x_plus +1
                if x_high > width:
                    x_high = width
                for xcounter in range(x_low,x_high):
                    print(2)
                    self.add_cell(xcounter,y_plus)
            if x_minus >= 0:                
                y_low = y_minus + 1
                if y_low < 0:
                    y_low = 0
                y_high = y_plus 
                if y_high > height:
                    y_high = height
                for ycounter in range(y_low,y_high):
                    print(3)
                    self.add_cell(x_minus,ycounter)
            if x_plus < width:
                y_low = y_minus + 1
                if y_low < 0:
                    y_low = 0
                y_high = y_plus 
                if y_high > height:
                    y_high = height
                for ycounter in range(y_low,y_high):
                    print(4)
                    self.add_cell(x_plus,ycounter)            


                """


        print("required_charcoal_loads_per_year: ",required_charcoal_loads_per_year)
        #self, pos, model, init_state=RUNNING, required_charcoal_loads_per_year=REQLOADS, cells_cut_for_charcoal_hearth=CELLSFORHEARTH,collection_radius=3):
        self.furnace = Furnace((width // 2,height // 2),self,1,required_charcoal_loads_per_year, cells_cut_for_charcoal_hearth, collection_radius)

        self.grid.place_agent(self.furnace, (width // 2, height // 2))
        self.schedule.add(self.furnace)

        self.datacollector = DataCollector(
            model_reporters={
                "Cut": compute_total_cut,
                "Age": compute_furnace_forest_average_age
            },
        )

        self.running = True
        self.datacollector.collect(self)


    def step(self):
        """
        Have the scheduler advance each cell by one step
        """
        print("Year: ", self.schedule.time)
        self.schedule.step()
        #self.cellsConsumed = 0
        self.total_cut = self.total_cut + self.furnace.cells_cut
        print("total cut: ", self.total_cut)
        self.datacollector.collect(self)
