import cv2
import numpy as np

def detect_shapes(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return

    # conversion en niveaux de gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ptit flou gaussien
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)

    # extraction des contours externes uniquement
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # dessin des contours sur l'image originale
    for contour in contours:
        # filtre sur la taille
        if cv2.contourArea(contour) > 500:
            cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)

    cv2.imshow("contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_shapes("test_shapes.png")