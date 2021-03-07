
import pytest

def format_data_for_display(people):
    return ["{} {}: {}".format(p["given_name"], p["family_name"], p["title"]) for p in people]

def format_data_for_excel(people):
    header = "given,family,title"
    body = [",".join(p.values()) for p in people]
    body = "\n".join(body)
    return header + "\n" + body

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) =="""given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager"""
