import sys
import math

def allIndicies(listOfElements, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    indexPosList = []
    indexPos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            indexPos = listOfElements.index(element, indexPos)
            # Add the index position in list
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
 
    return indexPosList

def parseFile(path):
	file = open(path, "r")

	lines = file.readlines()
	# Get number of each from line 0
	line = lines[0].split()
	data = {
		"numberOfBooks": int(line[0]),
		"numberOfLibraries": int(line[1]),
		"numberOfDays": int(line[2])
	}
	# Extract book scores
	data["bookScores"] = [int(number) for number in lines[1].split()]
	libraries = []
	for libraryNumber in range(0, data["numberOfLibraries"]):
		index = (libraryNumber + 1)*2
		infoLine = lines[index].split()
		bookLine = lines[index+1].split()
		library = {
			"numberOfBooks": int(infoLine[0]),
			"signup": int(infoLine[1]),
			"rate": int(infoLine[2]),
			"books": [int(book) for book in bookLine]
		}
		libraries.append(library)
	file.close()
	data["libraries"] = libraries
	return data

def outputData (path, data):
	file = open(path, "w")
	#Line 0
	file.write(f"{len(data)}\n")
	for library in data:
		file.write(f"{library['id']} {len(library['books'])}\n")
		for bookId in library["books"]:
			file.write(f"{bookId} ")
		file.write("\n")
	file.close()


def averageLibraries(data):
	libraries = data["libraries"]
	totalSpeeds = []
	scanSpeeds = []

	for i in libraries:
		totalScore = 0
		for b in i["books"]:
			totalScore += data["bookScores"][b]
		totalSpeed = totalScore/(i["signup"] + math.ceil(i["numberOfBooks"]/i["rate"]))
		totalSpeeds.append(totalSpeed)
		scanSpeed = totalScore/(math.ceil(i["numberOfBooks"]/i["rate"]))
		scanSpeeds.append(scanSpeed)
	
	return totalSpeeds, scanSpeeds

def maxLibrary (data):
	libraries = data["libraries"]
	total, scan = averageLibraries(data)

	indicies = allIndicies(total, max(total))
	if len(indicies) == 1:
		return indicies[0]
	relevantScanSpeeds = [scan[index] for index in indicies]
	indicies1 = allIndicies(relevantScanSpeeds, max(relevantScanSpeeds)) 
	if len(indicies1) == 1:
		return indicies[indicies1[0]]
	relevantLengths = [len(libraries[index]["books"]) for index in indicies]
	print(relevantLengths)
	indicies2 = allIndicies(relevantLengths, min(relevantLengths))
	return indicies[indicies1[indicies2[0]]]


def processData (data):
	results = []
	daysTaken = 0
	librariesUsed = []
	while daysTaken < data["numberOfDays"]:
		result = processLibrary(data)
		id = result["id"]
		# try:
		# 	librariesUsed.index(id)
		# 	print(f"List consumed at {daysTaken}")
		# 	break
		# except ValueError:
		# 	pass
		results.append(result)
		for book in result["books"]:
			data["bookScores"][book] = 0
		daysTaken += data["libraries"][id]["signup"]
		librariesUsed.append(id)
		print(f"{daysTaken} out of {data['numberOfDays']}. {id} processed")
	return results

def processLibrary (data):
	results = []
	maxLib = maxLibrary(data)
	booksSubmitted = sorted(data["libraries"][maxLib]["books"], key=lambda book: data["bookScores"][book], reverse=True)
	return {
		"id": maxLib,
		"books": booksSubmitted
	}

if __name__ == "__main__":
	data = (parseFile(sys.argv[1]))
	p = processData(data)
	outputData(sys.argv[2], p)