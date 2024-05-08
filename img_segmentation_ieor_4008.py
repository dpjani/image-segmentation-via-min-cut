# -*- coding: utf-8 -*-
"""img_segmentation_ieor_4008

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Eb3XBFE80c8GNR6uU85AOqxxCcTj1DW0

# Image Segmentation via Min-Cut

We use 3 algorithms for image segmentation:

* GrabCut
* Felzenszwalb Algorithm
* Boykov Kolmogorv Algorithm

## Example 1
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

# Function to perform GrabCut segmentation
def perform_grabcut(image):
    start_time = time.time()  # Start time

    rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)  # Example rectangle

    mask = np.zeros(image.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    segmented = image * mask2[:, :, np.newaxis]

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Felzenszwalb's segmentation
def perform_felzenszwalb(image):
    start_time = time.time()  # Start time

    segments = cv2.ximgproc.segmentation.createGraphSegmentation()
    segments.setSigma(0.5)
    segments.setK(100)
    segments.setMinSize(50)

    segmented = segments.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Boykov-Kolmogorov segmentation
def perform_boykov_kolmogorov(image):
    start_time = time.time()  # Start time

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    graph = cv2.ximgproc.segmentation.createGraphSegmentation()
    graph.setSigma(0.5)
    graph.setK(500)
    graph.setMinSize(50)

    segmented = graph.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to handle image path and processing
def handle_image_path(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get dimensions of the original image
    height, width, channels = img.shape

    # Perform segmentation using all three algorithms
    segmented_grabcut, time_grabcut = perform_grabcut(img)
    segmented_felzenszwalb, time_felzenszwalb = perform_felzenszwalb(img)
    segmented_boykov_kolmogorov, time_boykov_kolmogorov = perform_boykov_kolmogorov(img)

    # Display the segmented images
    plt.figure(figsize=(100, 50))

    plt.subplot(1, 4, 1)
    plt.imshow(img)
    plt.title('Original Image\nDimensions: {} x {}'.format(width, height), fontsize=55)

    plt.subplot(1, 4, 2)
    plt.imshow(segmented_grabcut)
    plt.title('GrabCut\nTime: {:.4f} sec'.format(time_grabcut), fontsize=55)

    plt.subplot(1, 4, 3)
    plt.imshow(segmented_felzenszwalb)
    plt.title('Felzenszwalb\nTime: {:.4f} sec'.format(time_felzenszwalb), fontsize=55)

    plt.subplot(1, 4, 4)
    plt.imshow(segmented_boykov_kolmogorov)
    plt.title('Boykov-Kolmogorov\nTime: {:.4f} sec'.format(time_boykov_kolmogorov), fontsize=55)

    plt.show()

# Specify the path to your image
image_path = 'tesla.jpg'

# Handle the image path
handle_image_path(image_path)

"""## Example 2"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

