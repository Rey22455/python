from PIL import Image

def faireUnCadre(image:Image,epaisseur:int)->Image:
    for j in range(epaisseur): 
            
        for i in range(0,image.width):
            image.putpixel((i,j),(0,255,0))

    for j in range(image.height-epaisseur,image.height): 

        for i in range(0,image.width):
            image.putpixel((i,j),(0,255,0))

    for j in range(image.height): 

            for i in range(0,epaisseur):
                image.putpixel((i,j),(0,255,0))

    for j in range(image.height): 

            for i in range(image.width-epaisseur,image.width):
                image.putpixel((i,j),(0,255,0))


    return image 

imageGOT = Image.open("GOT.png")
imageCadre = faireUnCadre(imageGOT,30)
imageCadre.show()