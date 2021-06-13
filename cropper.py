import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("./Dolar/png/teste.png")

cv.imshow("Image original", image)
cv.waitKey(0)

croped = image[100:200, 50:300]

cv.imshow("Imagem cropada", croped)
cv.waitKey(0)

cv.destroyAllWindows()