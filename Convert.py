from PIL import Image

img = Image.open("spy.png").convert("RGBA")

# kare yap (padding)
size = max(img.size)
new_img = Image.new("RGBA", (size, size), (0,0,0,0))
new_img.paste(img, ((size - img.size[0]) // 2, (size - img.size[1]) // 2))

img = new_img.resize((256,256), Image.LANCZOS)

img.save(
    "icon.ico",
    sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]
)