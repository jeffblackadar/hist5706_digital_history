def portrayAgent(agent):
    """
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the cell in its current state.
    :param cell:  the cell in the simulation
    :return: the portrayal dictionary.
    """
    assert agent is not None

    if agent is None:
        return

    if agent.type=="forest":
        portrayal = {"Shape": "hex", "r": 1, "Filled": "true", "Layer": 0}
        (x, y) = agent.pos
        portrayal["x"] = x
        portrayal["y"] = y
        portrayal["Color"] = agent.color   

    if agent.type=="furnace":
        portrayal = {"Shape": "hex", "r": 1, "Filled": "true", "Layer": 0}
        (x, y) = agent.pos
        portrayal["x"] = x
        portrayal["y"] = y
        portrayal["Color"] = agent.color 
        portrayal["Color"] = agent.color
        portrayal["text"] = agent.state_text
        portrayal["text_color"] = "White"

    if agent.type=="charcoal_hearth":
        portrayal = {"Shape": "circle", "r": 0.5, "Filled": "false", "Layer": 1}
        (x, y) = agent.pos
        portrayal["x"] = x
        portrayal["y"] = y
        portrayal["Color"] = agent.color     

    return portrayal




    