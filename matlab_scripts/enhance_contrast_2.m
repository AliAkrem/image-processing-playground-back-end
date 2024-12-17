function enhanced_img = enhance_contrast_2(img, a, b)
  im = img;
  im = double(im);
  [m,n] = size(im);

  t = zeros(m, n);

  for i=1:m
      for j=1:n
          f = im(i,j);
          if f <= a
              t(i,j) = (b/a)*f;
          else
              t(i,j) = ((255-b)*f + 255*(b-a))/(255-a);
          endif
      endfor
  endfor

  enhanced_img = uint8(t);
endfunction
