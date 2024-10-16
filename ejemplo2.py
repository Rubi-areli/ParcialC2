#El objetivo es abrir una imagen, convertirla
#a escala de grises y guardarla con un nuevo nombre, 
#manteniendo la imagen original intacta. 
#Además, muestra tanto la imagen original como la versión en escala de grises.
#

from PIL import Image

# Abre la imagen desde la ruta completa
imagen = Image.open(r'C:\Users\Gabriela Diaz\Pictures\Saved Pictures\neto.jpg')

# Mostrar la imagen original
imagen.show()

# Convertir la imagen a escala de grises
imagen_grises = imagen.convert('L')

# Guardar la imagen en escala de grises
imagen_grises.save(r'C:\Users\Gabriela Diaz\Pictures\Saved Pictures\neto_grises.jpg')

# Mostrar la imagen en escala de grises
imagen_grises.show()

# Mensaje de confirmación
print("La imagen se ha convertido a escala de grises y se ha guardado como 'carro_grises.jpg'")
