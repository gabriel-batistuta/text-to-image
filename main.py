from PIL import Image, ImageDraw, ImageFont

# Tamanho da imagem do Instagram (1080x1080 pixels)
image_width = 1080
image_height = 1080
background_color = "white"  # Cor de fundo da imagem
text_color = "black"  # Cor do texto
text_content = "Test"  # O texto que você quer adicionar

# Carregar uma fonte
font_path = "Arial.ttf"  # Substitua pelo caminho da sua fonte
font_size = 100
font = ImageFont.truetype(font_path, font_size)

# Criar uma nova imagem com o tamanho especificado e cor de fundo
image = Image.new("RGB", (image_width, image_height), background_color)

# Iniciar o desenho na imagem
draw = ImageDraw.Draw(image)

def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

# # Calcular a largura e a altura do texto
# text_width = draw.textlength(text_content, font=font)
# text_height = draw.(text_content)[1]
# text_width, text_height = draw.textsize(text_content, font=font)

text_width, text_height = textsize(text_content, font=font)

# Posição para centralizar o texto na imagem
text_x = (image_width - text_width) / 2
text_y = (image_height - text_height) / 2

# Adicionar o texto à imagem
draw.text((text_x, text_y), text_content, fill=text_color, font=font)

# Salvar a imagem como um arquivo PNG
image.save("imagem_para_instagram.png")
