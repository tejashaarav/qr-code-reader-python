import qrcode
inputlink = str(input("paste the link\n"))
imagename = str(input("image file name\n"))
img = qrcode.make(inputlink)
img.save(imagename+".png")