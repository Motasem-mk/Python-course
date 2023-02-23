# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------

from PIL import Image
# open the image
myimage = Image.open("/Users/elkihale.n-abualqumboz.mk/Desktop/1.jpg")

myimage.show()

# my crop image 
mybox = (300,300,800,800)
mynewimage = myimage.crop(mybox)

mynewimage.show()


#my convert mode image
myconvertedimage = myimage.convert("L")
myconvertedimage.show()