def binaryConverterCode(val):
    print('a')

    counter = 2
    optionValues = []

    for option in range(990):
        optionValues.append(counter ** option)

    val = int(val)
    valDone = 0
    convertedVal = []
    previousVal = 0
    vals = 0
    while valDone != val:
        if val < optionValues[vals]:

            convertedVal.append(previousVal) 
            val -= previousVal
            previousVal = 0
            vals = 0
        
        elif val == optionValues[vals]:
            convertedVal.append(optionValues[vals]) 
            val -= optionValues[vals]

        else:
            previousVal = optionValues[vals]
            vals += 1



    finalCounter = 0
    finalValues = [0] * len(optionValues) 
    for a in reversed(range(len(optionValues))):
       if finalCounter < len(convertedVal) or finalCounter == 0:
           if convertedVal[finalCounter] == optionValues[a]:
               finalValues[a] = 1
               finalCounter += 1
           else:
               finalValues[a] = 0

    finalValues.reverse()

    print(finalValues)
    finalValuesString = ''.join(map(str,finalValues))
    finalNumber = int(finalValuesString, 2)
    return bin(finalNumber)[2:]
