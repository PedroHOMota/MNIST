import struct
from PIL import Image
import PIL as pil
import gzip
import urllib.request as rs
import os
import time

#ToDo
#Implement download the data and extracting it
def DonwloadFile():
    if not os.path.exists("Downloads"):
        os.makedirs("Downloads")
    if not os.path.isfile("Downloads//trainIMG.gz"):
        imgD=rs.urlretrieve("http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz", "Downloads//trainIMG.gz")

    if not os.path.isfile("Downloads//trainLBL.gz"):
        lblsD=rs.urlretrieve("http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz", "Downloads//trainLBL.gz")

    with open("Downloads//trainIMG.gz","rb") as f:
        img=f.read()
        img=gzip.decompress(img)
        f.close()

    with open("Downloads//train-image","wb") as output:
        output.write(img)
        output.close()

    with open("Downloads//trainLBL.gz","rb") as f:
        img=f.read()
        img=gzip.decompress(img)
        f.close()

    with open("Downloads//train-label","wb") as output:
        output.write(img)
        output.close()
   


def extractIMG(): #variable will be used to dictate the number of imgs to be extracted
    with open("trainIMG.idx3-ubyte","rb") as f:
        byte=f.read(16) #Reading the magical number, number of images, number of rows and number of columns at once
        mn,ni,nr,nc=struct.unpack(">IIII",byte) #Converting to big endian; Each I represents 4 big endian bytes
        img=[]
        print("Magic Number: "+str(mn))
        print("Number of Imgs: "+str(ni))
        print("Number of rows: "+str(nr))
        print("Number of cols: "+str(nc))
        img=[[]]
        aux=[]
        now=time.time()
        print("Now "+str(now))
        for i in range(ni):
            print(i)
            #for j in range (nr):
               # aux.insert(j, f.read(28))
            img.insert(i, f.read(28*28))
        print(time.time()-now)
        #img=[[[int.from_bytes(f.read(1),byteorder='big') for j in range (28)] for i in range(28)] for n in range(129)]
   
    #f.closed()
    return img

def extractLBL():
    with open("train-labels.idx1-ubyte","rb") as f:
        byte=f.read(8)
        mn,ni=struct.unpack(">II",byte)
        print(mn,ni)
        labels=[int.from_bytes(f.read(1),byteorder='big') for n in range(ni)]
        
    #f.closed()
    return labels

def printIMG(imgArray,imgN): #Print the image to  the console
    aux=0    
    for i in range(0,28):
        for j in range(0,28):
            if(imgArray[imgN][aux]>127):
                print("#", end='')
            else:
                print(".", end='')
            aux+=1
        print('\n')

def SaveIMG(imgName,imgArray): #Convert the array and save it as a png image
    #arr=[]
    #a=0
    #for i in range(0,28): #Transform the 2d into a 1d
    #        for j in range(0,28):
    #            arr.insert(a,imgArray[i][j])
    #            a=a+1

    im=Image.new("L",(28,28)) #B&W
    #im.putdata(arr)
    img=pil.fromarray(imgArray)
    im.save("test-"+imgName+".png","PNG")
    #"train-%05i-%i.png" % (i,50)
 
#DonwloadFile()
imgs=extractIMG()
#lbl=extractLBL()
printIMG(imgs,128)
print("Started saving")
#for n in range(len(imgs)):
#    SaveIMG(n+"-"+lbl[n],imgs[n])

#Reference
#https://stackoverflow.com/questions/39969045/parsing-yann-lecuns-mnist-idx-file-formatv