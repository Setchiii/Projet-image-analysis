from PIL import Image


def threshold(image: Image.Image, threshold_value: int):
    update_image = image.copy()
    counter = 0
    pixels_in_line = image.size[0]

    for pixel in update_image.getdata():
        if sum(pixel) / 3 > threshold_value:
            update_image.putpixel(
                (counter % pixels_in_line, int(
                    counter / pixels_in_line)), (255, 255, 255)
            )
        else:
            update_image.putpixel(
                (counter % pixels_in_line, int(counter / pixels_in_line)), (0, 0, 0)
            )
        counter += 1

    return update_image


def threshold_remove_clear_bg(image: Image.Image, threshold_value: int):
    update_image = image.copy()
    counter = 0
    pixels_in_line = image.size[0]

    for pixel in update_image.getdata():
        if sum(pixel) / 3 > threshold_value:
            update_image.putpixel(
                (counter % pixels_in_line, int(
                    counter / pixels_in_line)), (255, 255, 255)
            )
        counter += 1

    return update_image
