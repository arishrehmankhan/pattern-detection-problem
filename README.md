# The pattern detection problem

## Introduction

In this problem, the goal is to write a python program to determine whether a given pattern appears in a data series, and if so, where it is located in the data series. This type of problems is very common in many disciplines, including computer science, engineering, medicine Android science. There are many different types of pattern detection problems, the setting of this assignment is similar to that used in radars.  A radar transmits a pulse of a specific shape and waits for a pulse of similar shape to return, in order to determine the position of an object. The method described below is known as matched filtering and is widely used in communication systems.

## Algorithm

The goal is to detect whether a certain pattern appears in the data series. In the following example, the pattern to be detected is a sequence of 4 numbers (see Fig 2); and the data series contains 10 data points (see Fig 1).

data_series = [-1, 2, -2, 3, 41, 38, 22, 10, -1, 3]
pattern = [40, 30, 20, 10]
Data Series Pattern
If you compare these two figures, you can see that this pattern appears between 5th (at index 4) to 8th (at index 7) data points of the data series. Note that it is not an exact match, but a fairly close one. Now you can spot the pattern using your eyes, let us see how an algorithm can do it.

Since the given pattern has 4 data points, we will take a segment of 4 consecutive data points from the data series at a time and compute a similarity measure. The similarity  measure should have the property that if a segment of the data series is similar to the given pattern, then the similarity measure of that segment is large, and vice versa. Hence, if we can compute the similarity measures of all possible segments, then we can identify the segment that is most similar to the given pattern. We will now provide more details.

The algorithm begins with computing the similarity measure between the given pattern and the first segment, which is formed by the first 4 data points of the data series. In terms of the two lists above, the similarity measure for the first segment is:

data_series[0]*pattern[0] + data_series[1]*pattern[1] + data_series[2]*pattern[2] + data_series[3]*pattern[3]
After this, we compute the similarity measure between the given pattern and the second segment, which is formed by the second to fifth data points of the data series. For the above example, the similarity measure for this segment is:

data_series[1]*pattern[0] + data_series[2]*pattern[1] + data_series[3]*pattern[2] + data_series[4]*pattern[3]
We then do the same with the segment formed by the third to sixth data points (the third segment), giving a similarity measure equals to:

data_series[2]*pattern[0] + data_series[3]*pattern[1] + data_series[4]*pattern[2] + data_series[5]*pattern[3]
We repeat this until we have computed the similarity measure for the last possible segment, which is formed by the 7th to 10th data points. The following is the similarity list for the above example and a plot:

similarity = [10, 490, 1210, 2330, 3320, 2370, 1190]


Similarity index

We need to consider the following cases.

Case 1: It is possible that the given data series is shorter than the given pattern, in this case, we return "Insufficient data".

Case 2: All the similarity measures are (strictly) less than the given threshold value. This means none of the segments is similar to the given pattern. In this case, we say the pattern is not present in the data series and return "Not detected". This is not the case for this example.

Case 3: At least one similarity measure is greater than or equal to the given threshold value. This is the case for this example. The similarity measure plot above shows that the fifth similarity measure is the largest. You can work out that the fifth similarity measure is computed by using the segment formed by the fifth (index 4) to eighth (index 7) data points of the data series. This procedure is therefore telling us that the segment consisting of fifth to eighth data points is most similar to the given pattern. Indeed this is what we had found by using visual inspection earlier. We will identify the location of the pattern by using the first index of the segment that has the highest similarity measure.

function pattern_search_max (described below): we return the index of the highest similarity measure that is also greater than or equal to the given threshold value. In Fig 3, the index of the highest similarity measure is 4.
function pattern_search_multiple (described below): Consider the following definition of overlapping indices,
We say two indices are overlapping if the distance between them is less than the width of the pattern (4 in the above example).

The function 'pattern_search_multiple' returns a list of non overlapping indices that are greater than or equal to the given threshold value, and that satisfy the following criteria:

an index is not selected if the value at the index is less than a value at one of it's overlapping indices.
an index is not selected if it is overlapping with first or last index.
In the following example, selected indices are marked with green circles. Here, index 6 is not selected because the value at index 5 (distance of 1) is greater than the value at index 6. Similarly index 32 is not selected because the value at index 34 (distance 2) is higher. The example in Fig 4 will return the list [5, 16, 34].

There are many different approaches to calculate similarity measures between data segments and a pattern, above we have discussed just one of them! Therefore, a given data series representing similarity measures may or may not have clearly defined 'pyramid' patterns as shown in Fig 3. For example, there are no clearly defined 'pyramid' patterns in Fig 4.
Similarity index

This completes the descript.

![Fig 1](/img/Fig_1-Data_Series "Fig 1")
![Fig 2](/img/Fig_2-Pattern "Fig 1")
![Fig 3](/img/Fig_3-Similarity "Fig 1")
![Fig 4](/img/Fig_4-pattern_search_multiple "Fig 1")