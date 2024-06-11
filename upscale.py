import cv2
from cv2 import dnn_superres


sr = dnn_superres.DnnSuperResImpl_create()

path = 'EDSR_x4.pb'
sr.readModel(path)

sr.setModel('edsr', 4)
image = cv2.imread('AG_034.jpg')

# upsample the image
upscaled = sr.upsample(image)
# save the upscaled image
cv2.imwrite('upscaled_test.png', upscaled)

# traditional method - bicubic
bicubic = cv2.resize(image, (upscaled.shape[1], upscaled.shape[0]), interpolation=cv2.INTER_CUBIC)
# save the image
cv2.imwrite('bicubic_test.png', bicubic)