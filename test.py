from PIL import Image
import numpy as np

img = Image.open("output.jpg").convert("RGB")
arr = np.array(img, dtype=np.float32)

# Estimate background from corners
corners = [arr[:20,:20], arr[:20,-20:], arr[-20:,:20], arr[-20:,-20:]]
bg_color = np.median(np.vstack([c.reshape(-1,3) for c in corners]), axis=0)

# Shift every pixel so background becomes white (255,255,255)
shift = 255 - bg_color
arr = np.clip(arr + shift, 0, 255).astype(np.uint8)

Image.fromarray(arr).save("output_fixed.jpg")
