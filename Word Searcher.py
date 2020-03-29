<<<<<<< HEAD
# Section: Import modules
=======
Section: Import modules
>>>>>>> 51350c2a50373a20c29b4766ffde3fa25a0954dc

import numpy as np
import math
from copy import copy
import time

<<<<<<< HEAD
# Section End

# Section: Data
=======
Section End

Section: Data
>>>>>>> 51350c2a50373a20c29b4766ffde3fa25a0954dc

matrix = ["HPMOQFHMQSRMEHBUSLASSIMQ",
          "BSPSIXTRQQGWLABIVYOXNQWN",
          "KTIAZJKDSLJEAZXCUDTYCSPO",

          "LAXREPPTQVFWVKGDQEIAAEVU",
          "KIWXTXGRKURBABYWFMOKNUGG",
          "ONYPGNZYBZLCEFMKHSNPDTCE",

          "REJGKKOWSESYFMMXADEYLASL",
          "TDTSTWLFTWLAMVNGVWMGETIC",
          "XGCZBDQAABUPNGJTSUTDSSAA",

          "TLHKZTIGTSTOECQDJTFCGHEN",
          "WAQTELLWIMCHUETOHLTPKNHR",
          "KSZPUNXUOSDSWHTUKEWOQOPE",

          "ESIYODTHNEDADYRSACJCJEXB",
          "CYVMLSRCSBWCPXNBCRRNDRTA",
          "EGAMEJRPOAXREICIWEYATEBT",

          "BJAIZUTEFKBIGYATPFMNHTSP",
          "SWRSCKWLTRKSCAPOHWNCQAJE",
          "OPJIJVSOHIITSUSTNJLNGWZJ",

          "NAFLDXJMEVMYOIBAAIAFUYWI",
          "JIREXDEKCAMTTQRLTWTROLHR",
          "XDITUPRBRTSOVYPTGZRYHOOW",

          "VLQIEBXFOORHYMVAFQFJBHXZ",
          "VFKLBSTXSYZZYXCRDZHYGGMT",
          "YEZAOHENSHQFJDWWKGPMOBMA"]

words = ["altar",
         "ambo",
         "candles",
         "crucifix",
         "font",
         "holy water",
         "missals",
         "pews",
         "priest",
         "repository",
         "sacristy",
         "sanctuary",
         "stained glass",
         "stations of the cross",
         "statues",
         "steeple",
         "stoup",
         "tabernacle"
         ]

# Section End

<<<<<<< HEAD
# Section: WordSearcher class

