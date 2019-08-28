import tkinter as tk
from tkinter import ttk
from tkinter import font  as tkfont
from PIL import ImageTk, Image
import multiprocessing
#import base64

Valve_type = ["GGC", "BALL"]
GGC_ITEM = ["GATE VALVE", "GLOBE VALVE", "SWING CHECK", "PISTION CHECK", "BUTTERFLY VALVE", "KNIFE GATE", "Y-TYPE GLOBE", "BELLOW SEAL GATE", "BELLOW SEAL GLOBE", "PRESSURE SEAL GATE", "PRESSURE SEAL GLOBE", "PRESSURE SEAL CHECK", "DUAL PLATE WAFER CHECK VALVE", "SLAB GATE VALVE", "BALL CHECK", "INSERT TYPE CHECK VALVE"]
GGC_ITEM_CODE = {'BALL CHECK':"CB", 'BELLOW SEAL GATE':"GB", 'BELLOW SEAL GLOBE': "GLB", 'SWING CHECK':"CW", 'PISTION CHECK':"CP", 'BUTTERFLY VALVE':"BFV", 'KNIFE GATE':"GK", 'Y-TYPE GLOBE':"GY", 'PRESSURE SEAL GATE':"GP", 'PRESSURE SEAL GLOBE':"GLP", 'PRESSURE SEAL CHECK':"PC", 'DUAL PLATE WAFER CHECK VALVE':"CD", 'SLAB GATE VALVE':"GS", 'INSERT TYPE CHECK VALVE':"CI", 'GATE VALVE': "G", 'GLOBE VALVE':"GL"}
GGC_ITEM_SIZE = ["1/4''","3/8''","1/2''","3/4''","1''","1 1/4''","1 1/2''","2''","2 1/2''","3''","4''","5''","6''","8''","10''","12''","14''","16''","18''","20''","24''","26''","28''","30''","32''","36''","40''","42''","48''","52''","54''","56''","60''"]
GGC_ITEM_SIZE_CODE = {"1/4''":"025", "1/2''":"050", "3/4''":"075", "1''":"1", "3/8''":"037","1 1/4''":"125", "1 1/2''":"150", "2''":"2", "2 1/2''":"250", "3''":"3", "4''":"4", "5''":"5", "6''":"6", "8''":"8", "10''":"10", "12''":"12", "14''":"14", "16''":"16", "18''":"18", "20''":"20", "24''":"24", "26''":"26", "28''":"28", "30''":"30", "32''":"32", "36''":"36", "40''":"40", "42''":"42", "48''":"48", "52''":"52", "54''":"54", "56''":"56", "60''":"60"}
GGC_ANSI_CLASS = ["150", "300", "600", "800", "900", "1500", "2500", "4500"]
GGC_ANSI_CLASS_CODE = {'150':"01", '300':"03", '600':"06", '800':"08", '900':"09", '1500': "15", '2500':"25", '4500':"45"}
GGC_VALVE_DESIGN_TYPE = ["ANGLE TYPE", "BASKET", "BOLTED BONNET", "CRYOGENIC DOUBLE OFFSET", "DOUBLE OFFSET", "DOUBLE OFFSET METAL SEATED", "Dual-door", "FLEXIBLE WEDGE", "FULL OPENING CHECK VALVE", "NEEDLE TYPE DISC", "NON RISING STEM", "NONE", "OS&Y", "PTFE FIREPROOFING DOUBLE OFFSET", "SINGLE OFFSET", "SOLID WEDGE", "TILTING TYPE CHECK", "TRIPLE OFFSET", "TRIPLE OFFSET METAL SEATED", "WELDED BONNET", "Y-TYPE"]
GGC_VALVE_DESIGN_TYPE_CODE = {"ANGLE TYPE":"AT", "BASKET":"BK", "BOLTED BONNET":"BB", "CRYOGENIC DOUBLE OFFSET":"CDO", "DOUBLE OFFSET":"DO", "DOUBLE OFFSET METAL SEATED":"DOM", "Dual-door":"DD", "FLEXIBLE WEDGE":"FW", "FULL OPENING CHECK VALVE":"FO", "NEEDLE TYPE DISC":"ND", "NON RISING STEM":"NR", "NONE":" ", "OS&Y":"OS", "PTFE FIREPROOFING DOUBLE OFFSET":" ", "SINGLE OFFSET":"SO", "SOLID WEDGE":"SW", "TILTING TYPE CHECK":"CT", "TRIPLE OFFSET":"TO", "TRIPLE OFFSET METAL SEATED":"TOM", "WELDED BONNET":"WB", "Y-TYPE":"YT"}
GGC_END_CONNECTION = ["BW","FLAT FLANGE/SMOOTH FLANGE","FNPT × MNPT","LUG","MLIP × FNPT","MSW × NPT","NPT/THREADED","RF","RF × FNPT","RTJ","SW × NPT","SW × SW","WAFER"]
GGC_END_CONNECTION_CODE = {"BW":"BW","FLAT FLANGE/SMOOTH FLANGE":"F","FNPT × MNPT":"TT","LUG":"LU","MLIP × FNPT":"LT","MSW × NPT":"MT","NPT/THREADED":"T","RF":"R","RF × FNPT":"RT","RTJ":"J","SW × NPT":"ST","SW × SW":"WF","WAFER":"WF"}
GGC_PORT_TYPE = ["FULL PORT", "REDUCED PORT", "REGULAR PORT"]
GGC_PORT_TYPE_CODE = {"FULL PORT": "FP", "REDUCED PORT": "RD", "REGULAR PORT":" "}
GGC_BODY_MATERIAL = ["ALLOY 20","ASTM A105N","ASTM A182 F1","ASTM A182 F5","ASTM A182 F9","ASTM A182 F11","ASTM A182 F22","ASTM A182 F51","ASTM A182 F53","ASTM A182 F55","ASTM A182 F60","ASTM A182 F91","ASTM A182 F304","ASTM A182 F304H","ASTM A182 F304L","ASTM A182 F316","ASTM A182 F316H","ASTM A182 F316L","ASTM A182 F317","ASTM A182 F317L","ASTM A182 F321","ASTM A182 F347","ASTM A216 WCB","ASTM A216 WCC","ASTM A217 C5","ASTM A217 C12","ASTM A217 C12A","ASTM A217 CA15","ASTM A217 WC1","ASTM A217 WC5","ASTM A217 WC6","ASTM A217 WC9","ASTM A350 LF2","ASTM A350 LF3","ASTM A351 CD4MCu","ASTM A351 CD4MCuN","ASTM A351 CF3","ASTM A351 CF3M","ASTM A351 CF8","ASTM A351 CF8C","ASTM A351 CF8M","ASTM A351 CF10","ASTM A351 CG3M","ASTM A351 CG8M","ASTM A351 CN7M","ASTM A352 LC1","ASTM A352 LC2","ASTM A352 LC3","ASTM A352 LCB","ASTM A352 LCC","ASTM A890 4A","ASTM A890 5A","ASTM A995 4A","ASTM A995 5A","CAST IRON","DUCTILE IRON","H C276","INCOLOY 800","INCOLOY 825","INCONEL 600","INCONEL 625","INCONEL 718","INCONEL  X-750","MONEL 400"]
GGC_BODY_MATERIAL_CODE = {"ALLOY 20":"S50","ASTM A105N":"C40","ASTM A182 F1":"H40","ASTM A182 F5":"H43","ASTM A182 F9":"H44","ASTM A182 F11":"H41","ASTM A182 F22":"H42","ASTM A182 F51":"D40","ASTM A182 F53":"D41","ASTM A182 F55":"D42","ASTM A182 F60":"D44","ASTM A182 F91":"H45","ASTM A182 F304":"S40","ASTM A182 F304H":"S45","ASTM A182 F304L":"S42","ASTM A182 F316":"S41","ASTM A182 F316H":"S45","ASTM A182 F316L":"S43","ASTM A182 F317":"S48","ASTM A182 F317L":"S47","ASTM A182 F321":"S46","ASTM A182 F347":"S44","ASTM A216 WCB":"C00","ASTM A216 WCC":"C01","ASTM A217 C5":"H03","ASTM A217 C12":"H04","ASTM A217 C12A":"H05","ASTM A217 CA15":"S30","ASTM A217 WC1":"H00","ASTM A217 WC5":"H06","ASTM A217 WC6":"H01","ASTM A217 WC9":"H02","ASTM A350 LF2":"L70","ASTM A350 LF3":"L40","ASTM A351 CD4MCu":"D07","ASTM A351 CD4MCuN":"D08","ASTM A351 CF3":"S02","ASTM A351 CF3M":"S03","ASTM A351 CF8":"S00","ASTM A351 CF8C":"S04","ASTM A351 CF8M":"S01","ASTM A351 CF10":"S05","ASTM A351 CG3M":"S07","ASTM A351 CG8M":"S06","ASTM A351 CN7M":"S08","ASTM A352 LC1":"L00","ASTM A352 LC2":"L01","ASTM A352 LC3":"L02","ASTM A352 LCB":"L20","ASTM A352 LCC":"L21","ASTM A890 4A":"D01","ASTM A890 5A":"D09","ASTM A995 4A":"D03","ASTM A995 5A":"D43","CAST IRON":"Z03","DUCTILE IRON":"Dl1","H C276":"N47","INCOLOY 800":"N45","INCOLOY 825":"N46","INCONEL 600":"N41","INCONEL 625":"N42","INCONEL 718":"N43","INCONEL  X-750":"N44","MONEL 400":"N40"}
GGC_DISC_MATERIAL = ["H.C276", "F44(U31254)","410 (1Cr13)","17-4PH","A105+CrC/ENP","A105N+WC","A105N-Cr","A105N/ENP","AISI 4140/ENP","ASTM A182 F53","ASTM A182 F60","ASTM A351 CF8C","ASTM A351 CG3M","ASTM A351 CG8M","ASTM A890 4A","ASTM A995 5A+STL6","BRONZE","CA15","CF8M","CF8M+WC","F51","F51+STL6","F55","F304","F304L","F316","F316+STL","F316+WC","F317","F321","F347","H C276","INCOLOY 825","Inconel 625","LF2+316 OVERLAY","LF2/ENP","MONEL400","SS316","WCB/ENP"]
GGC_DISC_MATERIAL_CODE = {"H C276":"N47","410 (1Cr13)":"1","CF8M":"2","A105N/ENP":"3","AISI 4140/ENP":"5","LF2+316 OVERLAY":"6","CA15":"7","LF2/ENP":"9","SS316":"D","F304":"0","17-4PH":"4","WCB/ENP":"8","F51":"A","F316":"B","A105N-Cr":"K","F304L":"C","MONEL400":"E","INCOLOY 825":"P","F321":"S","Inconel 625":"I","F44(U31254)":"F44","A105+CrC/ENP":"W","A105N+WC":"3W","F316+WC":"6W","CF8M+WC":"2W","ASTM A182 F53":"F53","F316+STL":"6S","ASTM A995 5A+STL6":"5A","BRONZE":"BZ","H.C276":"N47","F55":"D","ASTM A351 CG3M":"S7","ASTM A351 CG8M":"S8","ASTM A182 F60":"F60","ASTM A890 4A":"4A","F51+STL6":"AL","F317":"T","ASTM A351 CF8C":"S4","F347":"G"}
GGC_TRIM = ["1","2","3","4","5","5a","6","7","8","8a","9","10","11","11a","12","12a","13","14","14a","15","16","17","17/4PH","18","304","316","321","347","ALLOY 20","ALLOY 625","C276","F6","MONEL®","NONE","St  Gr6"]
GGC_TRIM_CODE = {"1":"1","2":"2","3":"3","4":"4","5":"5","5a":"5a","6":"6","7":"7","8":"8","8a":"8a","9":"9","10":"10","11":"11","11a":"11a","12":"12","12a":"12a","13":"13","14":"14","14a":"14a","15":"15","16":"16","17":"17","18":"18","F6":"F6","304":"304","316":"316","321":"321","347":"347","MONEL®":"MON","ALLOY 20":"A20","ALLOY 625":"A625","C276":"C267","17/4PH":"17P", "St  Gr6":"", "NONE":" "}
GGC_STEM_MATERIAL = ["410(1Cr13)","F304L","A105N/ENP","17-4PH","AISI 4140/ENP","F316","LF2/ENP","F51","1Cr13/ENP","F53","H.C276","F316/ENP","A105N-Cr","F51/ENP","INCOLOY 825","1Cr13(3)","F321","NITRONIC","17-7PH","F44(U31254)","INCONEL600","FXM-19+ENP","Inconel 625","DUCTILE IRON","F55","F317L","NONE","F60","F347"]
GGC_STEM_MATERIAL_CODE = {"410(1Cr13)":"1","F304L":"2","A105N/ENP":"3","17-4PH":"4","AISI 4140/ENP":"5","F316":"8","LF2/ENP":"9","F51":"A","1Cr13/ENP":"B","F53":"C","H.C276":"G","F316/ENP":"I","A105N-Cr":"K","F51/ENP":"L","INCOLOY 825":"P","1Cr13(3)":"T","F321":"S","NITRONIC":"X","17-7PH":"D","F44(U31254)":"F4","INCONEL600":"IN0","FXM-19+ENP":"FX","Inconel 625":"IN6","DUCTILE IRON":"DI","F55":"H","F317L":"F","F60":"J","F347":"E","NONE":" "}
GGC_SEAT_MATERIAL = ["410","304","310","F6","410+STL6","410+HF","304+STL6","316+STL6","347+STL6","Alloy 20+STL6","Bronze","Alloy 625","Monel 400","Monel 400+STL","Alloy 20","LF2+STL6","Integral + STL6","F317+HF","F51+STL","F60+STL6","Integral","F53","F321+HF","F316+GRAPHITE","PTFE"]
GGC_SEAT_MATERIAL_CODE = {"410":"1","304":"2","310":"3","F6":"4","410+STL6":"5","410+HF":"6","304+STL6":"7","316+STL6":"8","347+STL6":"9","Alloy 20+STL6":"A","Bronze":"B","Alloy 625":"C","Monel 400":"D","Monel 400+STL":"E","Alloy 20":"G","LF2+STL6":"L","Integral + STL6":"H","F317+HF":"I","F51+STL":"J","F60+STL6":"K","Integral":"0","F53":"F","F321+HF":"N","F316+GRAPHITE":"M","PTFE":"P"}
GGC_PACKING_MATERIAL = ["GRAPHITE","PTFE","PTFE+25%GRAPHIT","NONE"]
GGC_PACKING_MATERIAL_CODE = {"GRAPHITE":"1","PTFE":"2","PTFE+25%GRAPHIT":"3","NONE":" "}
GGC_ORING_MATERIAL = ["NBR","VITON A","VITON AED","VITON B","HNBR-70","HNBR","PTFE JACKETED VITON","VITON GLT","BUNA-N","ELAST-0-LION 101","EPDM","PCTFE","HNBR-82","VITON GF","HNBR-ED (Elast-O-Lion 985)","FFKM","VMQ","VITON F","FR 58/90","Lipseal","NONE"]
GGC_ORING_MATERIAL_CODE = {"NBR":"1","VITON A":"2","VITON AED":"3","VITON B":"4","HNBR-70":"5","HNBR":"6","PTFE JACKETED VITON":"7","VITON GLT":"8","BUNA-N":"9","ELAST-0-LION 101":"10","EPDM":"A","PCTFE":"B","HNBR-82":"C","VITON GF":"D","HNBR-ED (Elast-O-Lion 985)":"E","FFKM":"F","VMQ":"G","VITON F":"H","FR 58/90":"I","Lipseal":"J","NONE":" "}
GGC_DESIGN_STANDARD = ["API594","API 6A","API 6D","API 600","API 602","NONE"]
GGC_OPERATION_TYPE = ["LEVER OP","HAND WHEEL","GEAR OP","NONE", "CHAIN OP"]
GGC_OPERATION_TYPE_CODE = {"LEVER OP":"L","HAND WHEEL":"O","GEAR OP":"G","NONE":" ", "CHAIN OP":"C"}
GGC_DESIGN_FEATURE = ["ANGLE TYPE","BASKET","CRYOGENIC DOUBLE OFFSET","DOUBLE OFFSET","DOUBLE OFFSET METAL SEATED","FULL OPENING CHECK VALVE","NON RISING STEM","PTFE  FIREPROOFING  DOUBLE OFFSET","PTFE DOUBLE OFFSET","SINGLE OFFSET","TRIPLE OFFSET","TRIPLE OFFSET METAL SEATED","Y-TYPE ","WELDED BONNET","OS&Y","NON RISING STEM","Flexible wedge","Dual-door","ANGLE TYPE","BASKET","CRYOGENIC DOUBLE OFFSET","DOUBLE OFFSET","DOUBLE OFFSET METAL SEATED","FULL OPENING CHECK VALVE","BOLTED BONNET","NONE","EXTENDED BODY","BEVELED END"]
GGC_DESIGN_FEATURE_CODE = {"ANGLE TYPE":"AT","BASKET":"BK","CRYOGENIC DOUBLE OFFSET":"CDO","DOUBLE OFFSET":"DO","DOUBLE OFFSET METAL SEATED":"DOM","FULL OPENING CHECK VALVE":"FO","NON RISING STEM":"NR","PTFE  FIREPROOFING  DOUBLE OFFSET":" ","PTFE DOUBLE OFFSET":" ","SINGLE OFFSET":"SO","TRIPLE OFFSET":"TO","TRIPLE OFFSET METAL SEATED":"TOM","Y-TYPE ":"YT","WELDED BONNET":"WB","OS&Y":"OS","NON RISING STEM":"NR","Flexible wedge":"FW","Dual-door":"DD","ANGLE TYPE":"AT","BASKET":"BK","CRYOGENIC DOUBLE OFFSET":"CDO","DOUBLE OFFSET":"DO","DOUBLE OFFSET METAL SEATED":"DOM","FULL OPENING CHECK VALVE":"FO","BOLTED BONNET":"BB","NONE":" ","EXTENDED BODY":"E","BEVELED END":"B"}
GGC_FIRE_SAFE = ["NONE", "FIRE SAFE"]
GGC_FIRE_SAFE_CODE = {"FIRE SAFE":"FIRE SAFE", "NONE":""}
GGC_NACE = ["NACE MR-01-03","NACE MR-01-75", "NONE"]
GGC_NACE_CODE = {"NACE MR-01-03":"NACE MR-01-03","NACE MR-01-75":"NACE MR-01-75", "NONE":""}
GGC_LOCK = ["NONE", "LOCKING DEVICE"]
GGC_LOCK_CODE = {"LOCKING DEVICE":"LOCKING DEVICE","NONE":""}


