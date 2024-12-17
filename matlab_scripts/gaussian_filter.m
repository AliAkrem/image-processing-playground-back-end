function filtered_image = gaussian_filter(input_image, sigma, filter_size)


    [x, y] = meshgrid(-(filter_size-1)/2:(filter_size-1)/2, ...
        -(filter_size-1)/2:(filter_size-1)/2);

    % Gaussian filter formula]

    mask= (1 / (2 * pi * sigma^2)) * exp(-(x.^2 + y.^2) / (2 * sigma^2));
    mask = mask/ sum(mask(:));  % Normalize

    % Apply convolution
    filt_img = conv2(input_image, mask, 'same');

    filtered_image = uint8(filt_img);


end
