from PIL import Image

def getText():
    text = [] 
    with open("text.txt", "r") as f:
        contents = f.read().splitlines()
        text = contents
        f.close()

    return text


def createImage(text: list[str]):
    width = 50
    height = 100
    total_width = width * (max(len(s) for s in text))
    total_height = height * len(text) 

    image = Image.new("RGB", (total_width, total_height))

    for line_no, line in enumerate(text):
        for idx, letter in enumerate(line):
            if letter == " ":
                letter = "SPACE"
            if letter.islower() == True:
                letter = letter + "-Lower"

            img = Image.open(f"bw_images/{letter}.jpeg")

            scaled = img.resize((width, height))

            image.paste(scaled, (width * idx, height * line_no))
    
    image.save("merged_side_by_side.jpg")


if __name__ == "__main__":
   text = getText() 
   print(text)
   createImage(text)
