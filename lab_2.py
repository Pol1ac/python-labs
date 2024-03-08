def min_square_size(Number, Wide, Height):
    min_size = 1
    max_size = max(Wide, Height) * Number  
    while min_size < max_size:
        x = (min_size + max_size) // 2  
        sheets_row = x // Wide
        sheets_col = x // Height

        if sheets_row * sheets_col >= Number:  
            max_size = x
        else:
            min_size = x + 1

    return min_size
