import re
def isNumber(s):
    isDecimal=False
    regex=re.compile(r"^\s*?[-]?(\d+\.\d*|\d*\.\d+|\d+)(e[-]?\d+)?\s*?$")
    if(regex.match(s)!=None):
      isDecimal=True
 
    return isDecimal


        
list=[""," 0.14 ","abc","1 a","2e10"," -90e3   "," 1e","e3"," 6e-1"," 99e2.5 ","53.5e93"," --6 ","-+3","95a54e53"]
    

for i in list:
 print(i +'=>'+str(isNumber(i)))