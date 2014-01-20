from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
import unittest

class VBCourtsPassFF(unittest.TestCase):
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

class NumCourtsSimple01(VBCourtsPassFF):
    """ Tests a simple case that should pass.
    How many doubles players? 4
    How many group players? 6 

    """    

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("4")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("6")

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
            print 'Test01 2\'s court results passed'
        except AssertionError as e:
            print 'Test01 expected court results not found: ', e
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test01 3\'s court results passed'
        except AssertionError as e:
            print 'Test01 expected court results not found: ', e

class NumCourtsBoundarySingleDig02(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 8
    How many group players? 9 

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("8")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("9")

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
            print 'Test02 2\'s court results passed'
        except AssertionError as e:
            print 'Test02 expected court results not found: ', e
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test02 4\'s court results passed'
        except AssertionError as e:
            print 'Test02 expected court results not found: ', e
        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'Test02 extra players passed'
        except AssertionError as e2:
            print 'Test02 expected extra results not found: ', e2

class NumCourtsBoundaryDoubleDig03(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 12
    How many group players? 9 

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("12")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("9")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "3 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'Test03 2\'s court results passed'
        except AssertionError as e:
            print 'Test03 expected court results not found: ', e
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test03 4\'s court results passed'
        except AssertionError as e:
            print 'Test03 expected court results not found: ', e
        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'Test03 extra players passed'
        except AssertionError as e2:
            print 'Test03 expected extra results not found: ', e2

class NumCourtsBoundaryDoubleDig04(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 8
    How many group players? 10 

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("8")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("10")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "3 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'Test04 2\'s court results passed'
        except AssertionError as e:
            print 'Test04 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test04 3\'s court results passed'
        except AssertionError as e2:
            print 'Test04 expected court results not found: ', e2 

class NumCourtsBoundaryDoubleDig05(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 12
    How many group players? 10

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("12")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("10")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "4 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'Test05 2\'s court results passed'
        except AssertionError as e:
            print 'Test05 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test05 3\'s court results passed'
        except AssertionError as e2:
            print 'Test05 expected court results not found: ', e2 

class NumCourtsBoundaryMinValues06(VBCourtsPassFF):
    """Tests a simple case that should fail.
    How many doubles players? 0
    How many group players? 0

    """

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
            print 'Test06 unexpected pass. Found id: "crt_results"'
        except AssertionError as e2:
        #except NoSuchElementException as e2:
            print 'Test06 expected fail. NoSuchElementException for id: "crt_results"; ', e2

class NumCourtsBoundaryMaxValues07(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 16
    How many group players? 25

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("16")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("25")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "4 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'Test07 2\'s court results passed'
        except AssertionError as e:
            print 'Test07 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "4 courts for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test07 3\'s court results passed'
        except AssertionError as e2:
            print 'Test07 expected court results not found: ', e2 

        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'Test07 extra players passed'
        except AssertionError as e2:
            print 'Test07 expected extra results not found: ', e2    

class NumCourtsBoundaryDefaultValues08(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 (default)
    How many group players? 5 (default)

    """

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
            print 'Test08 court results passed'
        except AssertionError as e:
            print 'Test08 expected court results not found: ', e
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'Test08 extra players passed'
        except AssertionError as e2:
            print 'Test08 expected extra results not found: ', e2    

class NumCourtsBoundaryEvenTeam2s_09(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 4 
    How many group players? 0

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("4")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("0")

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
            print 'Test09 court results passed'
        except AssertionError as e:
            print 'Test09 expected court results not found: ', e

class NumCourtsBoundaryEvenTeam2s_10(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 12 
    How many group players? 0

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("12")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("0")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "3 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'Test10 court results passed'
        except AssertionError as e:
            print 'Test10 expected court results not found: ', e

class NumCourtsBoundaryEvenTeam3s_11(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 6

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("6")

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
            print 'Test11 passed'
        except AssertionError as e:
            print 'Test11 expected court results not found: ', e

class NumCourtsBoundaryEvenTeam3s_12(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 12

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("12")

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
            print 'Test12 passed'
        except AssertionError as e:
            print 'Test12 expected court results not found: ', e

class NumCourtsBoundaryEvenTeam4s_13(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 8

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("8")

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
            print 'Test13 passed'
        except AssertionError as e:
            print 'Test13 expected court results not found: ', e

class NumCourtsBoundaryEvenTeam4s_14(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 16

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("16")

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
            print 'Test14 passed'
        except AssertionError as e:
            print 'Test14 expected court results not found: ', e

class NumCourtsBoundaryEvenTeam2s3s_15(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 10

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("10")

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
            print 'Test15 2\'s court results passed'
        except AssertionError as e:
            print 'Test15 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test15 3\'s court results passed'
        except AssertionError as e2:
            print 'Test15 expected court results not found: ', e2

class NumCourtsBoundaryEvenTeam2s3s_16(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 4 
    How many group players? 6

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("4")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("6")

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
            print 'Test16 2\'s court results passed'
        except AssertionError as e:
            print 'Test16 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test16 3\'s court results passed'
        except AssertionError as e2:
            print 'Test16 expected court results not found: ', e2

class NumCourtsBoundaryEvenTeam2s3s_17(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 4 
    How many group players? 20

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("4")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("20")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "3 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'Test17 2\'s court results passed'
        except AssertionError as e:
            print 'Test17 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "2 courts for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test17 3\'s court results passed'
        except AssertionError as e2:
            print 'Test17 expected court results not found: ', e2

class NumCourtsBoundaryEvenTeam3s4s_18(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 14

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("14")

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
            print 'Test18 3\'s court results passed'
        except AssertionError as e:
            print 'Test18 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test18 4\'s court results passed'
        except AssertionError as e:
            print 'Test18 expected court results not found: ', e 

class NumCourtsBoundaryEvenTeam2s3s4s_19(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 4 
    How many group players? 14

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("4")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("14")

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
            print 'Test19 2\'s court results passed'
        except AssertionError as e:
            print 'Test19 expected court results not found: ', e
 
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test19 3\'s court results passed'
        except AssertionError as e2:
            print 'Test19 expected court results not found: ', e2

        try:
            element5 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element6 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element6.text)
            print 'Test19 4\'s court results passed'
        except AssertionError as e:
            print 'Test19 expected court results not found: ', e 

class NumCourtsBoundaryEvenTeam2s3s4s_20(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 12 
    How many group players? 14

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("12")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("14")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "3 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'Test20 2\'s court results passed'
        except AssertionError as e:
            print 'Test20 expected court results not found: ', e
 
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test20 3\'s court results passed'
        except AssertionError as e2:
            print 'Test20 expected court results not found: ', e2

        try:
            element5 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element6 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element6.text)
            print 'Test20 4\'s court results passed'
        except AssertionError as e:
            print 'Test20 expected court results not found: ', e 

class NumCourtsBoundaryOddTeam2s_21(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 8 
    How many group players? 5

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("8")

        #comment out to use default value
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
            strCourtResults = "3 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'Test21 2\'s court results passed'
        except AssertionError as e:
            print 'Test21 expected court results not found: ', e
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'Test21 extra players passed'
        except AssertionError as e2:
            print 'Test21 expected extra results not found: ', e2

class NumCourtsBoundaryOddTeam3s_22(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 7

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("7")

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
            print 'Test22 3\'s court results passed'
        except AssertionError as e:
            print 'Test22 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'Test22 extra players passed'
        except AssertionError as e2:
            print 'Test22 expected extra results not found: ', e2    

class NumCourtsBoundaryOddTeam3s_23(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 13

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("13")

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
            print 'Test23 3\'s court results passed'
        except AssertionError as e:
            print 'Test23 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'Test23 extra players passed'
        except AssertionError as e2:
            print 'Test23 expected extra results not found: ', e2 

class NumCourtsBoundaryOddTeam4s_24(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 9

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("9")

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
            print 'Test24 4\'s court results passed'
        except AssertionError as e:
            print 'Test24 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'Test24 extra players passed'
        except AssertionError as e2:
            print 'Test24 expected extra results not found: ', e2

class NumCourtsBoundaryOddTeam4s_25(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 17

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("17")

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
            print 'Test25 4\'s court results passed'
        except AssertionError as e:
            print 'Test25 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'Test25 extra players passed'
        except AssertionError as e2:
            print 'Test25 expected extra results not found: ', e2

class NumCourtsBoundaryOddTeam2s3s_26(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 4 
    How many group players? 7

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("4")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("7")

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
            print 'Test26 2\'s court results passed'
        except AssertionError as e:
            print 'Test26 expected court results not found: ', e
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test26 3\'s court results passed'
        except AssertionError as e:
            print 'Test26 expected court results not found: ', e
        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'Test26 extra players passed'
        except AssertionError as e2:
            print 'Test26 expected extra results not found: ', e2

class NumCourtsBoundaryOddTeam2s3s_27(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 11

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("11")

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
            print 'Test27 2\'s court results passed'
        except AssertionError as e:
            print 'Test27 expected court results not found: ', e

        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test27 3\'s court results passed'
        except AssertionError as e2:
            print 'Test27 expected court results not found: ', e2

        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'Test27 extra players passed'
        except AssertionError as e3:
            print 'Test27 expected extra results not found: ', e3

class NumCourtsBoundaryOddTeam2s3s_28(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 21

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("21")

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
            print 'Test28 2\'s court results passed'
        except AssertionError as e:
            print 'Test28 expected court results not found: ', e

        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "2 courts for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test28 3\'s court results passed'
        except AssertionError as e2:
            print 'Test28 expected court results not found: ', e2

        try:
            element5 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element5.text)
            print 'Test28 extra players passed'
        except AssertionError as e3:
            print 'Test28 expected extra results not found: ', e3

class NumCourtsBoundaryOddTeam3s4s_29(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 0 
    How many group players? 15

    """

    def runTest(self):
        #comment next 3 lines to keep default value, 0
        #sets select list option for How many doubles players
        #select = Select(self.driver.find_element_by_tag_name("select"))
        #select.select_by_visible_text("0")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("15")

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
            print 'Test29 3\'s court results passed'
        except AssertionError as e:
            print 'Test29 expected court results not found: ', e
        #finally:
            #print 'is this necessary?'
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element4 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test29 4\'s court results passed'
        except AssertionError as e:
            print 'Test29 expected court results not found: ', e 
        try:
            element3 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element3.text)
            print 'Test29 extra players passed'
        except AssertionError as e2:
            print 'Test29 expected extra results not found: ', e2

class NumCourtsBoundaryOddTeam2s3s4s_30(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 4 
    How many group players? 15

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("4")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("15")

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
            print 'Test30 2\'s court results passed'
        except AssertionError as e:
            print 'Test30 expected court results not found: ', e
 
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test30 3\'s court results passed'
        except AssertionError as e2:
            print 'Test30 expected court results not found: ', e2

        try:
            element5 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element6 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element6.text)
            print 'Test30 4\'s court results passed'
        except AssertionError as e:
            print 'Test30 expected court results not found: ', e 

        try:
            element7 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element7.text)
            print 'Test30 extra players passed'
        except AssertionError as e2:
            print 'Test30 expected extra results not found: ', e2

class NumCourtsBoundaryOddTeam2s3s4s_31(VBCourtsPassFF):
    """Tests a simple case that should pass.
    How many doubles players? 12 
    How many group players? 15

    """

    def runTest(self):
        #sets select list option for How many doubles players
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("12")

        #sets select list option for How many group players
        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("15")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        try:
            self.driver.implicitly_wait(5)
            self.driver.implicitly_wait(0);
            element = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results2")))
            element2 = self.driver.find_element_by_id("crt_results2")
            strCourtResults = "3 courts for 2\'s"
            self.assertTrue(strCourtResults in element2.text)
            print 'Test31 2\'s court results passed'
        except AssertionError as e:
            print 'Test31 expected court results not found: ', e
 
        try:
            element3 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results3")))
            element4 = self.driver.find_element_by_id("crt_results3")
            strCourtResults = "1 court for 3\'s"
            self.assertTrue(strCourtResults in element4.text)
            print 'Test31 3\'s court results passed'
        except AssertionError as e2:
            print 'Test31 expected court results not found: ', e2

        try:
            element5 = WebDriverWait(self.driver, 13).until(EC.presence_of_element_located((By.ID, "crt_results4")))
            element6 = self.driver.find_element_by_id("crt_results4")
            strCourtResults = "1 court for 4\'s"
            self.assertTrue(strCourtResults in element6.text)
            print 'Test31 4\'s court results passed'
        except AssertionError as e:
            print 'Test31 expected court results not found: ', e 

        try:
            element7 = self.driver.find_element_by_id("crt_results5")
            self.assertTrue(self.str_extra in element7.text)
            print 'Test31 extra players passed'
        except AssertionError as e2:
            print 'Test31 expected extra results not found: ', e2
 
if __name__ == '__main__':
    unittest.main()         
