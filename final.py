#Vampiris Dimitrios 3186 username dimitris_vampiris/cse63186/cs03186
#Zioudas Konstantinos 3225 username kzioudas/cse63225/cs03225
#[1.2.0] - 2020-03-03
#based on minimal++.v1.2
##Changed
#-<call-stat> as asked
#_<factor>
##Added
#-<idtail>
#[1.1.0] - 2020-02-26
#based on minimal++.v1.1
##Changed
#-<call-stat> as asked
#-<factor>  as asked
##Removed
#-<idtail> as asked
##debugging
#[1.0.0] - 2020-02-20
##all arrays are lists array names given for our own convenience
"""
###########################################################################################################################################################################################
READ BEFORE GRADE

o kodikas tis metatropis se mips den einai dikos mas einai kathara gia test tou upoloipou!! Den theloume na vathmologithoume gia to final code kai oute na theorithi antigrAafi
known issues:
    1.lex() kanena
    2.syntax()
        a.xanei tin seira sta tokens me apotelesma ena "count" na dimiurgei lathi se oli tin leitourgia
        b.logo tou parapano parembodizei tin metatropi se endiameso kodika opos kai ton pinaka symbolon
        c....
    3.Metatropi se endiameso den exoume vrei kati
    4.pinakas symbolon
        a.logo syntax den gemizei
    5.metatropi se .c kai grafei se .int arxeio themata logo syntax
        a.stin c den oloklirosame tin metatropi px. var klp
    6.final code !!!! NOT OUR CODE NA MI LIFTHEI IPOPSIN
    7. Genika
        a.Metafora onomatos apo in arxeio sta alla arxeia
        

    an uparxoun apories sxetika me ton kodika tis final epikinoniste mazi mas sto : cs03225@uoi.gr
############################################################################################################################################################################################
"""
programtk = 'program'

LeftBratk = '{'
RightBratk = '}'
LeftPartk = '('
RightPartk = ')'
declaretk = 'declare'
notdeclaretk = 'notdeclare'
char1 = ';'
functiontk = 'function'
proceduretk = 'procedure'
formalparstk = 'formalist'
assigmenttk = ':='
formalparitemtk = 'formalparitem'
intk = 'in'
inouttk = 'inout'
calltk = 'call'
printtk = 'print'
inputtk = 'input'
thentk = 'then'
iftk = 'if'
elsetk = 'else'
whiletk = 'while'
doublewhiletk = 'doublewhiletk'
looptk = 'loop'
exittk = 'exit'
actualparitemtk = 'actualparitem'
booltermtk = 'booleterm'
ortk = 'or'
andtk = 'and'
forcasetk = 'forcase'
char2tk = ':'
defaulttk = 'default'
incasetk = 'incase'
boolfactortk = 'boolfactor'
whentk = 'when'
nottk = 'not'
returntk = 'return'
LeftBrackettk = '['
RightBrackettk = ']'
addopertk = 'addo-oper'
termtk = 'term'
mulopertk = 'mul-oper'
factortk = 'factor'
equalstk = '='
mineqtk = '<='
maxeqtk = '>='
mintk = '<'
maxtk = '>'
minmaxtk = '<>'
plustk = '+'
minustk = '-'
multitk = '*'
dividetk = '/'

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['0','1','2','3','4','5','6','7','8','9']
arithmsymbol=['+','-','*','/']
correlationopers=['<','>','=','<=','>=','<>']
assignmentSymbol=":="
seperators=[';',',',':']
groupingopers=['(',')','{','}','[',']']
commseps=['/*','*/','//']
keywords=['program','declare','function','procedure','in','inout','if','else','while','doublewhile','loop','exit','forcase','incase','when','default','not','and','or','call','return','input','print']
statementslst=['if','else','while','doublewhile','loop','exit','forcase','incase','call','return','input','print',':=']
linenum=0
global tokens
tokens=[]
global symbolarray 
nq=0
count=0#for syntax
global countSA
countSA=0
global entitylist,entitylist2
entitylist=[]
entitylist2=[]
helpIC = []
"""Read File"""
piece = ''
f=input("Enter the file name:")
file=open(f,"r")

global offset

global countNT
countNT=1
final= open('final.asm',"w")


"""FINAL CODE"""

def gnlvcode(v):
    global symbolarray
    ent= searchentitybyName(v)
    if ent.typee=='f':    
        scopenestinglevel = symbolarray[-1].nestinglevel
        final.write('    lw      $t0, -4($t0)\n')
         
    while c > 0:
        final.write('    lw      $t0, -4($t0)\n')
        c -= 1
    final.write('    addi    $t0, $t0, -%d\n' % ent.offset)


def loadvr(v, r):
    global symbolarray
    if v in num:
        final.write('    li      $t%s, %d\n' % (r, v))
    else:
        ent = searchentitybyName(v)
        scopenestinglevel  = symbolarray[-1].nestinglevelvl
        if ent.typee == 'v' and ent.snl == 0:
            final.write('    lw      $t%s, -%d($s0)\n' % (r, ent.offset))
        elif (ent.typee == 'p' and ent.snl == scopenestinglevel ) or(ent.typee == 'p' and ent.parMode == 'CV' and ent.snl == scopenestinglevel) or (ent.typee == 't'):
            assembly_file.write('    lw      $t%s, -%d($sp)\n' % (r, ent.offset))
        elif ent.typee == 'p' and ent.parMode == 'REF' and ent.snl == scopenestinglevel:
            final.write('    lw      $t0, -%d($sp)\n' % ent.offset)
            final.write('    lw      $t%s, ($t0)\n' % r)
        elif (ent.typee == 'v' and ent.snl < scopenestinglevel) or (ent.typee == 'p' and ent.parMode == 'CV' and ent.snl < scopenestinglevel):
            gnvlcode(v)
            final.write('    lw      $t%s, ($t0)\n' % r)
        elif temp.elemtype == 'PARAMETER' and temp.partype == 'inout' and entlvl < curr_scope:
            gnvlcode(v)
            final.write('    lw      $t0, ($t0)\n')
            final.write('    lw      $t%s, ($t0)\n' % r)
        else:
            print("ERROR: Unreachable load argument from quad to register")
            


        
