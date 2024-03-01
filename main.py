from PIL import Image
import toolbox

# image_path = "Samples_carrier.jpg"
# image_object = Image.open(image_path)
# new_image_object = toolbox.threshold_remove_clear_bg(image_object, 150)
# new_image_object.save(image_path.replace(".jpg", "_threshold.jpg"), "JPEG")

image_path = "final_carrier.jpg"
image_object = Image.open(image_path)
new_image_object = toolbox.threshold_gray_remover(image_object, 25, 255, 0.27)
new_image_object.save(image_path.replace(".jpg", "_threshold.jpg"), "JPEG")
