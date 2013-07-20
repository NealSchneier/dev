import sys
import csv
from player import Player
from decimal import Decimal

def go(file, system):
     hitter = -1
     f = 0
     reader = csv.reader(open(file), delimiter=',')

     runs = -1
     hits = -1
     doubles = -1
     triples = -1
     homeruns = -1
     rbi = -1
     sb = -1
     cs = -1
     k = -1
     bb = -1
     
     g = -1
     wins = -1
     losses = -1
     cg = -1
     sho = -1
     sv = -1
     hr = -1
     strikeouts = -1
     hld = -1
     bsv = -1
     er = -1
     ip = -1
     
     for row in reader:
          
          row = str(row).strip('[]')
          if f == 0:
               f = 1
               #based off the first row gets the basic data
               try:
                    runs = row.index("'R'")
                    runs = row[:runs].count(',')
                    
                    hits = row.index("'H'")
                    hits = row[:hits].count(',')
                    
                    doubles = row.index("'2B'")
                    doubles = row[:doubles].count(',')
                    
                    triples = row.index("'3B'")
                    triples = row[:triples].count(',')
                    
                    homeruns = row.index("'HR'")
                    homeruns = row[:homeruns].count(',')
                    
                    rbi = row.index("'RBI'")
                    rbi = row[:rbi].count(',')
                    
                    sb = row.index("'SB'")
                    sb = row[:sb].count(',')

                    cs = row.index("'CS'")
                    cs = row[:cs].count(',')

                    k = row.index("'SO'")
                    k = row[:k].count(',')

                    bb = row.index("'BB'")
                    bb = row[:bb].count(',')

                    hitter = 1 #means it is a hitter
               except:
                    #pitchers data
                    try:
                         g = row.index("G")
                         g = row[:g].count(',')
                    except:
                         g = -1

                    wins = row.index("'W'")
                    wins = row[:wins].count(',')

                    losses = row.index("'L'")
                    losses = row[:losses].count(',')

                    try:
                         cg = row.index("'CG'")
                         cg = row[:cg].count(',')
                    except:
                         cg = -1
                    try:
                         sho = row.index("'SHO'")
                         sho = row[:sho].count(',')
                    except:
                         sho = -1

                    try:
                         sv = row.index("'SV'")
                         sv = row[:sv].count(',')
                    except:
                         sv = -1

                    hr = row.index("'HR'")
                    hr = row[:hr].count(',')

                    strikeouts = row.index("'SO'")
                    strikeouts = row[:strikeouts].count(',')
                    
                    try:
                         hld = row.index("'HLD'")
                         hld = row[:hld].count(',')
                    except:
                         hld = -1

                    try:
                         bsv = row.index("'BSV'")
                         bsv = row[:bsv].count(',')
                    except:
                         bsv = -1

                    try:
                         er = row.index("'R'")
                         er = row[:er].count(',')
                    except:
                         er = -1
                    try:
                         ip = row.index("'IP'")
                         ip = row[:ip].count(',')
                    except:
                         ip = -1
                    hitter = 0 #player is not hitter
               
          else:
               
               #get the players name
               tempRow = str(row)
               
               tempRow = tempRow[1:]
               temp = tempRow.index(',')-1
               Name = tempRow[:temp]

               if hitter == 1:
                    
                    i = 0
                    tempRow = str(row)
                    while i < hits:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    Hits = tempRow[2:temp-1]

                    i = 0
                    tempRow = str(row)
                    while i < runs:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    Runs = tempRow[2:temp-1]
                    
                    i = 0
                    tempRow = str(row)
                    while i < doubles:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    Doubles = tempRow[2:temp-1]

                    i = 0
                    tempRow = str(row)
                    while i < triples:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    Triples = tempRow[2:temp-1]

                    i = 0
                    tempRow = str(row)
                    while i < homeruns:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    Homeruns = tempRow[2:temp-1]

                    i = 0
                    tempRow = str(row)
                    while i < rbi:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    RBI = tempRow[2:temp-1]

                    i = 0
                    tempRow = str(row)
                    while i < sb:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    SB = tempRow[2:temp-1]
                    
                    i = 0
                    tempRow = str(row)
                    while i < bb:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    BB = tempRow[2:temp-1]

                    i = 0
                    tempRow = str(row)
                    while i < cs:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    CS = tempRow[2:temp-1]

                    i = 0
                    tempRow = str(row)
                    while i < k:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    K = tempRow[2:temp-1]
                    
                    
                    #total = int(Runs) + int(Hits) + (int(Doubles) * 2) + (int(Triples) * 3 )+ (int(Homeruns) * 4 )+ int(RBI) + int(SB) + int(BB) - (.5 * int(K)) - (.5 * int(CS))
                    total = int(Runs) + int(Hits) + int(int(Hits) - int(Doubles) - int(Triples) -int(Homeruns)) + (int(Doubles) * 2) + (int(Triples) * 3 )+ (int(Homeruns) * 4 )+ int(RBI) + int(SB) + int(BB) - (.5 * int(K)) - (.5 * int(CS))
                    try:
                         temp = mydict[Name]
                         if system == 'zips':
                              mydict[Name].zips = total
                         elif system == 'fans':
                              mydict[Name].fans = total
                         elif system == 'steamer':
                              mydict[Name].steamer = total
                         elif system == 'oliver':
                              mydict[Name].oliver = total
                         elif system == 'rotochamp':
                              mydict[Name].rotochamp = total
                    except:
                         #if the player is not in the system yet
                         if system == 'zips':
                              me = Player(Name, total, 0, 0, 0, 0)
                         elif system == 'fans':
                              me = Player(Name, 0, total, 0, 0, 0)
                         elif system == 'steamer':
                              me = Player(Name, 0, 0, total, 0, 0)
                         elif system == 'oliver':
                              me = Player(Name, 0, 0, 0, total, 0)
                         elif system == 'rotochamp':
                              me = Player(Name, 0, 0, 0, 0, total)
                         mydict[Name] = me
               elif hitter == 0:
                    i = 0
                    tempRow = str(row)
                    while i < wins:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    Wins = tempRow[2:temp-1]

                    i = 0
                    tempRow = str(row)
                    while i < losses:
                         temp = tempRow.index(',')
                         tempRow = tempRow[temp+1:]
                         i = i+1
                    temp = tempRow.index(',')
                    Losses = tempRow[2:temp-1]

                    i = 0
                    tempRow = str(row)
                    if g != -1:
                         while i < g:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         G = tempRow[2:temp-1]
                    else:
                         G = 0

                    i = 0
                    tempRow = str(row)
                    if cg != -1:
                         while i < cg:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         CG = tempRow[2:temp-1]
                    else:
                         CG = 0

                    i = 0
                    tempRow = str(row)
                    if sho != -1:
                         while i < sho:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         SHO = tempRow[2:temp-1]
                    else:
                         SHO = 0

                    i = 0
                    tempRow = str(row)
                    if sv != -1:
                         while i < sv:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         SV = tempRow[2:temp-1]
                    else:
                         SV = 0

                    i = 0
                    tempRow = str(row)
                    if hr != -1:
                         while i < hr:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         HR = tempRow[2:temp-1]
                    else:
                         HR = 0

                    i = 0
                    tempRow = str(row)
                    if strikeouts != -1:
                              
                         while i < strikeouts:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         Strikeouts = tempRow[2:temp-1]
                    else:
                         Strikeouts = 0

                    i = 0
                    tempRow = str(row)
                    if hld != -1:
                              
                         while i < hld:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         HLD = tempRow[2:temp-1]
                    else:
                         HLD= 0

                    i = 0
                    tempRow = str(row)
                    if bsv != -1:
                         
                         while i < bsv:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         BSV = tempRow[2:temp-1]
                    else:
                         BSV = 0
                    i = 0    
                    tempRow = str(row)
                    if er != -1:
                         
                         while i < er:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         ER = tempRow[2:temp-1]
                    else:
                         ER = 0
                    i = 0
                    tempRow = str(row)
                    if ip != -1:
                         
                         while i < ip:
                              temp = tempRow.index(',')
                              tempRow = tempRow[temp+1:]
                              i = i+1
                         temp = tempRow.index(',')
                         IP = tempRow[2:temp-1]
                    else:
                         IP = 0

                    #total = int(G) + (int(Wins) * 12) + (int(Losses) * -6) + (int(CG) * 6 )+ (int(SHO) * 3 )+ (int(SV) * 6) + (int(HR) * -1) + (int(Strikeouts) * 1.5) + (int(HLD) * 3) + (int(BSV) * -3) - int(ER)
                    #total = (int(Wins) * 10) + (int(Losses) * -5) + (int(CG) * 3 )+ (int(SHO) * 0 )+ (int(SV) * 7) + (int(HR) * 0) + (int(Strikeouts) * 1) + (int(HLD) * 3) + (int(BSV) * -4) - int(ER) + Decimal(IP)
                    total = (int(Wins) * 10) + (int(Losses) * -5) + (int(SHO) * 5 )+ (int(SV) * 8) + int(int(Strikeouts) * 1.5) + (int(BSV) * -4) - (int(ER)* 1) +  (int(Decimal(IP)) * 1) + (int(CG) * 5)
                    try:
                         temp = mydict[Name]
                         if system == 'zips':
                              mydict[Name].zips = total
                         elif system == 'fans':
                              mydict[Name].fans = total
                         elif system == 'steamer':
                              mydict[Name].steamer = total
                         elif system == 'oliver':
                              mydict[Name].oliver = total
                         elif system == 'rotochamp':
                              mydict[Name].rotochamp = total
                    except:
                         #if the player is not in the system yet
                         if system == 'zips':
                              me = Player(Name, total, 0, 0, 0, 0)
                         elif system == 'fans':
                              me = Player(Name, 0, total, 0, 0, 0)
                         elif system == 'steamer':
                              me = Player(Name, 0, 0, total, 0, 0)
                         elif system == 'oliver':
                              me = Player(Name, 0, 0, 0, total, 0)
                         elif system == 'rotochamp':
                              me = Player(Name, 0, 0, 0, 0, total)
                         mydict[Name] = me
                    

