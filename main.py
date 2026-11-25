"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line (at most 20 words) for a crypto
trader who was just liquidated, to /output/entry.txt.
"""

import os

FORTUNE = "You will meet a wealthy stranger soon, trader \u2014 it is you, before the liquidation."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(FORTUNE)
