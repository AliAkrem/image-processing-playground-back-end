function output = midian_filter(img)
    % Ensure the kernel size is odd
    kernel_size = 3;

    % Get image dimensions
    [rows, cols] = size(img);

    % Calculate the padding size
    pad_size = floor(kernel_size / 2);

    % Pad the image manually with zeros
    padded_img = zeros(rows + 2 * pad_size, cols + 2 * pad_size);
    padded_img(pad_size + 1:end - pad_size, pad_size + 1:end - pad_size) = img;

    % Initialize the output image
    output = zeros(size(img));

    % Loop over every pixel in the original image
    for i = 1:rows
        for j = 1:cols
            % Extract the neighborhood
            neighborhood = [];
            for k = -pad_size:pad_size
                for l = -pad_size:pad_size
                    % Add the neighboring pixel value to the list
                    neighborhood(end + 1) = padded_img(i + pad_size + k, j + pad_size + l);
                end
            end

            % Sort the neighborhood values manually
            for m = 1:length(neighborhood)
                for n = m + 1:length(neighborhood)
                    if neighborhood(m) > neighborhood(n)
                        % Swap values
                        temp = neighborhood(m);
                        neighborhood(m) = neighborhood(n);
                        neighborhood(n) = temp;
                    end
                end
            end

            % Get the median value
            median_index = ceil(length(neighborhood) / 2);
            median_value = neighborhood(median_index);

            % Assign the median value to the output pixel
            output(i, j) = median_value;
        end
    end

    % Convert the output to the same class as the input image
    output = cast(output, class(img));
end
