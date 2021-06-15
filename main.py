import os
import cv2 as cv
import matplotlib.pyplot as plt

# Funções externas
from FunctionAuxiliares import writeImage, writeBackground, writeArrayToCSV 

notas = [1, 5, 10, 50, 100]
nota = 0
newListImage = []
newListBackground = []
arrayImages = []

def getImages(n):
  path = './IFinal/'+str(n)+'dolar/'
  
  print("\n\tNota [{}]\n".format(n))

  arrayImages = []

  for imagesPath in range(1, 9):
    print("[°] Pegando imagens da pasta " + str(imagesPath) + "/")

    for images in os.walk(path + str(imagesPath) + "/"):
      for image in images[2]:
        pathFinalImage = path + str(imagesPath) + "/" + image
        imageF = cv.imread(pathFinalImage)
        arrayImages.append(imageF)
  
  newListImage.append(arrayImages)
  
def getBackground():
  for images in os.walk('./Fundo'):
    for background in images[2]:

      newListBackground.append(background)

  print("[!] Processo de leitura das imagens realizada!\n")

try:

  for i in notas:
    nota = i 
    getImages(i)

  print("\n")
  
  c = 0
  d = 0
  for nota in newListImage:
    print(len(nota), notas[c])
    print("Quantidade de notas: [" + str(len(nota)) + "] - [" + str(notas[c]) + "]")
    writeArrayToCSV(notas[c], nota, d)
    d = 1
    c+=1

  print("\n[!] Processo de leitura das imagens realizada!\n")

except Exception as e:
  print(e)
except KeyboardInterrupt:
  print("Você interrompeu na geração das notas de {}\n".format(nota))
  print("Obrigado por utilizar nossos serviços")
  