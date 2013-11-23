from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
import unittest

class VBResetFailFF002_005(unittest.TestCase):
    #testing on firefox

    def setUp(self):
        self.lst_doubles = ['0', '4', '8', '12', '16']
        self.lst_group = ['0', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',\
         '21', '22', '23', '24', '25']
        self.str_extra = "There will be 1 extra player to manually assign to teams."
        self.driver = webdriver.Firefox()
        file = "http://www.carolchung.com/vb"
        #file = "file://localhost/programming/mywebapp/vb/index.html"
        self.driver.get(file)

    #def is_text_present(self, string):
        #if str(string) in self.driver.page_source: return True
        #else: return False

    def tearDown(self):
        self.driver.quit()

class Reset002(VBResetFailFF002_005):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 5
    #Expect CSS id's for "crt_results" should have been removed
    #Without annotation, Test should fail because NoSuchElementException would result.
    #Generally, this test case would error out with a NoSuchElementException for id "crt_results"
    #but if the first try block were commented out, the NoSuchElementException would occur for id "crt_results2" 
    # and id = "crt_results5"

    def runTest(self):
        #do not set either select list option because just testing default values
        #sets select list option for How many group players
        #select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        #select2.select_by_visible_text("5")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()

        #click button Reset
        btnClear = self.driver.find_element_by_id("btnClear")
        btnClear.click()

        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results") == None)
            print 'Reset002 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'Reset002 NoSuchElementException for id: "crt_results"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results2") == None)
            print 'Reset002 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'Reset002 NoSuchElementException for id: "crt_results2"; ', e2
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results5") == None)
            print 'Reset002 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'Reset002 NoSuchElementException for id: "crt_results5"; ', e2
    
class Reset003(VBResetFailFF002_005):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 21
    #Expect CSS id's for "crt_results" should have been removed
    #Without annotation, Test should fail because NoSuchElementException would result.
    #Generally, this test case would error out with a NoSuchElementException for id "crt_results"
    #but if the first try block were commented out, the NoSuchElementException would occur for id "crt_results2" 
    #and id = "crt_results3"

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[17])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()

        #click button Reset
        btnClear = self.driver.find_element_by_id("btnClear")
        btnClear.click()

        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results") == None)
            print 'Reset003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'Reset003 NoSuchElementException for id: "crt_results"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results2") == None)
            print 'Reset003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'Reset003 NoSuchElementException for id: "crt_results2"; ', e2
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results3") == None)
            print 'Reset003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'Reset003 NoSuchElementException for id: "crt_results3"; ', e2

class Reset004(VBResetFailFF002_005):    
    @unittest.expectedFailure
    #Expect CSS id's for "crt_results" should have been removed
    #Without annotation, Test should fail because NoSuchElementException would result.
    #Generally, this test case would error out with a NoSuchElementException for id "crt_results"
    #but if the first try block were commented out, the NoSuchElementException would occur for id "crt_results2" 
    #and id = "crt_results5"

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text(self.lst_doubles[2])

        #comment next 3 lines to leave default value (5)
        #sets select list option for How many group players
        #select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        #select2.select_by_visible_text("5")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()

        #click button Reset
        btnClear = self.driver.find_element_by_id("btnClear")
        btnClear.click()

        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results") == None)
            print 'Reset004 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'Reset004 NoSuchElementException for id: "crt_results"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results2") == None)
            print 'Reset004 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'Reset004 NoSuchElementException for id: "crt_results2"; ', e2
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results5") == None)
            print 'Reset004 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'Reset004 NoSuchElementException for id: "crt_results5"; ', e2

class NumCourts005(VBResetFailFF002_005):    
    @unittest.expectedFailure
    #Expect CSS id's for "crt_results" should have been removed
    #Without annotation, Test should fail because NoSuchElementException would result.
    #Generally, this test case would error out with a NoSuchElementException for id "crt_results"
    #but if the first try block were commented out, the NoSuchElementException would occur for id "crt_results2", 
    #id = "crt_results3", and id = "crt_results5"

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[4])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results2") == None)
            print 'NumCourts005 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts005 NoSuchElementException for id: "crt_results3"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results3") == None)
            print 'NumCourts005 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts005 NoSuchElementException for id: "crt_results3"; ', e2
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results5") == None)
            print 'NumCourts005 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts005 NoSuchElementException for id: "crt_results5"; ', e2   
 
if __name__ == '__main__':
    unittest.main()         

