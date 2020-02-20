import sys

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

if __name__ == "__main__":
	print(parseFile(sys.argv[1]))

def averageLibraries(libraries):
	
	totalSpeeds = []
	scanSpeeds = []

    for i in libraries:
		totalScore = 0
        for b in i["book"]:
            totalScore += bookScores[b]

		totalSpeed = totalScore/(signup + numberOfBooks/rate)
		totalSpeeds.append(totalSpeed)
		scanSpeed = totalScore/(numberOfBooks/rate)
		scanSpeeds.append(scanSpeed)

	return totalSpeeds, scanSpeeds

def maxFromAverages (libraries)
	total, scan = averageLibraries(libraries)
	
