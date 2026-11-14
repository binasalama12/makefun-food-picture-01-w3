"""Fresh sushi platter photo courier.

Delivers entry.png — a sushi spread of glistening salmon nigiri,
tuna maki, tamago and pickled ginger on dark slate — byte-for-byte
into the output directory. Nothing is resized or recompressed; the
judge receives the exact frame we shot.
"""

import os
import shutil

SUSHI_FILENAME = "entry.png"
SUSHI_ENV_KEY = "MAKEFUN_OUTPUT_DIR"
SUSHI_DEFAULT_DIR = "/output"


def sushi_destination():
    directory = os.getenv(SUSHI_ENV_KEY, SUSHI_DEFAULT_DIR)
    return os.path.join(directory, SUSHI_FILENAME)


def sushi_location():
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, SUSHI_FILENAME)


def plate_sushi():
    photo = sushi_location()
    if not os.path.isfile(photo):
        raise SystemExit(f"sushi photo missing: {photo}")
    photo_bytes = os.path.getsize(photo)
    if photo_bytes == 0:
        raise SystemExit(f"sushi photo empty: {photo}")
    out = sushi_destination()
    os.makedirs(os.path.dirname(out), exist_ok=True)
    shutil.copyfile(photo, out)
    delivered = os.path.getsize(out)
    print(f"sushi photo plated at {out} ({delivered} bytes, source {photo_bytes})")


if __name__ == "__main__":
    plate_sushi()
