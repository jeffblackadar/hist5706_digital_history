from mesa import Agent


class Mill(Agent):
    STOPPED = 0
    RUNNING = 1
    MAXCUT=3

    def __init__(self, pos, model, init_state=RUNNING, max_cut=MAXCUT, mill_radius=3):
        """
        Create a mill, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.x, self.y = pos
        self.state = init_state
        self._nextState = None
        self.isConsidered = False
        self.color = "black"
        self.cells_cut = 0
        self.max_cut = max_cut
        self.mill_radius = mill_radius
        self.type = "mill"


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
        When a cell is made alive, its neighbors are able to be considered in the next step. Only cells that are considered check their neighbors for performance reasons.
        """
        # assume no state change
        self._nextState = self.state
        

        self.cells_cut = 0
        if self.state > 0:
            for neighbor in self.neighbors_outer(self.mill_radius):
                if neighbor.isForestMature() == True:
                    neighbor._nextState = neighbor.FORESTCUT
                    neighbor.forest_age = 0
                    neighbor.isConsidered = True
                    self.cells_cut = self.cells_cut + 1
                    if self.cells_cut >= self.max_cut:
                        break
        # Did mill harvest enough            
        if self.cells_cut < self.max_cut:
            self._nextState = 0
            print("Mill is out of business!")
            self.color = "grey"




    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState
