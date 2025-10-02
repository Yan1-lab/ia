from PIL import Image, ImageDraw, ImageFont
import os

# Crear carpeta assets si no existe
os.makedirs("assets", exist_ok=True)

# Tamaño del logo
W, H = 500, 500
img = Image.new("RGBA", (W, H), (255, 255, 255, 0))  # fondo transparente
draw = ImageDraw.Draw(img)

# Crear degradado azul → celeste
for y in range(H):
    r = 0
    g = int(102 + (153 - 102) * (y / H))
    b = int(204 + (255 - 204) * (y / H))
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# Dibujar círculo para que quede dentro del borde
mask = Image.new("L", (W, H), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((40, 40, W-40, H-40), fill=255)
circle = Image.new("RGBA", (W, H), (255, 255, 255, 0))
circle.paste(img, (0, 0), mask=mask)

# Crear imagen final
final_img = Image.new("RGBA", (W, H), (255, 255, 255, 0))
final_img.paste(circle, (0, 0), mask=mask)

# Fuente
try:
    font = ImageFont.truetype("arial.ttf", 180)
except:
    font = ImageFont.load_default()

text = "KB"
bbox = draw.textbbox((0,0), text, font=font)
w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
text_x, text_y = (W-w)/2, (H-h)/2

draw_final = ImageDraw.Draw(final_img)
# Sombra
draw_final.text((text_x+4, text_y+4), text, font=font, fill=(0,0,0,100))
# Letras principales
draw_final.text((text_x, text_y), text, font=font, fill=(255,255,255,255))

# Guardar
final_img.save("assets/logo.png")
print("✅ Logo KB generado en assets/logo.png")
