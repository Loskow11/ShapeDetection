import cv2
import numpy as np
import random

def generate_random_shapes():
    # créer une image noire 600x600
    img = np.zeros((600, 600, 3), dtype="uint8")
    
    # on va générer entre 5 et 10 formes aléatoires
    num_shapes = random.randint(5, 10)
    
    for _ in range(num_shapes):
        shape_type = random.choice(["circle", "rectangle", "triangle", "square"])
        
        # couleur aléatoire (on évite le trop sombre pour que ça se voit)
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        
        # coordonnées de base aléatoires (on garde une marge de 100px)
        cx = random.randint(100, 500)
        cy = random.randint(100, 500)
        size = random.randint(30, 80)

        if shape_type == "circle":
            cv2.circle(img, (cx, cy), size, color, -1)
            
        elif shape_type == "rectangle":
            # largeur et hauteur différentes
            w = size
            h = random.randint(30, 80)
            cv2.rectangle(img, (cx - w, cy - h), (cx + w, cy + h), color, -1)

        elif shape_type == "square":
            # largeur = hauteur
            cv2.rectangle(img, (cx - size, cy - size), (cx + size, cy + size), color, -1)
            
        elif shape_type == "triangle":
            # génération de 3 points autour du centre
            pt1 = (cx, cy - size)
            pt2 = (cx - size, cy + size)
            pt3 = (cx + size, cy + size)
            pts = np.array([pt1, pt2, pt3], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(img, [pts], color)

    # sauvegarde
    cv2.imwrite("test_shapes.png", img)
    print(f"nouvelle image générée avec {num_shapes} formes.")

if __name__ == "__main__":
    generate_random_shapes()