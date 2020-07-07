import calculate_similarity_list as csl

def pattern_search_max(data_series, pattern, threshold):
    data_series_length = len(data_series)
    pattern_length = len(pattern)
    
    # we can't calculate the similarity list if data_series_length < pattern_lenght
    if data_series_length < pattern_length:
        return "Error: Insufficient data!"

    # calculating similarity_list using calculate_similarity_list function
    similarity_list = csl.calculate_similarity_list(data_series, pattern)

    # initialize greatest_value with smallest value possible
    greatest_value = float('-inf')

    # position of greatest_value of similarity list is initialized with 0
    # at the begining
    position = 0

    # looping throught all the values of similarity list
    for i in range(len(similarity_list)):
        # if value is greater than current greatest_value, make it the greatest value
        # and update the position
        if similarity_list[i] > greatest_value:
            greatest_value = similarity_list[i]
            position = i

    # if all the values are smaller that threshold, return 'Not detected' error
    if greatest_value < threshold:
        return "Error: Not detected!"
    
    # return the position 
    return position