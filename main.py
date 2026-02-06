import cv2
import sys

def detect_shapes(image_path):
    # chargement de l'image
    img = cv2.imread(image_path)
    if img is None:
        # gestion d'erreur si le chemin est mauvais
        print("erreur: l'image est introuvable")
        return

    # affichage brut pour debug
    cv2.imshow("formes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_shapes("test_shapes.png")