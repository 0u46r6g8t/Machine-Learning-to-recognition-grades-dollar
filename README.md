# Projeto de reconhecimento de dolares

Este projeto tem como objetivo realizar a analise e detecção de notas da moeda internacional 'Dolar', sendo que o mesmo possui valores de 1, 5, 10, 50 e 100 dolares, para isso foi realizada uma série de processamentos em cima de uma dada quantidade de imagens que podem ser encontradas com facilidade na internet, feito isso foram retiradas algumas imagens de fundo como: Mesa, praia, entre outras. Com isso foram geradas imagens que podem ser chamadas de base de dados sintética, onde são realizadas transformações tanto em sua escala, rotação e translação para que a mesma possa ser localizada em várias partes diferentes na imagem do fundo.

Após realizar tais transformações, foi realizada a geração das imagens sintéticas onde para cada imagem de dolar (frente e verso) foram geradas cerca de 800 imagens, totalizando uma base de dados de 4000 imagens ao total que foram utilizadas para realizar o treinamento da rede neural (CNN) utilizando a biblioteca Tensorflow na linguagem Python 3.8.

## Sistema utilizado

  - Google Colab

    - 12 GB de Memória RAM;
    - 107 GB de armazenamento interno;

## Bibliotecas utilizadas

  - PIL
  - CSV
  - Numpy
  - Random
  - Matplotlib
  - Opencv (cv2)
  - Algumbumentation 
  - Biblioteca do sistema OS

## Dataset

  A base de dados depois de gerada e finalizada, foi convertida para um formato de arquivo chamado csv, onde o mesmo pode se comparar a uma tabela onde existem 2 (duas) colunas apenas, a primeira sendo o valor da nota respectivamente e o segundo o valor dos pixels da imagem.
  Para que os pixeis podessem ser armazenados de forma a qual seria possível serem lidos posteriormente e então utilizados, foi preciso realizar uma pequena conversão do formato matricial para um formato de array, para isso foi utilizado a função 'flatten'[1] em conjunto com 'tolist()'[2] da biblioteca numpy, cujo a primeira função realiza apenas a conversão de matrix para um formato de array, e logo após com a função [2] foi retornado para a variavel os valores completos do seu vetor, e então armazenados no arquivo '.csv'.
  
   