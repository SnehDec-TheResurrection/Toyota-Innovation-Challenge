import cv2
import numpy as np


def coveredOrNot(img, circles, overlaps, ):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert the (x, y) coordinates and radius of the circles to integers
    if (circles is None):
        print("No circles found")
        raise TypeError
    else:
        circles = np.round(circles[0, :]).astype("int")
        for circle in circles:
            cv2.circle(gray, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)

        # Initialize counters for small and large circles
        small_circles = 0
        large_circles = 0

        circleSize = []
        # Loop over detected circles
        count = 0
        for (x, y, r) in circles:
            if overlaps[count] == 1:
                circleSize.append(True)
                count += 1 
                continue
            # Initialize a flag for the current circle
            is_large = False
            # Loop over remaining circles to compare sizes
            count2 = 0
            for (x2, y2, r2) in circles:
                if overlaps[count2] == 1:
                    count2 += 1 
                    continue
                # Check if the other circle is not the same circle and has a smaller radius
                if (x, y, r) != (x2, y2, r2) and r > r2:
                    # Check if the current circle is about 1.2 times larger than the other circle
                    if r/r2 > 1.1 and r/r2 < 1.3:
                        is_large = True
                        break
                count2 += 1 
            # Increment the appropriate counter
            if is_large:
                circleSize.append(True)
                large_circles += 1
            else:
                circleSize.append(False)
                small_circles += 1
            count += 1
        if large_circles == 0 and r > 50:
            large_circles = small_circles
            small_circles = 0
            for item in circleSize:
                item = True
        # Print the results
        return circleSize