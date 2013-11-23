from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
import unittest

class VBCourtsPassOp002_010(unittest.TestCase):
    #testing on opera

    def setUp(self):
        self.lst_doubles = ['0', '4', '8', '12', '16']
        self.lst_group = ['0', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',\
         '21', '22', '23', '24', '25']
        self.str_extra = "There will be 1 extra player to manually assign to teams."
        self.driver = webdriver.Opera()
        file = "http://www.carolchung.com/vb"
        #file = "file://localhost/programming/mywebapp/vb/index.html"
        self.driver.get(file)

    #def is_text_present(self, string):
        #if str(string) in self.driver.page_source: return True
        #else: return False

    def tearDown(self):
        self.driver.quit()

class NumCourts002(VBCourtsPassOp002_010):    

    def runTest(self):
        #commenting out next 6 lines because testing the default values; 0, 5
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        #select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        #select2.select_by_visible_text("5")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "1 court for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts002 court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts002 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2    

class NumCourts003(VBCourtsPassOp002_010):    

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
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts003 passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e


class NumCourts004(VBCourtsPassOp002_010):    

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
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts004 passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts004 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2    

class NumCourts005(VBCourtsPassOp002_010):    

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
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element2 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts005 passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

class NumCourts006(VBCourtsPassOp002_010):    

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
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element2 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts006 passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts006 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

class NumCourts007(VBCourtsPassOp002_010):    

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
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "1 court for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts007 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts007 3\'s court results passed'
        except AssertionError as e2:
            print 'Expected court results not found: ', e2

class NumCourts008(VBCourtsPassOp002_010):    

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
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "1 court for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts008 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts008 3\'s court results passed'
        except AssertionError as e2:
            print 'Expected court results not found: ', e2
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts008 extra players passed'
        except AssertionError as e3:
            print 'Expected extra results not found: ', e3

class NumCourts009(VBCourtsPassOp002_010):    

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
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "2 courts for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts009 passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

class NumCourts010(VBCourtsPassOp002_010):    

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
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "2 courts for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts010 passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts010 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2
 
if __name__ == '__main__':
    unittest.main()         
