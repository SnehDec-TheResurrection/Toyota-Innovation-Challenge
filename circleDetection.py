import numpy as np
import matplotlib.pyplot as plt
import cv2


def edgeDetector(img, region):
    img = cv2.medianBlur(img,3)
    if region == 0: #Top Down View
        img_edge = cv2.Canny(img,100,200)
    else: #Angled Views
        img_edge = cv2.Canny(img,40,80)    
    return img_edge

def inspect(circles):
    num = circles.shape[1]
    circle_overlap = []
    sum = 0
    for x in range(num):
        sum += circles[0, x, 2]
        circle_overlap.append(0)
    for i in range(num):
        for j in range(i+1,num):
            c1 = np.array([circles[0, i, 0], circles[0, i, 1]])
            c2 = np.array([circles[0, j, 0], circles[0, j, 1]])
            dist = np.linalg.norm(c1 - c2)
            if (dist < circles[0, i, 2] + circles[0, j, 2]):
                circle_overlap[i] = 1
                circle_overlap[j] = 1
    return circle_overlap



def houghCircleDetector(img, img_edge, region, h):
    # 20      25      40
    # 0.052   0.065   0.103
    if region == 0:
        circles = cv2.HoughCircles(img_edge,cv2.HOUGH_GRADIENT,1,minDist=100,param1=60,param2=20, minRadius =65, maxRadius = 100) #min radius = 17
    elif region == 1:
        circles = cv2.HoughCircles(img_edge,cv2.HOUGH_GRADIENT,1,minDist=100,param1=60,param2=20, minRadius =70, maxRadius = 125) #min radius = 17
    elif region == 2:
        circles = cv2.HoughCircles(img_edge,cv2.HOUGH_GRADIENT,1,minDist=100,param1=60,param2=20, minRadius =70, maxRadius = 125) #min radius = 17
    return circles

path_to_img = 'indian_coins.jpg'

#houghLineDetector(path_to_img)
# houghCircleDetector(path_to_img)

def loseReflection(orig):
    # orig = cv2.cvtColor(orig, c/v2.COLOR_RGBA2BGR)
    ret,img_bin = cv2.threshold(orig,225,255,cv2.THRESH_BINARY)
    # bgr_image = cv2.cvtColor(img_bin, cv2.COLOR_GRAY2BGR)
    no_refl = cv2.subtract(orig, img_bin)
    return no_refl

def drawActualCircles(img, circles, overlaps, big):
    print(len(big))
    print(circles.shape[1])
    circles = np.uint16(np.around(circles))
    count = 0
    for val in circles[0,:]:
        if overlaps[count] == 1:
            color = (0,0,255)
        elif not big[count]:
            color = (255,0,0)
        else:
            color = (0,255,0)
        cv2.circle(img,(val[0],val[1]),val[2],color,2)
        count += 1
    return img

def drawCircles(orig, edge, circle):
    # plt.figure(figsize=(20,10))
    plt.subplot(221),plt.imshow(cv2.cvtColor(orig,cv2.COLOR_BGR2RGB)),plt.title('Original',color='c')
    plt.subplot(222),plt.imshow(cv2.cvtColor(edge,cv2.COLOR_BGR2RGB)),plt.title('Edges',color='c')
    plt.subplot(223),plt.imshow(cv2.cvtColor(circle,cv2.COLOR_BGR2RGB)),plt.title('Circles',color='c')
    
    plt.show()

def detectHoles(img, region):
    h = img.shape[0]
    edge = edgeDetector(img, region)
    circles = houghCircleDetector(img, edge, region, h)
    overlaps = inspect(circles)
    return circles, overlaps

if __name__ == "__main__":
    orig = cv2.imread("test.jpg",cv2.IMREAD_UNCHANGED)
    detectHoles(orig, 0)
    orig2 = cv2.imread("test.jpg",cv2.IMREAD_UNCHANGED)
    detectHoles(orig2, 1)
    orig3 = cv2.imread("test.jpg",cv2.IMREAD_UNCHANGED)
    detectHoles(orig3, 2)