def storerv(r, v):
    global symbolarray
    ent = searchentitybyName(v)
    scopenestinglevel  = symbolarray[-1].nestinglevelvl
    if (ent.typee == 'v' and ent.snl == 0):
      final.write('    sw      $t%s, -%d($s0)\n' %  (r, ent.offset))
      
    elif (ent.typee == 'v' and ent.snl == scopenestinglevel) or (ent.typee == 'p' and ent.parMode == 'CV' and ent.snl==scopenestinglevel) or (ent.typee == 't'):
        final.write('    sw      $t%s, -%d($sp)\n' % (r, ent.offset))
      
    elif (ent.typee == 'p' and ent.parMode == 'REF' and ent.snl == scopenestinglevel):
        final.write('    lw      $t0, -%d($sp)\n' % ent.offset)
        final.write('    sw      $t%s, ($t0)\n' % r)

    elif (ent.typee == 'v' and ent.snl <scopenestinglevel) or (ent.typee == 'p' and ent.parMode == 'CV' and ent.snl < scopenestinglevel):
        gnvlcode(v)
        assembly_file.write('    sw      $t%s, ($t0)\n' % r)

    elif (ent.typee == 'p' and ent.parMode == 'REF' and ent.snl < scopenestinglevel):
        gnvlcode(v)
        assembly_file.write('    lw      $t0, ($t0)\n')
        assembly_file.write('    sw      $t%s, ($t0)\n' % r) 
    else:
        print("ERROR: Unreachable store argument from quad to register")
        


def toassembly(q, n):
    global arithmsymbol, correlationopers, math_operations, branches

    
    branches = ('beq', 'bne', 'blt', 'ble', 'bgt', 'bge')
    
    arithmopers = ('add', 'sub', 'mul', 'div')

    global final,number_of_functions_mips,L_counter

    if q.op == 'jump':
        final.write('L_%d:\n'%(q.label))
        final.write('    j       L_%s\n' % q.z)
    elif q.op in relations:
        relop = branches[relations.array(q.op)]
        final.write('L_%d:\n'%(q.qlabel))
        loadvr(q.x, '1')
        loadvr(q.y, '2')
        assembly_file.write('    %s     $t1, $t2, L_%d\n' % (relop, q.z))
    elif q.op in math_symbols:
        op = branches[math_symbols.array(q.op)]
        final.write('L_%d:\n'%(q.label))
        loadvr(quad.x, '1')
        loadvr(quad.y, '2')
        final.write('    %s     $t1, $t2, $t2%d\n' % (op, q.z))
    elif q.op == ':=':  
        final.write('L_%d:\n' % (q.label))
        loadvr(q.x, '1')
        storerv('1', q.z)
    elif q.op == 'out':
        final.write('L_%d:\n'%(q.label))
        loadvr(q.x,'9')
        final.write('    li      $v0, 1\n')
        final.write('    add      $a0,$zero,$t9 \n')
        final.write('    syscall       \n')
    elif q.op == 'in':
        final.write('    li      $v0, 5\n')
        final.write('    syscall       \n')
    elif q.op == 'retv':
        loadvr(q.x, '1')
        final.write('    lw      $t0, -8($sp)\n')
        final.write('    sw      $t1, -8($t0)\n')
        final.write('    jr      $ra\n\n')
    elif q.op == 'par':
        if n == tokens[1][1]:
            function_c = 0
            framelength = mainframelength
        else:
            entity = search_entity(n, 'f')
            function_c= search_entity(n, 'f')
            framelength = entity.framelength
        if helpIC == []:
            final.write('    addi    $fp, $sp, -%d\n' % framelength)
        helpIC.append(q)
        temp_offset = 12 + 4 * helpIC.array(q)
        if q.y == 'CV':
            loadvr(qu.x, '0')
            final.write('    sw      $t0, -%d($fp)\n' % temp_offset)
        elif q.y == 'REF':
            varent = search_entity_by_name(q.x)
            var_c = search_entity_by_name(q.x)
            if function_c == var_c:
                if varent.typee == 'v':
                    final.write('    addi    $t0, $sp, -%s\n' % varent.offset)
                    final.write('    sw      $t0, -%d($fp)\n' % temp_offset) 
                elif varent.typee == 'p' and varent.parMode == 'CV':
                    final.write('    addi    $t0, $sp, -%s\n' % varent.offset)
                    final.write('    sw      $t0, -%d($fp)\n' % temp_offset)
                elif varent.typee == 'p' and varnt.parMode == 'REF':
                    final.write('    lw      $t0, -%d($sp)\n' % varent.offset)
                    final.write('    sw      $t0, -%d($fp)\n' % temp_offset)
            else:
                if varent.typee == 'v':
                    gnvlcode(q.x)
                    final.write('    sw      $t0, -%d($fp)\n' % temp_offset)	
                elif varent.typee == 'p' and varent.partMode == 'CV':
                    gnvlcode(q.x)
                    final.write('    sw      $t0, -%d($fp)\n' % temp_offset)
                elif varient.typee == 'p' and varent.parMode == 'REF':
                    gnvlcode(q.x)
                    final.write('    lw      $t0, 0($t0)\n')
                    final.write('    sw      $t0, -%d($fp)\n' % temp_offset)
        elif q.y == 'RET':
            varent = search_entity_by_name(q.x)
            var_c = search_entity_by_name(q.x)
            final.write('    addi    $t0, $sp, -%d\n' % varent.offset) 
            final.write('    sw      $t0, -8($fp)\n')
    elif q.op == 'call':
        if n == tokens[1][0]:
            function_c = 0
            framelength = mainframelength 
        else:
            par_function = search_entity(n, 'f')
            function_c = search_entity(n, 'f')
            framelength = entity.framelength
            child_function, child_function_c = search_entity(q.x, 'f')     
        if function_c == child_function_c:
            final.write('    lw      $t0, -4($sp)\n')
            final.write('    sw      $t0, -4($fp)\n')
        else:
            final.write('    sb      $sp, -4($fp)\n')
            final.write('    addi    $sp, $sp, %d\n' % framelength)
            final.write('    jal     L_%s\n' % str(child_function.startquad))
            final.write('    addi    $sp, $sp, -%d\n' % framelength)
    elif q.op == 'begin_block':
        if n == tokens[1][0]:
            final.write('    j       L_0\n')
            final.write('L_0:\n')
            final.seek(0,2)   
            final.write('    addi    $sp, $sp, %d\n' % mainframelength)
            final.write('    move    $s0, $sp\n')  
        else: 
            final.write('    j 		L_t%d\n'%(L_counter))
            function_c += 1
            final.write('L_d%d:\n' % (function_c))
            final.write('    sw      $ra, 0($sp)\n')
    elif q.op == 'end_block':
        final.write('    lw      $ra, 0($sp)\n')
        final.write('    jr      $ra\n\n')
    elif q.op == 'halt':
        final.write('L_d%d:\n' % (q.label))
        final.write('    li      $v0, 10\n')
        final.write('    syscall       \n')
    

    
