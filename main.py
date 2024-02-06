from PIL import Image
import toolbox

men1_img = Image.open(".\\images\\men1.jpg")
men1_img_threshold = toolbox.threshold(men1_img, 150)
men1_img_threshold.save("men1_img_threshold.jpg", "JPEG")
