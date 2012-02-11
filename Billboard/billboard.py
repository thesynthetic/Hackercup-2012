def maxFontSize(width,height,text):
	print 'Width: ', width
	print 'Height: ', height
	bwidth = int(width)
	bheight = int(height)
	words = text.replace('\n','').split(' ')
	wordLengthList = map(lambda x: len(x), words)
	#print words
	#print wordLengthList
	lineSpaceAvail = bwidth
	
	
	maxFontSize = 0
	for fontsize in range(bwidth/max(wordLengthList),-1,-1):
		#print 'Trying font size: ', fontsize
		firstWord = 1
		lineNum = 0
		lineSpaceAvail = bwidth
		for word in words:
			if firstWord:
				spaceNeeded = len(word)*fontsize
			else:
				spaceNeeded = (len(word)+1)*fontsize
			if spaceNeeded <= lineSpaceAvail:
				lineSpaceAvail  = lineSpaceAvail - spaceNeeded
				firstWord = 0
			else:
				spaceNeeded = len(word)*fontsize
				lineNum = lineNum + 1
				lineSpaceAvail = bwidth - spaceNeeded
			#print 'Word: ', word, ' on line: ', lineNum, ' and used ', spaceNeeded, ' spaces', ' with ', lineSpaceAvail, ' left'
		if (lineNum + 1)*fontsize <= bheight:
			maxFontSize = fontsize
			break
	print 'Max Font Size: ', maxFontSize




f = open('billboards.txt', 'r')
numOfLines = int(f.readline())
#for i in range(0,numOfLines):
for i in range(0,numOfLines):
	line = f.readline()
	x = line.split(' ',2)
	maxFontSize(x[0],x[1],x[2])
