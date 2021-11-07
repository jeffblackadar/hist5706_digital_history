def portrayAgent(agent):
    """
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the cell in its current state.
    :param cell:  the cell in the simulation
    :return: the portrayal dictionary.
    """
    assert agent is not None
    if agent.type == "forest":
        return {
            "Shape": "hex",
            "r": 1,
            "Filled": "true",
            "Layer": 0,
            "x": agent.x,
            "y": agent.y,
            "Color": agent.color,
            # "text": agent.forest_age,
            "text_color":"Black"
        
        }
    else:
        if agent.type == "furnace":
            return {
                "Shape": "hex",
                "r": 1,
                "Filled": "true",
                "Layer": 0,
                "x": agent.x,
                "y": agent.y,
                "Color": agent.color,
                "text": agent.state_text,
                "text_color":"White"
        }
        else:
            if agent.type == "charcoal_hearth":
                return {
                    "Shape": "circle",
                    "r": 1,
                    "Filled": "true",
                    "Layer": 1,
                    "x": agent.x,
                    "y": agent.y,
                    "Color": agent.color
                }


    