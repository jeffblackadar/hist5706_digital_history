from mesa import Agent
from charcoalproduction.charcoalhearth import CharcoalHearth

class Furnace(Agent): # The furnace consumes charcoal.
    """
    The furnace is at the center of the map.
    When colliers cut down the forest to make charcoal in a neighbouring cell, that cell's forest's age becomes 0 and is not mature. 
        
    Attributes:
        See comments below in __init__
    """

    STOPPED = 0
    RUNNING = 1
    REQLOADS=3
    CELLSFORHEARTH=2

    def __init__(self, pos, model, init_state=RUNNING, required_charcoal_loads_per_year=REQLOADS, cells_cut_for_charcoal_hearth=CELLSFORHEARTH,collection_radius=3):
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
        self.charcoal_loads_produced_this_year = 0
        # +int loads of chancoal produced
        self.required_charcoal_loads_per_year = required_charcoal_loads_per_year
        # +int required_charcoal_loads The required number of loads to operate the furnace
        self.cells_cut_for_charcoal_hearth = cells_cut_for_charcoal_hearth
        # +int cells_cut_for_charcoal_hearth The number of cells of wood required to build a charcoal hearth

        self.collection_radius = collection_radius
        # +int collection_radius The maximum distance from the furnace wood is cut and charcoal is harvested
        self.type = "furnace"
        # +str type The type of this agent (furnace)
        self.charcoal_hearths = []
        # +list charcoal_hearths The list of charcoal hearths surrounding the furnace


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
        # number of charcoal hearths the furnace needs in operation
        #ch_need = 2
        self.charcoal_loads_produced_this_year = 0
        
        # counter of the number of charcoal hearths in operation this step
        ch_built = 0

        # is furnace running?
        if self.state > 0:
            # Check if existing charcoal hearths have enough nearby harvestable wood to make a hearth.
            for ch in self.charcoal_hearths:
                # Check if hearth is relict. Already Built or Fired hearths can't be re-used
                if ch.state == ch.RELICT:
                
                    # find out if there is enough harvestable wood to make charcoal
                    # Make a list of possible harvest cells
                    ch_possible_cut_cells = []
                
                
                    chns = self.model.grid.iter_neighbors((ch.x, ch.y), True,1)

                    for chn in chns:
                        if chn.type == "forest":
                            if chn.isForestMature() == True:
                                ch_possible_cut_cells.append(chn)
                                if(len(ch_possible_cut_cells)>=self.cells_cut_for_charcoal_hearth):
                                    break
                    if(len(ch_possible_cut_cells)>=self.cells_cut_for_charcoal_hearth):
                        # cut the cells
                        for chn in ch_possible_cut_cells:
                            chn._nextState = chn.FORESTYOUNG
                            chn.state = chn.FORESTCUT
                            chn.forest_age = 0
                            chn.setColor()
                            chn.isConsidered = True
                            self.cells_cut = self.cells_cut + 1
                        # build the hearth
                        ch.state = ch.BUILT
                        ch.setColor()
                        self.charcoal_loads_produced_this_year = self.charcoal_loads_produced_this_year + 1
                        ch_built = ch_built + 1
                if self.charcoal_loads_produced_this_year >= self.required_charcoal_loads_per_year:
                    break

            # do we need to harvest more from a place with no charcoal hearths?
            if self.charcoal_loads_produced_this_year < self.required_charcoal_loads_per_year:

            # change for performance reasons
            # should loop though max_cut times
                #for neighbor in self.model.grid.__iter__():
                #    print(neighbor[1])
            
                for neighbor in self.neighbors_outer(self.collection_radius):
                #for neighbor in self.model.grid.__iter__(): 
                    print(neighbor)   
                    if neighbor.type == "forest":
                    #if neighbor.isForest() == True:
                        if neighbor.isForestMature() == True:
                            ch_possible_cut_cells = []
                            chns = self.model.grid.iter_neighbors((neighbor.x, neighbor.y), True,1)
                            for chn in chns:
                                if chn.type == "forest":
                                    if chn.isForestMature() == True:
                                        ch_possible_cut_cells.append(chn)
                                        if(len(ch_possible_cut_cells)>=self.cells_cut_for_charcoal_hearth):
                                            print("cut for hearth",len(ch_possible_cut_cells),self.cells_cut_for_charcoal_hearth)
                                            break
                    # Indented twice
                            if(len(ch_possible_cut_cells)>=self.cells_cut_for_charcoal_hearth):
                                charcoal_hearth_present_in_cut_area = False
                                for chn in ch_possible_cut_cells:
                                    chn._nextState = chn.FORESTYOUNG
                                    chn.state = chn.FORESTCUT
                                    chn.forest_age = 0
                                    chn.setColor()
                                    chn.isConsidered = True
                                    self.cells_cut = self.cells_cut + 1
                                # see if there is a hearth, if not set one
                                new_cell_for_charcoal_hearth = 0
                                new_cell_for_charcoal_hearth_neighbor_available = False               
                                for chn in ch_possible_cut_cells:                            
                                    if chn.has_charcoal_hearth == 1:
                                        # only a relict hearth can be rebuilt.  Built or fired hearths can't
                                        if chn.charcoal_hearth.state == chn.charcoal_hearth.RELICT:
                                           # Fire up existing hearth
                                           chn.charcoal_hearth.state = chn.charcoal_hearth.BUILT
                                           chn.charcoal_hearth.setColor()
                                           charcoal_hearth_present_in_cut_area = True
                                           self.charcoal_loads_produced_this_year = self.charcoal_loads_produced_this_year + 1
                                    else:
                                        # try to use the neighbour of the mill as the place to built a hearth, but only if it has no hearth aleady
                                        if neighbor.has_charcoal_hearth == 0:
                                            if neighbor.x == chn.x and neighbor.y == chn.y:
                                                new_cell_for_charcoal_hearth_neighbor_available = True

                                                 
                                        new_cell_for_charcoal_hearth = chn

                                # The neighbor cell is the best choice, if it was found, use it.          
                                if new_cell_for_charcoal_hearth_neighbor_available == True:
                                    new_cell_for_charcoal_hearth = neighbor

                                if charcoal_hearth_present_in_cut_area == False:

                                    charcoal_hearth = CharcoalHearth(new_cell_for_charcoal_hearth.pos, self)
                                    charcoal_hearth.state = charcoal_hearth.BUILT
                                    self.model.grid.place_agent(charcoal_hearth, new_cell_for_charcoal_hearth.pos)
                                    self.model.schedule.add(charcoal_hearth)
                                    new_cell_for_charcoal_hearth.has_charcoal_hearth = 1
                                    new_cell_for_charcoal_hearth.charcoal_hearth = charcoal_hearth
                                    self.charcoal_hearths.append(charcoal_hearth)
                                    self.charcoal_loads_produced_this_year = self.charcoal_loads_produced_this_year + 1
                        # end indented
                    if self.charcoal_loads_produced_this_year >= self.required_charcoal_loads_per_year:
                        break
        # At the end of this year, did furnace harvest enough?            
        if self.charcoal_loads_produced_this_year < self.required_charcoal_loads_per_year:
            self._nextState = 0
            print("Furnace is out of business!")
            self.color = "grey"

    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState

