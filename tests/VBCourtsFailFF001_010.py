from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
import unittest

class VBCourtsFailFF001_010(unittest.TestCase):
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

class NumCourts001(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 0
    #Expect no court results to display
    #Without annotation, Test should fail because no element with id = "crt_results" would be appended to the page
    #Without annotation, NoSuchElementException would result

    def runTest(self):
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("0")

        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("0")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            #element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results")))
            #element2 = self.driver.find_element_by_id("crt_results")
            self.assertTrue(self.driver.find_element_by_id("crt_results") == None)
            print 'found id: "crt_results"'
        except AssertionError as e2:
        #except NoSuchElementException as e2:
            print 'NumCourts001 NoSuchElementException for id: "crt_results"; ', e2

class NumCourts001b(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 0
    #Expect no court results to display
    #Without annotation, Test should fail because no element with id = "crt_results" would be appended to the page
    #Without annotation, TimeoutException would result (WebDriverWait)

    def runTest(self):
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("0")

        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("0")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results")))
            #element2 = self.driver.find_element_by_id("crt_results")
            self.assertTrue(self.driver.find_element_by_id("crt_results") == None)
            print 'found id: "crt_results"'
        except AssertionError as e2:
        #except TimeoutException as e2:
            print 'NumCourts001b TimeoutException for id: "crt_results"; ', e2


class NumCourts002(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 5
    #Expect no addition of CSS id's for "crt_results3" or "crt_results4"
    #Without annotation, Test should fail because no element with id = "crt_results3" or id = "crt_results4" 
    #would be appended to the page
    #Without annotation, NoSuchElementException would result
    #Generally, this test case would error out with a NoSuchElementException for id "crt_results3"
    #but if the first try block were commented out, the NoSuchElementException would occur for id "crt_results4"

    def runTest(self):
        #do not set either select list option because just testing default values
        #sets select list option for How many group players
        #select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        #select2.select_by_visible_text("5")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results3") == None)
            print 'NumCourts002 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts002 NoSuchElementException for id: "crt_results3"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results4") == None)
            print 'NumCourts002 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts002 NoSuchElementException for id: "crt_results4"; ', e2
    
class NumCourts003(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 6
    #Expect no addition of CSS id's for "crt_results2" or "crt_results4"
    #Without annotation, Test should fail. NoSuchElementException would result

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[2])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results2") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results3"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results4") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results4"; ', e2
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results5") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results5"; ', e2    

class NumCourts004(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 7
    #Expect no addition of CSS id's for "crt_results2" or "crt_results4"
    #Without annotation, Test should fail. NoSuchElementException would result

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[3])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results2") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results3"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results4") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results4"; ', e2   

class NumCourts005(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 8
    #Expect no addition of CSS id's for "crt_results2" or "crt_results3" or "crt_results5" 
    #Without annotation, Test should fail. NoSuchElementException would result

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

class NumCourts006(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 9
    #Expect no addition of CSS id's for "crt_results2" or "crt_results3"  
    #Without annotation, Test should fail. NoSuchElementException would result

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[5])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results2") == None)
            print 'NumCourts006 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts006 NoSuchElementException for id: "crt_results3"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results3") == None)
            print 'NumCourts006 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts006 NoSuchElementException for id: "crt_results3"; ', e2

class NumCourts007(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 10
    #Expect no addition of CSS id's for "crt_results4" or "crt_results5"  
    #Without annotation, Test should fail. NoSuchElementException would result

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[6])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results4") == None)
            print 'NumCourts007 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts007 NoSuchElementException for id: "crt_results4"; ', e2
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results5") == None)
            print 'NumCourts007 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts007 NoSuchElementException for id: "crt_results5"; ', e2   

class NumCourts008(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 11
    #Expect no addition of CSS id's for "crt_results4" 
    #Without annotation, Test should fail. NoSuchElementException would result

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[7])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results4") == None)
            print 'NumCourts008 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts008 NoSuchElementException for id: "crt_results4"; ', e2

class NumCourts009(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 12
    #Expect no addition of CSS id's for "crt_results2", "crt_results4", "crt_results5" 
    #Without annotation, Test should fail. NoSuchElementException would result

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[8])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results2") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results3"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results4") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results4"; ', e2
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results5") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results5"; ', e2    

class NumCourts010(VBCourtsFailFF001_010):    
    @unittest.expectedFailure
    #Tests where doubles players is 0 and group players is 13
    #Expect no addition of CSS id's for "crt_results2", "crt_results4"
    #Without annotation, Test should fail. NoSuchElementException would result

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[9])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(15)
            self.driver.implicitly_wait(0);
            self.assertTrue(self.driver.find_element_by_id("crt_results2") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results3"; ', e2 
        try:
            self.assertTrue(self.driver.find_element_by_id("crt_results4") == None)
            print 'NumCourts003 court results passed'
        except AssertionError as e:
        #except NoSuchElementEception as e:
            print 'NumCourts003 NoSuchElementException for id: "crt_results4"; ', e2
 
if __name__ == '__main__':
    unittest.main()         

