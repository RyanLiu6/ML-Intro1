import os
import cv2
import utils

import pytesseract as smt


OUT = "Output/"
ABSPATH = os.path.dirname(os.path.realpath(__file__))


def imageToString(imagefile):
    # Given a path to the image, oppen it as a pyImage object
    image = utils.pyImage(imagefile)

    outputStr = smt.image_to_string(image.imageMat, lang="eng")

    with open(os.path.join(ABSPATH, OUT, "test.txt"), "wb") as f:
        f.write(outputStr.encode("utf-8"))
