function [edges] = prewitt_edge_detection(image)
    % Convert image to grayscale if it's RGB
    if size(image, 3) == 3
        image = rgb2gray(image);
    end

    % Convert to double for calculations
    image = double(image);

    % Get image dimensions
    [rows, cols] = size(image);

    % Initialize output edge image
    edges = zeros(rows, cols);

    % Prewitt operators
    Gx = [-1 0 1;
          -1 0 1;
          -1 0 1];

    Gy = [-1 -1 -1;
           0  0  0;
           1  1  1];
           
    padded_image = zeros(rows + 2, cols + 2);
    padded_image(2:rows+1, 2:cols+1) = image;

    % Apply Prewitt operator using loops
    for i = 2:rows+1
        for j = 2:cols+1
            % Get 3x3 neighborhood
            neighborhood = padded_image(i-1:i+1, j-1:j+1);

            % Calculate gradients
            gradient_x = sum(sum(neighborhood .* Gx));
            gradient_y = sum(sum(neighborhood .* Gy));

            % Calculate magnitude of gradient
            edges(i-1, j-1) = sqrt(gradient_x^2 + gradient_y^2);
        end
    end

    % Normalize edges to range [0, 255]
    edges = edges * 255 / max(edges(:));
end
