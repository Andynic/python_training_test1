import pytest
from contacts import Contact
from contact import Contact_add


@pytest.fixture
def app(request):
    fixture = Contact_add()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contacts(app):
    app.open_create_page()
    app.login(username="admin", password="secret")
    app.fill_contact_firm(Contact(firstname="Test", middlename="test1", lastname="test2", nickname="test3",
                                           title="test4", phone_home="495590", mobile="1111111", phone_work="7890",
                                           fax="222222",
                                           email="t@t.ru", byear="1989", ayear="1989", address2="Moscow",
                                           phone2="54321"))
    app.logout()






