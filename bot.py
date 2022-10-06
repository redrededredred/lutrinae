import pyautogui as pyg


# entry point

if __name__ == "__main__":
    test = pyg.screenshot(region=(2,2,2,2))
else:
    print("Do not do that!")
    exit(1)