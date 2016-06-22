import re
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word',help = 'specify word to search for')
    parser.add_argument('fname',help = 'specify file to search for')
    args = parser.parse_args()
    
    searchfile = open(args.fname,'r')
    linenum = 0
    searchResult = {}
    for line in searchfile.readlines():
        line = line.strip('\n\r\t')
        linenum +=1
        search = re.findall(args.word,line,re.I)
        if search:
            searchResult[linenum] = line.replace('','')
        #searchResult.append(search)
    print(searchResult)
if __name__ == '__main__':
    main()