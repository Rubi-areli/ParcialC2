from PIL import Image

# Abre la imagen desde la ruta completa
imagen = Image.open(r'C:\Users\Gabriela Diaz\Pictures\Saved Pictures\neto.jpg')

# Mostrar la imagen original
imagen.show()

# Guardar la imagen en un formato diferente (PNG en este caso)
imagen.save(r'C:\Users\Gabriela Diaz\Pictures\Saved Pictures\neto_convertido.png', 'PNG')

# Mensaje de confirmación
print("La imagen se ha convertido y guardado como 'Carro_convertido.png'")
