#!/usr/bin/env python3
"""Render the compact ASCII symbol with a light, looping digital rain."""

from __future__ import annotations

import argparse
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SYMBOL = ROOT / "assets" / "ascii-art-compact.txt"
DEFAULT_OUTPUT = ROOT / "assets"

THEMES = {
    "dark": {
        "symbol": (220, 194, 255),
        "edge": (168, 85, 247),
        "rain": [(48, 16, 77), (123, 44, 191), (168, 85, 247), (196, 167, 255)],
    },
    "light": {
        "symbol": (72, 27, 112),
        "edge": (123, 44, 191),
        "rain": [(48, 16, 77), (123, 44, 191), (168, 85, 247), (196, 167, 255)],
    },
}


def load_symbol(path: Path) -> list[str]:
    rows = [line.rstrip("\r\n") for line in path.read_text(encoding="utf-8").splitlines()]
    rows = [row for row in rows if row.strip()]
    if not rows:
        raise ValueError(f"No symbol characters found in {path}")
    width = max(map(len, rows))
    rows = [row.ljust(width) for row in rows]
    occupied = [(x, y) for y, row in enumerate(rows) for x, char in enumerate(row) if char != " "]
    if not occupied:
        raise ValueError(f"The symbol in {path} contains only spaces")
    left = min(x for x, _ in occupied)
    right = max(x for x, _ in occupied) + 1
    top = min(y for _, y in occupied)
    bottom = max(y for _, y in occupied) + 1
    return [row[left:right] for row in rows[top:bottom]]


def load_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/consola.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
        Path("/Library/Fonts/Menlo.ttc"),
    ]
    for candidate in candidates:
        if candidate.exists():
            try:
                return ImageFont.truetype(str(candidate), size=size)
            except OSError:
                pass
    return ImageFont.load_default()


def make_palette(colors: list[tuple[int, int, int]]) -> Image.Image:
    # Palette index 0 is reserved for transparency; the visible colors begin at 1.
    palette = [0, 0, 0]
    for color in colors:
        palette.extend(color)
    palette.extend([0, 0, 0] * (256 - len(palette) // 3))
    palette_image = Image.new("P", (1, 1))
    palette_image.putpalette(palette[:768])
    return palette_image


def quantize_transparent(frame: Image.Image, palette: Image.Image) -> Image.Image:
    alpha = frame.getchannel("A")
    result = frame.convert("RGB").quantize(palette=palette, dither=Image.Dither.NONE)
    pixels = list(result.get_flattened_data())
    alpha_values = list(alpha.get_flattened_data())
    for index, opacity in enumerate(alpha_values):
        if opacity < 32:
            pixels[index] = 0
    result.putdata(pixels)
    return result


def render_frames(
    symbol: list[str],
    *,
    theme: str,
    width: int,
    height: int,
    font_size: int,
    frames: int,
    density: float,
    seed: int,
) -> list[Image.Image]:
    colors = THEMES[theme]
    font = load_font(font_size)
    probe = Image.new("RGBA", (1, 1))
    probe_draw = ImageDraw.Draw(probe)
    advance = max(1, round(probe_draw.textlength("0", font=font)))
    line_height = max(font_size, font.getbbox("0")[3] - font.getbbox("0")[1])
    symbol_width = max(map(len, symbol)) * advance
    symbol_height = len(symbol) * line_height
    margin_x = max(10, font_size * 2)
    margin_y = max(10, font_size * 2)
    if symbol_width + margin_x * 2 > width or symbol_height + margin_y * 2 > height:
        raise ValueError("The symbol is larger than the canvas; increase width/height or use a smaller font")
    symbol_x = (width - symbol_width) // 2
    symbol_y = (height - symbol_height) // 2

    rng = random.Random(seed)
    rain_count = max(1, round(width / (font_size * 2.4) * density))
    streams = []
    for _ in range(rain_count):
        streams.append({
            "x": rng.randrange(0, max(1, width - advance)),
            "y": rng.randrange(-height, height),
            "speed": rng.choice((1, 1, 2)),
            "length": rng.randrange(2, 5),
            "chars": [rng.choice("0123456789abcdef") for _ in range(6)],
            "color": rng.choice(colors["rain"]),
        })

    palette_colors = [colors["symbol"], colors["edge"], *colors["rain"]]
    palette = make_palette(palette_colors)
    output: list[Image.Image] = []
    for frame_index in range(frames):
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(frame)
        for stream in streams:
            x = stream["x"]
            head_y = (stream["y"] + frame_index * stream["speed"]) % (height + font_size * 8) - font_size * 8
            for trail_index in range(stream["length"]):
                y = head_y - trail_index * line_height
                if 0 <= y < height:
                    color = stream["color"] if trail_index else colors["edge"]
                    draw.text((x, y), stream["chars"][(frame_index + trail_index) % 6], font=font, fill=(*color, 205))

        for row_index, row in enumerate(symbol):
            for column_index, char in enumerate(row):
                if char == " ":
                    continue
                color = colors["symbol"] if char == "0" else colors["edge"]
                draw.text(
                    (symbol_x + column_index * advance, symbol_y + row_index * line_height),
                    char,
                    font=font,
                    fill=(*color, 255),
                )
        output.append(quantize_transparent(frame, palette))
    return output


def write_theme(args: argparse.Namespace, theme: str, symbol: list[str]) -> None:
    frames = render_frames(
        symbol,
        theme=theme,
        width=args.width,
        height=args.height,
        font_size=args.font_size,
        frames=args.frames,
        density=args.density,
        seed=args.seed,
    )
    output = args.output_dir / f"purple-rain-{theme}.gif"
    frames[0].save(
        output,
        save_all=True,
        append_images=frames[1:],
        duration=args.delay_ms,
        loop=0,
        optimize=True,
        disposal=2,
        transparency=0,
    )
    print(f"Wrote {output} ({output.stat().st_size:,} bytes)")
    if theme == "dark":
        preview = args.output_dir / "purple-rain-preview.png"
        still = Image.new("RGBA", frames[0].size, "#0D0714")
        still.alpha_composite(frames[0].convert("RGBA"))
        still.convert("RGB").save(preview)
        print(f"Wrote {preview} ({preview.stat().st_size:,} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbol", type=Path, default=DEFAULT_SYMBOL, help="ASCII art file; every non-space character is drawn")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT, help="Folder for GIF and preview output")
    parser.add_argument("--density", type=float, default=0.2, help="Rain stream density from 0.01 (sparse) to 1.0 (dense)")
    parser.add_argument("--delay-ms", type=int, default=110, help="Time per animation frame in milliseconds")
    parser.add_argument("--frames", type=int, default=18, help="Number of frames in the looping animation")
    parser.add_argument("--width", type=int, default=420, help="Canvas width in pixels")
    parser.add_argument("--height", type=int, default=380, help="Canvas height in pixels")
    parser.add_argument("--font-size", type=int, default=8, help="Monospaced character size in pixels")
    parser.add_argument("--seed", type=int, default=29, help="Random seed for reproducible rain")
    args = parser.parse_args()
    if not 0.01 <= args.density <= 1.0:
        parser.error("--density must be between 0.01 and 1.0")
    if args.frames < 2 or args.frames > 80:
        parser.error("--frames must be between 2 and 80")
    if args.delay_ms < 40:
        parser.error("--delay-ms must be at least 40")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    symbol = load_symbol(args.symbol)
    for theme in ("dark", "light"):
        write_theme(args, theme, symbol)


if __name__ == "__main__":
    main()

