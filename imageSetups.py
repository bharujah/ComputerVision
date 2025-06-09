import cv2
import numpy as np

# reading and writing the images......................................................................

#img = cv2.imread("./data/test.png",0) #grayscale -> img = cv2.imread("./data/test.png",cv2.IMREAD_GRAYSCALE)
img = cv2.imread("./data/test.png",1) #normal image

# dim = (200,300)
# resize = cv2.resize(img, dim)

# cv2.imshow("output",resize)
# cv2.imwrite("./data/outputimage.jpg",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#image resizing.........................................................................................

#print('original dimension', img.shape) # original dimension (991, 1354, 3) 

#morphological Operations ..............................................................................
 
# Dilation	                                                                        Erosion
# It increases the size of the objects.	                                                It decreases the size of the objects.
# It fills the holes and broken areas.	                                                It removes the small anomalies.
# It connects the areas that are separated by space smaller than structuring element.	It reduces the brightness of the bright objects.
# It increases the brightness of the objects.	                                        It removes the objects smaller than the structuring element.
# Distributive, duality, translation and decomposition properties are followed.	        It also follows the different properties like duality etc.
# It is XOR of A and B.	                                                                It is dual of dilation.
# It is used prior in Closing operation.	                                            It is used later in Closing operation.
# It is used later in Opening operation.	                                            It is used prior in Opening operation.

#kernel = np.ones((5,5),dtype = 'uint8')
# erosion = cv2.erode(img, kernel, iterations=1)
# dilation = cv2.dilate(img, kernel, iterations=1)

# cv2.imshow("dilation",dilation)
# cv2.imshow("erosion",erosion)
# cv2.waitKey(0)


#morphology open and close
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)
# closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE, kernel)
# cv2.imshow("opening",opening)
# cv2.imshow("closing",closing)
# cv2.waitKey(0)