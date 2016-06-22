import re
import argparse
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word',help = 'specify word to search for')
    parser.add_argument('fname',help = 'specify file to search for')
    args = parser.parse_args()
    
    searchfile = open(args.fname,'r')
    linenum = 0
    s1 = str(args.word)
    for line in searchfile.readlines():
        line = line.strip('\n\r')
        linenum +=1
        searchResult = re.findall(args.word,line,re.M|re.I)
    print(searchResult)

    if searchResult:
        print(str(linenum)+':'+line)
    #close(searchfile)

if __name__ == '__main__':
	Main()
