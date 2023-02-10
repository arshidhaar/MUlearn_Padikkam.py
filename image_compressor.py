from PIL import Image

print("\033[1m" + "IMAGE COMPRESSOR" + "\033[0m")
image = Image.open("C:/Users/Suhail/Downloads/Whats.jpeg")# Opening image
image.save("compressed_image.jpg", quality=30, optimize=True)# Compressing image
image.show()
print("compression is achieved")