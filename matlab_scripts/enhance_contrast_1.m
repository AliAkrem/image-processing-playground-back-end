function enhanced_img = enhance_contrast_1(img, a, b)
  pkg load image;
  im = img;
  im = double(im);
  [m,n] = size(im);

  t = zeros(m, n);  

  for i=1:m
      for j=1:n
          f = im(i,j);
          if f < a
              t(i,j) = 0;
          elseif f > b
              t(i,j) = 255;
          else
              t(i,j) = 255 * ((f-a)/(b-a));
          end
      end
  end
  enhanced_img = uint8(t);

endfunction
