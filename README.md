# Toyota-Innovation-Challenge
Code that our team used to complete and win the Toyota Innovation Challenge - 2023. 

There are 4 different files in this repository. I directly contributed to two of them (perspec.py and distinguishing.py) and helped to debug/plan the other two files as part of a 4-member group. 

The task was to create a system using Python that could receive a video feed from one or more cameras and identify "stickers" and "holes" in a rectangular object placed at various orientations. 

Perspec.py handles dealing with different feeds from multiple cameras, resolving lengths and depths of the rectangular block. Camcode.py handles drawing identifying circles onto the video feed to point out stickers and holes. Distinguishing.py handles distinguishing between holes and stickers based on marginal differences in size. circleDetection.py uses Hough transforms to identify circles within the rectangular block. 

Overall, I learnt a lot from this Hackathon and it was my first time dealing with image processing technology in Python. I had to do quite a bit of reading about how these libraries worked, but it was an interesting challenge and is a starting point for my ongoing (slow but undying, like a slug) journey in learning about pattern recognition.
