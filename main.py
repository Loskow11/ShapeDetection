import cv2
import numpy as np

def detect_shapes(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return

    # conversion en niveaux de gris pour que ça simplifie l'analyse
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # petit flou gaussien
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # binarisation pour isoler les formes du fond
    _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)

    # affichage du masque pour vérif
    cv2.imshow("threshold", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_shapes("test_shapes.png")