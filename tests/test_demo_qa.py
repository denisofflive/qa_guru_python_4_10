from demo_qa import registration_form

def test_fill_fields(browser_setup):
    registration_page = registration_form.RegistrationPage()


    # WHEN
    registration_page.open()
    registration_page.fill_first_name('Denis')
    registration_page.fill_last_name('Denisov')
    registration_page.fill_email('denisqaguru@gmail.com')
    registration_page.fill_date_of_birth('15', 'March', '1985')
    registration_page.gender('Male')
    registration_page.type_phone('9776136677')
    registration_page.select_subjects('Maths')
    registration_page.select_hobbies('Music')
    registration_page.upload_picture('picture.jpg')
    registration_page.fill_current_address('Moscow')
    registration_page.select_state('NCR')
    registration_page.select_city('Noida')

    registration_page.click_submit()

    # THEN
    registration_page.assert_registred_user_info(
        'Denis Denisov',
        'denisqaguru@gmail.com',
        'Male',
        '9776136677',
        '15 March,1994',
        'Maths',
        'Music',
        'picture.jpg',
        'Moscow',
        'NCR Noida'
    )
