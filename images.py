from PIL import Image

new_image = Image.open("astro.jpg")

new_image.thumbnail((400,400))

new_image.save('newAstro.jpg')
new_image.show()
