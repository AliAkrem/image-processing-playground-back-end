% Read an image
img = imread('pouti.png');

% Apply Prewitt edge detection
edges = prewitt_edge_detection(img);

% Display results
figure;
subplot(1,2,1); imshow(img); title('Original Image');
subplot(1,2,2); imshow(edges); title('Prewitt Edges');
