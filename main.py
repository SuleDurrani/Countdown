from CountdownLetters import lettersRound, generateLetters
import pytesseract
import cv2


def main():
    val = input("Enter address of file: ")
    temp = "n"
    if val != "":
        image = cv2.imread(val)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
        cv2.imshow('Binary Threshold', thresh1)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        text = pytesseract.image_to_string(thresh1)
        escapes = ''.join([chr(char) for char in range(1, 32)])
        translator = str.maketrans('', '', escapes)
        text = text.translate(translator)
        text = text.lower()
        print(text)
        temp = input("Are these the correct letters? y/n")

    if temp == "n":
        text = generateLetters()

    lettersRound(text)


if __name__ == '__main__':
    main()
