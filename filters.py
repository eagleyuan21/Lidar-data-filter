import unittest
import numpy as np

# constants for the range distance in meters
range_min = 0.03
range_max = 50




# ran_filter : 2d array of floats, float, float -> 2d array of floats
# Takes the lidar data and replaces all values under the designated minimum with the 
# designated minimum and replaces all values over the designated maximum with the 
# designated maximum

def ran_filter(updates, r_min, r_max):
    
    for i in range(len(updates)):
        
        for j in range(len(updates[i])):
            
            if updates[i][j] < r_min:
                updates[i][j] = r_min
            elif updates[i][j] > r_max:
                updates[i][j] = r_max
                
    return updates


# temp_med_filter : 2d array of floats, Natural Number -> 2d array of floats
# Takes the lidar data and calculates the median at each entry in the array in the time step
# with the previous "d" time step arrays

def temp_med_filter(updates, d):
    hold = []
    
    for i in range(len(updates)):
        
        meds = []
        temp = []
        if (i-d) < 0:
            j = 0
        else:
            j = i - d
            
        for l in range(len(updates[i])):
            
            for k in range(j, i+1):
                
                temp.append(updates[k][l])
            
            meds.append(np.median(temp))
            temp = []
            
        hold.append(meds)

    return hold

# Testing the functions: Tests 1 and 2 test ran_filter while Tests 3 and 4 test temp_med_filter
# These tests can be modified to test other cases if need be 

class Testing(unittest.TestCase):
    
    def test_1(self):
        updates = [[6, 2.3, 4.3, 2, 3, 10, 20], [0, 2.3, 4.3, 2, 3, 10, 20]]
        self.assertEqual(ran_filter(updates, range_min, range_max),
                         [[6, 2.3, 4.3, 2, 3, 10, 20], [0.03, 2.3, 4.3, 2, 3, 10, 20]])
    
    def test_2(self):
        updates = [[-3.4, 0.3, 0, 67.4, 123, -30], [-2, 0, 1.3, -2.9, 4.7, 51]]
        self.assertEqual(ran_filter(updates, range_min, range_max),
                         [[0.03, 0.3, 0.03, 50, 50, 0.03], [0.03, 0.03, 1.3, 0.03, 4.7, 50]])
    
    def test_3(self):
        updates = [[0, 1, 2, 1, 3], [1,5,7,1,3], [2,3,4,1,0], [3,3,3,1,3], [10,2,4,0,0]]
        d = 3
        self.assertEqual(temp_med_filter(updates, d), 
                         [[0.0, 1.0, 2.0, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0], 
                          [1.0, 3.0, 4.0, 1.0, 3.0], [1.5, 3.0, 3.5, 1.0, 3.0], 
                          [2.5, 3.0, 4.0, 1.0, 1.5]])
        
    def test_4(self):
        updates = [[0, 4, 6, 3], [2, 45, 5, 23], [32, 24, 1, 0], [13, 2, 0, 6]]
        d = 2
        self.assertEqual(temp_med_filter(updates, d), 
                         [[0, 4, 6, 3], [1, 24.5, 5.5, 13], 
                          [2, 24, 5, 3], [13, 24, 1, 6]])
    
if __name__ == '__main__':
    unittest.main()