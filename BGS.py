import cv

captura = cv.CaptureFromCAM(1)

cv.NamedWindow("Webcam", 1)
cv.NamedWindow("Mascara", 1)
cv.NamedWindow("Cinza", 1)

mascara = cv.CreateImage((640,480), 8, 3)
cinza = cv.CreateImage((640,480), 8, 1)

primeiraImagem = cv.LoadImage('Files/bg.jpg')
fundo = cv.CloneImage(primeiraImagem)
cv.Smooth(fundo,fundo,cv.CV_GAUSSIAN,3)

while True:
    imagem = cv.LoadImage('Files/test.jpg')
    # imagem = cv.QueryFrame(captura)
    cv.Smooth(imagem,imagem,cv.CV_GAUSSIAN,3)
    maiorArea = 0
    cv.AbsDiff(imagem,fundo,mascara)
    cv.CvtColor(mascara, cinza, cv.CV_BGR2GRAY)
    cv.Threshold(cinza,cinza, 50,255,cv.CV_THRESH_BINARY)

    cv.Dilate(cinza, cinza, None, 3)
    cv.Erode(cinza, cinza, None, 3) 

    cv.ShowImage("Mascara", mascara)
    cv.ShowImage("Cinza", cinza)
    cv.ShowImage("Webcam", imagem)
    
    if cv.WaitKey(7) % 0x100 == 27:
        break