"""CLASSES"""

##NA TO DOUME EPIGONTOS##
class QuadsforIC():
    def __init__(qIC, label, op, x, y, z):
        qIC.label=label
        qIC.op=op
        qIC.x=x
        qIC.y=y
        qIC.z=z
    def __str__(qIC):
         return str(qIC.label)+': '+str(qIC.op)+','+str(qIC.x)+','+str(qIC.y)+','+str(qIC.z)


class Scope():
    def __init__(sc, nestinglevel=0):
        #sc.entities=entities[]
        sc.entities=list()
        sc.nestinglevel=nestinglevel
        sc.offset = 12

    def addEntity(sc, entity,typee):
        entity.typee=typee
        entity.snl=sc.nestinglevel 
        sc.entities.append(entity)
        print(sc.entities)
    def getoffset(sc):
        ret = sc.offset
        sc.offset += 4
        return ret
    def getlistentity(sc):
        ret= sc.entities
        return ret
    def removeScopeEnt(sc):
        sc.entities=[]
  

class Argument():
    def __init__(arg, par_mode, typee):
        arg.par_mode = par_mode
        arg.typee = typee

    

    


class Entity():
    def __init__(ent, name):
        ent.name=name
        ent.snl=0
        

 


class Variable(Entity):
    def __init__(entv, name,typee,offset):
        super().__init__(name)
        entv.typee=typee
        entv.offset = offset
        
  

class Function(Entity):
    def __init__(entf, name,typee,startquad=0,arguments= None ,framelength=0):
        super().__init__(name)
        entf.typee=typee
        entf.startquad=startquad
        entf.arguments=arguments
        entf.framelength=framelength

    def addargument(entf, argument):
        entf.arguments.append(argument)

    def setframelen(entf, framelength):
        entf.framelength = framelength

    def setstartquad(entf, startquad):
        entf.startquad = startquad

    


class Constant(Entity):
    def __init__(entc,name,value):
        super().__init__(name)
        entp.value=value
        
       
        
class Parameter(Entity):
    def __init__(entp,name,parMode,offset=0):
        super().__init__(name)
        entp.parMode=parMode
        entp.offset = offset

    


class Temporaryvariable(Entity):
    def __init__(self,name,offset=0):
        super().__init__(name)
        self.offset = offset

    

         
##DONE
def addEntity(entity,typee):
    symbolarray[-1].addEntity(entity,typee)
def funbackpatchstartquad(name):
    global symbolarray
    start=nextquad()
    t=searchEntinybyNameandType(name,"f")
    if t==None:
        return
    else:
        t.setstartquad(start)
    return start
    
    
def funbackpatchframelen(name,fl):
    global symbolarray
    
    t=searchEntinybyNameandType(name,"f")
    if t==None:
        return
    else:
        t.setframelen(fl)    

def searchEntinybyNameandType(n,typee):
    global symbolarray
    
    g=-1
    scope=symbolarray[g]
    
    while scope != None:
        for entity in scope.entities:
                if entity==[]:
                    return
                elif entity.name==n and entity.typee==typee:
                    
                    return entity
        g-=1        
def searchEntinybyName(n):
    global symbolarray
    g=-1
    scope=symbolarray[g]
   
    while scope != None:
        for entity in scope.entities:
            if entity==[]:
                return
            elif entity.name== n :
                 return entity 
        g-=1                            

    

  

def addScope():
    
    global symbolarray,countSA
    
    scope=Scope(countSA)
    symbolarray.append(scope)
    countSA+=1
   

##done
def removeScope():
    global countSA , symbolarray
    
    if len(symbolarray)<0 or len(symbolarray)<countSA:
        return
    else:
        symbolarray[countSA-1].removeScopeEnt()
        symbolarray[countSA-1]=''
    countSA-=1
def backpatchsymbolarray():
    global symbolarray 
    
##done   
def recordScope(listentity):
    scope=symbolarray[countSA-1]
    scope.entities.append(listentity)
##na to do
def recordArgument(parMode,typee):
    arg=Argument(parMode,typee)
    return arg
##done    
def recordEntity_var(name,typee,):
    entity=Variable(name,typee,symbolarray[-1].getoffset())
    addEntity(entity,"v")
    
##semi-done
def recordEntity_fun(name,typee,startquad=0,argument=None,framelength=0):
    entity=Function(name,typee)
    addEntity(entity,"f")

##done    
def recordEntity_con(name,value):
    entity=Constant(name,value)
    addEntity(entity,"c")
##done    
def recordEntity_par(name,parMode):
    entity=Parameter(name,parMode,symbolarray[-1].getoffset())
    addEntity(entity,"p")
    
##done
def recordEntity_temp(name):
    entity=Temporaryvariable(name,symbolarray[-1].getoffset())
    addEntity(entity,"t")
    
    

    
""" IC defs"""
def mintointname(x):
    name=x[-4]
            
    
    return name
intfilename=mintointname(f)    

def intfile(ic):
    global intfilename
    name= str(intfilename)+'.int'
    intCode=open(name,"w")
    for i in ic:
        
        intCode.write(i.__str__()+'\n')
    intCode.close()
##lathos na to do
##almosta done    
def cfile(ic):
    global intfilename
    name=intfilename+'.c'
    cCode=open(name,"w")
    cCode.write('#include <stdio.h>'+'\n')
    print("in c file")
    for i in ic:
        print("c: "+i.__str__())
        if i.op in arithmsymbol:
            cCode.write(i.z+'='+i.x+i.op+i.y+';'+'\n')
        elif i.op=='jump':
            cCode.write('goto'+' '+i.z+';'+'\n')
        elif i.op in  correlationopers:
            op1=''
            if i.op == '=':
                op1='=='
            elif i.op== '<>':
                opl='!='
            else:
                opl=i.op
            cCode.write('if'+'('+i.x+op1+i.y+')'+' '+'goto'+' '+i.z+';'+'\n')
        elif i.op==':=':
            cCode.write(i.z+'='+i.x+';'+'\n')
        elif i.op=='out':
            cCode.write('printf('+i.x+')'+';'+'\n')
        elif i.op=='inp':
            cCode.write('scanf('+i.x+')'+';'+'\n')
        elif i.op=='ret':
            cCode.write('return'+i.x+';'+'\n')
        #elif 
        
    cCode.close()