BV_ITEM = ["BALL VALVE"]
BV_SIZE = ["1/4''","1/2''","3/4''","1''","1 1/4''","1 1/2''","2''","2 1/2''","3''","4''","5''","6''","8''","10''","12''","14''","16''","18''","20''","24''","26''","28''","30''","32''","36''","40''","42''","48''","52''","54''","56''","60''"]
BV_SIZE_CODE = {"1/4''":"025","1/2''":"050","3/4''":"075","1''":"1","1 1/4''":"125","1 1/2''":"150","2''":"2","2 1/2''":"250","3''":"3","4''":"4","5''":"5","6''":"6","8''":"8","10''":"10","12''":"12","14''":"14","16''":"16","18''":"18","20''":"20","24''":"24","26''":"26","28''":"28","30''":"30","32''":"32","36''":"36","40''":"40","42''":"42","48''":"48","52''":"52","54''":"54","56''":"56","60''":"60"}
BV_ANSI_CLASS = ["150","300","600","800","900","1500","2500","4500"]
BV_ANSI_CLASS_CODE = {"150":"01","300":"03","600":"06","800":"08","900":"09","1500":"15","2500":"25","4500":"45"}
BV_VALVE_DESIGN_TYPE = ["2PC FLOATING","3PC FLOATING ","1PC FLOATING ","2PC TRUNNION MOUNTED ","3PC TRUNNION MOUNTED ","TOP ENTRY TRUNNION MOUNTED","SPHERICAL TYPE FULLY WELDED TRUNNION ","SPHERICAL TYPE FULLY WELDED FLOATING"]
BV_VALVE_DESIGN_TYPE_CODE = {"2PC FLOATING":"BA","3PC FLOATING ":"BB","1PC FLOATING ":"BC","2PC TRUNNION MOUNTED ":"BD","3PC TRUNNION MOUNTED ":"BE","TOP ENTRY TRUNNION MOUNTED":"BF","SPHERICAL TYPE FULLY WELDED TRUNNION ":"BWD","SPHERICAL TYPE FULLY WELDED FLOATING":"BWA"}
BV_END_CONNECTION = ["RF","RTJ","BW","NPT/THREADED","SW×NPT","FLAT FLANGE/SMOOTH FLANGE","SWXSW","RFXFNPT","RFXSW","BWXFNPT","RF X BW"]
BV_END_CONNECTION_CODE = {"RF":"R","RTJ":"J","BW":"BW","NPT/THREADED":"T","SW×NPT":"ST","FLAT FLANGE/SMOOTH FLANGE":"F","SWXSW":"SW","RFXFNPT":"RT","RFXSW":"RW","BWXFNPT":"BF","RF X BW":"RB"}
BV_PORT_TYPE = ["FULL PORT","REDUCE PORT","REGULAR PORT"]
BV_PORT_TYPE_CODE = {"FULL PORT":"FP","REDUCE PORT":"RD","REGULAR PORT":"RP"}
BV_BODY_MATERIAL = ["ASTM A216 WCB","ASTM A216 WCC","ASTM A105N","ASTM A995 4A","ASTM A351 CD4MCu","ASTM A351 CD4MCuN","ASTM A890 5A","ASTM A890 4A","ASTM A182 F51","ASTM A182 F53","ASTM A182 F55","ASTM A182 F60","ASTM A217 WC1","ASTM A217 WC6","ASTM A217 WC9","ASTM A217 C5","ASTM A217 C12","ASTM A217 C12A","ASTM A217 WC5","ASTM A182 F1","ASTM A182 F11","ASTM A182 F22","ASTM A182 F5","ASTM A182 F9","ASTM A182 F91","ASTM A352 LC1","ASTM A352 LC2","ASTM A352 LC3","ASTM A352 LCB","ASTM A352 LCC","ASTM A350 LF3","ASTM A350 LF2","MONEL 400","INCONEL 600","INCONEL 625","INCONEL 718","INCONEL  X-750","INCOLOY 800","INCOLOY 825","H.C276","ASTM A351 CF8","ASTM A351 CF8M","ASTM A351 CF3","ASTM A351 CF3M","ASTM A351 CF8C","ASTM A351 CF10","ASTM A351 CG8M","ASTM A351 CG3M","ASTM A217 CA15","ASTM A182 F304","ASTM A182 F316","ASTM A182 F304L","ASTM A182 F316L","ASTM A182 F347","ASTM A182 F304H","ASTM A182 F321","ASTM A182 F317L","ASTM A182 F317","ASTM A182 F316H","ASTM A182 F44 (U31254)"]
BV_BODY_MATERIAL_CODE = {"ASTM A216 WCB":"C00","ASTM A216 WCC":"C01","ASTM A105N":"C40","ASTM A995 4A":"D03","ASTM A351 CD4MCu":"D07","ASTM A351 CD4MCuN":"D08","ASTM A890 5A":"D09","ASTM A890 4A":"D01","ASTM A182 F51":"D40","ASTM A182 F53":"D41","ASTM A182 F55":"D42","ASTM A182 F60":"D43","ASTM A217 WC1":"H00","ASTM A217 WC6":"H01","ASTM A217 WC9":"H02","ASTM A217 C5":"H03","ASTM A217 C12":"H04","ASTM A217 C12A":"H05","ASTM A217 WC5":"H06","ASTM A182 F1":"H40","ASTM A182 F11":"H41","ASTM A182 F22":"H42","ASTM A182 F5":"H43","ASTM A182 F9":"H44","ASTM A182 F91":"H45","ASTM A352 LC1":"L00","ASTM A352 LC2":"L01","ASTM A352 LC3":"L02","ASTM A352 LCB":"L20","ASTM A352 LCC":"L21","ASTM A350 LF3":"L40","ASTM A350 LF2":"L70","MONEL 400":"N40","INCONEL 600":"N41","INCONEL 625":"N42","INCONEL 718":"N43","INCONEL  X-750":"N44","INCOLOY 800":"N45","INCOLOY 825":"N46","H.C276":"N47","ASTM A351 CF8":"S00","ASTM A351 CF8M":"S01","ASTM A351 CF3":"S02","ASTM A351 CF3M":"S03","ASTM A351 CF8C":"S04","ASTM A351 CF10":"S05","ASTM A351 CG8M":"S06","ASTM A351 CG3M":"S07","ASTM A217 CA15":"S30","ASTM A182 F304":"S40","ASTM A182 F316":"S41","ASTM A182 F304L":"S42","ASTM A182 F316L":"S43","ASTM A182 F347":"S44","ASTM A182 F304H":"S45","ASTM A182 F321":"S46","ASTM A182 F317L":"S47","ASTM A182 F317":"S48","ASTM A182 F316H":"S49","ASTM A182 F44 (U31254)":"N51"}
BV_BALL_MATERIAL = ["410 (1Cr13)","CF8M","A105N/ENP","AISI 4140/ENP","LF2/ENP","CA15","F316","F304L","F51","F316L","MONEL400","A105N+WC","F316+WC","CF8M+WC","ASTM A182 F53","F316+STL","F44(U31254)","Inconel 625","H.C276","F55","F60","ASTM A182 F60","F316+Ni60","A105+Ni60","A105N/Cr","INCOLOY 825","F6A (1Cr13)+WC","AISI 4110/WC"]
BV_BALL_MATERIAL_CODE = {"410 (1Cr13)":"1","CF8M":"2","A105N/ENP":"3","AISI 4140/ENP":"5","LF2/ENP":"9","CA15":"7","F316":"B","F304L":"C","F51":"A","F316L":"E","MONEL400":"F","A105N+WC":"3W","F316+WC":"6W","CF8M+WC":"2W","ASTM A182 F53":"F53","F316+STL":"6S","F44(U31254)":"F44","Inconel 625":"I","H.C276":"N47","F55":"D","F60":"G","ASTM A182 F60":"F60","F316+Ni60":"6N","A105+Ni60":"6M","A105N/Cr":"4","INCOLOY 825":"J","F6A (1Cr13)+WC":"4W","AISI 4110/WC":"5W"}
BV_STEM_MATERIAL = ["17-4PH","17-7PH","A105N/ENP","AISI 4140/ENP","F316/ENP","F304L","F316","LF2/ENP","F51","1Cr13/ENP","H.C276","F316/ENP","F51/ENP","INCOLOY 825","INCONEL600","F44(U31254)","FXM-19+ENP","Inconel 625","F55","F316L","F60","F6a","INCONEL718"]
BV_STEM_MATERIAL_CODE = {"17-4PH":"4","17-7PH":"D","A105N/ENP":"3","AISI 4140/ENP":"5","F316/ENP":"I","F304L":"2","F316":"8","LF2/ENP":"9","F51":"A","1Cr13/ENP":"B","H.C276":"G","F316/ENP":"I","F51/ENP":"L","INCOLOY 825":"P","INCONEL600":"IN0","F44(U31254)":"F4","FXM-19+ENP":"FX","Inconel 625":"IN6","F55":"H","F316L":"E","F60":"J","F6a":"6","INCONEL718":"IN7"}
BV_SEAT_MATERIAL = [" PTFE","NYLON"," PEEK"," NYLON 12"," DEVLON"," KEL-F","RPTFE"," PCTFE"," MOLON"," PVDF","PTFE+25%Graphite"," TFM1700","LF2+ENP","F316+WC","A105N+WC","LF2+STL6","F316+STL6","A105N+STL6","F316","Inconel 625","F316+Ni55","A105+Ni55","F55","VITON","F6A(1Cr13)+WC","NICKEL OVERLAY","F60+STL"]
BV_SEAT_MATERIAL_CODE = {" PTFE":"1","NYLON":"2"," PEEK":"3"," NYLON 12":"4"," DEVLON":"5"," KEL-F":"6","RPTFE":"7"," PCTFE":"8"," MOLON":"9"," PVDF":"A","PTFE+25%Graphite":"B"," TFM1700":"C","LF2+ENP":"D","F316+WC":"E","A105N+WC":"F","LF2+STL6":"G","F316+STL6":"H","A105N+STL6":"I","F316":"J","Inconel 625":"K","F316+Ni55":"L","A105+Ni55":"M","F55":"N","VITON":"0","F6A(1Cr13)+WC":"P","NICKEL OVERLAY":"Q","F60+STL":"R"}
BV_PACKING_MATERIAL = ["GRAPHITE","PTFE","PTFE+25%GRAPHIT"]
BV_PACKING_MATERIAL_CODE = {"GRAPHITE":"1","PTFE":"2","PTFE+25%GRAPHIT":"3"}
BV_ORING_MATERIAL = ["BUNA-N","ELAST-0-LION 101","EPDM","FFKM","FR 58/90","HNBR","HNBR-70","HNBR-82","HNBR-ED (Elast-O-Lion 985)","Lipseal","NBR","NONE","PCTFE","PTFE JACKETED VITON","TBD","VITON A","VITON AED","VITON B","VITON F","VITON GF","VITON GLT","VMQ"]
BV_DESIGN_STANDARD = ["API6A","API 6D","API 608","NONE"]
BV_OPERATION_TYPE = ["LEVER OP","HAND WHEEL","GEAR OP","BARE STEM","PNEUMATIC ACTUATOR","OVAL HANDLE"]
BV_OPERATION_TYPE_CODE = {"LEVER OP":"L","HAND WHEEL":"O","GEAR OP":"G","BARE STEM":"B","PNEUMATIC ACTUATOR":"P","OVAL HANDLE":"V"}
BV_FIRE_SAFE = ["FIRE SAFE","NONE"]
BV_FIRE_SAFE_CODE = {"FIRE SAFE":"FIRE SAFE", "NONE":""}
BV_NACE = ["NACE MR-01-75", "NACE MR-01-03","NONE"]
BV_NACE_CODE = {"NACE MR-01-75":"NACE MR-01-75", "NACE MR-01-03":"NACE MR-01-03", "NONE":""}
BV_LOCK = ["LOCKING DEVICE","NONE"]
BV_LOCK_CODE = {"LOCKING DEVICE":"LOCKING DEVICE", "NONE":""}



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.iconbitmap()
        self.title_font = tkfont.Font(family='Arial', size=18, weight="bold", slant="italic")
        self.label_font = tkfont.Font(family = 'Arial', size = 10)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
        frame.winfo_toplevel().geometry("")

    

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bd=30)
        self.controller = controller
        label = tk.Label(self, text="SVI Product Code Generator", font=controller.title_font)
        label.grid(row = 0, column = 0, columnspan = 2)
        
        
        button1 = tk.Button(self, text="GGC",
                            command=lambda: controller.show_frame("PageOne"), fg="white", bg="midnight blue")
        button2 = tk.Button(self, text="BV",
                            command=lambda: controller.show_frame("PageTwo"), fg="white", bg="midnight blue")
        button3 = tk.Button(self, text="GGC/Trim",
                            command=lambda: controller.show_frame("PageThree"), fg="white", bg="midnight blue")
        
        button1.grid(row = 1, column = 0, columnspan = 2)
        button2.grid(row = 2, column = 0, columnspan = 2)
        button3.grid(row = 3, column = 0, columnspan = 2)
        
        #im = ImageTk.PhotoImage(data = image_data_base64_decoded_string)
        #render = ImageTk.PhotoImage(load)
        #ph = ImageTk.PhotoImage(load)
        #img = tk.Label(self, image=im)
        #img.image = render
        #img.grid(row = 4, column = 0, columnspan = 2)

