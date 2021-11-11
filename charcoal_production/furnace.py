from mesa import Agent
from charcoal_production.charcoal_hearth import CharcoalHearth

class Furnace(Agent): # The furnace consumes charcoal.
    """
    The furnace is at the center of the map.
    When colliers cut down the forest to make charcoal in a neighbouring cell, that cell's forest's age becomes 0 and is not mature. 
        
    Attributes:
        See comments below in __init__
    """

    STOPPED = 0
    RUNNING = 1
    MAXCUT=3

    def __init__(self, pos, model, init_state=RUNNING, max_cut=MAXCUT, collection_radius=3):
        """
        Create a furnace, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.x, self.y = pos
        # +int x position
        # +int y
        self.state = init_state
        # +int state 1=running 0=stopped/closed
        self._nextState = None
        # +int _nextState The state this will be at the end of a step
        self.isConsidered = False
        # +bool isConsidered Determines if this is considered for processing.
        self.color = "black"
        # +str color The background color of the cell
        self.cells_cut = 0
        # +int cells_cut The number of land_cells the furnace has cut or harvested
        self.max_cut = max_cut
        # +int max_cut The maximum number of cells cut in a year
        self.collection_radius = collection_radius
        # +int collection_radius The maximum distance from the furnace wood is cut and charcoal is harvested
        self.type = "furnace"
        # +str type The type of this agent (furnace)


    @property
    def neighbors(self):
        return self.model.grid.neighbor_iter((self.x, self.y))


    def neighbors_outer(self, radius):
        return self.model.grid.iter_neighbors((self.x, self.y),False,radius)       
    
    @property
    def state_text(self):
        if self.state == self.RUNNING:
            return "Running"
        else:
            return "Closed"

    @property
    def considered(self):
        return self.isConsidered is True

    def step(self):
        """
        Only cells that are considered check their neighbors for performance reasons.
        """
        # assume no state change
        self._nextState = self.state        

        self.cells_cut = 0
        if self.state > 0:
            # change for performance reasons
            # should loop though max_cut times
            for neighbor in self.neighbors_outer(self.collection_radius):
                if neighbor.type == "forest":
                    if neighbor.isForestMature() == True:
                        neighbor._nextState = neighbor.FORESTYOUNG
                        neighbor.state = neighbor.FORESTCUT
                        neighbor.forest_age = 0
                        neighbor.setColor()
                        neighbor.isConsidered = True
                        self.cells_cut = self.cells_cut + 1

                        if neighbor.has_charcoal_hearth == 1:
                            # Fire up existing hearth
                            neighbor.charcoal_hearth.state = neighbor.charcoal_hearth.BUILT
                            neighbor.charcoal_hearth.setColor()                            
                        else:
                            charcoal_hearth = CharcoalHearth(neighbor.pos, self)
                            self.model.grid.place_agent(charcoal_hearth, neighbor.pos)
                            self.model.schedule.add(charcoal_hearth)
                            neighbor.has_charcoal_hearth = 1
                            neighbor.charcoal_hearth = charcoal_hearth
                        if self.cells_cut >= self.max_cut:
                            break
        # Did furnace harvest enough?            
        if self.cells_cut < self.max_cut:
            self._nextState = 0
            print("Furnace is out of business!")
            self.color = "grey"

    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState

