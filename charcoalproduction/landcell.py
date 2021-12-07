from mesa import Agent

class LandCell(Agent):
    """ 
    Represents a single area of forest in the simulation.

    The land cell is most often a forest that can be mature (above the age of a mature forest and ready to cut) or young (not read to cut)
    The land cell where the furnace is located is not a forest.
    The age of the forest increases each year and is displayed in the cell. The color of the cell is determined by land cell state or forest age.    
    
    Attributes:
        See comments below in __init__
    """

    # Forest State
    NOTFOREST=0
    FORESTMATURE=1
    FORESTCUT=2
    FORESTYOUNG=3

    def __init__(self, pos, model, init_state=FORESTMATURE, init_age=100, init_color="grey"):
        """
        Create a cell, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.x, self.y = pos
        # +int x position
        # +int y
        self.state = init_state
        # +int state 1=running        
        self.forest_age = init_age
        # +int forest_age
        self._nextState = None
        # +int _nextState The state this will be at the end of a step
        self.isConsidered = False
        # +bool isConsidered Determines if this is considered for processing.        
        self.color = init_color        
        # +str color The background color of the cell. Changes with setColor()       
        self.color_number = (0,90,0)
        # +int color decimal number cell
        self.type = "forest"
        # +str type The type of this agent (forest)
        self.charcoal_hearth = 0
        # +object charcoal_hearth This landcell's charcoal hearth, if present
        self.has_charcoal_hearth = 0
        # +bool has_charcoal_hearth This landcell has a charcoal hearth
        self.label = ""
        # +str label The label to be displayed on the visualization

    def setColor(self):

        if self.state == self.NOTFOREST:
            self.color = "black"
            self.color_number = (0,0,0)
            self.label = ""
        else:
            if self.state == self.FORESTMATURE:
                self.color = "darkgreen"
                self.color_number = (0,90,0)
                self.label = "Mature"
            else:
                if self.state == self.FORESTCUT:
                    self.color = "brown"
                    self.color_number = (90,90,0)
                    self.label = "Cut"
                else:
                    if self.state == self.FORESTYOUNG:
                        young_green = 230-(round(self.forest_age / self.model.forest_age_maturity * 130))
                        self.color_number = (0,young_green,0)
                        strhex = hex(young_green)
                        strhex = strhex[2:]
                        self.color = "#00"+strhex+"00"
                        self.label = "Age: "+str(self.forest_age)
                    else:
                        self.color = "pink"

    def getColorNumber(self):
         return self.color_number

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
        Only cells that are considered check their neighbors for performance reasons.
        """
        # assume no state change
        self._nextState = self.state
                    
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

    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState
   
