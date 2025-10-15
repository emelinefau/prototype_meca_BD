from pdf2image import convert_from_path

images = convert_from_path('_static/hyperstatisme_A4_2ppf.pdf')

for i, image in enumerate(images):
    image.save(f'_static/page_{i+1}.png', 'PNG')

print("Conversion terminée !")