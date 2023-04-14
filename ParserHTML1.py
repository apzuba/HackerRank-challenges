# A custom made HTML Parser (without relying on the HTML Parser package).



import sys, re

N = input()
code = ""

for line in sys.stdin.readlines():
    code+=line.rstrip("\n")
  
splitted = re.split(r"(?=<)", str(code))
code_on = 'true'
for el in splitted:
    if re.search(r"<!--", el): code_on = 'false'
    if code_on == 'true':
        base_on = 'false'
        if re.search(r"<\/\w+", el): # <-- END GROUP
            el = re.search(r"(?<=<\/)[a-zA-Z0-9]+", el).group()
            print("End   :", el)
        elif re.search(r"<[a-zA-Z0-9-]+>", el): # <-- START GROUP SINGLE
            el_1 = re.search(r"([a-zA-Z0-9-]+)", el).group(1)
            print("Start :", el_1)
        else:
            if re.search(r"\/>", el): # <-- EMPTY GROUP
                el_1 = re.search(r"([a-zA-Z0-9-]+)", el).group(1)
                print("Empty :", el_1)
                base_on = 'true'
            elif re.search(r"<[a-zA-Z0-9-]+", el): # <-- START GROUP MULTI
                el_1 = re.search(r"([a-zA-Z0-9-]+)", el).group(1)
                print("Start :", el_1)
                base_on = 'true'
            if base_on == 'true': # <-- ATTRIBUTES FOR START AND EMPTY GROUPS
                el = re.sub(r"\t\t", " ", el)
                no_tit = re.sub(r"(<[a-zA-Z0-9-]+ )|((?=>).+)", "", el)
                spl = re.split(r"(?<=\" )", no_tit)
                if len(spl)>0: 
                    for sp in spl:
                        w_val = re.finditer(rf"([a-zA-Z0-9-]+)(=[\'\"](?P<val>.+)[\'\"])?", sp)
                        [print("->", i.group(1), ">", i.group("val")) for i in  w_val]
    if re.search(r"-->", el): code_on = 'true'




        
