# Documenter
# Extracts comments from selected classes
# Formats comments into class diagrams in markdown/html using Mermaid
# https://mermaid-js.github.io/mermaid/#/classDiagram


from model import CharcoalProductionMap
from furnace import Furnace
from landcell import LandCell
from charcoalhearth import CharcoalHearth
import os
thisdir = os.path.dirname(__file__)


def process_class(py_file, write_f):
    write_f.write('        <div class="mermaid">\n')
    write_f.write('classDiagram\n')
    class_name = ""
    with open(py_file) as read_f:
        for line in read_f:
            # print(line)
            line_strip = line.strip()
            if(line_strip[:5] =="class"):
                class_name = line_strip[6:line_strip.find('(')].strip()
                class_text = line_strip[6:].strip()
                write_f.write('    class ' + class_name + '\n')
            if(line_strip[:4] =="def " and str(class_name)!=""):
                method_name = line_strip[4:-1].strip()
                write_f.write(class_name + " : +" + method_name + '\n')
            if(line_strip[:1]=="#" and (line_strip.find('int ')>0 or line_strip.find('bool ')>0 or line_strip.find('object ')>0) and str(class_name)!=""):
                write_f.write(class_name + " : " + line_strip[line_strip.find('#')+1:]+'\n')
    read_f.close
    write_f.write('        </div>\n')

def include_html_file(web_file, write_f):
    with open(web_file) as read_f:
        line_count = 0
        for line in read_f:
            line_count = line_count + 1
            if line_count > 4:
                line_strip = line.strip()
                write_f.write(line_strip +'\n')
    read_f.close
    write_f.write('        </div>\n')

write_f = open("C:\\Users\\jblackad\\mesa\\src\\mesa\\hist5706_digital_history\\docs\\doc_charcoalproduction.html", "w")
write_f.write('\n')
write_f.write('<html>\n')
write_f.write('  <body>\n')
write_f.write('    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>\n')
write_f.write('    <script>mermaid.initialize({startOnLoad:true});</script>\n')
write_f.write('<h1>Charcoal Production Model</h1>\n')
write_f.write('<h2>Model: CharcoalProductionMap class</h2>\n')
write_f.write((CharcoalProductionMap.__doc__).replace('#',"</p>"))
process_class(os.path.join(thisdir,'model.py'), write_f)

write_f.write('<h2>Agent: Furnace class</h2>\n')
write_f.write((Furnace.__doc__).replace('#',"</p>"))
process_class(os.path.join(thisdir,'furnace.py'), write_f)
include_html_file(os.path.join(thisdir, '..','docs','doc_furnace.html'), write_f)

write_f.write('<h2>Agent: LandCell class</h2>\n')
write_f.write((LandCell.__doc__).replace('#',"</p>"))
process_class(os.path.join(thisdir,'landcell.py'), write_f)
include_html_file(os.path.join(thisdir, '..','docs','doc_landcell.html'), write_f)

write_f.write('<h2>Agent: CharcoalHearth class</h2>\n')
write_f.write((CharcoalHearth.__doc__).replace('#',"</p>"))
process_class(os.path.join(thisdir,'charcoalhearth.py'), write_f)
include_html_file(os.path.join(thisdir, '..','docs','doc_charcoalhearth.html'), write_f)

write_f.write('<hr>Back to <a href="https://jeffblackadar.github.io/hist5706_digital_history/">Documentation page</a>.')
write_f.write('  </body>\n')
write_f.write('</html>\n')
write_f.close
