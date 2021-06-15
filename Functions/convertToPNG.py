#Bibliotecas
import random
import cv2 as cv
import numpy as np

def saveImage(path, name, image):
  try:
    path = path + name

    cv.imwrite(path, image)

  except Exception as e:
    return e.message

def showImage(img):
  cv.imshow("Imagem", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

def imageWrapper(pathI, image, pathB, background, save):
  # Recebendo as imagens e os fundos

  imageF = pathI + image
  backgroundF = pathB + background

  imageF = cv.imread(imageF, cv.COLOR_BGR2GRAY)
  backgroundF = cv.imread(backgroundF, cv.COLOR_BGR2GRAY)

  imageF = np.dstack([imageF, np.ones(imageF.shape[:2], dtype='uint8') * 255 ])
  
  newBackground = np.dstack([backgroundF, np.ones(backgroundF.shape[:2], dtype='uint8') * 255])

  scale_newBackground = 30

  w = int(600 * scale_newBackground / 100)
  h = int(400 * scale_newBackground / 100)

  dim = (w, h)
  
  newBackground = cv.resize(newBackground, dim, interpolation=cv.INTER_AREA)

  base = np.zeros((newBackground.shape[0], newBackground.shape[1], 4), dtype='uint8')
  hF = int(350 * 30 / 100)
  wF = int(550 * 30 / 100)
  
  dimF = (wF, hF)

  imageF = cv.resize(imageF, dimF, interpolation=cv.INTER_AREA)

  ph = int(h/2)
  pw = int(w/2)
  dh, dw = imageF.shape[:2]
  ph = int(ph - (dh/2))
  pw = int(pw - (dw/2))

  for a in range(dh):
    for l in range(dw):
      base[a + ph][l + pw] = imageF[a][l]
  
  point = (dw/2, dh/2)
  angle = random.randint(-30, 30)
  scale = 0.6

  rotacao = cv.getRotationMatrix2D(point, angle, scale)
  base = cv.warpAffine(base, rotacao, (0, ph))

  for a in range(int(h)):
    for l in range(int(w)):
      if(base[a][l][3] > 0):
        newBackground[a][l] = [0,0,0,0]

  newImageSave = cv.bitwise_or(base, newBackground)

  path = save + image 
  cv.imwrite(path, newImageSave)