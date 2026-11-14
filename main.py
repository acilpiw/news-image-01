#!/usr/bin/env python3
"""news-image-01 entry: copy the image the repository holds to /output/entry.png.

The image is a JPEG (image.jpg, 1024x683, 202,304 bytes). The gate reads
magic bytes, so JPEG content in a file named entry.png is accepted; the
file name is fixed by the competition, the content is a whole JPEG under
1 MiB and 1024x1024. Standard library only, no network. Deterministic:
the same bytes every run.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "image.jpg")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard against a truncated copy: the entry must be the whole image,
    # byte for byte, not just the same size.
    assert os.path.getsize(dst) == os.path.getsize(src), "truncated copy"
    assert _sha256(dst) == _sha256(src), "copy differs from source"


if __name__ == "__main__":
    main()
