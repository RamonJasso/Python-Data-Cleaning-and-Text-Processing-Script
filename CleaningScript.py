import csv
xyT= []
nBase =[]
with open("Xytech.txt") as f:
    xytech_file = f.read().splitlines()
    
baselight_file = open("BaseLight_export.txt", "r")

for line in baselight_file:
    

    parseLine= line.split()
    
    if parseLine:
        cFolder = parseLine.pop(0)
        pFolder = cFolder.split("/")
        pFolder.pop(1)
        nFolder = "/".join(pFolder)

        for check in xytech_file:
            if nFolder in check:
                cFolder = check.strip()
            
        tStart = 0
        tLast = 0

        for number in parseLine:
            if not number.isnumeric():
                continue
            if tStart == 0:
                tStart = number
                continue
            if number == str(int(tStart)+1):
                tLast = number
                continue
            elif number == str(int(tLast)+1):
                tLast = number
                continue
            else:
                if int(tLast) >0:
                    nBase.append(f"{cFolder} {tStart}-{tLast}")
                else:
                    nBase.append(f"{cFolder} {tStart}")
                tStart = number
                tLast = 0
        if int(tLast) > 0:
            nBase.append(f"{cFolder} {tStart}-{tLast}")
        else:
            nBase.append(f"{cFolder} {tStart}")
            tStart = number
            tLast = 0




#nBase = '\n'.join(nBase)        
#print(nBase)


for line in xytech_file:
    if "/" not in line:
        xyT.append(line.strip())

#xyTL = list(xyT)
nXytech = xyT + nBase
print(nXytech)

with open("project1.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows([item.split() for item in nXytech])
        



