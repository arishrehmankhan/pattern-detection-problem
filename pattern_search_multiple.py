def pattern_search_multiple(data_series, pattern_width, threshold):

    data_series_length = len(data_series)

    # suppose pattern width is 4, we can't find the pattern in the data_series
    # if lenght of data_series is less than 9 (due to given conditions).
    if data_series_length < 2 * pattern_width + 1:
        return "Error: Insufficient data!"

    selected = [] # list to store selected values
    flag = 0 # set flag to 0

    # loop through all the values of data series according to the given conditions.
    for i in range(pattern_width, data_series_length - pattern_width + 1):
        flag = 0
        # if we get any values greater than the data_series[i] in the overlapping
        # indices, we will discard that value
        for j in range(i-pattern_width, i+pattern_width):
            if data_series[j] > data_series[i]:
                flag = 1
                break
        if flag == 0:
            # if data_series[i] is greater than threshold, then only it will be selected
            if data_series[i] > threshold:
                selected += [i]
    
    # if selected list is empty, we have not detected any pattern.
    if selected == []:
        return "Error: Not detected!"

    # return the selected list
    return selected