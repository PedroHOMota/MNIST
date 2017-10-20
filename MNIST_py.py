import struct
from PIL import Image
import PIL as pil
import gzip
import urllib.request as rs
import os
import time

def DonwloadFile():
    if not os.path.exists("Downloads"): #Check if folder exits, if not, create it
        os.makedirs("Downloads")
    if not os.path.isfile("Downloads//trainIMG.gz"): #Check if file exits, if not, create it
        imgD=rs.urlretrieve("http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz", "Downloads//trainIMG.gz")

    if not os.path.isfile("Downloads//trainLBL.gz"):
        lblsD=rs.urlretrieve("http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz", "Downloads//trainLBL.gz")

    with open("Downloads//trainIMG.gz","rb") as f: #Decompressing gzipped img file
        img=f.read()
        img=gzip.decompress(img)
        f.close()

    with open("Downloads//train-image","wb") as output: #Saving the decompressed file from memory to disk
        output.write(img)
        output.close()

    with open("Downloads//trainLBL.gz","rb") as f:
        img=f.read()
        img=gzip.decompress(img)
        f.close()

    with open("Downloads//train-label","wb") as output:
        output.write(img)
        output.close()
   
def extractIMG(): 
    with open("Downloads\\train-image","rb") as f:
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
            img.insert(i, f.read(28*28)) #Read all bits from image at once for better performance
        print(time.time()-now)
    f.close()
    return img

def extractLBL():
    with open("Downloads\\train-label","rb") as f:
        byte=f.read(8)
        mn,ni=struct.unpack(">II",byte)
        print(mn,ni)
        labels=[int.from_bytes(f.read(1),byteorder='big') for n in range(ni)]
        
        f.close()
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

def printIMGAll(imgArray): #Print all images to  the console
    aux=0
    for i in range(len(imgArray)):
        for j in range(0,28*28):
                if(imgArray[i][j]>127):
                    print("#", end='')
                else:
                    print(".", end='')
                
        print('\n')

def SaveIMG(imgNumber,imgLabel,imgArray): #Receive the array corresponding to the image and save it as png
    im=Image.new("L",(28,28)) #B&W
    im.putdata(imgArray)
    im.save("Images\\train-%05i-%i.png" % (imgNumber,imgLabel),"PNG")
   
    
 
DonwloadFile()
imgs=extractIMG()
lbl=extractLBL()
#printIMGAll(imgs)
print("Started saving")

if not os.path.exists("Images"):
        os.makedirs("Images")

for n in range(len(imgs)):
    SaveIMG(n,lbl[n],imgs[n])

#Reference
#https://stackoverflow.com/questions/39969045/parsing-yann-lecuns-mnist-idx-file-formatv