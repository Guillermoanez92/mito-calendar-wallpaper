from PIL import Image, ImageDraw, ImageFont
import calendar
from datetime import date

# ---- CONFIG ----
WIDTH, HEIGHT = 1170, 2532  # iPhone wallpaper resolution
BG_COLOR = "#000000"
PRIMARY = "#58855C"

FONT_PATH = "/System/Library/Fonts/SFNS.ttf"  # macOS system font
TITLE_SIZE = 96
DAY_SIZE = 56
TODAY_SIZE = 64

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

title_font = ImageFont.truetype(FONT_PATH, TITLE_SIZE)
day_font = ImageFont.truetype(FONT_PATH, DAY_SIZE)
today_font = ImageFont.truetype(FONT_PATH, TODAY_SIZE)

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
start_y = 400

for d in range(1, month_days + 1):
    idx = d + first_weekday - 1
    row = idx // cols
    col = idx % cols

    x = col * cell_w + cell_w // 2
    y = start_y + row * cell_h

    if d < day:
        color = "#444444"
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
        color = "#888888"
        font = day_font

    text = str(d)
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text((x - w / 2, y - h / 2), text, color, font=font)

# ---- SAVE ----
img.save(OUTPUT)
print("Wallpaper generated:", OUTPUT)
