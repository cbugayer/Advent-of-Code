import os

script_dir = os.path.dirname(os.path.realpath(__file__))
file = 'sample.txt'
# file = 'input.txt'
with open(os.path.join(script_dir, file), "r") as f:
    input = f.read()

ranges = input.split(',')

class Range:
    def __init__(self, range):
        start, end = range.split('-')
        self.start = start
        self.end = end
    
    def no_potential(self):
        return len(self.start) % 2 and len(self.start) == len(self.end)
    
    def begin(self):
        half = len(self.start) // 2
        if len(self.start) % 2:
            half_zeros = '0'*half
            return ('1'+half_zeros) * 2
        else:
            half1, half2 = self.start[:half], self.start[half:] 
            if int(half1) >= int(half2):
                return half1 * 2
            else:
                half1_zero = int(half1 + ('0' * len(half2)))
                min_half2 = int('11' + ('0' * (len(half2)-1))) + 1
                added = str(half1_zero + min_half2)
                assert not len(added) % 2, added
                assert len(added) == len(self.start), f"len({added}) != len({self.start})"
                return added[:half] * 2


            #     10008000 -> 10011001
            #        11001
            #     1000.app(0000) + 11001

            #     10009000 -> 10011001

            #     10099000 -> 10101010
            #        11001
            #     1009.app(0000) + 11001
            #     10090000
            #        11001
            #     10101001 -> 1010 *2

            #     90009001
            #        11001
            #     9000.app(0000) + 11001
            #     90011001

            #     99989999
            #        11001
            #     99980000
            #     +  11001  
            #     99991001   
            #     9999 * 2

            #     25
            #     10
            #     20
            #   + 11
            #     31
            #     3*2

            #     15
            #     10
            #     10
            #   + 11
            #     21
            #     2*2
                
            #     1050
            #      110
            #     1000
            #      111
            #     1111
            #     11 * 2
                        
    def find_next(self, begin):

        pass
        
            
for range in ranges:
    my_range = Range(range)
    print(my_range.start, "-", my_range.end, ": ", my_range.begin())