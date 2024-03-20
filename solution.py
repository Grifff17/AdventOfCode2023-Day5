def solvepart1():
    #format input data
    data = fileRead("input.txt")
    seeds = data[0].split(":")[1].strip().split(" ")
    data = data[2:]
    allMapsStrings = []
    currentMap = []
    for row in data:
        if (row != "\n"):
            currentMap.append(row)
        else:
            allMapsStrings.append(currentMap)
            currentMap = []
    allMapsStrings.append(currentMap)
    maps = []
    for mapString in allMapsStrings:
        map = []
        for row in mapString[1:]:
            map.append(row.strip().split(" "))
        maps.append(map)
    print(maps)

    #figure out location for each seed
    leastLocation = 9999999999999
    for seed in seeds:
        currentVal = int(seed)
        for map in maps:
            currentVal = readMap(map, currentVal)
        if(currentVal<leastLocation):
            leastLocation = currentVal
    print(leastLocation)

#read map and input value to produce output value
def readMap(map, inval):
    outval = -1
    for row in map:
        if (inval >= int(row[1]) and inval < int(row[1])+int(row[2])):
            outval = int(row[0]) + (inval-int(row[1]))
    if outval == -1:
        outval = inval
    return outval

def solvepart2():
    #format input data
    data = fileRead("input.txt")
    seedsRaw = data[0].split(":")[1].strip().split(" ")
    seeds = []
    temp = ""
    for i in range(len(seedsRaw)):
        if ( i%2 == 0 ):
            temp = seedsRaw[i]
        else:
            seeds.append([int(temp),int(seedsRaw[i])])
    data = data[2:]
    allMapsStrings = []
    currentMap = []
    for row in data:
        if (row != "\n"):
            currentMap.append(row)
        else:
            allMapsStrings.append(currentMap)
            currentMap = []
    allMapsStrings.append(currentMap)
    maps = []
    for mapString in allMapsStrings:
        map = []
        for rowStr in mapString[1:]:
            row = rowStr.strip().split(" ")
            row = [ int(i) for i in row ]
            map.append(row)
        maps.append(map)

    #figure out least location for each seed range
    leastLocation = 9999999999999
    for seed in seeds:
        currentRanges = [seed]
        for map in maps:
            newRanges = []
            for currentRange in currentRanges:
                newRanges = newRanges + readMapRange(map, currentRange)
            currentRanges = newRanges
        for outRange in currentRanges:
                if outRange[0] < leastLocation:
                    leastLocation = outRange[0]


    print(leastLocation)

#reads map and a range of input values to produce an array of ranges of output values
def readMapRange(rangesMap, inRange):
    outRanges = []
    remainingRanges = [inRange]
    for row in rangesMap:
        rowStart = row[1] #150
        rowSize = row[2]  #50
        rowEnd = row[1] + rowSize - 1 #199
        rowStartOut = row[0] #1000
        newRemaining = []
        for subRange in remainingRanges:
            startRange = subRange[0] #1
            sizeRange = subRange[1] #100
            endRange = subRange[0] + sizeRange - 1 #100
            # F
            if ( (startRange <= rowStart) and (endRange >= rowEnd) ):
                outRanges.append([rowStartOut, rowSize])
                newRemaining.append([startRange, rowStart-startRange])
                newRemaining.append([rowEnd+1, endRange - rowEnd])
            # E
            elif ( (startRange > rowStart) and (endRange < rowEnd) ):
                outRanges.append([rowStartOut+(startRange-rowStart), sizeRange])
            # A
            elif ((startRange <= rowStart) and (endRange >= rowStart) ):
                newRemaining.append([startRange, sizeRange-(endRange-rowStart)-1])
                outRanges.append([rowStartOut, endRange-rowStart+1])
            # B
            elif ((endRange >= rowEnd) and (startRange <= rowEnd)):
                newRemaining.append([rowEnd+1, sizeRange-(rowEnd-startRange)-1])
                outRanges.append([rowStartOut+(startRange-rowStart), rowEnd-startRange+1])
            # C & D
            else: # (endRange < rowStart) or (startRange > rowEnd)
                newRemaining.append(subRange)
        remainingRanges = newRemaining
        # print(remainingRanges)
        # print(outRanges)
        # print("\n")
    for extraRange in remainingRanges:
        outRanges.append(extraRange)
    finalRanges = []
    for outRange in outRanges:
        if outRange[1] > 0:
            finalRanges.append(outRange)
    return finalRanges
    
#read data from file
def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart2()
# print(readMapRange([[1000, 0, 50 ],[2000, 50, 50]], [25, 50 ]))