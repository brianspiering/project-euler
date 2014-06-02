import problem_1
import unittest

class KnownValues(unittest.TestCase):
    knownValues = ( (10, 23), # n, sum_multiples
                    (1000, 233168))

    def test_method_1_to_known_values(self):                           
        """method_1 should give known result with known input"""
        for n, sum_multiples in self.knownValues:              
            result = problem_1.sum_multiples_method_1(n)                     
            self.assertEqual(sum_multiples, result)   

    def test_method_2_to_known_values(self):                           
        """method_2 should give known result with known input"""
        for n, sum_multiples in self.knownValues:              
            result = problem_1.sum_multiples_method_2(n)                     
            self.assertEqual(sum_multiples, result)   

if __name__ == '__main__':
    unittest.main()