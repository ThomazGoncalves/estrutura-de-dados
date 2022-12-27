from PIL import Image

# Abrindo a imagem
imagem = Image.open("C:/Users/thoma/Desktop/Logo-site.png")

imagem = imagem.convert("RGB")

# Salvando a imagem com uma nova extensão
imagem.save("C:/Users/thoma/Desktop/Logo-site.jpg")
