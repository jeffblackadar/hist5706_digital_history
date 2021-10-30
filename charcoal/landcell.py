from mesa import Agent


class LandCell(Agent):
    """Represents a single ALIVE or DEAD cell in the simulation."""

    DEAD = 0
    ALIVE = 1

    # Hearth state
    NONE=0
    ACTIVE=1
    INACTIVE=2

    # Forest State
    NOTFOREST=0
    FORESTMATURE=1
    FORESTCUT=2
    FORESTYOUNG=3

    #FORESTAGEMATURE = 20


    def __init__(self, pos, model, init_state=FORESTMATURE, init_age=100, init_color="grey"):
        """
        Create a cell, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.x, self.y = pos
        self.state = init_state
        self.forest_age = init_age
        self._nextState = None
        self.isConsidered = False
        self.color = init_color
        self.type = "forest"

    def setColor(self):

        if self.state == self.NOTFOREST:
            self.color = "black"
        else:
            if self.state == self.FORESTMATURE:
                self.color = "darkgreen"
            else:
                if self.state == self.FORESTCUT:
                    self.color = "brown"
                else:
                    if self.state == self.FORESTYOUNG:
                        strhex = hex(230-(round(self.forest_age / self.model.forest_age_maturity * 130)))
                        #print(round(self.forest_age / self.FORESTAGEMATURE))
                        strhex = strhex[2:]
                        #strhex = "lightgreen"
                        #self.color = "00"+strhex+"00"
                        self.color = "#00"+strhex+"00"
                        #print("00"+strhex+"00")
                    else:
                        self.color = "pink"

    @property
    def isForest(self):        
        return self.state > self.NOTFOREST

    def isForestMature(self):
        return self.state == self.FORESTMATURE

    @property
    def neighbors(self):
        return self.model.grid.neighbor_iter((self.x, self.y))

    @property
    def considered(self):
        return self.isConsidered is True

    def step(self):
        """
        The state is not
        changed here, but is just computed and stored in self._nextState,
        because our current state may still be necessary for our neighbors
        to calculate their next state.
        When a cell is made alive, its neighbors are able to be considered in the next step. Only cells that are considered check their neighbors for performance reasons.
        """
        # assume no state change
        self._nextState = self.state
        #self.isConsidered = True
        #print(self.isForestMature())
        #if (not self.isForestMature()) and self.isConsidered:
        #    print("Not mature")
            # Get the neighbors and apply the rules 
            # at the next tick.
        #    for neighbor in self.neighbors:
        #        #if(model.cellsConsumed <= model.MAXCELLS):
        #        if neighbor.isForestMature() == True:
        #            neighbor._nextState = self.FORESTCUT
        #            neighbor.forest_age = 0
        #            neighbor.isConsidered = True
                    # model.cellsConsumed = model.cellsConsumed + 1
                    
                    
        if self.state == self.FORESTCUT:
            self._nextState = self.FORESTYOUNG
            self.forest_age = self.forest_age + 1
        else:
            if self.state == self.FORESTYOUNG:
                self.forest_age = self.forest_age + 1
                if self.forest_age > self.model.forest_age_maturity:
                    self._nextState = self.FORESTMATURE
            else:                     
                if self.state == self.FORESTMATURE:
                    self.forest_age = self.forest_age + 1
        self.setColor()
        #print(self.forest_age)
       
  

    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState
   
