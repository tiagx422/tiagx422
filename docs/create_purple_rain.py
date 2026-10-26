from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "purple-rain.gif"
W, H, FRAMES = 720, 190, 36
FONT_PATH = Path(r"C:\Windows\Fonts\consola.ttf")
font = ImageFont.truetype(str(FONT_PATH), 18) if FONT_PATH.exists() else ImageFont.load_default(size=18)
small = ImageFont.truetype(str(FONT_PATH), 12) if FONT_PATH.exists() else ImageFont.load_default(size=12)
# Fixed seeds and integer wrap make the loop return cleanly to frame zero.
seeds = [(i * 37 % W, i * 53 % H, 1 + (i % 3), 9 + (i * 7 % 19)) for i in range(54)]
frames=[]
for f in range(FRAMES):
    im=Image.new("RGB",(W,H),"#12091f"); d=ImageDraw.Draw(im)
    d.rounded_rectangle((10,10,W-10,H-10),radius=13,fill="#1b1029",outline="#6d28d9",width=2)
    d.rounded_rectangle((10,10,W-10,43),radius=13,fill="#28113f")
    d.rectangle((10,30,W-10,43),fill="#28113f")
    for x,c in ((30,"#a855f7"),(49,"#d8b4fe"),(68,"#70f0a0")): d.ellipse((x-4,22,x+4,30),fill=c)
    d.text((90,19),"PURPLE STAGE  /  VISUAL LOOP",font=small,fill="#d8b4fe")
    d.text((W-144,19),"RAIN / 01",font=small,fill="#b7a7c9")
    # Small dim streams sit behind terminal copy.
    for x,y,speed,length in seeds:
        yy=(y + f*speed) % (H-52) + 48
        d.line((x,yy-length,x,yy),fill="#6d28d9",width=1)
        d.point((x,yy),fill="#d8b4fe")
    d.rounded_rectangle((26,58,W-26,H-25),radius=8,fill="#160d22",outline="#49305d",width=1)
    d.text((47,78),"tiagx422@purple-stage:~$",font=font,fill="#a855f7")
    d.text((47,108),"learning code, one riff at a time",font=font,fill="#f3e8ff")
    d.text((47,141),"git  /  javascript  /  python  /  mysql",font=small,fill="#b7a7c9")
    # Gentle signal meter, decorative rather than a claim about real activity.
    for i in range(16):
        h=3+int(4*(1+math.sin((i+f)*.45)))
        d.rectangle((W-245+i*10,147-h,W-240+i*10,147),fill="#a855f7" if i%4 else "#d8b4fe")
    frames.append(im.quantize(colors=48,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE))
frames[0].save(OUT,save_all=True,append_images=frames[1:],duration=120,loop=0,optimize=True,disposal=2)
print(f"{OUT}: {OUT.stat().st_size} bytes, {FRAMES} frames, {FRAMES*120/1000:.2f}s loop, {W}x{H}")