# Function to perform GrabCut segmentation
def perform_grabcut(image):
    start_time = time.time()  # Start time

    rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)  # Example rectangle

    mask = np.zeros(image.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    segmented = image * mask2[:, :, np.newaxis]

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Felzenszwalb's segmentation
def perform_felzenszwalb(image):
    start_time = time.time()  # Start time

    segments = cv2.ximgproc.segmentation.createGraphSegmentation()
    segments.setSigma(0.5)
    segments.setK(100)
    segments.setMinSize(50)

    segmented = segments.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Boykov-Kolmogorov segmentation
def perform_boykov_kolmogorov(image):
    start_time = time.time()  # Start time

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    graph = cv2.ximgproc.segmentation.createGraphSegmentation()
    graph.setSigma(0.5)
    graph.setK(500)
    graph.setMinSize(50)

    segmented = graph.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to handle image path and processing
def handle_image_path(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get dimensions of the original image
    height, width, channels = img.shape

    # Perform segmentation using all three algorithms
    segmented_grabcut, time_grabcut = perform_grabcut(img)
    segmented_felzenszwalb, time_felzenszwalb = perform_felzenszwalb(img)
    segmented_boykov_kolmogorov, time_boykov_kolmogorov = perform_boykov_kolmogorov(img)

    # Display the segmented images
    plt.figure(figsize=(100, 50))

    plt.subplot(1, 4, 1)
    plt.imshow(img)
    plt.title('Original Image\nDimensions: {} x {}'.format(width, height), fontsize=55)

    plt.subplot(1, 4, 2)
    plt.imshow(segmented_grabcut)
    plt.title('GrabCut\nTime: {:.4f} sec'.format(time_grabcut), fontsize=55)

    plt.subplot(1, 4, 3)
    plt.imshow(segmented_felzenszwalb)
    plt.title('Felzenszwalb\nTime: {:.4f} sec'.format(time_felzenszwalb), fontsize=55)

    plt.subplot(1, 4, 4)
    plt.imshow(segmented_boykov_kolmogorov)
    plt.title('Boykov-Kolmogorov\nTime: {:.4f} sec'.format(time_boykov_kolmogorov), fontsize=55)

    plt.show()

# Specify the path to your image
image_path = 'bird.jpg'

# Handle the image path
handle_image_path(image_path)

"""## Example 4"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

# Function to perform GrabCut segmentation
def perform_grabcut(image):
    start_time = time.time()  # Start time

    rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)  # Example rectangle

    mask = np.zeros(image.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    segmented = image * mask2[:, :, np.newaxis]

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Felzenszwalb's segmentation
def perform_felzenszwalb(image):
    start_time = time.time()  # Start time

    segments = cv2.ximgproc.segmentation.createGraphSegmentation()
    segments.setSigma(0.5)
    segments.setK(100)
    segments.setMinSize(50)

    segmented = segments.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Boykov-Kolmogorov segmentation
def perform_boykov_kolmogorov(image):
    start_time = time.time()  # Start time

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    graph = cv2.ximgproc.segmentation.createGraphSegmentation()
    graph.setSigma(0.5)
    graph.setK(500)
    graph.setMinSize(50)

    segmented = graph.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to handle image path and processing
def handle_image_path(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get dimensions of the original image
    height, width, channels = img.shape

    # Perform segmentation using all three algorithms
    segmented_grabcut, time_grabcut = perform_grabcut(img)
    segmented_felzenszwalb, time_felzenszwalb = perform_felzenszwalb(img)
    segmented_boykov_kolmogorov, time_boykov_kolmogorov = perform_boykov_kolmogorov(img)

    # Display the segmented images
    plt.figure(figsize=(100, 50))

    plt.subplot(1, 4, 1)
    plt.imshow(img)
    plt.title('Original Image\nDimensions: {} x {}'.format(width, height), fontsize=55)

    plt.subplot(1, 4, 2)
    plt.imshow(segmented_grabcut)
    plt.title('GrabCut\nTime: {:.4f} sec'.format(time_grabcut), fontsize=55)

    plt.subplot(1, 4, 3)
    plt.imshow(segmented_felzenszwalb)
    plt.title('Felzenszwalb\nTime: {:.4f} sec'.format(time_felzenszwalb), fontsize=55)

    plt.subplot(1, 4, 4)
    plt.imshow(segmented_boykov_kolmogorov)
    plt.title('Boykov-Kolmogorov\nTime: {:.4f} sec'.format(time_boykov_kolmogorov), fontsize=55)

    plt.show()

# Specify the path to your image
image_path = 'giraffe.jpg'

# Handle the image path
handle_image_path(image_path)

"""## Example 3"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

# Function to perform GrabCut segmentation
def perform_grabcut(image):
    start_time = time.time()  # Start time

    rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)  # Example rectangle

    mask = np.zeros(image.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    segmented = image * mask2[:, :, np.newaxis]

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Felzenszwalb's segmentation
def perform_felzenszwalb(image):
    start_time = time.time()  # Start time

    segments = cv2.ximgproc.segmentation.createGraphSegmentation()
    segments.setSigma(0.5)
    segments.setK(100)
    segments.setMinSize(50)

    segmented = segments.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Boykov-Kolmogorov segmentation
def perform_boykov_kolmogorov(image):
    start_time = time.time()  # Start time

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    graph = cv2.ximgproc.segmentation.createGraphSegmentation()
    graph.setSigma(0.5)
    graph.setK(500)
    graph.setMinSize(50)

    segmented = graph.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to handle image path and processing
def handle_image_path(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get dimensions of the original image
    height, width, channels = img.shape

    # Perform segmentation using all three algorithms
    segmented_grabcut, time_grabcut = perform_grabcut(img)
    segmented_felzenszwalb, time_felzenszwalb = perform_felzenszwalb(img)
    segmented_boykov_kolmogorov, time_boykov_kolmogorov = perform_boykov_kolmogorov(img)

    # Display the segmented images
    plt.figure(figsize=(100, 50))

    plt.subplot(1, 4, 1)
    plt.imshow(img)
    plt.title('Original Image\nDimensions: {} x {}'.format(width, height), fontsize=55)

    plt.subplot(1, 4, 2)
    plt.imshow(segmented_grabcut)
    plt.title('GrabCut\nTime: {:.4f} sec'.format(time_grabcut), fontsize=55)

    plt.subplot(1, 4, 3)
    plt.imshow(segmented_felzenszwalb)
    plt.title('Felzenszwalb\nTime: {:.4f} sec'.format(time_felzenszwalb), fontsize=55)

    plt.subplot(1, 4, 4)
    plt.imshow(segmented_boykov_kolmogorov)
    plt.title('Boykov-Kolmogorov\nTime: {:.4f} sec'.format(time_boykov_kolmogorov), fontsize=55)

    plt.show()

# Specify the path to your image
image_path = 'selfie1.jpg'

# Handle the image path
handle_image_path(image_path)

"""## Example 5"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

# Function to perform GrabCut segmentation
def perform_grabcut(image):
    start_time = time.time()  # Start time

    rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)  # Example rectangle

    mask = np.zeros(image.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    segmented = image * mask2[:, :, np.newaxis]

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Felzenszwalb's segmentation
def perform_felzenszwalb(image):
    start_time = time.time()  # Start time

    segments = cv2.ximgproc.segmentation.createGraphSegmentation()
    segments.setSigma(0.5)
    segments.setK(100)
    segments.setMinSize(50)

    segmented = segments.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Boykov-Kolmogorov segmentation
def perform_boykov_kolmogorov(image):
    start_time = time.time()  # Start time

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    graph = cv2.ximgproc.segmentation.createGraphSegmentation()
    graph.setSigma(0.5)
    graph.setK(500)
    graph.setMinSize(50)

    segmented = graph.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to handle image path and processing
def handle_image_path(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get dimensions of the original image
    height, width, channels = img.shape

    # Perform segmentation using all three algorithms
    segmented_grabcut, time_grabcut = perform_grabcut(img)
    segmented_felzenszwalb, time_felzenszwalb = perform_felzenszwalb(img)
    segmented_boykov_kolmogorov, time_boykov_kolmogorov = perform_boykov_kolmogorov(img)

    # Display the segmented images
    plt.figure(figsize=(100, 50))

    plt.subplot(1, 4, 1)
    plt.imshow(img)
    plt.title('Original Image\nDimensions: {} x {}'.format(width, height), fontsize=55)

    plt.subplot(1, 4, 2)
    plt.imshow(segmented_grabcut)
    plt.title('GrabCut\nTime: {:.4f} sec'.format(time_grabcut), fontsize=55)

    plt.subplot(1, 4, 3)
    plt.imshow(segmented_felzenszwalb)
    plt.title('Felzenszwalb\nTime: {:.4f} sec'.format(time_felzenszwalb), fontsize=55)

    plt.subplot(1, 4, 4)
    plt.imshow(segmented_boykov_kolmogorov)
    plt.title('Boykov-Kolmogorov\nTime: {:.4f} sec'.format(time_boykov_kolmogorov), fontsize=55)

    plt.show()

# Specify the path to your image
image_path = 'selfie3.jpg'

# Handle the image path
handle_image_path(image_path)

"""## Example 6"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

# Function to perform GrabCut segmentation
def perform_grabcut(image):
    start_time = time.time()  # Start time

    rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)  # Example rectangle

    mask = np.zeros(image.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    segmented = image * mask2[:, :, np.newaxis]

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Felzenszwalb's segmentation
def perform_felzenszwalb(image):
    start_time = time.time()  # Start time

    segments = cv2.ximgproc.segmentation.createGraphSegmentation()
    segments.setSigma(0.5)
    segments.setK(100)
    segments.setMinSize(50)

    segmented = segments.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to perform Boykov-Kolmogorov segmentation
def perform_boykov_kolmogorov(image):
    start_time = time.time()  # Start time

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    graph = cv2.ximgproc.segmentation.createGraphSegmentation()
    graph.setSigma(0.5)
    graph.setK(500)
    graph.setMinSize(50)

    segmented = graph.processImage(image)

    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Elapsed time

    return segmented, execution_time

# Function to handle image path and processing
def handle_image_path(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get dimensions of the original image
    height, width, channels = img.shape

    # Perform segmentation using all three algorithms
    segmented_grabcut, time_grabcut = perform_grabcut(img)
    segmented_felzenszwalb, time_felzenszwalb = perform_felzenszwalb(img)
    segmented_boykov_kolmogorov, time_boykov_kolmogorov = perform_boykov_kolmogorov(img)

    # Display the segmented images
    plt.figure(figsize=(100, 50))

    plt.subplot(1, 4, 1)
    plt.imshow(img)
    plt.title('Original Image\nDimensions: {} x {}'.format(width, height), fontsize=55)

    plt.subplot(1, 4, 2)
    plt.imshow(segmented_grabcut)
    plt.title('GrabCut\nTime: {:.4f} sec'.format(time_grabcut), fontsize=55)

    plt.subplot(1, 4, 3)
    plt.imshow(segmented_felzenszwalb)
    plt.title('Felzenszwalb\nTime: {:.4f} sec'.format(time_felzenszwalb), fontsize=55)

    plt.subplot(1, 4, 4)
    plt.imshow(segmented_boykov_kolmogorov)
    plt.title('Boykov-Kolmogorov\nTime: {:.4f} sec'.format(time_boykov_kolmogorov), fontsize=55)

    plt.show()

# Specify the path to your image
image_path = 'xray.jpg'

# Handle the image path
handle_image_path(image_path)
