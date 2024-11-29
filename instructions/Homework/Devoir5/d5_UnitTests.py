import unittest
import d5

class d5_Tests(unittest.TestCase):
    
    def test_q3(self):
        print("\nTest de la  question 3")
        print("Q3_1")
        n=d5.prodListePos_rec([1,-2,5,0,6,-5], len([1,-2,5,0,6,-5]))
        self.assertEqual(n,30)
        n=d5.prodLRec1([1,-2,5,0,6,-5])
        self.assertEqual(n,30)
        print("Q3_2")
        n=d5.prodListePos_rec([],len([]))
        self.assertEqual(n, 1)
        n=d5.prodLRec1([])
        self.assertEqual(n,1)
        print("Q3_3")
        n=d5.prodListePos_rec([-2,-19,-4,-8], len([-2,-19,-4,-8]))
        self.assertEqual(n, 1)
        n=d5.prodLRec1([-2,-19,-4,-8])
        self.assertEqual(n,1)
        print("Q3_4")
        n=d5.prodListePos_rec([54,-2,5,1,0],len([54,-2,5,1,0]))
        self.assertEqual(n, 270)
        n=d5.prodLRec1([54,-2,5,1,0])
        self.assertEqual(n,270)


if __name__ == '__main__':
    unittest.main()

        
