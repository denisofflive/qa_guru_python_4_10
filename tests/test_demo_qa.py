import allure
from demo_qa import registration_form
from users.users import User, Subjects, Hobbies


student = User(
    first_name='Denis',
    last_name="Denisov",
    email='denisqaguru@gmail.com',
    day_of_birth='15',
    month_of_birth='March',
    year_of_birth='1985',
    gender='Male',
    phone_number='9776136677',
    subjects=[Subjects.maths.value, Subjects.biology.value],
    hobbies=[Hobbies.Music.value, Hobbies.Sports.value],
    name_picture='picture.jpg',
    adress='Moscow',
    state='NCR',
    city='Noida',
)


@allure.title('Register user')
def test_fill_fields(browser_setup):
    registration_page = registration_form.RegistrationPage(browser_setup)

    # WHEN
    with allure.step('Open the page'):
        registration_page.open_page_autoform()
    with allure.step('Filling user data'):
        registration_page.register(student)
    with allure.step('Submit'):
        registration_page.click_submit()
    # THEN
    registration_page.assert_registred_user(student)
