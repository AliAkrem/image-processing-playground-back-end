
function filtered_image =  gaussian_filter(input_image)
im_br = double(im_br);
[m, n] = size(im_br);
im_filt = zeros(m, n);

for i = 2:m-1
    for j = 2:n-1
        im_filt(i, j) = mean(mean(im_br(i-1:i+1, j-1:j+1)));
    end
end

im_filt_conv = zeros(m, n);
masque = ones(3) / 9;
im_filt_conv = conv2(im_filt, masque, 'same');
subplot(133), imshow(uint8(im_filt_conv));