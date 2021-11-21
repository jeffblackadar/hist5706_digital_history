from mesa import Agent
from datetime import datetime



class Mill(Agent): # The mill cuts the wood of neighbouring forest cells if they are mature.
    """
    The saw mill is at the center of the map.
    When the mill's loggers cut down the forest in a neighbouring cell, that cell's forest's age becomes 0 and is not mature. 
    For the mill to stay running, it needs to harvest a set number of mature forest cells each year. If the mill fails to harvest enough forest cells, the mill closes and its state changes to 0 (stopped/closed).    
    
    Attributes:
        See comments below in __init__
    """

    STOPPED = 0
    RUNNING = 1
    MAXCUT=3

    def __init__(self, pos, model, init_state=RUNNING, max_cut=MAXCUT, mill_radius=3):
        """
        Create a mill, in the given state, at the given x, y position.
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
        # +int cells_cut The number of land_cells the mill has cut or harvested
        self.max_cut = max_cut
        # +int max_cut The maximum number of cells cut in a year
        self.mill_radius = mill_radius
        # +int mill_radius The maximum distance from the mill wood is cut
        self.type = "mill"
        # +str type The type of this agent (mill)


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
        Compute if the cell will be dead or alive at the next tick. A dead
        cell will become alive if it has only one neighbor. The state is not
        changed here, but is just computed and stored in self._nextState,
        because our current state may still be necessary for our neighbors
        to calculate their next state.
        Only cells that are considered check their neighbors for performance reasons.
        """
        # assume no state change
        self._nextState = self.state        

        self.cells_cut = 0
        if self.state > 0:
            # change for performance reasons
            # should loop though max_cut times

            print("start Current Time =", datetime.now())
            
            for neighbor in self.neighbors_outer(self.mill_radius):            
            #for neighbor in self.model.grid.__iter__():   
                
                if neighbor.isForestMature() == True:
                    neighbor._nextState = neighbor.FORESTYOUNG
                    neighbor.state = neighbor.FORESTCUT
                    neighbor.forest_age = 0
                    neighbor.setColor()
                    neighbor.isConsidered = True
                    self.cells_cut = self.cells_cut + 1
                    if self.cells_cut >= self.max_cut:
                        break
            print("end Current Time =", datetime.now())
        # Did mill harvest enough?            
        if self.cells_cut < self.max_cut:
            self._nextState = 0
            print("Mill is out of business!")
            self.color = "grey"

    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState

