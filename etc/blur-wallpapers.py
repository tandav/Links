from PIL import Image, ImageFilter

im = Image.open('image.jpg')
im_blurred = im.filter(ImageFilter.GaussianBlur(radius=100))
im_blurred.save('image-blurred.jpg')
