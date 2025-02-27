import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys

class ImageProcessor:
    def load(self, path):
        try:
            img = mpimg.imread(path)
            array = np.array(img)
            print(f"Loading image of dimensions {array.shape[0]} x {array.shape[1]}")
            #array[:,:,0:3] to extract only RGB
            return array[:,:,0:3]
        except Exception as e:
            print(f"Exception : {e.__class__.__name__} -- strerror: {e}")
        return None
    
    def display(self, array):
        array = np.multiply(array, 255)
        array = array.astype(np.uint8)
        plt.imshow(array)
        plt.show()


if __name__ == "__main__":
    imp = ImageProcessor()
    array = imp.load(sys.argv[1])
    print(array)
    print()
    imp.display(array)