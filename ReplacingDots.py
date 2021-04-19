def printingLines (prevLine,currLine):
    print("--------------------")
    print(prevLine)
    print(currLine)

#input file
fin = open("test.txt", "rt")
#output file to write the result to
fout = open("out.txt", "wt")


separator = ''
previousLine = next(fin)
dotIndex = 0
for line in fin:
  currentLine = line.split()
  previousLine = previousLine.split()
  printingLines(previousLine,currentLine)

  for char in currentLine:
      if char == ".":
          currentLine[dotIndex] = previousLine[dotIndex]
          print("------------------")
          print(index)
          print(currentLine[dotIndex])
      dotIndex = dotIndex + 1

  currentLine = separator.join(currentLine)    
  previousLine = line
  print(currentLine)
  dotIndex = 0
  fout.write(currentLine + "\n")




#close input and output files.write
fin.close()
fout.close()
