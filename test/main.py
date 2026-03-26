import cv2
import numpy as np

img = cv2.imread("input.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary
thresh = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY_INV,
    15, 8
)

# Detect horizontal lines
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (150, 3))
lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Create mask for lines
mask = lines

# Remove lines using inpainting (THIS is the key)
clean = cv2.inpaint(gray, mask, 3, cv2.INPAINT_TELEA)

# Re-threshold after cleaning
thresh = cv2.adaptiveThreshold(
    clean, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY_INV,
    15, 8
)
# 3. Find rows using horizontal projection
horizontal_proj = np.sum(thresh, axis=1)

rows = []
in_row = False
start = 0

for i, val in enumerate(horizontal_proj):
    if val > 500 and not in_row:
        start = i
        in_row = True
    elif val <= 500 and in_row:
        rows.append((start, i))
        in_row = False

letter_id = 0

# 4. Process each row
for (y1, y2) in rows:
    row_img = thresh[y1:y2, :]

    vertical_proj = np.sum(row_img, axis=0)

    in_char = False
    start = 0

    for i, val in enumerate(vertical_proj):
        if val > 200 and not in_char:
            start = i
            in_char = True
        elif val <= 200 and in_char:
            x1, x2 = start, i
            char = img[y1:y2, x1:x2]

            if char.shape[0] > 15 and char.shape[1] > 10:
                cv2.imwrite(f"char_{letter_id}.png", char)
                letter_id += 1

            in_char = False

print("Extracted:", letter_id)
