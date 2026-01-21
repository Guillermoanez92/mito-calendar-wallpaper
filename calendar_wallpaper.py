from PIL import Image, ImageDraw, ImageFont
import calendar
from datetime import date

# ---- CONFIG ----
# ---- CONFIG ----
WIDTH, HEIGHT = 1170, 2532
BG_COLOR = "#58855C"
PRIMARY = "#000000"

TITLE_SIZE = 96
DAY_SIZE = 56
TODAY_SIZE = 64

def load_font(size):
    try:
        return ImageFont.truetype("SFNS.ttf", size)
    except:
        try:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
        except:
            return ImageFont.load_default()

title_font = load_font(TITLE_SIZE)
day_font = load_font(DAY_SIZE)
today_font = load_font(TODAY_SIZE)


OUTPUT = "calendar_wallpaper.png"



# ---- DATE ----
today = date.today()
year, month, day = today.year, today.month, today.day
month_name = calendar.month_name[month]
month_days = calendar.monthrange(year, month)[1]
first_weekday = calendar.monthrange(year, month)[0]

# ---- IMAGE ----
img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)



# ---- TITLE ----
title_text = f"{month_name.upper()} {year}"
bbox = draw.textbbox((0, 0), title_text, font=title_font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
draw.text(((WIDTH - tw) / 2, 200), title_text, PRIMARY, font=title_font)

# ---- CALENDAR GRID ----
cols = 7
cell_w = WIDTH // cols
cell_h = 120
start_y = HEIGHT / 2

for d in range(1, month_days + 1):
    idx = d + first_weekday - 1
    row = idx // cols
    col = idx % cols

    x = col * cell_w + cell_w // 2
    y = start_y + row * cell_h

    if d < day:
        color = "#888888"
        font = day_font
    elif d == day:
        color = PRIMARY
        font = today_font
        draw.ellipse(
            [x - 42, y - 42, x + 42, y + 42],
            outline=PRIMARY,
            width=4
        )
    else:
        color = "#000000"
        font = day_font

    text = str(d)
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text((x - w / 2, y - h / 2), text, color, font=font)

# ---- SAVE ----
img.save(OUTPUT)
print("Wallpaper generated:", OUTPUT)
