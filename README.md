# Lidar-data-filter
Two filter functions for lidar data 

The first function takes in lidar data and minimum and maximum values and replaces any values less than the designated minimum value with the minimum value and replaces any values greater than the designated maximum value with the maximum value. 

The second function takes in lidar data and an integer "d", and it finds the temporal median at each time which is the median of each element with the previous "d" times.

Example: Where d = 2,
| Time | Input     | Output          |
|-------|----------|----------------|
| 0    | [2, 4, 9] | [2, 4, 9]       |
| 1    | [1, 3, 2] | [1.5, 3.5, 5.5] |
| 2    | [6, 4, 8] | [2, 4, 8]       |
| 3    | [3, 7, 4] | [3, 4, 4]       |

At the bottom there are unit tests that test both functions. These can be modified to test more cases.
