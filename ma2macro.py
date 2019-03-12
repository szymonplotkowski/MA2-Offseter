#MA 2 MACRO BUILD LIB 4 PYTHON
#Written by Szymon Plotkowski
#szymonplotkowski@gmail.com


def create(filename):
        with open(filename ,"w+") as macro:
            macro.write ('<?xml version="1.0" encoding="utf-8"?>\n')
            macro.write ('<MA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.malighting.de/grandma2/xml/MA" xsi:schemaLocation="http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.4.0/MA.xsd" major_vers="3" minor_vers="4" stream_vers="0">\n')
            macro.write ('\t<Info datetime="2018-01-20T19:30:29" showfile="Created with MA2MBL4P" />\n')
            return

def close(filename):
        with open(filename ,"a") as macro: 
            macro.write ('</MA>')
            return

def begin_macro(filename, macro_number, macro_name):
        macro_number= str(macro_number)
        with open(filename ,"a") as macro:
            macro.write ('\t<Macro index="'+macro_number+'" name="'+macro_name+'">\n')
            return
            
def end_macro(filename):
        with open(filename ,"a") as macro:
            macro.write ('\t</macro>\n')
            return
            
def macro_line(filename, line_number, macro_line):
        line_number=str(line_number)
        with open(filename , "a") as macro:
            macro.write ('\t \t <Macroline index="'+ line_number +' ">\n')
            macro.write ('\t \t \t <text>'+macro_line+'</text>\n' )
            macro.write ('\t \t </Macroline>\n')
            return