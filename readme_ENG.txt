OFFSETER 4 MA2 developed by Szymon Płotkowski
szymonplotkowski@gmail.com

DESCRIPTION:
Programm compares two MA2 position presets files and writes a macro that sets fixture offsets based on calculated difference.
In most cases, using this program will makes all position presets looks good, without touching them.
You just have to correct one of them and run macro. In worst case scenario You'll finish with good base for small tweaks.
Macro don't overwrite or change anything in Your old presets. It's just setting offsets in Patch.

Why use it instead of stage calibration?
SC is more complicated and force You to correct 4 presets, and have knowlege about coordinates of points You choose.


STEB BY STEP:
-Reset offsets for fixtures You want to correct
-import EXPORT 4 OFFSETER.xml macro to Your desk
-Select which preset will be Your reference preset. For example preset made in WYSIWYG, or from previous show (best results with presets like "center"/"all fixtures in one point". 
-Copy that preset on new position, run it and try to correct it. Store new values using UPDATE
-Run macro EXPORT 4 OFFSETER
-Macro will ask You for Drive number (4 if You want to use Your flash drive), and numbers of reference and corrected presets !!!DONT USE MA SYNTAX "2.X" - JUST NUMBER ('33' for preset 2.33)!!!
-Now You should have a two XML files(wyg.xml and corrected.xml) in gma2\importexport on Your flashdrive. Put EXE file in same directory and run it 
-If everything goes well You should have new offsets.xml file in gma2/macros on flashdrive
-Import Offsets.xml as macro
-Run Macro
-Enjoy saved time :D 


Version info:

V 2.3
- Macro write engine rewrited using MA2_Python_lib (preparation for MA3)

V 2.2
- Preset parser engine rewrited 
- Added programm icon
- Minimal MA software version lowered to 3.4.0

V 2.1
- Preset validation engine totaly rewrited. Program will not make a macro if presets have different quantity or selection order. 
- Exception geters
- Added author info

V 2.0
- Function added: copying result macro to gma2\macros directory

V 1.0
- Concept proof


