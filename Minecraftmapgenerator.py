"""
This was designed to convert an image into an image that only uses colors you can get on a minecraft map
this is useful so that you can make custom paintings in minecraft

The image to convert must be in a folder called convert and there must be a folder called converted for them to go into.
"""
from PIL import Image

def load_colors(file):
    file = open(file)
    data = file.read()
    file.close()
    linearDat = data.split("\n")
    colors = [x.split(".") for x in linearDat]
    return colors

def load_image(file):
    image = Image.open("convert/"+file)
    image = image.convert('RGB')
    if image.size != (128,128):
        return "IMGSZERR"
    return image
    
def convert_pixels(image):
    pixels = image.load()
    colors = load_colors("colors")
    for x in range(128):
        for y in range(128):
            pixel = pixels[x,y]
            closestColor = None
            closestDistance = None
            for z in colors:
                color = (int(z[0]),int(z[1]),int(z[2]))
                distance = 0
                for a in range(3):
                    distance += abs(color[a]-pixel[a])
                if closestColor == None or closestDistance > distance:
                    closestColor = color
                    closestDistance = distance
            pixels[x,y] = closestColor
    return image

    
def convert_image(file):
    image = load_image(file)
    pixels = convert_pixels(image)
    pixels.save("converted/"+file)


if __name__ == "__main__":
    convert_image(input("Image Name: "))
