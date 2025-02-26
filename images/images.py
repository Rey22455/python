from PIL import Image
"""
def echauffement():
    img = Image.new("RGB",(100,100)) 
    for i in range(100): 
      img.putpixel((i,10),(255,0,0))
      img.putpixel((i,40),(20,255,10))
      img.putpixel((i,70),(255,255,0))
      img.putpixel((i,90),(25,40,200))

    return img 
image = echauffement()
image.show()
"""
"""
def opposer(image:Image)->Image:
    imgmodif = Image.new("RGB",((img.width, img.height)))
    for j in range(image.height):    
        for i in range(image.width):
            r,v,b=img.getpixel((i,j))
            r= 255-r
            v= 255-v
            b= 255-b
            imgmodif.putpixel((i,j),(r,v,b))

    return imgmodif
img = Image.open("starWars.jpg")
imageOpposee = opposer(img)
imageOpposee.show()
"""
"""
def niveauDeGris(image:Image)->Image:
    imgmodif = Image.new("RGB",((image.width, image.height)))
    for j in range(image.height):    
        
        for i in range(image.width):
            r,v,b=image.getpixel((i,j))
            r2= (r+v+b)//3
            v2= (r+v+b)//3
            b2= (r+v+b)//3
            imgmodif.putpixel((i,j),(r2,v2,b2))
    return imgmodif

img = Image.open("starWars.jpg")
imageOpposee = niveauDeGris(img)
imageOpposee.show()
"""
"""
def faireUnCadre(image:Image,epaisseur:int)->Image:
    for j in range(epaisseur): 
            
        for i in range(0,image.width):
            image.putpixel((i,j),(255,255,255))

    for j in range(image.height-epaisseur,image.height): 

        for i in range(0,image.width):
            image.putpixel((i,j),(255,255,255))

    for j in range(image.height): 

            for i in range(0,epaisseur):
                image.putpixel((i,j),(255,255,255))

    for j in range(image.height): 

            for i in range(image.width-epaisseur,image.width):
                image.putpixel((i,j),(255,255,255))


    return image 

imageSW = Image.open("starWars.jpg")
imageCadre = faireUnCadre(imageSW,30)
imageCadre.show()
"""
"""
def retrouverImageCachee(image:Image)->Image:
    img = Image.new("RGB",((image.width, image.height)))
    for j in range(image.height):
        for i in range(image.width):
            r,v,b=image.getpixel((i,j))
            r = (r&7)<<5
            v = (v&7)<<5
            b = (b&7)<<5
            img.putpixel((i,j),(r,v,b))


    return img
imageSW = Image.open("starWarsImageCachee.png")
imageCahee = retrouverImageCachee(imageSW)
imageCahee.show()
"""
💖
def melange(image:Image,image3:Image)->Image:
   for j in range(image.height):
        for i in range(image.width):
            r,v,b=image.getpixel((i,j))
            r2,v2,b2=image2.getpixel((i,j))
            

   
   
   
    return None

imageSW = Image.open("starWars.png")
imageC = Image.open("ceciEstUnEssai.png")
imageMelangee = melange(imageSW,imageC)
imageMelangee.show()