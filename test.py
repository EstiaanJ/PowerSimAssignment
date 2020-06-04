import unittest
from source import Appliances

class TestAppliance(unittest.TestCase):
    test_on_matrix_on = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    test_on_matrix_off = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def testIsOn(self):
        testAppl = Appliances.Appliance("test",1,1,1)
        testAppl.setOnMatrix(TestAppliance.test_on_matrix_on)
        for i in range(24):
            self.assertEqual(testAppl.isOn(i),True)

        testAppl.setOnMatrix(TestAppliance.test_on_matrix_off)
        for i in range(24):
            self.assertEqual(testAppl.isOn(i),False)
        #TODO: A test for 50%

    def testTickEnergy(self):
        for k in range(-1000,1000,100):
            for j in range(-1000,1000,100):
                testAppl = Appliances.Appliance("test",k,0,j) #name,mean_power,power_devation,operational_power
                testAppl.setOnMatrix(TestAppliance.test_on_matrix_on) 
                for i in range(24):
                    self.assertEqual(testAppl.tickEnergy(i),(3600 * j))

                testAppl.setOnMatrix(TestAppliance.test_on_matrix_off)
                for i in range(24):
                    self.assertEqual(testAppl.tickEnergy(i),0)


if __name__ == '__main__':
    unittest.main()


        

        