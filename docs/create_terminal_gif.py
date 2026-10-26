from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "terminal-anim.gif"
W, H = 720, 320
FONT_CANDIDATES = [
    Path(r"C:\Windows\Fonts\consola.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
    Path("/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf"),
]
FONT_PATH = next((str(path) for path in FONT_CANDIDATES if path.exists()), None)

def mono(size):
    return ImageFont.truetype(FONT_PATH, size) if FONT_PATH else ImageFont.load_default(size=size)

FONT = mono(16)
SMALL = mono(12)
TINY = mono(10)

SCENES = [
    ("git status", ["branch: learning", "state: exploring"]),
    ("python learning.py", ["# one step at a time"]),
    ("node explore.js", ['stack.load("javascript")', 'stack.load("python")']),
    ("mysql --learning-mode", ['stack.load("mysql")']),
    ("keep_building --with-intention", []),
]


def draw_frame(command, outputs, phase, cursor_on):
    im = Image.new("RGB", (W, H), "#0B0B0D")
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((12, 12, W - 12, H - 12), radius=15, fill="#171717", outline="#741925", width=2)
    d.rounded_rectangle((12, 12, W - 12, 50), radius=15, fill="#202020")
    d.rectangle((12, 33, W - 12, 50), fill="#202020")
    for x, color in ((34, "#B51F35"), (55, "#D2A45D"), (76, "#8D72C7")):
        d.ellipse((x - 5, 25, x + 5, 35), fill=color)
    d.text((100, 22), "PURPLE-DEV  /  VISUAL SIMULATION", font=SMALL, fill="#D2A45D")
    d.text((W - 125, 22), "TRACK_01", font=TINY, fill="#F4F0E8")

    # A quiet stage-light sweep and discreet pinstripes stay behind the terminal text.
    sweep_x = 468 + int(28 * math.sin(phase * 0.16))
    d.line((sweep_x, 54, sweep_x + 60, H - 28), fill="#302327", width=1)
    for x in range(596, 696, 18):
        d.line((x, 58, x, 243), fill="#F4F0E8", width=1)
        # Keep pinstripes almost invisible so they don't compete with the text.
        d.line((x, 58, x, 243), fill="#262326", width=1)

    y = 76
    x = 34
    user = "tiagx422"
    host = "@purple-dev"
    path_prompt = ":~$ "
    d.text((x, y), user, font=FONT, fill="#B51F35")
    x += d.textlength(user, font=FONT)
    d.text((x, y), host, font=FONT, fill="#D2A45D")
    x += d.textlength(host, font=FONT)
    d.text((x, y), path_prompt, font=FONT, fill="#F4F0E8")
    x += d.textlength(path_prompt, font=FONT)
    d.text((x, y), command, font=FONT, fill="#F4F0E8")
    x += d.textlength(command, font=FONT)
    if cursor_on:
        d.rectangle((x + 3, y + 3, x + 12, y + 22), fill="#D2A45D")

    out_y = 116
    for line in outputs[:2]:
        d.text((52, out_y), line, font=FONT, fill="#F4F0E8")
        out_y += 30

    # A moving segment works as a quiet process indicator without implying a skill score.
    d.text((34, 204), "SESSION", font=TINY, fill="#D2A45D")
    start_x = 108
    active = int(phase / 3) % 5
    for i in range(5):
        color = "#B51F35" if i == active else "#40363A"
        d.rounded_rectangle((start_x + i * 22, 202, start_x + i * 22 + 13, 211), radius=3, fill=color)
    d.text((246, 201), "exploring", font=TINY, fill="#F4F0E8")

    # Low-amplitude waveform bars move slowly like a small audio-console meter.
    base_y = 267
    d.line((34, base_y, W - 34, base_y), fill="#514438", width=1)
    colors = ["#D2A45D", "#B51F35", "#8D72C7"]
    for i in range(42):
        wave = math.sin(i * 0.62 + phase * 0.14) * 5 + math.sin(i * 0.21 - phase * 0.09) * 3
        height = 3 + abs(wave)
        x_bar = 42 + i * 15
        d.line((x_bar, base_y - height, x_bar, base_y + height), fill=colors[i % 3], width=2)
    d.text((34, 285), "learning loop  ·  quiet signal", font=TINY, fill="#9B9087")
    return im.convert("P", palette=Image.Palette.ADAPTIVE, colors=48, dither=Image.Dither.NONE)

frames = []
durations = []
phase = 0
for command, outputs in SCENES:
    for n in range(0, len(command) + 1, 2):
        frames.append(draw_frame(command[:n], [], phase, cursor_on=(phase // 4) % 2 == 0))
        durations.append(140)
        phase += 1
    # Let each line settle while the waveform and session marker move gently.
    for _ in range(4):
        frames.append(draw_frame(command, outputs, phase, cursor_on=(phase // 4) % 2 == 0))
        durations.append(350)
        phase += 1

# A quiet final pause makes the loop feel deliberate rather than hurried.
frames.append(draw_frame(SCENES[-1][0], [], phase, cursor_on=True))
durations.append(1200)
OUT.parent.mkdir(parents=True, exist_ok=True)
frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=True, disposal=1)
print(f"{OUT}\t{OUT.stat().st_size}\t{len(frames)} frames\t{sum(durations) / 1000:.2f} seconds")




