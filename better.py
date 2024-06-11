from PIL import Image, ImageEnhance

# Bild öffnen
image = Image.open('AG_034.jpg')

# Helligkeit anpassen
enhancer = ImageEnhance.Brightness(image)
image_brightened = enhancer.enhance(1.5)  # 1.5 ist der Faktor der Helligkeitsanpassung

# Kontrast anpassen
enhancer = ImageEnhance.Contrast(image_brightened)
image_contrasted = enhancer.enhance(1.5)  # 1.5 ist der Faktor der Kontrasteinstellung

# Ergebnis speichern
image_contrasted.save('enhanced_image.jpg')

# Optional: Ergebnis anzeigen
image_contrasted.show()