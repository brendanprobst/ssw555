#interprets GEDCOM file and determines if each line is valid
import os
print("Working dir:", os.getcwd())
def formatLevel0(list):
    #checks that level 0 entries are a person,family, or note
    result = ""
    if (list[1] == 'NOTE' or list[1] == 'HEAD' or list[1] == 'TRLR'):
        result = list[1] + '|Y|' + list[2]
    elif (list[2] == 'FAM' or list[2] == 'INDI'):
        result = list[2] + '|Y|' + list[1]
    else:
        result = list[1] + '|N|' + list[2]
    return result

def formatLevel1(list):
    #checks that level 1 entries are a not a date
    result = ""
    isGood = 'N'
    level1Values = ['NAME','SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'CHIL', 'DIV', 'WIFE', 'HUSB']
    if (list[1] in level1Values):
        isGood = 'Y'
    result = list[1] + '|' + isGood + '|' + list[2]
    return result
def formatLevel2(list):
    #checks that level 2 entries are are valid
    result = ""
    isGood = 'N'
    if (list[1] == 'DATE'):
        isGood = 'Y'
    result = list[1] + '|' + isGood + '|' + list[2]
    return result  
    
def formatList(line):
    #takes a string and returns a list of size 3
    result = ['level','arg','ad_arg']
    list = line.split()
    result[0] = list[0]
    result[1] = list[1]
    result[2] = ' '.join(list[2:])
    return result


def formatOutput(line):
    print('--> ',line) #prints input line
    result = "" #result will be appended to 
    list = formatList(line)
    level = list[0]
    result = level + '|'
    if (level == '0'):
        #test if its a note or the start of a person or family
        result = result + formatLevel0(list)
    if (level == '1'):
        #test if its a person or family attribute
        result = result + formatLevel1(list)
    if (level == '2'):
        #test if its a date
        result = result + formatLevel2(list)
    return '<-- ' + result

#takes input file
file = open('HW2_GEDCOM/testData.txt','r');
#loop through each line in the file
for line in file:
    inputLine = line.strip()
    print(formatOutput(inputLine))