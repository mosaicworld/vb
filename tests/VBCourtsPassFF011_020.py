from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
import unittest

class VBCourtsPassFF011_020(unittest.TestCase):
    #global vars

    def setUp(self):
        self.lst_doubles = ['0', '4', '8', '12', '16']
        self.lst_group = ['0', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',\
         '21', '22', '23', '24', '25']
        self.str_extra = "There will be 1 extra player to manually assign to teams."
        self.driver = webdriver.Firefox()
        #file = "http://www.carolchung.com/vb"
        file = "file://localhost/programming/mywebapp/vb/index.html"
        self.driver.get(file)

    #def is_text_present(self, string):
        #if str(string) in self.driver.page_source: return True
        #else: return False

    def tearDown(self):
        self.driver.quit()

class NumCourts011(VBCourtsPassFF011_020):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[10])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts011 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts011 4\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e 

class NumCourts012(VBCourtsPassFF011_020):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[11])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts012 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts012 4\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e 
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts012 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

class NumCourts013(VBCourtsPassFF011_020):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[12])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element2 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "2 courts for 4\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts013 4\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e 

class NumCourts014(VBCourtsPassFF011_020):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[13])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element2 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "2 courts for 4\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts014 4\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e 
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts014 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

class NumCourts015(VBCourtsPassFF011_020):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[14])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "3 courts for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts015 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

class NumCourts016(VBCourtsPassFF011_020):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[15])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "3 courts for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts016 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts016 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

class NumCourts017(VBCourtsPassFF011_020):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[16])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "2 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts017 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "2 courts for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts017 3\'s court results passed'
        except AssertionError as e2:
            print 'Expected court results not found: ', e2

class NumCourts018(VBCourtsPassFF011_020):    

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
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "2 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts018 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "2 courts for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts018 3\'s court results passed'
        except AssertionError as e2:
            print 'Expected court results not found: ', e2
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts018 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

class NumCourts019(VBCourtsPassFF011_020):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[18])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts019 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "2 courts for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts019 4\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e 

class NumCourts020(VBCourtsPassFF011_020):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[19])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts020 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "2 courts for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts020 4\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e 
        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'NumCourts020 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

if __name__ == '__main__':
    unittest.main()         