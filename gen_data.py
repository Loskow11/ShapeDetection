import cv2
import numpy as np
import random

# les versions précédent ont un gros problème : des collisions entre les formes générées peuvent arriver, ce qui
# fausse complétement les résultats de l'algorithme de détection des formes.

def generate_random_shapes():
    # creation image noire 600x600
    img = np.zeros((600, 600, 3), dtype="uint8")
    
    # masque d'occupation pour gestion des collisions (les collisions sont très ennuyantes)
    occupancy_mask = np.zeros((600, 600), dtype="uint8")

    # generation aleatoire de 5 a 10 formes
    num_shapes = random.randint(5, 10)
    
    for _ in range(num_shapes):
        # tentatives max par forme pour trouver un espace libre
        max_attempts = 50
        
        for attempt in range(max_attempts):
            # masque temporaire pour la forme candidate
            temp_mask = np.zeros((600, 600), dtype="uint8")
            
            shape_type = random.choice(["circle", "rectangle", "triangle", "square"])
            
            # couleur et parametres aleatoires
            color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            # j'ai reduit un peu la zone de pop pour eviter les bords
            cx = random.randint(50, 550)
            cy = random.randint(50, 550)
            size = random.randint(30, 70)

            # dessin sur le masque temporaire (blanc pour verification)
            if shape_type == "circle":
                cv2.circle(temp_mask, (cx, cy), size, 255, -1)
                
            elif shape_type == "rectangle":
                w = size
                h = random.randint(30, 70)
                cv2.rectangle(temp_mask, (cx - w, cy - h), (cx + w, cy + h), 255, -1)

            elif shape_type == "square":
                cv2.rectangle(temp_mask, (cx - size, cy - size), (cx + size, cy + size), 255, -1)
                
            elif shape_type == "triangle":
                pt1 = (cx, cy - size)
                pt2 = (cx - size, cy + size)
                pt3 = (cx + size, cy + size)
                pts = np.array([pt1, pt2, pt3], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.fillPoly(temp_mask, [pts], 255)

            # ajout de la marge de securité (dilatation)
            # on gonfle artificiellement les formes deja existantes pour pas que la nouvelle se colle
            kernel = np.ones((15, 15), np.uint8)
            occupancy_dilated = cv2.dilate(occupancy_mask, kernel, iterations=1)

            # verification de collision : intersection entre masque dilaté et temp
            intersection = cv2.bitwise_and(occupancy_dilated, temp_mask)
            
            # si collision detectee, on reessaie
            if np.count_nonzero(intersection) > 0:
                continue 

            # pas de collision : application sur l'image finale
            img[temp_mask == 255] = color
            
            # mise a jour du masque d'occupation (le vrai, pas le dilaté)
            occupancy_mask = cv2.bitwise_or(occupancy_mask, temp_mask)
            break

    # sauvegarde
    cv2.imwrite("test_shapes.png", img)
    print(f"generation terminee : {num_shapes} formes (sans overlap).")

if __name__ == "__main__":
    generate_random_shapes()