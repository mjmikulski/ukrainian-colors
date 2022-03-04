import cv2
import numpy as np

# colors from here: https://en.wikipedia.org/wiki/Flag_of_Ukraine
STRONG_AZURE_COLOR = np.array([183, 87, 0], dtype='uint8')
UKRAINE_YELLOW_COLOR = np.array([0, 215, 255], dtype='uint8')

STRONG_AZURE_HUE = cv2.cvtColor(STRONG_AZURE_COLOR.reshape((1, 1, 3)), cv2.COLOR_BGR2HSV)[0, 0, 0]
UKRAINE_YELLOW_HUE = cv2.cvtColor(UKRAINE_YELLOW_COLOR.reshape((1, 1, 3)), cv2.COLOR_BGR2HSV)[0, 0, 0]


def make_ukrainian_colors(img: np.ndarray, saturate: bool = True) -> np.ndarray:
    """ Change colors in a picture so it looks like flag of Ukraine

    Parameters
    ----------
    img : np.ndarray
        Image to be Ukrainian-colored, in BGR format.
    saturate : bool, optional
        If True (default) image will be fully saturated. For more gentle
         effects use False.

    Returns
    -------
    np.ndarray
        Colored image, in BGR format.
    """
    assert img.dtype == np.uint8, \
        f'Only uint8 pictures allowed, received {img.dtype} instead.'

    split_line = img.shape[0] // 2
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img_hsv[:split_line, :, 0] = STRONG_AZURE_HUE
    img_hsv[split_line:, :, 0] = UKRAINE_YELLOW_HUE

    if saturate:
        img_hsv[..., 1] = 255

    output_img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    output_img[-1, -2, :] = (70, 67, 75)
    output_img[-1, -1, :] = (80, 84, 78)

    return output_img
