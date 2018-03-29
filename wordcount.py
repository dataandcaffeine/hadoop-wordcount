#Define mapper class
def mapper(_, text, writer):
import re
#break up tab separated lines
lines = text.split("\n") 

#iterate through word pairs
for line in lines:
    #strip punctuation from text and convert to lowercase
    line = re.sub('[^A-Za-z]+', ' ', line).lower()
    #split words
    words = line.split()
    #iterate through pairs
        for word1 in line:
            for word2 in line:
                pair = tuple([word1, word2])
writer.emit(pair, "1")

#Define reducer class
#takes in pairs from mapper class
def reducer(pair, icounts, writer):
    writer.emit(pair, sum(map(int, icounts)))
    
 