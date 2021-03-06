from mesa import Agent

class CharcoalHearth(Agent):
    """ 
    Represents a single charcoal hearth that is situated in an area of forest (LandCell) in the simulation.

    The charcoal hearth may be in any type of forest and has three states: 
    Active = 1: The meiler is constructed from wood cut in neighboring cell and fired to produce charcoal.
    Relict = 0: A charcoal hearth that was fired previously.
    
    Attributes:
        See comments below in __init__
    """    
    
    ACTIVE = 1
    RELICT = 0

    def __init__(self, pos, model):
        """
        Create a charcoal_hearth, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        
        self.x, self.y = pos
        # +int x position
        # +int y
        self.type = "charcoal_hearth" 
        # +str type The type of this agent (charcoal_hearth)       
        self.unique_id = self.type + ("000"+str(self.x))[-3:]+("000"+str(self.y))[-3:]
        # +str unique_id ex. charcoal_hearth00x00y
        self.state = self.ACTIVE
        # +int state ACTIVE = 1, RELICT = 0
        self._nextState = None
        # +int _nextState The state this will be at the end of a step        
        self.color = "yellow"
        # +str color The color of circular hearth symbol. Changes with setColor()
        self.setColor()      

    def setColor(self):

        if self.state == self.ACTIVE:
            self.color = "yellow"
        else:
            if self.state == self.RELICT:
                self.color = "black"
            else:
                self.color = "pink"

    @property
    def neighbors(self):
        return self.model.grid.neighbor_iter((self.x, self.y))

    def neighbors_outer(self, radius):
        return self.model.grid.iter_neighbors((self.x, self.y),False,radius)   

    @property
    def considered(self):
        return self.isConsidered is True