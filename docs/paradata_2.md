A Slow Burn: Paradata for a Model of Charcoal Production in the Eastern United States.
Jeff Blackadar 100139943
HIST5706F Digital History
Dr.Shawn Graham
December 5, 2021

I have been studying the archaeological evidence of the charcoal making industry that fueled iron production in the eastern United States from its colonial period until the mid-nineteenth century, when it was gradually replaced by bituminous coal. In areas where iron was produced, such as Western Maryland, Pennsylvania, Northern New Jersey, Connecticut, Vermont and Eastern New York State, forested areas contain numerous relict charcoal hearths (RCH) distributed across the landscape.

This project attempts to simulate the work of colliers and loggers who produced charcoal to better understand the pattern of distribution of charcoal hearths and relate that to the archaeological record. A greater understanding of the pattern of construction of charcoal hearths leads to better estimates of historical charcoal production, especially in areas that are now developed where the evidence of RCH has been built or plowed over. This simulation will also explore how work was accomplished in an industry vital to the economic development of the United
States and to better understand the history of its workers.

I use Agent Based Modelling or ABM for this simulation. [[1]](#-ftn1) To perform ABM I considered three options: [NetLogo](https://ccl.northwestern.edu/netlogo/), an ABM written in Java with its own modelling language with the same name; [Hash.ai](https://hash.ai/), an ABM on-line platform and Mesa, an ABM framework for Python. [[2]](#-ftn2) I wanted ABM software that was extensible, open and portable, so I ruled out Hash.ai since it required users to store models on its platform. I chose Mesa because its Python code seemed more readily extensible than Netlogo 's Java application. I prefer using Python, which has an established and large user base with historians, rather than using NetLogo, which, while being a well-established language for ABM, appears to have a smaller community of users overall.

I hoped to program and use models on Google Collaboratory since it has Python already installed. However, early in my work with Mesa, I saw Mesa 's web visualization would not work on Google Colab. Instead, I made the model work on a personal computer. I programmed it on a PC and tested it on both a PC and a Chromebook. I first made a simple model of a lumber mill to test concepts and develop my knowledge before modelling an iron furnace 's charcoal consumption.

Using Mesa, two dimensional models are stored in grids of (x,y) coordinates. Grids can be visualized as squares or hexagons. I chose hexagons because they seem to visually represent a pattern of logging where cut wood would be brought to centralized points, better than squares.

Each hexagon represents an area. Early in the development of the model, I considered specifying the dimensions of the hexagon where, for example, each would be 100 feet wide to easily
reflect the distances colliers would walk from their huts to maintain a group of charcoal hearths.

Based on reading Victor Rolando 's article  "19th-Century Charcoal Production in Vermont " and sections of Robert Gordon 's, _American Iron, 1607-1900_, this model equates the amount of wood cut on an acre of forest being equal to the amount of wood required to build a single charcoal hearth meiler, or pile. In the model each hexagon has an area of 1 acre. [[3]](#-ftn3) An acre of trees produced 30 cords of charcoal wood on average and 30 cords were required to build a typical meiler. [[4]](#-ftn4) This simplifies the visualization of a model. If a furnace held 12,000 acres of forest, it would be represented by an equal number of hexagons. A cutting cycle of 20 years would consume 600 acres of woodland annually. [[5]](#-ftn5)

Since equating an acre of wood production to the amount required to construct a meiler is fundamental to the model, I tested this. Gordon cites an example of a woodland producing 20 cords an acre in Connecticut. [[6]](#-ftn6) David Marquis, in his article  "Clearcutting in Northern Hardwood: Results after 30 Years ", notes an acre of old growth forest in New Jersey produced 60 cords of split wood per acre when cut in the 1930 's. [[7]](#-ftn7) My calculation using Marquis ' table of tree regrowth 25 years after clearcutting multiplied by the amount of firewood produced per tree according to Marshall Patmos ' document  "Estimating Firewood from Standing Trees " was only 7.3 cords of wood after 25 years. [[8]](#-ftn8) As a result of this, I questioned whether the basis of my model is wrong. However, my calculation of 7.3 cords of
wood per acre is based on a table to calculate the amount of firewood, not charcoal a tree produces. Checking Patmos ' source of S. R. Gevorkiantz and L. P Olsen 's  "Composite Volume Tables for Timber and Their Application in the Lake States" showed the authors considered only wood above 4 inches in diameter in their volume calculations. [[9]](#-ftn9) Lapwood, the smaller pieces of wood used to fill spaces in a meiler, was as thin as 3.8 cm (1.5 inches) in diameter [[10]](#-ftn10).

I was calculating a volume of wood for each tree that was too low. I also used a source that measured the number of trees growing after 25 years on a clear-cut in New Jersey. It is possible that the more intensive methods to clear-cut forests in the mid-twentieth century inhibited the regeneration of trees more so than clearing with an axe in earlier centuries, as damaging to forests as that also was. It is likely loggers using axes left trees to grow that were smaller than 3.8 cm (1.5 inches) in diameter. Also, coppicing of hardwood trees would have been practiced rather than a full clear cut. On the other hand, an argument in favour of a lower volume is Marquis' graph is for tree regeneration after 25 years, not just 20 years as practiced by some furnaces. What is clear is that there is great variation in the amount of wood produced by an acre. While 30 cords per acre is a usable figure for a model, this number is likely high for less productive forests or forests degraded after repeated cycles of cutting. To reflect this uncertainly and variability the model has a parameter for number of cells cut per charcoal hearth. This can be set to a higher value to reflect relatively unproductive forests and large meilers or set as small as one cell of wood required per meiler. Finally, the idea that each cell is an acre can be rethought to consider this uncertainty. A cell may be thought of as half an acre or a certain width, such as 30 meters, for example. The number of cells required to construct a charcoal hearth can be adjusted to a model with hexagons of different sized areas.

Each step for the model is a year and charcoal making happened over a season of each year. Gordon writes that colliers preferred to work during the summer with dry weather and a lack of wind. [[11]](#-ftn11) Rolondo states that colliers worked from then end of the winter to the start of the next, which in Vermont 's Green Mountains at that time may be a shorter period than at first thought. [[12]](#-ftn12) If the construction of a meiler took 1 week, burning 1-2 more with a further week to rake out charcoal, let it cool and load it in a wagon, it is probable that the
same site was used more than once in a year, if sufficient wood was nearby to build another meiler. [[13]](#-ftn13) This probability is based on efficiency and evidence charcoal hearths were reused. Building a site for a charcoal hearth requires leveling the site which is labour intensive in a hilly area with tree stumps. This work would be done only if necessary and with consideration that the transporting wood to a charcoal hearth is also labour intensive or may
require teamsters to haul the wood, increasing the cost of production. New charcoal hearths would have been built near available wood rather than hauling logs a long distance to an existing charcoal hearth. Colliers needed to pay close attention when making charcoal so they would need to be nearby to check a hearth frequently. They often tended more than one hearth at a time in order to maximize the productivity of their labour. [[14]](#-ftn14) The model's parameter  "Radius from charcoal hearth of cut area " is used to simulate how far wood would be hauled to construct a meiler.

The questions the model examines are how far away were charcoal hearths from one another considering the factors of construction effort, transportation and travel distance of the
collier between hearths? How did these factors determine the pattern of construction of charcoal hearths? How does the model 's patterns compare to the archaeological record? The model is now in a state the allows simulation using parameters to explore these questions further. The model's [documentation](https://jeffblackadar.github.io/hist5706_digital_history/doc_charcoalproduction.html) provides more detail about its function.

## References

### Books

Gevorkiantz , S. R, and L. P Olsen. _Composite Volume Tables for Timber and Their Application in the Lake States_.
Washington, DC: U.S. Government Printing Office, 1955. [https://naldc.nal.usda.gov/download/CAT86201093/PDF](https://naldc.nal.usda.gov/download/CAT86201093/PDF).

Gordon, Robert B. _American Iron, 1607-1900_. Baltimore: Johns Hopkins University Press, 2001. [https://muse.jhu.edu/book/72153/pdf](https://muse.jhu.edu/book/72153/pdf).

Graham, Shawn. _An Enchantment of Digital Archaeology: Raising the Dead with Agent-Based Models, Archaeogaming and Artificial Intelligence_. New York: Berghahn Books, 2020.

Graham, Shawn, Neha Gupta, Jolene Smith, Andreas Angourakis, Andrew Reinhard, Kate Ellenberger, Zack Batist, Joel Rivard, Ben Marwick, Michael Carter, Beth Compton, Rob Blades, Cristina Wood, and Gary Nobles. _The Open Digital Archaeology Textbook_. [https://o-date.github.io/draft/book/index.html](https://o-date.github.io/draft/book/index.html).

Kemper, Jackson. _American Charcoal Making in the Era of the Cold-Blast Furnace_. Washington, D.C.: U.S. Department of the Interior; National Park Service, 1941. [https://www.nps.gov/parkhistory/online_books/popular/14/index.htm](https://www.nps.gov/parkhistory/online_books/popular/14/index.htm).

Marquis, David A and Northeastern Forest Experiment Station. _Clearcutting in Northern Hardwood: Results after 30 Years_. Upper Darby, Pa: Northeastern Forest Experiment Station, 1967. [https://www.fs.fed.us/ne/newtown_square/publications/research_papers/pdfs/scanned/rp85.pdf](https://www.fs.fed.us/ne/newtown_square/publications/research_papers/pdfs/scanned/rp85.pdf).

Romanowska , Iza, Colin D Wren, and Stefani A Crabtree. _Agent-Based Modeling for Archaeology: Simulating the Complexity of Societies_. Santa Fe: Santa Fe Institute Press, 2021.

### Journal Articles

Carter, Benjamin P., Jeff H. Blackadar, and Weston L. A. Conner.  "When Computers Dream of Charcoal: Using Deep Learning, Open Tools, and Open Data to Identify Relict Charcoal Hearths in
and around State Game Lands in Pennsylvania. " Advances in Archaeological Practice 9, no. 4 (November 2021): 257-71. [https://doi.org/10.1017/aap.2021.17](https://doi.org/10.1017/aap.2021.17).

Rolando, Victor R.  "19th-Century Charcoal Production in Vermont. " IA. The Journal of the Society for Industrial Archeology 17, no. 2 (1991): 15-36.

Walker, Joseph E.  "A Comparison of Negro and White Labor in a Charcoal Iron Community. " Labor History 10, no. 3 (June 1, 1969): 487-97. [https://doi.org/10.1080/00236566908584090](https://doi.org/10.1080/00236566908584090).

### Websites

Patmos, Marshall.  "Estimating Firewood from Standing Trees. " Educational. University of New Hampshire Cooperative Extension, January 2005, Accessed December 5, 2021. [https://extension.unh.edu/sites/default/files/migrated_unmanaged_files/Resource001044_Rep1200.pdf](https://extension.unh.edu/sites/default/files/migrated_unmanaged_files/Resource001044_Rep1200.pdf).

United States National Parks Service.  "Catoctin Iron Furnace - Catoctin Mountain Park (U.S. National Park Service)." Accessed November 28, 2021. [https://www.nps.gov/cato/learn/historyculture/furnace.htm](https://www.nps.gov/cato/learn/historyculture/furnace.htm).<br>

United States National Parks Service. "Hopewell Furnace National Historic Site (U.S. National Park Service)." Accessed November 28, 2021. [https://www.nps.gov/hofu/index.htm](https://www.nps.gov/hofu/index.htm).

Stack Overflow.  "Stack Overflow - Where Developers Learn, Share, & Build Careers." Accessed November 28, 2021. [https://stackoverflow.com/](https://stackoverflow.com/).

"Acre. " In Wikipedia, October 26, 2021. Accessed December 5, 2021. [https://en.wikipedia.org/w/index.php?title=Acre&oldid=1051863271](https://en.wikipedia.org/w/index.php?title=Acre&oldid=1051863271).

"Hexagon. " In Wikipedia, November 29, 2021. Accessed December 5, 2021. [https://en.wikipedia.org/w/index.php?title=Hexagon&oldid=1057674429](https://en.wikipedia.org/w/index.php?title=Hexagon&oldid=1057674429).

### Software

Kazil , Jackie, David Masad and Andrew Crooks. Mesa: Agent-Based Modeling in Python 3+. Python. 2014. Reprint, Project Mesa, 2021. [https://github.com/projectmesa/mesa/blob/ab3cec5b788104d2dad6f27434f1fadfb8a7452f/CITATION.bib](https://github.com/projectmesa/mesa/blob/ab3cec5b788104d2dad6f27434f1fadfb8a7452f/CITATION.bib).

Sveidqvist , Knut. Mermaid. [https://github.com/mermaid-js/mermaid](https://github.com/mermaid-js/mermaid).

Van Rossum, G., & Drake, F. L. _Python 3 Reference Manual_. Scotts Valley, CA: CreateSpace, 2009.

"Visual Studio Code - Code Editing. Redefined." [https://code.visualstudio.com/](https://code.visualstudio.com/).


***

[[1]](#-ftnref1)Shawn Graham, _An Enchantment of Digital Archaeology: Raising the Dead with Agent-Based Models,Archaeogamingand Artificial Intelligence_ (New York: Berghahn
Books, 2020). The idea to use ABM came from this book.

[[2]](#-ftnref2) Jackie Kazil, David Masad and Andrew Crooks. Mesa: Agent-Based Modeling in Python 3+. Python. 2014. Reprint, Project Mesa, 2021. [https://github.com/projectmesa/mesa/blob/ab3cec5b788104d2dad6f27434f1fadfb8a7452f/CITATION.bib](https://github.com/projectmesa/mesa/blob/ab3cec5b788104d2dad6f27434f1fadfb8a7452f/CITATION.bib).

[[3]](#-ftnref3) Victor R. Rolando,  "19th-Century Charcoal Production in Vermont, " IA. The Journal of the Society for Industrial Archeology 17, no. 2 (1991): 15-16.

Robert B. Gordon, _American Iron, 1607-1900_(Baltimore: Johns Hopkins University
Press, 2019), 40, [https://muse.jhu.edu/book/72153/pdf](https://muse.jhu.edu/book/72153/pdf).

[[4]](#-ftnref4) Rolando,  "19th-Century Charcoal Production in Vermont, " 18. "A mound of these dimensions used 30 cords of wood, the equivalent of a one-acre woodlot."

[[5]](#-ftnref5) Gordon, _American Iron_, 40.

[[6]](#-ftnref6) Gordon, _American Iron_, 40.

[[7]](#-ftnref7) David A Marquis and Northeastern Forest Experiment Station, _Clearcutting in Northern Hardwood: Results after 30 Years_ (Upper Darby, Pa: Northeastern Forest Experiment Station, 1967), 2, [https://www.fs.fed.us/ne/newtown_square/publications/research_papers/pdfs/scanned/rp85.pdf](https://www.fs.fed.us/ne/newtown_square/publications/research_papers/pdfs/scanned/rp85.pdf).

[[8]](#-ftnref8) Marquis, _Clearcutting in Northern Hardwood_, 7.

Marshall Patmos,  "Estimating Firewood from Standing Trees, " Educational, University of New Hampshire Cooperative Extension, January 2005, Accessed December 5, 2021, [https://extension.unh.edu/sites/default/files/migrated_unmanaged_files/Resource001044_Rep1200.pdf](https://extension.unh.edu/sites/default/files/migrated_unmanaged_files/Resource001044_Rep1200.pdf).

My calculation is here: [https://github.com/jeffblackadar/hist5706_digital_history/blob/main/charcoalhearth_paradata_workbook.ipynb](https://github.com/jeffblackadar/hist5706_digital_history/blob/main/charcoalhearth_paradata_workbook.ipynb).

[[9]](#-ftnref9) S. R. Gevorkiantz and L. P. Olsen, _Composite Volume Tables for Timber and Their Application in the Lake States_ (Washington, DC: U.S. Government Printing Office, 1955), 7,
[https://naldc.nal.usda.gov/download/CAT86201093/PDF](https://naldc.nal.usda.gov/download/CAT86201093/PDF).

Gevorkiantz and Olsen 's Table 4 measures cord volume to a variable  "top diameter inside bark of not less than 4.0 inches."

[[10]](#-ftnref10) Jackson Kemper, _American Charcoal Making in the Era of the Cold-Blast Furnace_ (Washington, D.C.: U.S. Department of the Interior; National Park Service, 1941), 10, [https://www.nps.gov/parkhistory/online_books/popular/14/index.htm](https://www.nps.gov/parkhistory/online_books/popular/14/index.htm).

[[11]](#-ftnref11) Gordon, <i>American
Iron</i>, 34.

[[12]](#-ftnref12) Rolando,  "19th-Century Charcoal
Production in Vermont, " 18.

[[13]](#-ftnref13) Rolando,  "19th-Century Charcoal
Production in Vermont, " 18.

Gordon,
<i>American Iron</i>, 35.

Kemper,
<i>American Charcoal Making</i>, 22.

Charcoal
burning took between 1-2 weeks. Raking our charcoal was a tedious task due to the
risk of fire.

[[14]](#-ftnref14) Gordon, <i>American
Iron</i>, 36.
