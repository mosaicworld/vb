from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
import unittest

class VBRandomVisualFF001_010(unittest.TestCase):
    #testing on firefox

    def setUp(self):
        self.lst_doubles = ['0', '4', '8', '12', '16']
        self.lst_group = ['0', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',\
         '21', '22', '23', '24', '25']
        self.str_extra = "There will be 1 extra player to manually assign to teams."
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(480, 800);
        file = "http://www.carolchung.com/vb"
        #file = "file://localhost/programming/mywebapp/vb/index.html"
        self.driver.get(file)

    #def is_text_present(self, string):
        #if str(string) in self.driver.page_source: return True
        #else: return False

    #def tearDown(self):
        #self.driver.quit()

class NumCourts001(VBRandomVisualFF001_010):    

    def runTest(self):
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text("0")

        select2 = Select(self.driver.find_element_by_id("NumGroupPlayers"))
        select2.select_by_visible_text("0")

        #click button Get Number of Courts
        btnNumCourts = self.driver.find_element_by_id("btnNumSizeCourt")
        btnNumCourts.click()
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()

class NumCourts002(VBRandomVisualFF001_010):    

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
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()   

class NumCourts003(VBRandomVisualFF001_010):    

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
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()

class NumCourts004(VBRandomVisualFF001_010):    

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
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()

class NumCourts005(VBRandomVisualFF001_010):    

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
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()

class NumCourts006(VBRandomVisualFF001_010):    

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
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()

class NumCourts007(VBRandomVisualFF001_010):    

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
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()

class NumCourts008(VBRandomVisualFF001_010):    

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
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()

class NumCourts009(VBRandomVisualFF001_010):    

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
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()

class NumCourts010(VBRandomVisualFF001_010):    

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
        self.driver.implicitly_wait(15)

        #click button Get random teams
        btnRdmTeams = self.driver.find_element_by_id("btnRandomGroup")
        btnRdmTeams.click()

if __name__ == '__main__':
    unittest.main()         