=======
>>>>>>> 51350c2a50373a20c29b4766ffde3fa25a0954dc
class WordSearcher():

    def __init__(self, words, matrix, memoize=True, debug=False):
        self.words = self.preprocessWords(words)
        self.matrix = self.preprocessMatrix(matrix)
        self.memoize = memoize
        self.debug = debug

        self.foundLetters = {}

    # Division: Toggle functions

    def memoizeToggle(self):
        self.memoize = not self.memoize

    def debugToggle(self, debugBool):
        self.debug = debugBool

    # Division End

    # Division: Pre-processing functions

    def preprocessWords(self, words):
        processedWords = []
        for word in words:
            processedWords.append(word.replace(" ", ""))
        return processedWords

    def preprocessMatrix(self, matrix):
        processedMatrix = []
        for row in matrix:
            processedMatrix.append(list(row.lower()))
        return processedMatrix

    # Division End

    def run(self):
        startTime = time.time()
        foundWords = []
        for word in self.words:
            result = self.wordSearch(word, self.matrix)
            foundWords.append([word, result])
        endTime = time.time()

        self.outputResult(foundWords, matrix)

    # Division: Output functions

    def outputResults(self, foundWords, matrix):
        self.printMatrix(matrix)

        secondsElapsed = endTime - startTime
        milsecondsElapsed = secondsElapsed * 1000
        milsecondsElapsedPerWord = milsecondsElapsed/len(foundWords)
        print(f"\nWords found in {milsecondsElapsed:.2f} ms")
        print(f"That's one word every {milsecondsElapsedPerWord:.2f} ms")

        self.printFoundWords(foundWords)

    def printMatrix(self, matrix):
        rowDigits = math.floor(math.log(len(matrix), 10)) + 1
        columnDigits = math.floor(math.log(len(matrix[0]), 10)) + 1 + 1

        rowSpacerCharacter = "-"

        columnCounter = 0
        spacer = "".ljust(rowDigits)
        print(f"{spacer}| ", end="")
        for column in matrix[0]:
            countString = str(columnCounter).ljust(columnDigits)
            print(f"{countString}",end="")
            columnCounter += 1

        print(f"\n{rowSpacerCharacter}", end="")
        for columnDigit in range(columnDigits + 1):
            print(f"{rowSpacerCharacter}", end="")
        for column in matrix[0]:
            for columnDigit in range(columnDigits):
                print(f"{rowSpacerCharacter}", end="")
            columnCounter += 1

        rowCounter = 0
        for row in matrix:
            countString = str(rowCounter).ljust(rowDigits)
            print(f"\n{countString}| ", end="")
            for letter in row:
                letter = letter.ljust(columnDigits)
                print(f"{letter}",end="")
            rowCounter += 1
        print()

    def printFoundWords(self, foundWords):
        print()
        xDirections = [" left", "", " right"]
        yDirections = [" upward", "", " downward"]
        for foundWord in foundWords:
            word = foundWord[0]
            vector = foundWord[1]
            if vector == []:
                print(f"Unable to find '{word}'")
            else:
                startPosition = vector[0]
                direction = vector[1]
                yDirection = direction[0] + 1
                xDirection = direction[1] + 1
                print(f"Found '{word}' starting at {startPosition} in a"
                      f"{xDirections[xDirection]}{yDirections[yDirection]} direction")

    # Division End

    # Division: Searching functions

    def wordSearch(self, word, matrix):
        if self.debug:
            print(f"Finding '{word}'")
        startLetter = word[0]

        if self.memoize:
            if startLetter in self.foundLetters:
                startPositions = self.foundLetters[startLetter]
            else:
                startPositions = self.letterSearch(startLetter, matrix)
                self.foundLetters[startLetter] = startPositions
        else:
            startPositions = self.letterSearch(startLetter, matrix)

        for startPosition in startPositions:
            secondLetter = word[1]
            directions = self.neighbourSearch(secondLetter, startPosition, matrix)
            for direction in directions:
                if self.debug:
                    print(f"In direction '{direction}'")
                if self.checkDirection(word, startPosition, direction, matrix):
                    return [startPosition, direction]
        return []

    def checkDirection(self, word, startPosition, direction, matrix):
        vector = copy(startPosition)
        for letter in word:
            try:
                if matrix[vector[0]][vector[1]] != letter:
                    return False
            except(IndexError):
                return False
            vector += direction
        return True

    def neighbourSearch(self, letter, startPosition, matrix):
        if self.debug:
            print(f"\nLooking at neighbours around {startPosition} for {letter}")
        y, x = startPosition
        directions = []
        for yOffset in range(-1,2):
            for xOffset in range(-1,2):
                if not (xOffset == 0 and yOffset == 0):
                    if x + xOffset >= 0 and y + yOffset >= 0:
                        if (x + xOffset < len(matrix[0]) and y + yOffset < len(matrix)):
                            if self.debug:
                                print(f"Neighbour {matrix[y + yOffset][x + xOffset]}")
                            if matrix[y + yOffset][x + xOffset] == letter:
                                directions.append(np.array((yOffset, xOffset)))
        return directions

    def letterSearch(self, letter, matrix):
        positions = []
        for y in range(len(matrix)):
            row = matrix[y]
            for x in range(len(row)):
                cell = row[x]
                if cell.lower() == letter.lower():
                    positions.append(np.array((y, x)))
        return positions

    # Division End

# Section End

# Section: Main function

def main():
    WS = WordSearcher(words, matrix)
    WS.run()
    WS.memoizeToggle()
    print()
    WS.run()

if __name__ == "__main__":
    main()

<<<<<<< HEAD
# Section End
=======
WS = WordSearcher(words, matrix)
WS.run()
WS.memoizeToggle()
print()
WS.run()

Section End
>>>>>>> 51350c2a50373a20c29b4766ffde3fa25a0954dc
