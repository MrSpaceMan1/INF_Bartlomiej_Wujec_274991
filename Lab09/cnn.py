import numpy as np
from matplotlib import pyplot as plt

# tworzymy tablice o wymiarach 128x128x3 (3 kanaly to RGB)
# uzupelnioną zerami = kolor czarny
data = np.zeros((128, 128, 3), dtype=np.uint8)


# chcemy zeby obrazek byl czarnobialy,
# wiec wszystkie trzy kanaly rgb uzupelniamy tymi samymi liczbami
# napiszmy do tego funkcje
def draw(img, x, y, color):
    img[x, y] = [color, color, color]


# zamalowanie 4 pikseli w lewym górnym rogu
draw(data, 5, 5, 100)
draw(data, 6, 6, 100)
draw(data, 5, 6, 255)
draw(data, 6, 5, 255)

# rysowanie kilku figur na obrazku
for i in range(128):
    for j in range(128):
        if (i - 64) ** 2 + (j - 64) ** 2 < 900:
            draw(data, i, j, 200)
        elif i > 100 and j > 100:
            draw(data, i, j, 255)
        elif (i - 15) ** 2 + (j - 110) ** 2 < 25:
            draw(data, i, j, 150)
        elif (i - 15) ** 2 + (j - 110) ** 2 == 25 or (i - 15) ** 2 + (j - 110) ** 2 == 26:
            draw(data, i, j, 255)


def kernel_fits(image, kernel, stride):
    output_x = (image.shape[0] - kernel.shape[0]) / stride + 1
    output_y = (image.shape[1] - kernel.shape[1]) / stride + 1
    return output_x, output_y, (output_x.is_integer() and output_y.is_integer())


def conv(image: np.array, kernel: np.array, stride: int, activation_func=None) -> np.array:
    fit = kernel_fits(image, kernel, stride)
    if fit[2]:
        output = np.zeros((int(fit[0]), int(fit[1]), image.shape[2]))

        output_x, output_y = 0, 0
        start_x, start_y = 0, 0
        end_x, end_y = kernel.shape

        # output[output_x, output_y, 0] = np.sum(image[start_x:end_x, start_y:end_y, 0] * kernel)

        while end_x <= image.shape[0]:
            output_y = 0
            start_y = 0
            end_y = kernel.shape[1]

            while end_y <= image.shape[1]:
                for channel in [0, 1, 2]:
                    if activation_func is None:
                        output[output_x, output_y, channel] = np.sum(
                            image[start_x:end_x, start_y:end_y, channel] * kernel)
                    else:
                        output[output_x, output_y, channel] = activation_func(np.sum(
                            image[start_x:end_x, start_y:end_y, channel] * kernel))

                output_y += 1
                start_y += stride
                end_y += stride

            output_x += 1
            start_x += stride
            end_x += stride

    return output


def reLU(x):
    return x * (x > 0)


def linear(x):
    return 255 * (x > 255) + x * (0 <= x <= 255)


vertical_edges = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

horizontal_edges = np.array([
    [ 1,  1,  1],
    [ 0,  0,  0],
    [-1, -1, -1]
])

sobel = np.array([
    [0, 1, 2],
    [-1, 0, 1],
    [-2, -1, 0]
])

layer1 = conv(data, vertical_edges, 1, linear)
layer2 = conv(layer1, horizontal_edges, 1, linear)
layer3 = conv(layer2, sobel, 1, linear)

# konwersja macierzy na obrazek i wyświetlenie
plt.imshow(layer3, interpolation='nearest')
plt.show()
