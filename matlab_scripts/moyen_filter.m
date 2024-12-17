function filtered_image = moyen_filter(im_br)
    im_br = double(im_br);
    [m, n] = size(im_br);
    im_filt = zeros(m, n);

    for i = 2:m-1
        for j = 2:n-1
            im_filt(i, j) = mean(mean(im_br(i-1:i+1, j-1:j+1)));
        end
    end

    filtered_image = uint8(im_filt);
end
