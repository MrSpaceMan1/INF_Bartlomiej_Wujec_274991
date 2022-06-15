import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

LOGGING = True


def preprocess(file_path, upper, lower) -> np.array:
    img = cv.imread(file_path, flags=cv.IMREAD_GRAYSCALE)

    img_avg = np.average(img)
    img = img[upper:lower, :]

    for i in range(0):
        img = cv.threshold(img, int(img_avg*0.9), 255, cv.THRESH_BINARY)[1]
        img = cv.blur(img, (5, 1))
        img = cv.blur(img, (1, 5))

    # plt.imshow(img, cmap="gray")

    top = img.shape[1]
    bottom = 0
    for row in range(img.shape[0]):
        row_avg = np.average(img[row, :])
        if img_avg-row_avg > 0:
            if row < top:
                top = row
            if row > bottom:
                bottom = row
    img = img[max(0, top-10):min(bottom+10, img.shape[0]), :]

    left = img.shape[1]
    right = 0
    for col in range(img.shape[1]):
        col_avg = np.average(img[:, col])
        if img_avg - col_avg > 0:
            if col < left:
                left = col
            if col > right:
                right = col
    img = img[:, max(0, left-10):min(right+10, img.shape[1])]

    letters = []
    space = False
    left = 0
    right = None
    for col in range(img.shape[1]):
        col_avg = np.average(img[:, col])
        if img_avg-col_avg < 0 and not space:
            right = col
            letters.append(img[:, left:right])
            space = True

        if img_avg-col_avg > 0 and space:
            left = col
            space = False

    resized_list = []
    for letter in letters:
        try:
            resized = cv.resize(letter, (28, 28))
            resized = np.invert(resized) / 255
            resized_list.append(resized)
        except cv.error:
            print("Something something")

    if LOGGING:
        if len(resized_list) > 0:
            fig, ax = plt.subplots(1, len(resized_list))
            i = 0
            for l in resized_list:
                ax[i].imshow(l, cmap="gray")
                i += 1
        plt.show()

    return np.array(resized_list)

preprocess("test.png", 0, 63)