f = open('rumi.txt', 'r') #relative path , r: read mode, opens the stream and defines its direction
# f = open('D:\python-lecture\Week6\rumi.txt', 'r') #absolute path
poem = f.read() #read all file content
print(poem)
f.close() #close the stream

#open file and close it automatically with "with"
with open('rumi.txt', 'r') as f:
    poem = f.read() #read all file content
    print(poem)

