import pyautogui

location = 'D:/bloom/'

def clik(l):
    while True:
        try:

            region = (746, 500, 1172, 100)  # Search along a horizontal line at y=708
            l = pyautogui.locateOnScreen(location + str(l) + ".png", confidence=0.8, region=region)
            if l is not None:
                print("Found:", l)
                x, y = pyautogui.center(l)
                y = y-50
                pyautogui.click(x, y)

                break
            else:
                print("Searching for", l, "button")
        except pyautogui.ImageNotFoundException:
            print("Image not found. Retrying...")



while True:
    clik("b")