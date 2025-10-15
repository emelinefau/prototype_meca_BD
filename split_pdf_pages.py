from pdf2image import convert_from_path
from PIL import Image

# Convertir le PDF en images
images = convert_from_path('_static/hyperstatisme/hyperstatisme_A4_2ppf.pdf')

for i, image in enumerate(images, start=1):
    width, height = image.size
    mid = width // 2  # Milieu de l'image
    
    # Découper la partie gauche
    left_part = image.crop((0, 0, mid, height))
    left_part.save(f'_static/page_{i}_gauche.png', 'PNG')
    
    # Découper la partie droite
    right_part = image.crop((mid, 0, width, height))
    right_part.save(f'_static/page_{i}_droite.png', 'PNG')
    
    print(f"Page {i} découpée en gauche et droite")

print("Découpage terminé !")