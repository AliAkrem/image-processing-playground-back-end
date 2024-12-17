function base64_image = plot_generator(data)
    % Create a figure
    fig = figure('visible', 'off');
    
    % Generate plot
    plot(data.x, data.y, '-o');
    title(data.title);
    xlabel(data.xlabel);
    ylabel(data.ylabel);
    grid on;
    
    % Save plot to temporary file
    temp_file = tempname;
    print(fig, temp_file, '-dpng');
    
    % Read file and convert to base64
    fid = fopen([temp_file '.png'], 'rb');
    bytes = fread(fid, inf, 'uint8');
    fclose(fid);
    
    % Delete temporary file
    delete([temp_file '.png']);
    
    % Convert to base64
    base64_image = base64encode(bytes);
endfunction

% Helper function for base64 encoding
function base64 = base64encode(bytes)
    base64 = matlab.net.base64encode(bytes);
endfunction 