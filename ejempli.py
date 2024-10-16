from PIL import Image

# Abre la imagen desde la ruta completa
imagen = Image.open(r'C:\Users\Gabriela Diaz\Pictures\Saved Pictures\isic.jpg')

# Mostrar la imagen original
imagen.show()

# Cambiar el tamaño de la imagen (200x200 píxeles)
imagen_redimensionada = imagen.resize((200, 200))

# Guardar la imagen redimensionada en la misma carpeta
imagen_redimensionada.save(r'C:\Users\Gabriela Diaz\Pictures\Saved Pictures\ejemplo_redimensionado.jpg')

# Mostrar un mensaje indicando que se ha guardado la imagen redimensionada
print("La imagen redimensionada se ha guardado como 'ejemplo_redimensionado.jpg'")