def nextquad():
    global nq
    
    return nq

def genquad(op,x,y,z):
    global nq
    global helpIC
    nextquad=nq
    nq+=1
    quad=QuadsforIC(nextquad,op,x,y,z) 
    helpIC.append(quad) 
    
 
def newtemp():
    global counterNT
    t='t'+str(counterNT)
    hlp=symbolarray[-1]
    offset=hlp.getoffset()
    recordEntity_temp(t,offset)
    
    return t
    

def emptylist():
    emptylist = []

    return emptylist

def makelist(x):
    t=[]
    t.append(x)
    return t

def merge(l1,l2):
    retlist=[]
    retlist = l1+l2
    
    return retlist

def backpatch(l1,z):
    
    for i in l1:
        for j in helpIC:
            if i==j.label:
                j.z=z

    return
"""start of lex"""

def lex():
    
    
    #global tokens
    
    print("mpikelex")
     
    def readInlines(file):#"""Read file after opening line by line"""
            print("mpike read")
            
            #data = file.readline()
            linenum=1
            lines=[]
            while True:
                data = file.readline()
                #print("mpike while lines")
                lines.append([data,linenum])
                linenum+=1
                if not data:
                    break
            #print(lines)
            return lines    
                #print ( data )
    
   



    
    
   
#"""helping fucntion"""               
    def splithlp(word):
        t=[char for char in word]
        print(t)
        return [char for char in word]
        
    #def remove_comm(l):
      #  for i in  range(len(l)):
       #     if(l[i]=='/'):
                
        #        k=1
         #       s=1
          #      prev=''
           # elif l[i]=='\n' :
                
            #    k=0
             #   s=0
              #  prev=''
            #elif(prev=='/' and l[i]=='*'and s==0):
             #   k=1
              #  s=1
               # prev=''
            #elif(prev=='*' and l[i]=='/')and s==1:
             #    k=0
              #   s=0
#"""helping function. Removes Excess stuff because of a bug at stateEngine"""
    def removeExcess(array):
        tokens=[]
        tokens=array
       
        for i in range(0,len(tokens)-1):
            
            if tokens[i][0]==':=' and tokens[i+1][0]=='=':
                tokens[i+1][0]=''
            elif tokens[i][0]=='<>' and tokens[i+1][0]=='>':
                tokens[i+1][0]=''
            elif tokens[i][0]=='<=' and tokens[i+1][0]=='=':
                tokens[i+1][0]=''
            elif tokens[i][0]=='>=' and tokens[i+1][0]=='=':
                
                tokens[i+1][0]=''
            else:
                pass
                
        return removeSpace(tokens)    
#"""stateEngine function. Produces tokens. """
    #TODO: Fix issue with wrong order of tokens.
    def stateEngine(array):
        s=""
        n=''
        st=''
        tokenshlp=[]
        global tokens
        tokens=[] 
        for i in range(0,len(array)):
            
                         
                if array[i][0]  in alphabet :
                    
                        s=s+array[i][0]
                    
                        pass
                elif array[i][0] in num:
                    if array[i-1][0] in alphabet:
                        
                        s=s+array[i][0]
                    else:
                        n=n+array[i][0]
                        if int(n)>32767 or int(n)<-32767:

                            numb=n
                            print('Error int {numb} out of bounds')
                
                else:
                   
                    tokenshlp.append([s,array[i][1]])
                    tokenshlp.append([n,array[i][1]])
                    
                    if ((array[i][0] in arithmsymbol) or  (array[i][0] in  correlationopers) or  (array[i][0] in  seperators) or  (array[i][0] in  groupingopers) ):
                        if array[i][0]==':' and array[i+1][0]=='=':
                            st=':='
                        elif  array[i][0]=='<' and array[i+1][0]=='>':
                            st='<>'
                        elif array[i][0]=='<' and array[i+1][0]=='=':
                            st='<='
                        elif  array[i][0]=='>' and array[i+1][0]=='=':
                            st='>='
                        else:
                            st=array[i][0]
                        tokenshlp.append([st,array[i][1]])
                    n=''
                    s=""
                    st=''
                    continue
                
        tokens=removeExcess(removeSpace(tokenshlp))
        print(tokens)  
            


#"""Helping Function: Removes white char"""  
    def removeWhites(array):
        #print("whites")
        #print(array)
        #print("len array: ")
        #print(len(array))
        ret=[]
        
        whites=[]
        for i in range(len(array)):
            #print("whites for")
            #print(array[i])
            if array[i][0] in whites:
                continue
                
            else:
                ret.append(array[i])
             
        return ret
#"""Helping Function: Removes white char"""      
    def removeSpace(array):
        tokens=[]
        for i in range(0,len(array)):
            if array[i][0]==' ' or array[i][0]=='':
                pass
            else:
                tokens.append(array[i])
        
        return tokens        
        
#"""shapedata function: Shapes data so they can be easily used by stateEngine"""
#TODO: FIX ignore comment issue
    def shapedata(piece):#
        archar=[]
        array=[]
        for i in range(len(piece)):
            tok=splithlp(piece[i][0])
            print(tok)
            for j in range(len(tok)):
                archar.append([tok[j],piece[i][1]])
       # print("shape")
        #print(piece)
        keeplines=[]
        keeplines2=[]
        hlp2line=0
        k=0
        for p in range(len(archar)):
            i=int(p)
            char=archar[i][0]
            #charaft=archar[i+1][0]
            charline=archar[i][1]
            if char=='/':
                if archar[i+1][0]=='/':
                    keeplines.append(charline)
                elif archar[i+1][0]=='*':
                    hlp2lines=charline
                    k=1
                else:
                    pass
            elif char=='*':
                if archar[i+1][0]=='/'and k==1:
                    
                    keeplines2.append([hlp2lines,charline])
                else:
                    pass
            else:
                array.append(archar[i])
                    
        for j,val in enumerate(archar):
             for k in range(len(keeplines2)):
                 
                 if archar[j][1] in list(range(keeplines[k][0],keeplines[k][1]))or archar[j][1] in keeplines:
                     pass
                 else:
                     array.append([archar[j][0],archar[j][1]])
            
        
                    
        stateEngine(array)            
        
        
        
   
    
     
    shapedata(readInlines(file))
    #SreadInlines(file)  
    
    
    return tokens
    
#finaltoken = [lex()]
#counter = 0                               
#"""Start of Syntax"""            
              
