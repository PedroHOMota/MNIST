import struct  


def extractIMG(numberOfImages): #variable will be used to dictate the number of imgs to be extracted
    with open("trainIMG.idx3-ubyte","rb") as f:
        byte=f.read(16)
        mn,ni,nr,nc=struct.unpack(">IIII",byte)
        #print(mn,ni,nr,nc)
        img=[]
        for n in range(0,numberOfImages):
            pics=[]
            for i in range(0,28):
                s=[]
                for j in range(0,28):
                    s.insert(j,int.from_bytes(f.read(1),byteorder='big'))
            pics.insert(i,s)   
        img.insert(n,pics)
        


    f.closed()
    return img


with open("train-labels.idx1-ubyte","rb") as f:
    byte=f.read(8)
    mn,ni=struct.unpack(">II",byte)
    print(mn,ni)
    labels=[]
    while 1:
        label=f.read(1)
        if label=="":
            break

        labels.__add__(label)
f.closed()

def printIMG(imgArray):
    aux=""    
    for i in range(0,28):
        for j in range(0,28):
            if(imgArray[i][j]>127):
                print("#", end='')
            else:
                print(".", end='')
#Reference
#https://stackoverflow.com/questions/39969045/parsing-yann-lecuns-mnist-idx-file-formatv