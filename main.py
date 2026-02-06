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
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # filtre de bruit
        if cv2.contourArea(contour) < 500:
            continue

        # approximation polygonale pour simplifier la forme
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # récupération de la bounding box pour le placement du texte
        x, y, w, h = cv2.boundingRect(approx)
        shape_name = "inconnu"
        
        # logique de classification basée sur le nombre de sommets
        vertices = len(approx)

        if vertices == 3:
            shape_name = "triangle"
        
        elif vertices == 4:
            # calcul du ratio pour différencier carré et rectangle
            aspect_ratio = float(w) / h
            shape_name = "carre" if 0.95 <= aspect_ratio <= 1.05 else "rectangle"
        
        elif vertices > 4:
            # on assume cercle pour les polygones complexes dans ce contexte
            shape_name = "cercle"

        # affichage final
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
        cv2.putText(img, shape_name, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    cv2.imshow("resultat", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_shapes("test_shapes.png")