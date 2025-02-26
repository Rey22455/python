from PIL import Image

def ligneVerte2(largeur:int,hauteur:int)->Image:
    img = Image.new("RGB",(100,600)) 
    for j in range(largeur): 
            
        for i in range(0,largeur.width):
            img.putpixel((largeur,hauteur),(0,255,0))
    return img 

imageV = ligneVerte2()
imageV.show()

