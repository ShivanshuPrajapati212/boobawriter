from PIL import Image
from numpy import random



width = 16 
height = 33 
x_offset = 193
y_offset = 118
line_gap = 10
slope = 0.5 

def getText():
    text = [] 
    with open("text.txt", "r") as f:
        contents = f.read().splitlines()
        text = contents
        f.close()

    return text


def createImage(text: list[str]):
    # total_width = width * (max(len(s) for s in text))
    # total_height = height * len(text) 

    image = Image.open("paper.jpeg")

    for line_no, line in enumerate(text):
        for idx, letter in enumerate(line):
            if letter == " ":
                letter = "SPACE"
            if letter.islower() == True:
                letter = letter + "-Lower"

            img = Image.open(f"shivanshu-handwriting/{letter}.jpeg")

            scaled = img.resize((width, height))

            inregularity_x = random.randint(-2, 2)
            inregularity_y = random.randint(-2, 2)


            image.paste(scaled, (width * idx + x_offset + inregularity_x , height * line_no + y_offset + line_gap*line_no + int(idx * slope) + inregularity_y))
    
    image.save("output.jpg")


if __name__ == "__main__":
   text = getText() 
   print(text)
   createImage(text)
