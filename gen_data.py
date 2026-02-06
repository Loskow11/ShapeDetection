import cv2
import numpy as np

# créer une image noire (500x500)
img = np.zeros((500, 500, 3), dtype="uint8")

# dessiner un carré (haut gauche)
cv2.rectangle(img, (50, 50), (150, 150), (255, 255, 255), -1)

# dessiner un rectangle (haut droite)
cv2.rectangle(img, (300, 50), (450, 150), (255, 255, 255), -1)

# dessiner un cercle (bas gauche)
cv2.circle(img, (100, 350), 50, (255, 255, 255), -1)

# dessiner un triangle (bas droite)
pts = np.array([[375, 300], [300, 400], [450, 400]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(img, [pts], (255, 255, 255))

# sauvegarder l'imagee
cv2.imwrite("test_shapes.png", img)
print("image 'test_shapes.png' générée avec succès.")