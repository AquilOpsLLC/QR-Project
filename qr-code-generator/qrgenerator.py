import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make("TEXT HERE")

myqr.save("TEXTHERE.png", scale = 8)

b = decode(Image.open("text.png"))
print (b[0].data.decode("ascii"))
