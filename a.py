from PIL import Image
import time

#Read the two images

start = time.time()

image1 = Image.open('test1.png')
# image1.show()
image2 = Image.open('test2.png')
# image2.show()
image3 = Image.open('test3.png')
# image3.show()

#resize, first image
image1_size = image1.size
image2_size = image2.size
image3_size = image3.size
new_image = Image.new('RGB',(image1_size[0]+image2_size[0]+image3_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.paste(image3,(image1_size[0]+image2_size[0],0))
new_image.save("merged_image.png","png")
print('Thời gian là: %.3f'%(time.time()-start))
new_image.show()