class PageOne(tk.Frame):

    def generate_code(self):
        #result = ""
        Item = GGC_ITEM[self.label_1_Combo.current()]
        Item_Code = GGC_ITEM_CODE.get(Item)
        
        Size = GGC_ITEM_SIZE[self.label_2_Combo.current()]
        Size_Code = GGC_ITEM_SIZE_CODE.get(Size)
        
        ANSI_Class = GGC_ANSI_CLASS[self.label_3_Combo.current()]
        ANSI_Class_Code = GGC_ANSI_CLASS_CODE.get(ANSI_Class)
        
        Valve_Design_Type = GGC_VALVE_DESIGN_TYPE[self.label_4_Combo.current()]
        Valve_Design_Type_Code = GGC_VALVE_DESIGN_TYPE_CODE.get(Valve_Design_Type)
        
        End_Connection = GGC_END_CONNECTION[self.label_5_Combo.current()]
        End_Connection_Code = GGC_END_CONNECTION_CODE.get(End_Connection)
        
        Port_Type = GGC_PORT_TYPE[self.label_6_Combo.current()]
        Port_Type_Code = GGC_PORT_TYPE_CODE.get(Port_Type)
        
        Body_Material = GGC_BODY_MATERIAL[self.label_7_Combo.current()]
        Body_Material_Code = GGC_BODY_MATERIAL_CODE.get(Body_Material)
        
        Disc_Material = GGC_DISC_MATERIAL[self.label_8_Combo.current()]
        Disc_Material_Code = GGC_DISC_MATERIAL_CODE.get(Disc_Material)
        
        Stem_Material = GGC_STEM_MATERIAL[self.label_9_Combo.current()]
        Stem_Material_Code = GGC_STEM_MATERIAL_CODE.get(Stem_Material)
        
        Seat_Material = GGC_SEAT_MATERIAL[self.label_10_Combo.current()]
        Seat_Material_Code = GGC_SEAT_MATERIAL_CODE.get(Seat_Material)
        
        Packing_Material = GGC_PACKING_MATERIAL[self.label_11_Combo.current()]
        Packing_Material_Code = GGC_PACKING_MATERIAL_CODE.get(Packing_Material)
        
        Oring_Material = GGC_ORING_MATERIAL[self.label_12_Combo.current()]
        Oring_Material_Code = GGC_ORING_MATERIAL_CODE.get(Oring_Material)
        
        Design_Standard = GGC_DESIGN_STANDARD[self.label_13_Combo.current()]
        
        Operation_Type = GGC_OPERATION_TYPE[self.label_14_Combo.current()]
        Operation_Type_Code = GGC_OPERATION_TYPE_CODE.get(Operation_Type)
        
        Design_Feature = GGC_DESIGN_FEATURE[self.label_15_Combo.current()]
        Design_Feature_Code = GGC_DESIGN_FEATURE_CODE.get(Design_Feature)
        
        Fire_Safe = GGC_FIRE_SAFE[self.label_16_Combo.current()]
    
        Nace = GGC_NACE[self.label_17_Combo.current()]
        
        Lock = GGC_LOCK[self.label_18_Combo.current()]
        
        
        Code = "PART#:    " + Item_Code + "-" + Body_Material_Code + "-" + Size_Code + "-" + ANSI_Class_Code + End_Connection_Code + Operation_Type_Code + "/" + Disc_Material_Code + Stem_Material_Code + Seat_Material_Code + Packing_Material_Code + Port_Type_Code + Valve_Design_Type_Code + Design_Feature_Code
        Special_Note = self.special_Note_TextBox.get("1.0","end-1c")
        Description = "Description: " + Item + ", " + Size + ", " + "CLASS " + ANSI_Class + "," + End_Connection + ", " + Port_Type + ", " + "BODY " + Body_Material + ", " + "DISC " + Disc_Material + ", " + "STEM " + Stem_Material + ", " + "SEAT " + Seat_Material + ", " + "ORING " + Oring_Material + ", " + "PACKING " + Packing_Material + ", " + Operation_Type + ", " + Fire_Safe + ", " + Nace + ", " + Lock + ". " + Special_Note
        Result = Code + "\n" + Description
        
        self.popupmsg(Result)
        
    def client_exit(self):
        exit()
    
    def popupmsg(self, msg):
        popup = tk.Tk()
        
        def leavemini():
            popup.destroy()
                
            
        label = tk.Label(popup, text="Result")
        label.grid()
        Result_text = tk.Text(popup, height = 10, width = 50)
        Result_text.insert(tk.INSERT,msg)
        Result_text.config(state = "normal")
        Result_text.grid()
        B1 = ttk.Button(popup, text = "Ok", command = leavemini)
        B1.grid()
        popup.tkraise()
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Frame.config(self, bd=30)
        label = tk.Label(self, text="GGC Valve Page", font=controller.title_font)
        label.grid(row = 0, column = 0, columnspan = 2, sticky = 'we')
        button = tk.Button(self, text="Go to the previous page",
                           command=lambda: controller.show_frame("StartPage"), fg="white", bg="midnight blue")
        button.grid(row = 1, column = 0, columnspan = 2, sticky = 'we')
        
        label_1 = tk.Label(self, text = "ITIEM:    ", font=controller.label_font)
        label_1.grid(row = 2, column = 0)
        self.label_1_Combo = ttk.Combobox(self, value = GGC_ITEM, state = 'readonly')
        self.label_1_Combo.grid(row = 2, column = 1)
        
        label_2 = tk.Label(self, text = "SIZE:    ", font=controller.label_font)
        label_2.grid(row = 3, column = 0)
        self.label_2_Combo = ttk.Combobox(self, value = GGC_ITEM_SIZE, state = 'readonly')
        self.label_2_Combo.grid(row = 3, column = 1)
        
        label_3 = tk.Label(self, text = "ANSI CLASS:    ", font=controller.label_font)
        label_3.grid(row = 4, column = 0)
        self.label_3_Combo = ttk.Combobox(self, value = GGC_ANSI_CLASS, state = 'readonly')
        self.label_3_Combo.grid(row = 4, column = 1)
        
        label_4 = tk.Label(self, text = "VALVE DESIGN TYPE:    ", font=controller.label_font)
        label_4.grid(row = 5, column = 0)
        self.label_4_Combo = ttk.Combobox(self, value = GGC_VALVE_DESIGN_TYPE, state = 'readonly')
        self.label_4_Combo.grid(row = 5, column = 1)
        
        label_5 = tk.Label(self, text = "END CONNECTION:    ", font=controller.label_font)
        label_5.grid(row = 6, column = 0)
        self.label_5_Combo = ttk.Combobox(self, value = GGC_END_CONNECTION, state = 'readonly')
        self.label_5_Combo.grid(row = 6, column = 1)
        
        label_6 = tk.Label(self, text = "PORT TYPE:    ", font=controller.label_font)
        label_6.grid(row = 7, column = 0)
        self.label_6_Combo = ttk.Combobox(self, value = GGC_PORT_TYPE, state = 'readonly')
        self.label_6_Combo.grid(row = 7, column = 1)
        
        label_7 = tk.Label(self, text = "BODY MATERIAL:    ", font=controller.label_font)
        label_7.grid(row = 8, column = 0)
        self.label_7_Combo = ttk.Combobox(self, value = GGC_BODY_MATERIAL, state = 'readonly')
        self.label_7_Combo.grid(row = 8, column = 1)
        
        label_8 = tk.Label(self, text = "DISC MATERIAL:    ", font=controller.label_font)
        label_8.grid(row = 9, column = 0)
        self.label_8_Combo = ttk.Combobox(self, value = GGC_DISC_MATERIAL, state = 'readonly')
        self.label_8_Combo.grid(row = 9, column = 1)
        
        label_9 = tk.Label(self, text = "STEM MATERIAL:    ", font=controller.label_font)
        label_9.grid(row = 10, column = 0)
        self.label_9_Combo = ttk.Combobox(self, value = GGC_STEM_MATERIAL, state = 'readonly')
        self.label_9_Combo.grid(row = 10, column = 1)
        
        label_10 = tk.Label(self, text = "SEAT MATERIAL:    ", font=controller.label_font)
        label_10.grid(row = 11, column = 0)
        self.label_10_Combo = ttk.Combobox(self, value = GGC_SEAT_MATERIAL, state = 'readonly')
        self.label_10_Combo.grid(row = 11, column = 1)
        
        label_11 = tk.Label(self, text = "PACKING MATERIAL:    ", font=controller.label_font)
        label_11.grid(row = 12, column = 0)
        self.label_11_Combo = ttk.Combobox(self, value = GGC_PACKING_MATERIAL, state = 'readonly')
        self.label_11_Combo.grid(row = 12, column = 1)
        
        label_12 = tk.Label(self, text = "ORING MATERIAL:    ", font=controller.label_font)
        label_12.grid(row = 13, column = 0)
        self.label_12_Combo = ttk.Combobox(self, value = GGC_ORING_MATERIAL, state = 'readonly')
        self.label_12_Combo.grid(row = 13, column = 1)
        
        label_13 = tk.Label(self, text = "DESIGN STANDARD:    ", font=controller.label_font)
        label_13.grid(row = 14, column = 0)
        self.label_13_Combo = ttk.Combobox(self, value = GGC_DESIGN_STANDARD, state = 'readonly')
        self.label_13_Combo.grid(row = 14, column = 1)
        
        label_14 = tk.Label(self, text = "OPERATION TYPE:    ", font=controller.label_font)
        label_14.grid(row = 15, column = 0)
        self.label_14_Combo = ttk.Combobox(self, value = GGC_OPERATION_TYPE, state = 'readonly')
        self.label_14_Combo.grid(row = 15, column = 1)
        
        label_15 = tk.Label(self, text = "DESIGN FEATURE:    ", font=controller.label_font)
        label_15.grid(row = 16, column = 0)
        self.label_15_Combo = ttk.Combobox(self, value = GGC_DESIGN_FEATURE, state = 'readonly')
        self.label_15_Combo.grid(row = 16, column = 1)
        
        label_16 = tk.Label(self, text = "FIRE SAFE:    ", font=controller.label_font)
        label_16.grid(row = 17, column = 0)
        self.label_16_Combo = ttk.Combobox(self, value = GGC_FIRE_SAFE, state = 'readonly')
        self.label_16_Combo.grid(row = 17, column = 1)
        
        label_17 = tk.Label(self, text = "NACE:    ", font=controller.label_font)
        label_17.grid(row = 18, column = 0)
        self.label_17_Combo = ttk.Combobox(self, value = GGC_NACE, state = 'readonly')
        self.label_17_Combo.grid(row = 18, column = 1)
        
        label_18 = tk.Label(self, text = "LOCK:    ", font=controller.label_font)
        label_18.grid(row = 19, column = 0)
        self.label_18_Combo = ttk.Combobox(self, value = GGC_LOCK, state = 'readonly')
        self.label_18_Combo.grid(row = 19, column = 1)

        label_19 = tk.Label(self, text = "SPECIAL NOTE: \n", font=controller.label_font)
        label_19.grid(row = 20, columnspan = 2, sticky = 'we')
        
        self.special_Note_TextBox = tk.Text(self, width = 10, height = 5, font = "Arial")
        self.special_Note_TextBox.grid(row = 21, columnspan = 2, sticky = 'we')
        
        Submit = tk.Button(self, text="GENERATE", command=self.generate_code, fg="white", bg="midnight blue")
        Submit.grid(column = 0, columnspan = 2, sticky = 'we')
        #print("gogogogo")
    
    
    

