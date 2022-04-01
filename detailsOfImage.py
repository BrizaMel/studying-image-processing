import cv2

# assume width = height
def rotateImage(img):
    left, right = 0, img.shape[0]-1

    while (left < right):
        top, bottom = left, right

        for i in range(0, right-left):
            topLeft = img[top][left + i]

            img[top][left + i] = img[bottom - i][left]
            img[bottom - i][left] = img[bottom][right - i]
            img[bottom][right - i] = img[top + i][right]
            img[top + i][right] = topLeft
        
        left += 1
        right -= 1
    
    return img

def negativeImage(img):

    img = 255 - img

    return img

def grayScale(img):
    h, w = img.shape[0], img.shape[1]

    """
    weights: 
        red: 0.2989
        green: 0.5870
        blue: 0.1140
    """

    for i in range(h):
        for j in range(w):
            pixel = img[i][j]
            lum = int(0.1140*pixel[0] + 0.5870*pixel[1] + 0.2989*pixel[2])
            img[i][j] = (lum, lum, lum)
    
    return img



img = cv2.imread('data/square.jpg')

print("height, width and channels: ", img.shape)

print("Dimension of the imagem: ", img.ndim)

print("Min value pixel at channel B: ", img[:, :, 0].min())

img2 = rotateImage(img)

cv2.imshow('Rotated Image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = cv2.imread('data/woman.jpg')
img3 = cv2.resize(img3, (0,0), fx=0.5, fy=0.5)
img3 = negativeImage(img3)

grayScale(img3)

cv2.imshow('Negative Image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()