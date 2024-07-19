# import the necessary packages
import numpy as np
import cv2



def splitInHalf(srcImg):
    h, w = srcImg.shape[:2]
    width_cutoff = w // 2
    s1 = srcImg[:, :width_cutoff]
    s2 = srcImg[:, width_cutoff:]
    return s1, s2

def createPerspectiveImages(image):
    img1, img2 = splitInHalf(image)
    # run for top image
    pts1 = np.array([[298, 346], [1696, 298], [240, 480], [1747, 442]], dtype=np.float32)
    height, width = img2.shape[:2]
    pts2 = np.float32([[0,height*0.35], [width,height*0.35], [0, height*0.60], [width, height*0.60]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    TopOfPipe = cv2.warpPerspective(img2, M, (width, height))

    # run for side view
    pts1 = np.array([[240, 480], [1747, 442], [365, 728], [1624, 706]], dtype=np.float32)
    height, width = img2.shape[:2]
    pts2 = np.float32([[0,height*0.25], [width,height*0.25], [0, height*0.75], [width, height*0.75]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    SideOfPipe = cv2.warpPerspective(img2, M, (width, height))
    TopCROP = TopOfPipe[360:720]
    SideCROP = SideOfPipe[270:810]
    cv2.waitKey()
    return TopCROP, SideCROP, img1

if __name__ == "__main__":
    img1, img2, img3 = createPerspectiveImages(cv2.imread('img.jpg'))
    cv2.imshow("1", img1)
    cv2.imshow("2", img2)
    cv2.imshow("3", img3)
    cv2.imwrite("1.jpg", img1)
    cv2.imwrite("2.jpg", img2)
    cv2.imwrite("3.jpg", img3)