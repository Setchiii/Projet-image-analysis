from PIL import Image
import toolbox

men1_img = Image.open("Samples_carrier.jpg")
men1_img_threshold = toolbox.threshold_remove_clear_bg(men1_img, 150)
men1_img_threshold.save("Samples_carrier_threshold150.jpg", "JPEG")
