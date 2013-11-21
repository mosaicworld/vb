from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
import unittest

class VBCourtsPassFF021_030(unittest.TestCase):
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

class NumCourts021(VBCourtsPassFF021_030):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[20])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "4 courts for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts021 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

class NumCourts022(VBCourtsPassFF021_030):    

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[21])

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element2 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "4 courts for 3\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts022 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts022 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

class NumCourts023(VBCourtsPassFF021_030):    

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text(self.lst_doubles[1])

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[0])

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
            print 'NumCourts023 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

class NumCourts024(VBCourtsPassFF021_030):    

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text(self.lst_doubles[1])

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[1])

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
            print 'NumCourts024 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'NumCourts024 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

class NumCourts025(VBCourtsPassFF021_030):    

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text(self.lst_doubles[1])

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[2])

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
            print 'NumCourts025 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts025 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

class NumCourts026(VBCourtsPassFF021_030):    

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text(self.lst_doubles[1])

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[3])

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
            print 'NumCourts026 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts026 3\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'NumCourts026 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

class NumCourts027(VBCourtsPassFF021_030):    

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text(self.lst_doubles[1])

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[4])

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
            print 'NumCourts027 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts027 4\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e

class NumCourts028(VBCourtsPassFF021_030):    

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text(self.lst_doubles[1])

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text(self.lst_group[5])

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
            print 'NumCourts028 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts028 4\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'NumCourts028 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

class NumCourts029(VBCourtsPassFF021_030):    

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text(self.lst_doubles[1])

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
            strCourtResults = "2 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts029 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts029 3\'s court results passed'
        except AssertionError as e2:
            print 'Expected court results not found: ', e2

class NumCourts030(VBCourtsPassFF021_030):    

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text(self.lst_doubles[1])

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
            strCourtResults = "2 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'NumCourts030 2\'s court results passed'
        except AssertionError as e:
            print 'Expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'NumCourts030 3\'s court results passed'
        except AssertionError as e2:
            print 'Expected court results not found: ', e2
        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'NumCourts030 extra players passed'
        except AssertionError as e2:
            print 'Expected extra results not found: ', e2

if __name__ == '__main__':
    unittest.main()         