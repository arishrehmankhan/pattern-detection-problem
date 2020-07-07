import calculate_similarity as cs

def calculate_similarity_list(data_series, pattern):
    data_series_length = len(data_series)
    pattern_length = len(pattern)
    
    # list to store the similarity values
    similarity_list = []

    # loop will run from 0 to data_series_length - pattern_length + 1
    for i in range(data_series_length - pattern_length + 1):
        # append the similarity value calculated using calculate_similarity
        # function to the similarity_list 
        similarity_list += [cs.calculate_similarity(data_series[i:i+pattern_length], pattern)]

    # return the similarity_list
    return similarity_list