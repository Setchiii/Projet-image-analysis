import unittest
from PIL import Image
from toolbox import threshold


class TestToolboxMethods(unittest.TestCase):

    def test_threshold(self):
        # Create a test image
        test_image = Image.new('RGB', (1, 1), color=(73, 109, 137))

        # Apply the threshold function
        result_image = threshold(test_image, 100)

        # Check the result
        self.assertEqual(result_image.getpixel((0, 0)), (255, 255, 255))


if __name__ == '__main__':
    unittest.main()