mydict = {}
go("fans.csv", 'fans')          
go("zips.csv", 'zips')
go("oliver.csv", 'oliver')
go("rotochamp.csv", 'rotochamp')
go("steamer.csv", 'steamer')

f = open("hitters.csv", "w")
f.write("Name,Zips,Fans,Steamer,Oliver,Rotochamp,Average,Total\n")
for item in mydict:
     f.write(mydict[item].name + "," + str(mydict[item].zips) + "," + str(mydict[item].fans) + "," + str(mydict[item].steamer) + "," + str(mydict[item].oliver) + "," + str(mydict[item].rotochamp) + "," + str(mydict[item].average()) + "," + str(mydict[item].total()) + "\n")
f.close()

p = open("players.csv", "w")
p.write("Name,Position,Zips,Fans,Steamer,Oliver,Rotochamp,Average,Total\n")
for item in mydict:
     p.write(mydict[item].name + ",Hitter,"+ str(mydict[item].zips) + "," + str(mydict[item].fans) + "," + str(mydict[item].steamer) + "," + str(mydict[item].oliver) + "," + str(mydict[item].rotochamp) + "," + str(mydict[item].average()) + "," + str(mydict[item].total()) + "\n")

mydict.clear()

go("fansPitchers.csv", 'fans')
go("zipsPitchers.csv", 'zips')
go("oliverPitchers.csv", 'oliver')
go("rotochampPitchers.csv", 'rotochamp')
go("steamerPitchers.csv", 'steamer')

f = open("pitchers.csv", "w")
f.write("Name,Zips,Fans,Steamer,Oliver,Rotochamp,Average,Total\n")
for item in mydict:
     f.write(mydict[item].name + "," + str(mydict[item].zips) + "," + str(mydict[item].fans) + "," + str(mydict[item].steamer) + "," + str(mydict[item].oliver) + "," + str(mydict[item].rotochamp) + "," + str(mydict[item].average()) + "," + str(mydict[item].total()) + "\n")
f.close()

for item in mydict:
     p.write(mydict[item].name + ",Pitcher," + str(mydict[item].zips) + "," + str(mydict[item].fans) + "," + str(mydict[item].steamer) + "," + str(mydict[item].oliver) + "," + str(mydict[item].rotochamp) + "," + str(mydict[item].average()) + "," + str(mydict[item].total()) + "\n")

p.close()
mydict.clear()



