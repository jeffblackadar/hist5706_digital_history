from comment_parser import comment_parser

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
                write_f.write('    class ' + class_name + '\n')
            if(line_strip[:4] =="def " and str(class_name)!=""):
                method_name = line_strip[4:-1].strip()
                write_f.write(class_name + " : +" + method_name + '\n')
            if(line_strip[:1]=="#" and (line_strip.find('int ')>0 or line_strip.find('bool ')>0 or line_strip.find('object ')>0) and str(class_name)!=""):
                write_f.write(class_name + " : " + line_strip[line_strip.find('#')+1:]+'\n')
    read_f.close
    write_f.write('        </div>\n')

write_f = open("C:\\Users\\jblackad\\mesa\\src\\mesa\\hist5706_digital_history\\charcoal\\doc.html", "w")
write_f.write('\n')
write_f.write('<html>\n')
write_f.write('  <body>\n')
write_f.write('    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>\n')
write_f.write('    <script>mermaid.initialize({startOnLoad:true});</script>\n')


process_class('C:\\Users\\jblackad\\mesa\\src\\mesa\\hist5706_digital_history\\charcoal\\mill.py', write_f)
process_class('C:\\Users\\jblackad\\mesa\\src\\mesa\\hist5706_digital_history\\charcoal\\landcell.py', write_f)
process_class('C:\\Users\\jblackad\\mesa\\src\\mesa\\hist5706_digital_history\\charcoal\\model.py', write_f)

"""
    class BankAccount
    BankAccount : +String owner
    BankAccount : +Bigdecimal balance
    BankAccount : +deposit(amount)
    BankAccount : +withdrawl(amount)
"""






write_f.write('  </body>\n')
write_f.write('</html>\n')
write_f.close
"""
<html>
  <body>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true});</script>
"""