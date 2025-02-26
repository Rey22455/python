from PIL import Image

def ligneVerte()->Image:
    img = Image.new("RGB",(300,300)) 
    for i in range(300): 
      img.putpixel((150,i),(0,255,0))
    return img 
 
imageV = ligneVerte()
imageV.show()


