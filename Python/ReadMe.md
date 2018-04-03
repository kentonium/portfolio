## Tracking Example

This is a relatively simple example to showcase use of some general OpenCV tools and demonstrate knowledge of how Python works. The code looks for full frontal faces using Histogram of Orients and Haar Cascades. When it finds a face, it draws a rectangle around it. 

## Full Body Detection

This is the base code I used for further work on the job at EhEye Inc. to test out some methods and functions before swapping to using Darknet and now Detectron for our detection. The code here uses Histogram of Oriented Gradients to find a person using pre-trained full body Haar Cascade. Once it finds a person it draws a box around them. I used this to find how far someone is from the camera, make motion detectors, create a license plate scraper and other use cases.

## Video Example

This is something from my learnings where I selected a point on the camera and told the program to only look within the bounds for features, and draw a dot wherever it found one.

https://www.youtube.com/watch?v=UoDe8an8q1Q