class PageTwo(tk.Frame):

    
    def generate_code(self):
        #result = ""
        Item = BV_ITEM[self.label_1_Combo.current()]
        #Item_Code = GGC_ITEM_CODE.get(Item)
        
        Size = BV_SIZE[self.label_2_Combo.current()]
        Size_Code = BV_SIZE_CODE.get(Size)
        
        ANSI_Class = BV_ANSI_CLASS[self.label_3_Combo.current()]
        ANSI_Class_Code = BV_ANSI_CLASS_CODE.get(ANSI_Class)
        
        Valve_Design_Type = BV_VALVE_DESIGN_TYPE[self.label_4_Combo.current()]
        Valve_Design_Type_Code = BV_VALVE_DESIGN_TYPE_CODE.get(Valve_Design_Type)
        
        End_Connection = BV_END_CONNECTION[self.label_5_Combo.current()]
        End_Connection_Code = BV_END_CONNECTION_CODE.get(End_Connection)
        
        Port_Type = BV_PORT_TYPE[self.label_6_Combo.current()]
        Port_Type_Code = BV_PORT_TYPE_CODE.get(Port_Type)
        
        Body_Material = BV_BODY_MATERIAL[self.label_7_Combo.current()]
        Body_Material_Code = BV_BODY_MATERIAL_CODE.get(Body_Material)
        
        Ball_Material = BV_BALL_MATERIAL[self.label_8_Combo.current()]
        Ball_Material_Code = BV_BALL_MATERIAL_CODE.get(Ball_Material)
                
        Stem_Material = BV_STEM_MATERIAL[self.label_9_Combo.current()]
        #Stem_Material_Code = BV_STEM_MATERIAL_CODE.get(Stem_Material)
        
        Seat_Material = BV_SEAT_MATERIAL[self.label_10_Combo.current()]
        Seat_Material_Code = BV_SEAT_MATERIAL_CODE.get(Seat_Material)
        
        Packing_Material = BV_PACKING_MATERIAL[self.label_11_Combo.current()]
        #Packing_Material_Code = BV_PACKING_MATERIAL_CODE.get(Packing_Material)
        
        Oring_Material = BV_ORING_MATERIAL[self.label_12_Combo.current()]
        #Oring_Material_Code = BV_ORING_MATERIAL_CODE.get(Oring_Material)
        
        Design_Standard = BV_DESIGN_STANDARD[self.label_13_Combo.current()]
        
        Operation_Type = BV_OPERATION_TYPE[self.label_14_Combo.current()]
        Operation_Type_Code = BV_OPERATION_TYPE_CODE.get(Operation_Type)
        
        
        Fire_Safe = BV_FIRE_SAFE[self.label_15_Combo.current()]
    
        Nace = BV_NACE[self.label_16_Combo.current()]
        
        Lock = BV_LOCK[self.label_17_Combo.current()]
        
        
        Special_Note = self.special_Note_TextBox.get("1.0","end-1c")
        Code = "PART#:    " + Valve_Design_Type_Code + "-" + Body_Material_Code + "-" + Size_Code + "-" + ANSI_Class_Code + End_Connection_Code + Operation_Type_Code + "/" + Ball_Material_Code + Port_Type_Code + Seat_Material_Code
        Description = "Description: " + Item + ", "  + Size + ", " + "CLASS " + ANSI_Class + ", " + Valve_Design_Type + "," + End_Connection + ", " + Port_Type + ", " + "BODY " + Body_Material + ", " + "BALL " + Ball_Material + ", " + "STEM " + Stem_Material + ", " + "SEAT " + Seat_Material + ", " + "PACKING " + Packing_Material + ", " + "ORING " + Oring_Material + ", " + Design_Standard + ", " + Operation_Type + ", " + Fire_Safe + ", " + Nace + ", " + Lock + ". " + Special_Note
        Result = Code + "\n" + Description
        
        self.popupmsg(Result)
        
    def popupmsg(self, msg):
        popup = tk.Tk()
        
        def leavemini():
            popup.destroy()
                
            
        label = tk.Label(popup, text="Result")
        label.grid()
        Result_text = tk.Text(popup, height = 10, width = 50)
        Result_text.insert(tk.INSERT,msg)
        Result_text.config(state = "normal")
        Result_text.grid()
        B1 = ttk.Button(popup, text = "Ok", command = leavemini)
        B1.grid()
        popup.tkraise()
        
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bd=30)
        self.controller = controller
        label = tk.Label(self, text="Ball Valve Page", font=controller.title_font)
        label.grid(row = 0, column = 0, columnspan = 2, sticky = 'we')
        button = tk.Button(self, text="Go to the previous page",
                           command=lambda: controller.show_frame("StartPage"), fg="white", bg="midnight blue")
        button.grid(row = 1, column = 0, columnspan = 2, sticky = 'we')
        
        label_1 = tk.Label(self, text = "ITEM:    ", font=controller.label_font)
        label_1.grid(row = 2, column = 0)
        self.label_1_Combo = ttk.Combobox(self, value = BV_ITEM, state = 'readonly')
        self.label_1_Combo.grid(row = 2, column = 1)
        
        label_2 = tk.Label(self, text = "SIZE:    ", font=controller.label_font)
        label_2.grid(row = 3, column = 0)
        self.label_2_Combo = ttk.Combobox(self, value = BV_SIZE, state = 'readonly')
        self.label_2_Combo.grid(row = 3, column = 1)
        
        label_3 = tk.Label(self, text = "ANSI CLASS:    ", font=controller.label_font)
        label_3.grid(row = 4, column = 0)
        self.label_3_Combo = ttk.Combobox(self, value = BV_ANSI_CLASS, state = 'readonly')
        self.label_3_Combo.grid(row = 4, column = 1)
        
        label_4 = tk.Label(self, text = "VALVE DESIGN TYPE:    ", font=controller.label_font)
        label_4.grid(row = 5, column = 0)
        self.label_4_Combo = ttk.Combobox(self, value = BV_VALVE_DESIGN_TYPE, state = 'readonly')
        self.label_4_Combo.grid(row = 5, column = 1)
        
        label_5 = tk.Label(self, text = "END CONNECTION:    ", font=controller.label_font)
        label_5.grid(row = 6, column = 0)
        self.label_5_Combo = ttk.Combobox(self, value = BV_END_CONNECTION, state = 'readonly')
        self.label_5_Combo.grid(row = 6, column = 1)
        
        label_6 = tk.Label(self, text = "PORT TYPE:    ", font=controller.label_font)
        label_6.grid(row = 7, column = 0)
        self.label_6_Combo = ttk.Combobox(self, value = BV_PORT_TYPE, state = 'readonly')
        self.label_6_Combo.grid(row = 7, column = 1)
        
        label_7 = tk.Label(self, text = "BODY MATERIAL:    ", font=controller.label_font)
        label_7.grid(row = 8, column = 0)
        self.label_7_Combo = ttk.Combobox(self, value = BV_BODY_MATERIAL, state = 'readonly')
        self.label_7_Combo.grid(row = 8, column = 1)
        
        label_8 = tk.Label(self, text = "BALL MATERIAL:    ", font=controller.label_font)
        label_8.grid(row = 9, column = 0)
        self.label_8_Combo = ttk.Combobox(self, value = BV_BALL_MATERIAL, state = 'readonly')
        self.label_8_Combo.grid(row = 9, column = 1)
        
        label_9 = tk.Label(self, text = "STEM MATERIAL:    ", font=controller.label_font)
        label_9.grid(row = 10, column = 0)
        self.label_9_Combo = ttk.Combobox(self, value = BV_STEM_MATERIAL, state = 'readonly')
        self.label_9_Combo.grid(row = 10, column = 1)
        
        label_10 = tk.Label(self, text = "SEAT MATERIAL:    ", font=controller.label_font)
        label_10.grid(row = 11, column = 0)
        self.label_10_Combo = ttk.Combobox(self, value = BV_SEAT_MATERIAL, state = 'readonly')
        self.label_10_Combo.grid(row = 11, column = 1)
        
        label_11 = tk.Label(self, text = "PACKING MATERIAL:    ", font=controller.label_font)
        label_11.grid(row = 12, column = 0)
        self.label_11_Combo = ttk.Combobox(self, value = BV_PACKING_MATERIAL, state = 'readonly')
        self.label_11_Combo.grid(row = 12, column = 1)
        
        label_12 = tk.Label(self, text = "ORING MATERIAL:    ", font=controller.label_font)
        label_12.grid(row = 13, column = 0)
        self.label_12_Combo = ttk.Combobox(self, value = BV_ORING_MATERIAL, state = 'readonly')
        self.label_12_Combo.grid(row = 13, column = 1)
        
        label_13 = tk.Label(self, text = "DESIGN STANDARD:    ", font=controller.label_font)
        label_13.grid(row = 14, column = 0)
        self.label_13_Combo = ttk.Combobox(self, value = BV_DESIGN_STANDARD, state = 'readonly')
        self.label_13_Combo.grid(row = 14, column = 1)
        
        label_14 = tk.Label(self, text = "OPERATION TYPE:    ", font=controller.label_font)
        label_14.grid(row = 15, column = 0)
        self.label_14_Combo = ttk.Combobox(self, value = BV_OPERATION_TYPE, state = 'readonly')
        self.label_14_Combo.grid(row = 15, column = 1)
        
        label_15 = tk.Label(self, text = "FIRE SAFE:    ", font=controller.label_font)
        label_15.grid(row = 16, column = 0)
        self.label_15_Combo = ttk.Combobox(self, value = BV_FIRE_SAFE, state = 'readonly')
        self.label_15_Combo.grid(row = 16, column = 1)
        
        label_16 = tk.Label(self, text = "NACE:    ", font=controller.label_font)
        label_16.grid(row = 17, column = 0)
        self.label_16_Combo = ttk.Combobox(self, value = BV_NACE, state = 'readonly')
        self.label_16_Combo.grid(row = 17, column = 1)
        
        label_17 = tk.Label(self, text = "LOCK:    ", font=controller.label_font)
        label_17.grid(row = 18, column = 0)
        self.label_17_Combo = ttk.Combobox(self, value = BV_LOCK, state = 'readonly')
        self.label_17_Combo.grid(row = 18, column = 1)
        
        label_18 = tk.Label(self, text = "SPECIAL NOTE: \n", font=controller.label_font)
        label_18.grid(row = 19, columnspan = 2, sticky = 'we')
        
        self.special_Note_TextBox = tk.Text(self, width = 10, height = 5, font = "Arial")
        self.special_Note_TextBox.grid(row = 20, columnspan = 2, sticky = 'we')
        
        Submit = tk.Button(self, text="GENERATE", command=self.generate_code, fg="white", bg="midnight blue")
        Submit.grid(columnspan = 2, sticky = 'we')
        
