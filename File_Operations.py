import os
def fileOperations():
    fo = open('/home/affine/iput_data/sample1.txt','r')
    line = fo.read()
    print(line)
    position = fo.tell()
    print(position)
    fo.close()
# OS MODULE PRACTICE
def osmodule():
    # renaming the file
    #os.rename('/home/affine/iput_data/sample.txt','/home/affine/iput_data/sample1.txt')

    # removing the file from directory
    #os.remove('home/affine/iput_data/sample1.txt')

    # directory role
    os.mkdir(path='/home/affine/iput_data/temp',mode =777)

    os.rmdir(path = '/home/affine/iput_data/temp')

if __name__ == '__main__':
    fileOperations()
    osmodule()