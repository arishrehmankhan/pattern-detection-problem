def calculate_similarity(data_segment, pattern):
    data_segment_length = len(data_segment)
    pattern_length = len(pattern)

    # if the lengths of data_segment and pattern are different,
    # we can't calculate the similarity
    if data_segment_length != pattern_length:
        return "Error: Data segement and pattern have different lengths!"
    
    # sum variable will store the similarity value
    sum = 0

    # calculating similarity
    for i in range(data_segment_length):
        sum += data_segment[i] * pattern[i]

    # return the result
    return sum