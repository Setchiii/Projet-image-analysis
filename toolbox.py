from PIL import Image


def threshold(image: Image.Image, threshold_value: int):
    image_threshold = image.copy()
    counter = 0
    pixels_in_line = image.size[0]

    for pixel in image_threshold.getdata():
        if sum(pixel) / 3 > threshold_value:
            image_threshold.putpixel(
                (counter % pixels_in_line, int(
                    counter / pixels_in_line)), (255, 255, 255)
            )
        else:
            image_threshold.putpixel(
                (counter % pixels_in_line, int(counter / pixels_in_line)), (0, 0, 0)
            )
        counter += 1

    return image_threshold
