import os
import re
import xml.etree.cElementTree as ET
import ma2macro

def offseter():
    #czytaj pliki presetów
    PositionPreset_wyg = ET.parse('wyg.xml')
    PositionPreset_cor = ET.parse('corrected.xml')

    #definiuj słowniki
    pan_wyg = {}    #słownik wartości pan ideal
    tilt_wyg = {}   #słownik wartości tilt ideal
    pan_cor = {}    #słownik wartości pan poprawionej
    tilt_cor = {}   #słownik wartości tilt poprawionej
    pan_off ={}     #słownik obliczonych offsetów pan
    tilt_off = {}   #słownik obliczonych offserów tilt

    #przepisz wartości "idealne" do słowników
    print ('====================================================')
    print ('')
    print ('Original:')
    
    
    #TODO PARSOWANIE DO PRZEPISANIA
    ######################################################################################################################

    root = PositionPreset_wyg.getroot()
    for child in root.iterfind('.//{http://schemas.malighting.de/grandma2/xml/MA}Preset//{http://schemas.malighting.de/grandma2/xml/MA}Values//{http://schemas.malighting.de/grandma2/xml/MA}Channels//{http://schemas.malighting.de/grandma2/xml/MA}PresetValue'):
        val_w = child.get ('Value')
        for child2 in child.iter():
            fixid_w = child2.get ('fixture_id')
            attrib_w = child2.get ('attribute_name')

        if attrib_w == 'PAN':
            pan_wyg[fixid_w]=float(val_w)
            print ('Fix Id= ' +fixid_w+ ' '+attrib_w+'= '+val_w)

        if attrib_w == 'TILT':
            tilt_wyg[fixid_w]=float(val_w)
            print ('Fix Id= ' +fixid_w+ ' '+attrib_w+'= '+val_w)

	####
    #przepisz wartości "poprawione" do słowników
    print ('====================================================')
    print ('')
    print ('Corrected:')
	
    root = PositionPreset_cor.getroot()
    for child in root.iterfind('.//{http://schemas.malighting.de/grandma2/xml/MA}Preset//{http://schemas.malighting.de/grandma2/xml/MA}Values//{http://schemas.malighting.de/grandma2/xml/MA}Channels//{http://schemas.malighting.de/grandma2/xml/MA}PresetValue'):
        val_c = child.get ('Value')
        for child2 in child.iter():
            fixid_c = child2.get ('fixture_id')
            attrib_c = child2.get ('attribute_name')

        if attrib_c == 'PAN':
            pan_cor[fixid_c]=float(val_c)
            print ('Fix Id= ' +fixid_c+ ' '+attrib_c+'= '+val_c)

        if attrib_c == 'TILT':
            tilt_cor[fixid_c]=float(val_c)
            print ('Fix Id= ' +fixid_c+ ' '+attrib_c+'= '+val_c)
	
    print ('====================================================')
    print ('')
    #####################################################################################################################
    
    
    #pobierz listy fix ID do sprawdzenia, czy presety są identyczne pod względem sortowania ID
    wyg_keys_pan = list(pan_wyg.keys())
    wyg_keys_tilt = list(tilt_wyg.keys())
    cor_keys_pan = list(pan_cor.keys())
    cor_keys_tilt = list(tilt_cor.keys())

    #sprawdź, czy listy sortowania są identyczne
    if wyg_keys_pan == cor_keys_pan and wyg_keys_tilt == cor_keys_tilt:
        print ('Presets seems OK. Starting calculations.')
	    #iteracyjnie odejmuj wartości atrybutów i przepisuj do słownika offset PAN
        print ('Offset PAN for:')
        pan_keys = list(pan_wyg.keys())
        for i in pan_wyg:
            fixid_o = pan_keys.pop(0)
            val_w = pan_wyg.get(i)
            val_c = pan_cor.get(i)
            val_o = val_c - val_w
            str_val_o = str(val_o)
            print ('Fix ID: ' + fixid_o + ' = ' + str_val_o)
            pan_off[fixid_o] = float(val_o)
        print ('')
    
        #iteracyjnie odejmuj wartości atrybutów i przepisuj do słownika offset TILT
        print ('Offset TILT for:')
        tilt_keys = list(tilt_wyg.keys())
        for i in tilt_wyg:
            fixid_o = tilt_keys.pop(0)
            val_w = tilt_wyg.get(i)
            val_c = tilt_cor.get(i)
            val_o = val_c - val_w
            str_val_o = str(val_o)
            print ('Fix ID: ' + fixid_o + ' = ' + str_val_o)
            tilt_off[fixid_o] = float(val_o)
	    #TODO PRZEPISANIE DLA BIBLIOTEKI SPLIB
		
			
	    #TWORZENIE PLIKU XML (MA2 MACRO)
        directory=os.getcwd()
        drive=re.findall("\w:" ,directory)
        macrodir=drive[0]+"\\gma2\\macros"
			
        print('')
        print('===========================================================')
        print('')
        print('Macro directory:'+macrodir)
        os.chdir(macrodir)
        macroname = "Offsets.xml"        
        ma2macro.create (macroname)
        ma2macro.begin_macro (macroname, 0, 'SET OFFSETS')				
		#Ustaw licznik lini macro
        macro_line_nr = 0
		#przepisywanie wartości do offset tilt
        tilt_off_keys= list(tilt_off.keys())
		
        for i in tilt_off:
            fixid_o = tilt_off_keys.pop(0)
            val_o = tilt_off.get(i)
            str_fixid_o = str(fixid_o)
            str_val_o = str (val_o)
            str_line = str (macro_line_nr)
            macroline = 'Assign Fixture '+ str_fixid_o +' /tiltoffset='+ str_val_o
            ma2macro.macro_line(macroname, str_line, macroline)		
            macro_line_nr = macro_line_nr +1
					
	    		#przepisywanie wartości do offser pan
            pan_off_keys= list(pan_off.keys())
					
        for i in pan_off:
            fixid_o = pan_off_keys.pop(0)
            val_o = pan_off.get(i)
            str_fixid_o = str(fixid_o)
            str_val_o = str (val_o)
            str_line = str (macro_line_nr)
            macroline = 'Assign Fixture '+ str_fixid_o +' /panoffset='+ str_val_o 
            ma2macro.macro_line(macroname, str_line, macroline)							
            macro_line_nr = macro_line_nr +1
						
		#zamknięcie MACRO
        ma2macro.end_macro (macroname)
        ma2macro.close (macroname)
        print('Macrofile created and saved. Import macro offsets.xml on console and run to set offsets.')
        print ('')
        print('===========================================================')
        print('Developed by Szymon Plotkowski')
        print('szymonplotkowski@gmail.com')
        print('Feel free to write if You like/dislike this app ar You have some ideas how to improve it.')
        print('You can also make donation, using my email on PayPal')
        print('===========================================================')
        input('Press ENTER to EXIT')           
        return ()
    else:
        print ('Presets in Reference and Corrected preset was created for different sets of fixtures. Export proper positions and try again')
        print ('')
        print ("wyg Fix IDs pan:")
        print (wyg_keys_pan)
        print ("Corrected Fix IDs pan:")
        print (cor_keys_pan)   
        print ("wyg Fix IDs tilt:")
        print (wyg_keys_tilt)
        print ("Corrected Fix IDs tilt:")
        print (cor_keys_tilt)
        print ('')
        print('===========================================================')
        print('Developed by Szymon Plotkowski')
        print('szymonplotkowski@gmail.com')
        print('Feel free to write if You like/dislike this app ar You have some ideas how to improve it.')
        print('You can also make donation, using my email on PayPal')
        print('===========================================================')
        input ('Press Enter to EXIT')
        return ()


offseter ()
quit ()