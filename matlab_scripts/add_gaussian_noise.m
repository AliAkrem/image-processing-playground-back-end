% Octave function (save as add_gaussian_noise.m)
function noisy_img = add_gaussian_noise(img)
    pkg load image;

    % Convert input to double in range [0,1]
    img_double = double(img) / 255.0;

    % Add Gaussian noise
    noisy_img_double = imnoise(img_double, 'gaussian', 0, 0.01);

    % Convert back to uint8 range [0,255]
    noisy_img = uint8(noisy_img_double * 255);
endfunction
