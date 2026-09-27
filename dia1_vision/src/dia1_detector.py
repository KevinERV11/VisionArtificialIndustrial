import cv2

#Cargar imagen
img = cv2.imread("../imgs/pieza.jpg")
if img is None:
    raise FileNotFoundError("Coloca una imagen llamada pieza.jpg en la carpeta imgs")

#Escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Filtro Gaussiano
blur = cv2.GaussianBlur(gray, (5, 5), 1.2)

#Detectores de bordes
edges = cv2.Canny(blur, 80, 160)

#Guardar resultados
cv2.imwrite("../imgs/bordes_pieza.jpg", edges)

print("Dia 1 completado.Resultado guardado en imgs/bordes_pieza.jpg")
