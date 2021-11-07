from mesa import Agent



class CharcoalHearth(Agent):
    FIRED = 1
    RELICT = 0

    def __init__(self, pos, model):
        """
        Create a charcoal_hearth, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        
        self.x, self.y = pos
        self.type = "charcoal_hearth"
        print(self.type + (("000"+str(self.x))[:-3])+(("000"+str(self.y))[:-3]))
        self.unique_id = self.type + (("000"+str(self.x))[:-3])+(("000"+str(self.y))[:-3])
        print(self.unique_id)
        self.state = self.FIRED
        self.setColor()      

    def setColor(self):

        if self.state == self.FIRED:
            self.color = "red"
        else:
            if self.state == self.RELICT:
                self.color = "black"

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
                    
        if self.state == self.FIRED:
            self._nextState = self.RELICT
        self.setColor()    
        
    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState