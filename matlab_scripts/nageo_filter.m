function result = nageo_filter(im)
    [rows, cols] = size(im);
    res = zeros(rows, cols);
    padded = padarray(im, [2 2], 'replicate');

    % Pre-allocate the windows matrix
    windows = zeros(3, 3, 9);

    for i = 3:rows+2
        for j = 3:cols+2

            windows(:,:,1) = padded(i-2:i, j-2:j);
            windows(:,:,2) = padded(i-2:i, j-1:j+1);
            windows(:,:,3) = padded(i-2:i, j:j+2);
            windows(:,:,4) = padded(i-1:i+1, j-2:j);
            windows(:,:,5) = padded(i-1:i+1, j-1:j+1);
            windows(:,:,6) = padded(i-1:i+1, j:j+2);
            windows(:,:,7) = padded(i:i+2, j-2:j);
            windows(:,:,8) = padded(i:i+2, j-1:j+1);
            windows(:,:,9) = padded(i:i+2, j:j+2);

            % Calculate means and variances for all windows at once
            means = squeeze(mean(mean(windows)));
            vars = squeeze(var(reshape(windows, 9, [])));

            % Find window with minimum variance and use its mean
            [~, idx] = min(vars);
            res(i-2, j-2) = means(idx);
        endfor
    endfor

    result = uint8(res);
endfunction



