function filtered_img = max_filter(img)

    kernel_size = 3 ;
    % Get image size
    [rows, cols] = size(img);
    
    % Compute padding size
    pad = floor(kernel_size / 2);
    
    % Pad the image with zeros
    padded_img = zeros(rows + 2 * pad, cols + 2 * pad);
    padded_img(pad + 1:end - pad, pad + 1:end - pad) = img;
    
    % Initialize output image
    filtered_img = zeros(rows, cols);
    
    % Apply maximum filter
    for i = 1:rows
        for j = 1:cols
            % Extract the kernel window
            window = zeros(kernel_size^2, 1);
            count = 1;
            for m = -pad:pad
                for n = -pad:pad
                    window(count) = padded_img(i + pad + m, j + pad + n);
                    count = count + 1;
                end
            end
            
            % Find maximum value manually
            max_val = window(1);
            for k = 2:length(window)
                if window(k) > max_val
                    max_val = window(k);
                end
            end
            
            % Assign maximum value to the output image
            filtered_img(i, j) = max_val;
        end
    end
    
    % Convert to uint8 for display
    filtered_img = uint8(filtered_img);
end
