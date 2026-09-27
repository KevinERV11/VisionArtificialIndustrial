import cv2
import numpy as np
import os
import random

output_dir = "../imgs/dataset_sintetico"
os.makedirs(output_dir, exist_ok=True)

def generar_pieza_sintetica(idx):
    img = np.zeros((480, 640, 3), dtype=np.uint8)

    # Fondo industrial gris
    img[:] = (random.randint(80,120), random.randint(80,120), random.randint(80,120))

    # Dibujar pieza (círculo, rectángulo, engranaje simple)
    tipo = random.choice(["circulo", "rectangulo", "engranaje"])

    if tipo == "circulo":
        cv2.circle(img, (320,240), random.randint(60,120), (200,200,200), -1)

    elif tipo == "rectangulo":
        cv2.rectangle(img, (200,150), (440,330), (200,200,200), -1)

    elif tipo == "engranaje":
        for i in range(12):
            angle = i * 30
            x = int(320 + 100 * np.cos(np.radians(angle)))
            y = int(240 + 100 * np.sin(np.radians(angle)))
            cv2.circle(img, (x,y), 20, (200,200,200), -1)
        cv2.circle(img, (320,240), 60, (200,200,200), -1)

    # Ruido industrial
    ruido = np.random.normal(0, 20, img.shape).astype(np.int16)
    img = np.clip(img.astype(np.int16) + ruido, 0, 255).astype(np.uint8)

    # Blur industrial
    if random.random() > 0.5:
        img = cv2.GaussianBlur(img, (5,5), random.uniform(0.5, 1.5))

    # Sombras duras
    if random.random() > 0.5:
        sombra = np.zeros_like(img)
        cv2.circle(sombra, (random.randint(0,640), random.randint(0,480)),
                   random.randint(80,200), (random.randint(0,40),)*3, -1)
        img = cv2.addWeighted(img, 1, sombra, 0.5, 0)

    # Defectos simulados
    if random.random() > 0.7:
        cv2.line(img,
                 (random.randint(0,640), random.randint(0,480)),
                 (random.randint(0,640), random.randint(0,480)),
                 (0,0,0), random.randint(2,6))

    cv2.imwrite(f"{output_dir}/pieza_{idx}.jpg", img)


# Generar 20 imágenes
for i in range(20):
    generar_pieza_sintetica(i)

print("Dataset sintético generado en imgs/dataset_sintetico/")