def syntax():
    
    global  count ,countarray,symbolarray,arg
    arg=[]
    symbolarray=[] 
    #"""IC helping var"""
    idplace=''
    Eplace=''#addoper
    Tplace=''#muloper
    Fplace=''
    Btrue=[]
    Bfalse=[]
    Qtrue=[]
    Qfalse=[]
    Rtrue=[]
    Rfalse=[]
    condtrue=[]
    condfalse=[]
    
    
    tokens1=lex()
    def tokenlst():#returns only the token value from tokenlst
        global count
        if len(tokens)>0:
            token= tokens1[count][0]
            count+=1
            print("token: "+token)
            print("count: "+str(count))
            return token
        else:
            print("There is a problem with token generation at lexer")
    def tokenlstnum():#return only the token linenum
        global count
        if len(tokens)>0:
            return str(tokens1[count][1])
        else:
            print("There is a problem with token generation at lexer")
            
    def program():
        
        global count
        global symbolarray
        token=tokenlst()
        
        
        if ( token== programtk):
                
                
                #continue
                #counter = counter + 1
                #tokens[0] = lex()
                
                token=tokenlst()
               
                if (isinstance(token,str)==True):
                    #continue
                    name=token
                    
                    token=tokenlst()
                    
                    
                    if (token == LeftBratk):
                        genquad('begin_block',name,'_','_')
                        
                        addScope()
                        recordScope([])
                        block()
                        
                        #scopePatch(idn,entities,offset())
                        genquad('halt','_','_','_')
                        genquad('end_block',name,'_','_')
                        count+=1
                        token=tokenlst()
                        
                        
                        if (token == RightBratk):
                            
                            return
                        else:
                             print("ERROR!!!The '}' expected) in line: "+tokenlstnum())
                    else:
                        print("ERROR!!!The '{' expected in line: "+tokenlstnum())
                else:
                    print("ERROR!!!Program name expected in line: "+tokenlstnum())
        else:
                print("ERROR!!!The keyword 'program' expected in line: "+tokenlstnum())
    
    #<block> ::= <declarations> <subprograms> <statements>
    def block():
       
        declariations()
        subprograms()
        statements()
        
            
    #<declarations> ::= (declare <varlist>;)*

    def declariations():
        
        global count
        
        token=tokenlst()
        
          
        if (token == declaretk):
                    
                    varlist()
                    
                    token=tokenlst()
                    
                    if (token == char1):
                       
                        return    
                        
                        
                    else:
                        print("ERROR!!!The ';' expected in line: "+tokenlstnum())
                        
        else:
                print("ERROR!!!The declariation expected in line: "+tokenlstnum())
                return

    #<varlist> ::= | id ( , id )*            
    def varlist():
        
        global count
        global varforc
        
        token1=tokenlst()
        
        if (isinstance(token1,str)== True and token1 in correlationopers or  token1  in  seperators or token1  in  groupingopers or token1 in keywords):#prepei na einai str alla oxi symbol
            count-=1
            return ""
           
        
        elif (isinstance(token1,str)==True and token1 not in correlationopers and  token1 not in  seperators and token1 not in  groupingopers and token1 not in keywords):#prepei na einai str alla oxi symbol
            
            token2=tokenlst()
            
            recordEntity_var(token1,'?')
            
               
            while token2==',':
                    
                    token3=tokenlst()
                    
                    #na vroume tropo pou na ksexorizei ama einai se function 
                    if ((isinstance(token3,str)==True) and (token3 not in correlationopers) and  (token3 not in  seperators) and (token3 not in  groupingopers)and (token3 not in  keywords)):
                        recordEntity_var(token3,'?')
                        
                        token2=tokenlst()
                        
                        if token2==';':
                            count-=1
                        
                    else:
                        print("ERROR!!! name expected in line: "+tokenlstnum())
                        continue
                
                    break
                    
                    
        else:
            print("ERROR!!!Program name expected in line: "+tokenlstnum())

    #<subprograms> ::= (<subprogram>)*

    def subprograms():
        global count
        global token1
        
        token1=tokenlst()
        
        
        while token1 == functiontk or token1==proceduretk:
            
            subprogram(token1)
                   
        count-=1     
              
    #<subprogram> ::= function id <funcbody> | procedure id <funcbody>            
    def subprogram(t):
        global count
        global arg
        
        if (t == functiontk):
            
            token=tokenlst()
            
            if ((isinstance(token,str)==True) and (token not in correlationopers) and  (token not in  seperators) and (token not in  groupingopers)):
                fname= token
                genquad('begin_block',fname,'_','_')
                
                addScope()
                recordScope([])
                recordEntity_fun(fname,'?')
                  
                funcbody()
                funbackpatchstartquad(fname)
                funbackpatchframelen(fname,symbolarray[-1].getoffset())
                removeScope()
                ##arg=[]
                genquad('end_block',fname,'_','_')
            else:
                print("ERROR!!!The function name expected in line: "+tokenlstnum())
           
        elif (t == proceduretk):
            
            token=tokenlst()
           
            if ((isinstance(token,str)==True) and (token not in correlationopers) and  (token not in  seperators) and (token not in  groupingopers)):
                #t2 = lex()
                pname= token
                genquad('begin_block',pname,'_','_')
                addScope()
                recordScope([])
                recordEntity_fun(pname,'?')
                  
                funcbody()
                funbackpatchstartquad(pname)
                funbackpatchframelen(pname,symbolarray[-1].getoffset())
                removeScope(symbolarray[-1])
                arg=[]
                genquad('end_block',pname,'_','_')
            else:
                print ("ERROR!!!Procedure name expecte in line: "+tokenlstnum())
        elif (t != proceduretk):
            print("ERROR!!!The keyword 'procedure' expected in line: "+tokenlstnum())        
        elif (t != functiontk):
            print("ERROR!!!The keyword 'function' expected in line: "+tokenlstnum())         
        
           
    #<funcbody> ::= <formalpars> { <block> }
    def funcbody():
            global count
            formalpars()
           
            token=tokenlst()
            
            if (token == LeftBratk):
                block()
                
                token=tokenlst()
                
                if (token == RightBratk):
                    
                    removeScope(symbolarray[-1])
                else:
                    print ("ERROR!!!The '}' expected in line: "+tokenlstnum())
            else:
                print("ERROR!!!The '{' expected in line: "+tokenlstnum())
      
    #<formalpars> ::= ( <formalparlist> )

    def formalpars():
        global count
        token=tokenlst()
        
        if (token == LeftPartk):
            
            formalparlist()
            token=tokenlst()
            
            if (token == RightPartk):
                pass 
            else:
                print ("ERROR!!!The ')' expected formalpars in line: "+tokenlstnum())
        else:
            print("ERROR!!!The '(' expectedformalpars in line: "+tokenlstnum())
            
    #<formalparlist> ::= <formalparitem> ( , <formalparitem> )* | 
    def formalparlist():
        global count
        
        formalparitem()
        token1=tokenlst()
        
        
        while token1 == ',' :
            
                
            
            formalparitem()
            token1=tokenlst()
            
            #break
        count-=1
           
           
        
                
    #<formalparitem> ::= in id | inout id 
    def formalparitem():
        global count
        global arg
        token1=tokenlst()
        
        
        if (token1 == intk):
            token=tokenlst()
            
            if ((isinstance(token,str)==True) and (token not in correlationopers) and  (token not in  seperators) and (token not in  groupingopers)):
                idn=token
                genquad('par',idn,'CV','_')
                recordEntity_par(idn,'CV')
                arg=recordArgument('CV','in')
                #symbolarray[-1].entities[-1].addargument(arg)
                
                
            else:
                print("ERROR!!!The in name expected in line: "+tokenlstnum())
        
        elif (token1 == inouttk):
            token=tokenlst()
            
            if((isinstance(token,str)==True) and (token not in correlationopers) and  (token not in  seperators) and (token not in  groupingopers)):
                idn2=token
                genquad('par',idn2,'REF','_')
                recordEntity_par(idn2,'REF',)
                
                arg=recordArgument('REF','inout')
                #symbolarray[-1].entities[-1].addargument(arg)
            else:
                 print("ERROR!!!The inout name expected in line: "+tokenlstnum())
        elif (token1 != intk):
            print("ERROR!!!The keyword 'in' expected in line: "+tokenlstnum())         
        elif (token1 != inout):
            print("ERROR!!!The keywortd 'inout' expected in line: "+tokenlstnum())
            

    #<statements> ::= <statement> | { <statement> ( ; <statement> )* }
    def statements():#edo prepei na vroume tropo na diaxiristoume tin pithanotita or | 
        global count
        token=tokenlst()
        
        
        if token not in statementslst and token != LeftBratk:
            
            pass

        elif token in statementslst:
            print('statement ok')
            statement()
            
            
        elif(token == LeftBratk):
           
            statement()
            token2=tokenlst()
            
            while(token2==char1):
                
                statement()
                token2=tokenlst()
                
                        
                 
                   
                #count-=1    
            
            if(token2==RightBra):
                pass
            else:
                print("ERROR!!!The '}' expected in line: "+tokenlstnum())
        else:
            print("ERROR!!!The '{' expected in line: "+tokenlstnum())



    #<statement> ::= <assignment-stat> |<if-stat> |<while-stat> |<doublewhile-stat> |<loop-stat> |<exit-stat> |<forcase-stat> |<incase-stat> |<call-stat> |<return-stat> |<input-stat> |<print-stat>         
    def statement():
        
        global count
        
        token=tokenlst()
        
        #count+=1
        if(token==assigmenttk):#themataki me :=
            
            assigment_stat()
        elif(token==iftk):
                
            if_stat()
        elif(token==whiletk):
            
            while_stat()
        elif(token==doublewhiletk):
            
            doublewhile_stat()
        elif(token==looptk):
            
            loop_stat()
        elif(token==exittk):
            
            exit_stat()
        elif(token==forcasetk):
            
            forcase_stat()
        elif(token==incasetk):
            
            incase_stat()
        elif(token==calltk):
            
            call_stat()
        elif(token==returntk):
            
            return_stat()
        elif(token==inputtk):
            
            input_stat()
        elif(token==printtk):
            
            print_stat()
        return

    #<assignment-stat> ::= id := <expression>

    def assignment_stat(): #otan lisoume to thema me to := tha einai komple
        global count
        count-=2
        token=tokenlst()
        
        if((isinstance(token,str)==True) and (token not in correlationopers) and  (token not in  seperators) and (token not in  groupingopers)):
            t2=tokenlst()
            if(t2==assigmenttk):
                
                t=expression()
                genquad(':=',t,'_',token)
                recordEntity_con(t1,t)##???????????????????
                
            else:
                print("ERROR!!!The ':=' expected in line: "+tokenlstnum()) 
        else:
            print("ERROR!!!The assigment name expected in line: "+tokenlstnum()) 

    #<if-stat> ::= if (<condition>) then <statements> <elsepart>

    def if_stat():
        global count
        nonlocal Btrue
        token=tokenlst()
        
        
        if(token==LeftPartk):
            
            token=tokenlst()
            
            condition()
            if(token==RightPartk):
                token=tokenlst()
                
                if(token==thentk):
                    statements()
                    backpatch(Btrue,nextquad())#c theortika oti einai true
                    iflist=makelist(nextquad())
                    
                    k=genquad('jump','_','_','_')
                    Bfalse.append(k)
                    
                    elsepart(iflist)
                else:
                    print("ERROR!!!The keyword 'then' expected in line: "+tokenlstnum())
            else:
                print("ERROR!!!The ')' expected in line: "+tokenlstnum())
        else:
            print("ERROR!!!The '(' expected in line: "+tokenlstnum()) 

    #<elsepart> ::=  | else <statements>
            # ti tha kanoume me to e to keno xoris else diladi 
    def elsepart(iflist):
        global count
        nonlocal Bfalse
        token=tokenlst()
        
        iflist= iflist
        
        if(token==elsetk):
            statements()
            backpatch(Bfalse,nextquad())
            
            backpatch(iflist,nextquad())

        else:
            
            pass     

    #<while-stat> ::= while (<condition>) <statements>
    def while_stat():
        global count
        nonlocal Btrue, Bfalse
        token=tokenlst()
        
        if(token==LeftPartk):
            Bquad=nextquad()
            condition()
            token=tokenlst()
            
            if(token==RightPartk):
                backpatch(Btrue,nextquad())
                statements()
               
                genquad('jump','_','_',Bquad)
                backpatch(Bfalse,nextquad())
                
            else:
                print("ERROR!!!The ')' expected while in line: "+tokenlstnum()) 
        else:
            print("ERROR!!!The '(' expected while in line: "+tokenlstnum())
        
    """
    This is a multiline
comment.
    #<doublewhile-stat> ::= doublewhile (<condition>) <statements>
    # else <statements>

    def doublewhile_stat():

        
        t1=lex()
        if(t1==LeftPartk):
            Bquad=nextquad()
            condition()
            t1=lex()
            backpatch(t,nextquad())
            genquad('jump','_','_',Bquad)
            if(t3==RightPartk):
                
                t=statements()
                backpatch(t,nextquad())
                genquad('jump','_','_',Bquad)
                
                t1=lex()
                if(t1==elsetk):
                    
                    f=statements()
                    backpatch(f,nextquad())
                else:
                    print("ERROR!!!The keyword 'else' expected") 
                        
                        
            else:
                print("ERROR!!!The ')' expected") 
        else:
            print("ERROR!!!The '(' expected")
        
            

    #<loop-stat> ::= loop <statements>
    def loop_stat():
        
        
        statements()
        
    #<exit-stat> ::= exit
    def exit_stat():#mexri stigmis den xreiazete na kanei kati
        #if(t1==exittk):
         #   t1=lex()
        #else:
         #    print("ERROR!!!The keyword 'exit' expected")
        pass
        """
    #<forcase-stat> ::= forcase
    # ( when (<condition>) : <statements> )*
    # default: <statements> 
    def for_case():
        global count
        nonlocal Btrue,Bfalse                                       
        
            
        t3=tokenlst()
          
        
        while t3==whentk:
            t4=tokenlst()
            t4num=tokenlstnum()
            if(t4==LeftPartk):
                sQuad=nextquad()
                condition()
                t5=tokenlst()
                t5num=tokenlstnum()
                            
                if(t5==RightPartk):
                    t6=tokenlst()
                    t6num=tokenlstnum()
                    if(t6==char2):
                        statements()
                        backpatch(Btrue,sQuad)                            
                    else:
                        print("ERROR!!!The  ':' expected in line: "+t6num)
                else:
                    print("ERROR!!!The ')' expected in line "+t5num)
            else:
                print("ERROR!!!The '(' expected in line: "+t4num)
        
                
        
        if(t3==defaulttk):
            token=tokenlst()
            
            if(token==char2):
                statements()
                backpatch(Bfalse,nextquad())
            else:
                print("ERROR!!!The ':' expected in line: "+tokenlstnum())
        else:
            print("ERROR!!!The keyword 'default' expected in line: "+tokenlstnum())

        


    '''
    #<incase-stat> ::= incase
    #( when (<condition>) : <statements> )*
    def incase_stat():
                                      #kai auti diorthosi prosoxi me tis parentheseis kai ta when 
        t1=lex()
        while(t1==incasetk):
            if(t2==LeftPartk):
                t2=lex()
                if(t3==whentk):
                    t3=lex()
                    if(t4==lex()):
                        condition()
                        if(t4==RightPartk):
                            token=lex()
                            if(t5==char2):
                                token=lex()
                                statements()
                            else:
                                print("ERROR!!!The  ':' expected")
                        else:
                            print("ERROR!!!The ')' expected")
                    else:
                        print("ERROR!!!The '(' expected")
                else:
                    print("ERROR!!!The keyword 'when' expected")
            else:
                print("ERROR!!!The '(' expected")
         
                
    
        

    '''
    #<return-stat> ::= return <expression>
    def return_stat():
            global count
            nonlocal Eplace
            expression()
            t=Eplace
            genquad('retv',t,'_','_')
            
    #<call-stat> ::= call id <actualpars>

    def call_stat():
        global count
        t1=tokenlst()
        
        if((isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers)):
            
            
            actualpars()
               
                
                
        else:        
                print("ERROR!!!The call name expected in line: "+tokenlstnum())
        
            
    #<print-stat> ::= print (<expression>)
    def print_stat():
        global count
        nonlocal Eplace
        
        t=tokenlst()
        t1num=tokenlstnum()
        if(t == LeftPartk):
            
            expression()
            e=Eplace
            t=tokens()
            tnum=tokenlstnum()
            if (t == RightPartk):
                genquad('out',e,'_','_')
            else:
                print("ERROR!!!The ')' expected in line: "+tnum)
        else:
            print("ERROR!!!The '(' expected in line: "+t1num)
       
            
    #<input-stat> ::= input (id)
    def input_stat():
        global count
        t1=tokenlst()
        t111num=tokenlstnum()
        if (t1 == LeftPartk):
            t1=tokenlst()
            t11num=tokenlstnum()
            if((isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers)):
                idn=t1
                t1=tokenlst()
                t1num=tokenlstnum()
                if (t1== RightPartk):
                    genquad('inp',idn,'_','_')
                else:
                    print("ERROR!!!The ')' expected input in line: "+t1num)
            else:
                print("ERROR!!!The input name expected in line: "+t11num)
        else:
            print("ERROR!!!The '(' expected in line: "+t111num)
    
            
    #<actualpars> ::= ( <actualparlist> ) 
    def actualpars():
        global count
        t1=tokenlst()
        t1num=tokenlstnum()
        if (t1 == LeftPartk):
            
            actualparlist()
            t1=tokenlst()
            t2num=tokenlstnum()
            if (t1 == RightPartk):
                pass
            else:
                print("ERROR!!!The ')' epxected in line: "+t2num)
            
        else:
            print("ERROR!!!The '(' expected in line: "+t1num)
        return  
            
    #<actualparlist> ::= <actualparitem> ( , <actualparitem> )* | 
    def actualparlist():
        global count
        
        actualparitem()
        t1=tokenlst()
        
        while t1 == Comatk :
            
               
            actualparitem()
            t1=tokenlst()
            
            
            break
        count-=1
        return    
    #<actualparitem> ::= in <expression> | inout id
    def actualparitem():
        global count
        nonlocal Eplace
        t1=tokenlst()
        
        if (t1 == intk):
             
             expression()
             e=Eplace
             genquad('par',e,'CV','_')
             recordEntity_par(e,'CV')
             
        elif (t1 == inouttk):
                t1=tokenlst()
                t2num=tokenlstnum()
                if((isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers)):
                    genquad('par',t1,'REF','_')
                    recordEntity_par(t1,'REF')
                   
                else:
                    print("ERROR!!!The inout name expected in line: "+t2num)
        #elif (t1 != inout):
         #   print("ERROR!!!The keyword 'inout' expected in line: "+tokenlstnum())
        #elif (t1 != intk):
         #   print("ERROR!!!The keyword 'in' expected in line: "+tokenlstnum())
        
        return 
    #<condition> ::= <boolterm> (or <boolterm>)*

    def condition():
        global count
        nonlocal Btrue, Bfalse,Qtrue,Qfalse
        
        
        boolterm()
        Btrue=Qtrue
        Bfalse=Qfalse
        #count+=1
        t1=tokenlst()
        
        
        #count+=1
        while t1 == ortk:
            backpatch(Bfalse,nextquad())
            boolterm()
            Btrue=merge(Btrue,Qtrue)
            Bfalse=Qfalse
            t1=tokenlst()
            
            break 
            
        
           
        return 
                
    #<boolterm> ::= <boolfactor> (and <boolfactor>)*

    def boolterm():
        global count
        nonlocal Qtrue,Qfalse,Rtrue,Rfalse
        boolfactor()
        Qtrue=Rtrue
        Qfalse=Rfalse
        t1=tokenlst()
        #count+=1
        while t1== andtk :
            backpatch(Qtrue,nextquad())
            boolfactor()
            Qfalse=merge(Qfalse,Rfalse)
            Qtrue=Rtrue
            t1=tokenlst()
            
            break
            count-=1
        return       
    #<boolfactor> ::= not [<condition>] | [<condition>] |<expression> <relational-oper> <expression> 
    def boolfactor():
        global count
        nonlocal Rtrue,Rfalse,Btrue,Bfalse,Eplace
        
        t1=tokenlst()
        t1num=tokenlstnum()
        #count+=1
        if (t1 == nottk):
            t2=tokenlst()
            t2num=tokenlstnum()
            if (t2 == LeftBrackettk):
                
                condition()
                Rtrue=Bfalse
                Rfalse=Btrue
                t2=tokenlst()
                t21num=tokenlstnum()
                if (t2 == RightBrackettk):
                    return
                else:
                    print("ERROR!!!The ']' expected in line: "+t21num)
            else:
                print("ERROR!!!The '[' exptected in line: "+t2num)
        elif (t1 == LeftBrackettk):
            
            condition()
            Rtrue=Btrue
            Rfalse=Bfalse
            t1=tokenlst()
            t12num=tokenlstnum()
                    
            if (t1 == RightBrackettk):
                return
            else:
                print("ERROR!!!The ']' exptected in line: "+t12num)
        
        
                    
        else:
            count-=1
            expression()
            e1=Eplace
            
            relop=relationaloper()
            
            
            expression()
            e2=Eplace
            
            Rtrue=makelist(nextquad())
            genquad(relop,e1,e2,'_')
            Rfalse=makelist(nextquad())
            genquad('jump','_','_','_')
            
         
            return                
                
            
       
    #<expression> ::= <optional-sign> <term> ( <add-oper> <term>)* 
    def expression():
        global count
        nonlocal Tplace,Eplace
        
        #optionalsign()
        term()
        t1=Tplace
        
        op=addoper()
        while op in ['+','-']:
                w=newtemp()
                op=addoper()
                term()
                
                t2=Tplace
                genquad(op,t1,t2,w)
                t1=w
                break
        #count-=1    
        Eplace=t1
        
        return 
                
    #<term> ::= <factor> (<mul-oper> <factor>)*
    def term():
        global count
        nonlocal Tplace
        
        f1=factor()
        
        op=muloper()
        while op in ['*','/']:
                w=newtemp()
                
                
                
                f2=factor()
                
                genquad(op,f1,f2,w)
                f1=w
                break
                
        Tplace = f1
        
        return    
    #<factor> ::= constant | (<expression>) | id <idtail>
    def factor():
        nonlocal Eplace
        
        global count
        ret=''
        p=0
        t1=tokenlst()
        t1num=tokenlstnum()
        
        if t1!= LeftPartk and  (isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers):
            ret= t1
            p=1
            
            
        elif (t1 == LeftPartk and p==0):
            
            expression()
            ret=Eplace
            t2=tokenlst()
            t2num=tokenlstnum()
            
            if (t2 == RightPartk):
                pass
            else:
                print("ERROR!!!The ')' expected in line: "+t2num)
        elif(t1 != LeftPartk and p==0):
            print("ERROR!!!The '(' expected in line: "+t1num())
                
        elif (isinstance(t1,str)==True) and (t1 not in correlationopers) and  (t1 not in  seperators) and (t1 not in  groupingopers):
            thlp=genquad(':=','_','_',t1)
            idtail()
            
        return ret
           
    #<idtail> ::= | <actualpars>

    def idtail(): #kati prepei na kanoume edo
        global count
        t=tokenlst()
        
        if t=='(':
            for i in range(len(helpIC)):
                if thlp == i:
                    actualpars()
                    helpIc[i][1]='??'


    #<relational-oper> ::= = | <= | >= | > | < | <>
    def relationaloper():
        global count
        t1=tokenlst[count]
        
        
        if (t1 == equalstk):
            #t1 = lex()
            return t1
        elif (t1 == mineqtk):
            
            #t1 = lex()
            return t1
        elif (t1 == maxeqtk):
            
                #t1 = lex()
            return t1
        elif (t1 == maxtk):
                #t1 = lex()
            return t1
        elif (t1 == mintk):
                #t1 = lex()
            return t1
        elif (t1 == minmaxtk):
                #t1 = lex()
            return t1
        else:
            return
        #elif (t1 != minmaxtk):
         #   print("ERROR!!!The '<>' expected")
        #elif (t1 != mintk):
         #   print("ERROR!!!The '<' expected")
        #elif (t1 != maxtk):
         #   print("ERROR!!!The '>' expected")
        #elif (t1 != maxeqtk):
         #   print("ERROR!!!The '>=' expected")
        #elif (t1 != mineqtk):
         #   print("ERROR!!!The '<=' expected")
        #elif (t1 != equalstk):
           # print("ERROR!!!The '=' expected")

    #<add-oper> ::= + | -

    def addoper():
        global count
        token=tokenlst()
        
        if (token == plustk):
            return token
        elif (token==minustk):
            return token
        else:
            count-=1
            
        
            
      
        
    #<mul-oper> ::= * | /

    def muloper():
        global count
        token=tokenlst()
        #count+=1
        if (token == multitk):
            return
        elif (token == dividetk):
            return
        else:
            
            count-=1
            
        
    #<optional-sign> ::= | <add-oper>
    #TODO: FIX NOTHING CASE
    def optionalsign():
        
        addoper()
        return 
    program()          
syntax()
file.close()
print(symbolarray)
cfile(helpIC)
intfile(helpIC)
#cfile(helpIC)

  
