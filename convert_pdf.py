nom_pdf = 'derivee_vectorielle_A4_2ppf.pdf'
pdf_chemin = f'_static/pdfs/{nom_pdf}'
dossier_sortie = 'ressources/img/derivee_vectorielle/'

from pdf2image import convert_from_path

images = convert_from_path(pdf_chemin)

for i, image in enumerate(images):
    image.save(f'{dossier_sortie}/0_page_{i+1}.png', 'PNG')

print("Conversion 2ppf terminée !")


from pdf2image import convert_from_path
from PIL import Image

# Convertir le PDF en images
images = convert_from_path(pdf_chemin)

for i, image in enumerate(images, start=1):
    width, height = image.size
    mid = width // 2  # Milieu de l'image
    
    # Découper la partie gauche
    left_part = image.crop((0, 0, 0.975*mid, height))
    left_part.save(f'{dossier_sortie}page_{i}_gauche.png', 'PNG')
    
    # Découper la partie droite
    right_part = image.crop((1.025*mid, 0, width, height))
    right_part.save(f'{dossier_sortie}page_{i}_droite.png', 'PNG')
    
    print(f"Page {i} découpée en gauche et droite")

print("Découpage gauche-droite terminé !")