import unittest
import Appliances
import ApplianceOwner


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

class TestSolarPanel(unittest.TestCase):
    pass

class TestPerson(unittest.TestCase):
    test_on_matrix_on = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    test_on_matrix_off = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def testSetSolarPanelStatus(self):
        test_person = ApplianceOwner.Person()
        test_person.setSolarPanelStatus(False)
        test_person.createAppliances(1)
        
        self.assertEqual(test_person.solar_panel_status,False)
        self.assertEqual(test_person.has_solar_panel,False)



        test_person.setSolarPanelStatus(True)
        test_person.createAppliances(1)

        self.assertEqual(test_person.solar_panel_status,True)
        self.assertEqual(test_person.has_solar_panel,True)

    def testTickEnergy(self):
        test_appl = Appliances.Appliance("test",1,1,1)
        test_appl.setOnMatrix(TestPerson.test_on_matrix_on)
        test_appliance_off = Appliances.Appliance("test",1,1,1)
        test_appliance_off.setOnMatrix(TestPerson.test_on_matrix_off)

        test_person = ApplianceOwner.Person()
        test_person.appliance_list.append(test_appl)
        test_person.appliance_list.append(test_appliance_off)
        
        for i in range(24):
            self.assertEqual(test_person.tickEnergy(i),3600)
        





if __name__ == '__main__':
    unittest.main()


        

        