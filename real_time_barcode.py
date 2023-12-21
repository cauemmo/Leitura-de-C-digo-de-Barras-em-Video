import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)  # webcam

cap.set(3, 640)
cap.set(4, 480)
#ler cada linha do arquivo texto mydata e passar para uma linha de verificação
with open('BdProdutos.text') as f:
    BdLista = f.read().splitlines()
#print(BdLista) --> mostra os arrquivos da lista


while True:

    sucess, img = cap.read()
    img = cv2.flip(img, 0)

    for barcode in decode(img):  #lendo o codigo de barras
        codigoBarra = barcode.data.decode('utf-8')  # tirando o b e as aspas da frente do codigo
        print(codigoBarra)  #escrevendo o valor de codigo debarra

        #vendo se o produto ta na lista
        if codigoBarra in BdLista:
            print('Produto no sistema')
            produto_barcode =codigoBarra
            print('O código do produto analisado é{}'.format(produto_barcode))
        else:
            print('Produto não avaliado,tente novamente')

        # marcando o codigo de barras com contorno
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)

    cv2.imshow('Result', img)
    cv2.waitKey(1)



