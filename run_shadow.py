#!/usr/bin/env -S python3 -B

from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["middle_square", "square", "inclined_plane", "ccc", "cube", "box"]:
        print(f"Рассматривается полиэдр {name}")
        Polyedr(f"data/{name}.geom").draw(tk)
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
