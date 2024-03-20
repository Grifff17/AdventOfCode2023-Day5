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
    
#read data from file
def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart1()