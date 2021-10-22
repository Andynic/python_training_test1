from selenium import webdriver
class Contact_add:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def logout(self):
            # logout
            wd = self.wd
            wd.find_element_by_link_text("Logout").click()

    def fill_contact_firm(self,contacts):
            # fill contact firm
            wd = self.wd
            wd.find_element_by_xpath("//div[@id='content']/form/label[3]").click()
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contacts.firstname)
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contacts.middlename)
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contacts.lastname)
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contacts.nickname)
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contacts.title)
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contacts.phone_home)
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contacts.mobile)
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contacts.phone_work)
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contacts.fax)
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contacts.email)
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contacts.byear)
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contacts.ayear)
            wd.find_element_by_name("theform").click()
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(contacts.address2)
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contacts.phone2)
            wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

        def login(self, username, password):
            # login
            wd = self.wd
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_xpath("//input[@value='Login']").click()

        def open_create_page(self):
            # open create page
            wd = self.wd
            wd.get("http://localhost/addressbook/edit.php")

        def destroy(self):
            self.wd.quit()
