import struct
from PIL import Image

#ToDo
#Implement download the data and extracting it

def extractIMG(numberOfImages): #variable will be used to dictate the number of imgs to be extracted
    with open("trainIMG.idx3-ubyte","rb") as f:
        byte=f.read(16) #Reading the magical number, number of images, number of rows and number of columns at once
        mn,ni,nr,nc=struct.unpack(">IIII",byte) #Converting to big endian; Each I represents 4 big endian bytes
        img=[]
        
            
        for n in range(0,numberOfImages):
            pics=[]
            for i in range(0,28):
                s=[]
                for j in range(0,28):
                    byte=f.read(1)
                    s.insert(j,int.from_bytes(byte,byteorder='big')) #Convert bytes to int using the Big Endian
                pics.insert(i,s)   
            img.insert(n,pics)

    f.closed()
    return img

def extractLBL(numberOfLabes):
    with open("train-labels.idx1-ubyte","rb") as f:
        byte=f.read(8)
        mn,ni=struct.unpack(">II",byte)
        print(mn,ni)
        labels=[]
        for n in range(0,ni):
            labels.__add__(int.from_bytes(f.read(1),byteorder='big')) #Convert byte to big endian int
    f.closed()
    return labels

def printIMG(imgArray,imgN): #Print the image to  the console
    aux=""    
    for i in range(0,28):
        for j in range(0,28):
            if(imgArray[imgN][i][j]>127):
                print("#", end='')
            else:
                print(".", end='')
        print('\n')

def SaveIMG(imgName,imgArray,imgNumber): #Convert the array and save it as a png image
    arr=[]
    a=0
    for i in range(0,28): #Transform the 2d into a 1d
            for j in range(0,28):
                arr.insert(a,imgArray[imgNumber][i][j])
                a=a+1

    im=Image.new("L",(28,28)) #B&W
    im.putdata(arr)
    im.save(imgName+".png","PNG")

 

imgs=extractIMG(3)
printIMG(imgs,1)
SaveIMG("atest2",imgs,1)

#Reference
#https://stackoverflow.com/questions/39969045/parsing-yann-lecuns-mnist-idx-file-formatv