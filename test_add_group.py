from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group
from contacts import Contacts

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="group1", header="group1", footer="group1"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_to_groups_page(wd)
        self.logout(wd)



    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    class test_add_contacts(unittest.TestCase):
        def setUp(self):
            self.wd = webdriver.Firefox()
            self.wd.implicitly_wait(30)

        def test_add_contacts(self):
            wd = self.wd
            self.open_add_new_page(wd)
            self.login_2(wd, username="admin", password="secret")
            self.fill_contacts_firm(wd, Contacts("Test", "test1", "test2", "test3", "test4", "test5", "1111111", "facebook",
                                    "222222", "t@t.ru", "8", "August", "1989", "10", "October", "1989", "Moscow",
                                    "Moscow"))
            self.logout_2(wd)

        def logout_2(self, wd):
            # logout 2
            wd.find_element_by_link_text("Logout").click()

        def fill_contacts_firm(self, wd, contacts):
            # fill contacts firm
            wd.find_element_by_xpath("//div[@id='content']/form/label[3]").click()
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contacts.firstname)
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contacts.middlename)
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contacts.contacts.lastname)
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contacts.nickname)
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contacts.title)
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contacts.home)
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contacts.mobile)
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contacts.work)
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contacts.fax)
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contacts.email)
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contacts.bday)
            wd.find_element_by_xpath("//option[@value='8']").click()
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contacts.bmonth)
            wd.find_element_by_xpath("//option[@value='August']").click()
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contacts.byear)
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contacts.aday)
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[12]").click()
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contacts.amonth)
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[11]").click()
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contacts.ayear)
            wd.find_element_by_name("theform").click()
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(contacts.adress2)
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contacts.phone2)
            wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

        def login_2(self, wd, username, pasword):
            # login 2
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(pasword)
            wd.find_element_by_xpath("//input[@value='Login']").click()

        def open_add_new_page(self, wd):
            # open add new page
            wd.get("http://localhost/addressbook/edit.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
