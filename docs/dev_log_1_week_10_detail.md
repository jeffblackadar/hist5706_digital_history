---
tutorial: Mesa ABM with Python
date: 2021 Nov 21
tags: hist5706, Mesa, Python
---

# Devlog Week 10 Details

I had problems scaling the model using the http server. I'm going to see if I can render a larger model using an image.

First I am making the model run text only, like below, using server_image.py

```
required_charcoal_loads_per_year:  4
Year:  0
total cut:  16
Year:  1
total cut:  32
Year:  2
total cut:  48
```
I had the width, height mixed up
self.grid = HexGridMulti(width, height, torus=False)