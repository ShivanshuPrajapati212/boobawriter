from PIL import Image

def getText():
    text = input("Enter the text: ")
    return text.lower()


def createImage(text):
    width = 50
    height = 100
    total_width = width * len(text)

    image = Image.new("RGB", (total_width, height))

    for idx, letter in enumerate(text):
        img = Image.open(f"letters/{letter}.jpg")

        scaled = img.resize((width, height))

        image.paste(scaled, (width * idx, 0))
    
    image.save("merged_side_by_side.jpg")


if __name__ == "__main__":
   text = getText() 
   createImage(text)
