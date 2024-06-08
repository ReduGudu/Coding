def wordcount(tiles):
    fhandle=open(tiles)
    fread=fhandle.read()
    text=fread.split()
    wcount=0
    for w in text:
        wcount=wcount+1

    print(wcount)

def words(tabs):
    word=dict()
    fhandle2=open(tabs)
    text=fhandle2.read()
    i=0
    for w in text:
        w=word[i]

    print(word)


    
file=input('Enter the file name with extension:')
fname=open(file)

count=0
for line in fname:
    count=count+1

print("The number of line in this file is:")
print(count)
print("The number of words in this file is:")
wordcount(file)

print('---------------------\n' *5)
words(file)
