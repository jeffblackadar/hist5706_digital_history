from mesa import Agent



class CharcoalHearth(Agent):
    BUILT = 2
    FIRED = 1
    RELICT = 0

    def __init__(self, pos, model):
        """
        Create a charcoal_hearth, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        
        self.x, self.y = pos
        #print(self.x, self.y)
        self.type = "charcoal_hearth"        
        self.unique_id = self.type + ("000"+str(self.x))[-3:]+("000"+str(self.y))[-3:]
        print(self.unique_id)
        self.state = self.BUILT
        # +int state FIRED = 1, RELICT = 0, BUILT = 2
        self.color = "black"
        # +str color The color of circular hearth symbol. Changes with setColor()
        self.setColor()      

    def setColor(self):

        if self.state == self.FIRED:
            self.color = "yellow"
        else:
            if self.state == self.RELICT:
                self.color = "black"
            else:
                if self.state == self.BUILT:
                    self.color = "darkbrown"
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

    def step(self):
        # assume no state change
        self._nextState = self.state
        
        if self.state == self.BUILT:
            self._nextState = self.FIRED

        if self.state == self.FIRED:
            self._nextState = self.RELICT
        self.setColor()    
        
    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState
        self.setColor()