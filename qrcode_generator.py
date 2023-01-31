pip install qrcode
import qrcode
print("QR code generator using python")
s=input("enter the text: ")
img=qrcode.make(s)
img.save("test.png")
img.show("test.png")