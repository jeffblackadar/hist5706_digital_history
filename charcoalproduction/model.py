from mesa import Model
from mesa.time import SimultaneousActivation
# changing to HexGridMulti
# from mesa.space import HexGrid
from charcoalproduction.HexGridMulti import HexGridMulti

from mesa.datacollection import DataCollector
from charcoalproduction.landcell import LandCell
from charcoalproduction.furnace import Furnace
from charcoalproduction.charcoalhearth import CharcoalHearth

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
    

    def __init__(self, height=100, width=120, required_charcoal_loads_per_year=2, cells_cut_for_charcoal_hearth=3,collection_radius=3, forest_age_maturity=30):
        """
        Create a new playing area of (height, width) cells.
        """

        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.
        self.schedule = SimultaneousActivation(self)

        # Use a hexagonal grid, where edges don't wrap around (it's a map of a part of the earth's surface).
        self.grid = HexGridMulti(height, width, torus=False)
        #+object grid HexGrid a grid to represent the map.

        #self.cellsConsumed = 0
        self.forest_age_maturity = forest_age_maturity
        self.total_cut = 0

        # Place a dead cell at each location.
        for (contents, x, y) in self.grid.coord_iter():
            if(not (x==width // 2 and y==height // 2)):
                land_cell = LandCell((x, y), self)
                self.grid.place_agent(land_cell, (x, y))
                self.schedule.add(land_cell)

        # activate the center(ish) cell.
        #centerishCell = self.grid[width // 2][height // 2]

        #centerishCell.state = 0
        #centerishCell.setColor()
        #for a in centerishCell.neighbors:
        #    a.isConsidered = True

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
        self.schedule.step()
        #self.cellsConsumed = 0
        self.total_cut = self.total_cut + self.furnace.cells_cut
        self.datacollector.collect(self)
