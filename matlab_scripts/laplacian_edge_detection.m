function output_image = laplacian_edge_detection(image, s)
    
    
    if size(image, 3) == 3
        image = rgb2gray(image);
    end

M1 = [ 0 -1 0 ;
       -1 4 -1 ;
       0 -1 0];

out_1 = conv2(image , M1 ,'same');

out_1_bw = out_1 > s;

out_1_bw = out_1_bw * 255 / max(out_1_bw(:));


output_image = out_1_bw;

endfunction