class PageThree(tk.Frame):

    def generate_code(self):
        Item = GGC_ITEM[self.label_1_Combo.current()]
        Item_Code = GGC_ITEM_CODE.get(Item)
        
        Size = GGC_ITEM_SIZE[self.label_2_Combo.current()]
        Size_Code = GGC_ITEM_SIZE_CODE.get(Size)
        
        ANSI_Class = GGC_ANSI_CLASS[self.label_3_Combo.current()]
        ANSI_Class_Code = GGC_ANSI_CLASS_CODE.get(ANSI_Class)
        
        #Valve_Design_Type = GGC_VALVE_DESIGN_TYPE[self.label_4_Combo.current()]
        #Valve_Design_Type_Code = GGC_VALVE_DESIGN_TYPE_CODE.get(Valve_Design_Type)
        
        End_Connection = GGC_END_CONNECTION[self.label_4_Combo.current()]
        End_Connection_Code = GGC_END_CONNECTION_CODE.get(End_Connection)
        
        Port_Type = GGC_PORT_TYPE[self.label_5_Combo.current()]
        #Port_Type_Code = GGC_PORT_TYPE_CODE.get(Port_Type)
        
        Body_Material = GGC_BODY_MATERIAL[self.label_6_Combo.current()]
        Body_Material_Code = GGC_BODY_MATERIAL_CODE.get(Body_Material)
        
        #Disc_Material = GGC_DISC_MATERIAL[self.label_8_Combo.current()]
        #Disc_Material_Code = GGC_DISC_MATERIAL_CODE.get(Disc_Material)
        
        Disc_Trim = GGC_TRIM[self.label_7_Combo.current()]
        Disc_Trim_Code = GGC_TRIM_CODE.get(Disc_Trim)
        
        #Stem_Material = GGC_STEM_MATERIAL[self.label_10_Combo.current()]
        #Stem_Material_Code = GGC_STEM_MATERIAL_CODE.get(Stem_Material)
        
        #Seat_Material = GGC_SEAT_MATERIAL[self.label_11_Combo.current()]
        #Seat_Material_Code = GGC_SEAT_MATERIAL_CODE.get(Seat_Material)
        
        Packing_Material = GGC_PACKING_MATERIAL[self.label_8_Combo.current()]
        #Packing_Material_Code = GGC_PACKING_MATERIAL_CODE.get(Packing_Material)
        
        #Oring_Material = GGC_ORING_MATERIAL[self.label_13_Combo.current()]
        #Oring_Material_Code = GGC_ORING_MATERIAL_CODE.get(Oring_Material)
        
        #
        
        Operation_Type = GGC_OPERATION_TYPE[self.label_9_Combo.current()]
        Operation_Type_Code = GGC_OPERATION_TYPE_CODE.get(Operation_Type)
        
        Design_Standard = GGC_DESIGN_STANDARD[self.label_10_Combo.current()]
        #Design_Feature = GGC_DESIGN_FEATURE[self.label_16_Combo.current()]
        #Design_Feature_Code = GGC_DESIGN_FEATURE_CODE.get(Design_Feature)
        
        Fire_Safe = GGC_FIRE_SAFE[self.label_11_Combo.current()]
        #Fire_Safe_Code = GGC_FIRE_SAFE_CODE.get(Fire_Safe)
    
        Nace = GGC_NACE[self.label_12_Combo.current()]
        #Nace_Code = GGC_NACE_CODE.get(Nace)
        
        Lock = GGC_LOCK[self.label_13_Combo.current()]
        #Lock_Code = GGC_LOCK_CODE.get(Lock)
        
        Special_Note = self.special_Note_TextBox.get("1.0","end-1c")
        Code = "PART#:    " + Item_Code + "-" + Body_Material_Code + "-" + Size_Code + "-"  + ANSI_Class_Code + End_Connection_Code + Operation_Type_Code + "/" + Disc_Trim_Code
        Description = "Description: " + Item + ", " + Size + ", " + "ANSI CLASS " + ANSI_Class + "," + End_Connection + ", " + Port_Type + ", " + "BODY " + Body_Material + ", " + "TRIM# " + Disc_Trim + ", " + Design_Standard + ", "  + Operation_Type + ", " + "PACKING " + Packing_Material +  ", " + Fire_Safe + ", " + Nace + ", " + Lock + ". " + Special_Note
        Result = Code + "\n" + Description
        
        self.popupmsg(Result)
        
    def popupmsg(self, msg):
        popup = tk.Tk()
        
        def leavemini():
            popup.destroy()
                
            
        label = tk.Label(popup, text="Result")
        label.grid()
        Result_text = tk.Text(popup, height = 10, width = 50)
        Result_text.insert(tk.INSERT,msg)
        Result_text.config(state = "normal")
        Result_text.grid()
        B1 = ttk.Button(popup, text = "Ok", command = leavemini)
        B1.grid()
        popup.tkraise()
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bd=30)
        self.controller = controller
        label = tk.Label(self, text="GGC Valve Page (Trim)", font=controller.title_font)
        label.grid(row = 0, column = 0, columnspan = 2, sticky = 'we')
        button = tk.Button(self, text="Go to the previous page",
                           command=lambda: controller.show_frame("StartPage"), fg="white", bg="midnight blue")
        button.grid(row = 1, column = 0, columnspan = 2, sticky = 'we')

        label_1 = tk.Label(self, text = "ITEM:    ", font=controller.label_font)
        label_1.grid(row = 2, column = 0)
        self.label_1_Combo = ttk.Combobox(self, value = GGC_ITEM, state = 'readonly')
        self.label_1_Combo.grid(row = 2, column = 1)
        
        label_2 = tk.Label(self, text = "SIZE:    ", font=controller.label_font)
        label_2.grid(row = 3, column = 0)
        self.label_2_Combo = ttk.Combobox(self, value = GGC_ITEM_SIZE, state = 'readonly')
        self.label_2_Combo.grid(row = 3, column = 1)
        
        label_3 = tk.Label(self, text = "ANSI CLASS:    ", font=controller.label_font)
        label_3.grid(row = 4, column = 0)
        self.label_3_Combo = ttk.Combobox(self, value = GGC_ANSI_CLASS, state = 'readonly')
        self.label_3_Combo.grid(row = 4, column = 1)
        
        label_4 = tk.Label(self, text = "END CONNECTION:    ", font=controller.label_font)
        label_4.grid(row = 5, column = 0)
        self.label_4_Combo = ttk.Combobox(self, value = GGC_END_CONNECTION, state = 'readonly')
        self.label_4_Combo.grid(row = 5, column = 1)
        
        label_5 = tk.Label(self, text = "PORT TYPE:    ", font=controller.label_font)
        label_5.grid(row = 6, column = 0)
        self.label_5_Combo = ttk.Combobox(self, value = GGC_PORT_TYPE, state = 'readonly')
        self.label_5_Combo.grid(row = 6, column = 1)
        
        label_6 = tk.Label(self, text = "BODY MATERIAL:    ", font=controller.label_font)
        label_6.grid(row = 7, column = 0)
        self.label_6_Combo = ttk.Combobox(self, value = GGC_BODY_MATERIAL, state = 'readonly')
        self.label_6_Combo.grid(row = 7, column = 1)
        
        label_7 = tk.Label(self, text = "TRIM#:    ", font=controller.label_font)
        label_7.grid(row = 8, column = 0)
        self.label_7_Combo = ttk.Combobox(self, value = GGC_TRIM, state = 'readonly')
        self.label_7_Combo.grid(row = 8, column = 1)
        
        label_8 = tk.Label(self, text = "PACKING MATERIAL:    ", font=controller.label_font)
        label_8.grid(row = 9, column = 0)
        self.label_8_Combo = ttk.Combobox(self, value = GGC_PACKING_MATERIAL, state = 'readonly')
        self.label_8_Combo.grid(row = 9, column = 1)
        
        label_9 = tk.Label(self, text = "OPERATION TYPE:    ", font=controller.label_font)
        label_9.grid(row = 10, column = 0)
        self.label_9_Combo = ttk.Combobox(self, value = GGC_OPERATION_TYPE, state = 'readonly')
        self.label_9_Combo.grid(row = 10, column = 1)
        
        label_10 = tk.Label(self, text = "DESIGN STANDARD:    ", font=controller.label_font)
        label_10.grid(row = 11, column = 0)
        self.label_10_Combo = ttk.Combobox(self, value = GGC_DESIGN_STANDARD, state = 'readonly')
        self.label_10_Combo.grid(row = 11, column = 1)
        
        label_11 = tk.Label(self, text = "FIRE SAFE:    ", font=controller.label_font)
        label_11.grid(row = 12, column = 0)
        self.label_11_Combo = ttk.Combobox(self, value = GGC_FIRE_SAFE, state = 'readonly')
        self.label_11_Combo.grid(row = 12, column = 1)
        
        label_12 = tk.Label(self, text = "NACE:    ", font=controller.label_font)
        label_12.grid(row = 13, column = 0)
        self.label_12_Combo = ttk.Combobox(self, value = GGC_NACE, state = 'readonly')
        self.label_12_Combo.grid(row = 13, column = 1)
        
        label_13 = tk.Label(self, text = "LOCK:    ", font=controller.label_font)
        label_13.grid(row = 14, column = 0)
        self.label_13_Combo = ttk.Combobox(self, value = GGC_LOCK, state = 'readonly')
        self.label_13_Combo.grid(row = 14, column = 1)
        
        label_14 = tk.Label(self, text = "SPECIAL NOTE: \n", font=controller.label_font)
        label_14.grid(row = 15, columnspan = 2, sticky = 'we')
        
        self.special_Note_TextBox = tk.Text(self, width = 10, height = 5, font = "Arial")
        self.special_Note_TextBox.grid(row = 16, columnspan = 2, sticky = 'we')
        
        
        Submit = tk.Button(self, text="GENERATE", command=self.generate_code, fg="white", bg="midnight blue")
        Submit.grid(columnspan = 2, sticky = 'we')

if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = SampleApp()
    app.title("SVI Product Code Generator")
    app.mainloop()
    
