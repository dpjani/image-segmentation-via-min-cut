# This is a script for image segmentation via min-cut/max-flow algorithm on a sample image named 'bird.jpg'


import networkx as nx
import numpy as np
from skimage import io, color, filters
import matplotlib.pyplot as plt
import time

def image_to_graph(image, foreground_mask, background_mask):
    """Converts an image to a graph for max-flow, min-cut."""
    rows, cols = image.shape[:2]
    graph = nx.DiGraph()

    # Add nodes for pixels
    for i in range(rows):
        for j in range(cols):
            node_id = i * cols + j
            graph.add_node(node_id, pos=(j, -i), label='pixel')

    # Add source and sink nodes
    graph.add_node('source', label='source')
    graph.add_node('sink', label='sink')

    # Connect source to foreground pixels
    for i in range(rows):
        for j in range(cols):
            if foreground_mask[i, j]:
                node_id = i * cols + j
                graph.add_edge('source', node_id, capacity=np.inf)

    # Connect sink to background pixels
    for i in range(rows):
        for j in range(cols):
            if background_mask[i, j]:
                node_id = i * cols + j
                graph.add_edge(node_id, 'sink', capacity=np.inf)

    # Connect neighboring pixels
    for i in range(rows):
        for j in range(cols):
            node_id = i * cols + j
            if j > 0:
                neighbor_id = i * cols + (j - 1)
                weight = np.linalg.norm(image[i, j] - image[i, j - 1])
                graph.add_edge(node_id, neighbor_id, capacity=weight)
            if i > 0:
                neighbor_id = (i - 1) * cols + j
                weight = np.linalg.norm(image[i, j] - image[i - 1, j])
                graph.add_edge(node_id, neighbor_id, capacity=weight)

    return graph

def automatic_foreground_background(image):
    """Automatically select foreground and background using simple thresholding."""
    # Convert image to grayscale
    gray_image = color.rgb2gray(image)
    # Apply Otsu's thresholding
    thresh = filters.threshold_otsu(gray_image)
    # Create masks for foreground and background
    foreground_mask = gray_image > thresh
    background_mask = ~foreground_mask
    return foreground_mask, background_mask

def interactive_segmentation(image_path):
    """Performs interactive image segmentation using max-flow, min-cut."""
    # Read image
    image = io.imread(image_path)
    # Automatically select foreground and background
    foreground_mask, background_mask = automatic_foreground_background(image)
    # Convert image to grayscale
    gray_image = color.rgb2gray(image)
    # Create graph
    graph = image_to_graph(gray_image, foreground_mask, background_mask)
    # Find the minimum cut and measure time
    start_time = time.time()
    cut_value, partition = nx.minimum_cut(graph, 'source', 'sink')
    segmentation_time = time.time() - start_time
    # Retrieve the reachable and non-reachable nodes
    reachable, _ = partition
    # Create segmented image
    rows, cols = gray_image.shape[:2]
    segmented_image = np.zeros_like(gray_image, dtype=np.uint8)
    for node in reachable:
        if node != 'source':
            i, j = divmod(node, cols)
            segmented_image[i, j] = 255
    return gray_image, segmented_image, segmentation_time

# Example usage
image_path = "bird.jpg"
original_image, segmented_image, segmentation_time = interactive_segmentation(image_path)

# Print segmentation time
print("Segmentation Time:", segmentation_time, "seconds")

# Plot original image
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')

# Plot segmented image
plt.subplot(1, 2, 2)
plt.imshow(segmented_image, cmap='gray')
plt.title('Segmented Image')
plt.axis('off')

plt.show()
