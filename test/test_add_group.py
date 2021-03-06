from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="group1", header="group1", footer="group1"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="", header="", footer=""))
    app.session.logout()
