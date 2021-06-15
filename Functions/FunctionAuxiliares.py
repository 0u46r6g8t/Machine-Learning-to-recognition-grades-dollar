import albumentations as A
from PIL import Image
import numpy as np
import cv2
import csv

# Funções extras
from convertToPNG import imageWrapper, showImage

def writeImage(valor):
  transformImage = A.Compose(
    [
      A.Resize(height=200, width=500),
      A.HorizontalFlip(p=0.9),
      A.VerticalFlip(p=0.1),
      A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.9),
      A.OneOf([
        A.Blur(blur_limit=3, p=0.3),
        A.ColorJitter(p=0.5),
      ], p=1.0)
    ]
  )

  nameO = str(valor) + " dolar verso.png"

  image = Image.open("./Dolar/png/" + nameO)

  image = np.array(image)

  for i in range(50):
    augmentations = transformImage(image=image)
    augmentations_image = augmentations["image"]

    image_list = (augmentations_image)
    name = nameO
    
    name, ext = name.split(".")
    name = name + "-" + str(i) + "." + ext
    cv2.imwrite('./Dolar/' + str(valor) + 'dolar/' + name, image_list)

def writeBackground(listImage, listBackground, path, nota):
  c = 0

  for i in range(len(listBackground)):

    c+=1
    print("\n[°] Iniciando a montagem do pack: {} de notas com os fundos".format(c))
    for j in range(len(listImage)):
      background = listBackground[i]
      image = listImage[j]

      save = "./IFinal/"+str(nota)+"dolar/"+str(c)+"/"
      imageWrapper(path, image, "./Fundo/", background, save)
  print("\n Processo finalizado com sucesso!")

def writeArrayToCSV(dollar, arrayImages, c):
  
  file_data = open('dataset_image_dolar.csv', 'a', newline='', encoding='utf-8')

  w = csv.writer(file_data)    

  if c == 0:  
    w.writerow(["Nota", "Pixels"])

  for image in arrayImages:

    image = image.flatten().tolist()
  
    w.writerow([dollar, image])
