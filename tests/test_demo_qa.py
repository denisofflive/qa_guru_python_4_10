from demo_qa import registration_form


def test_fill_fields(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    registration_page.open()
    registration_page.fill_first_name('Denis')
    registration_page.fill_last_name('Denisov')
    registration_page.fill_email('denisofflive@mail.ru')
    registration_page.fill_date_of_birth('15', 'March', '1985')
    registration_page.gender('Male')
    registration_page.type_phone('79776136665')
    registration_page.select_subjects('Maths')
    registration_page.select_hobbies('Music')
    registration_page.upload_picture()
    registration_page.fill_current_address('Moscow')
    registration_page.select_state('NCR')
    registration_page.select_city('Noida')

    registration_page.click_submit()

    # THEN
    registration_page.assert_registred_user_info(
        'Denis Denisov',
        'denisofflive@mail.ru',
        'Male',
        '79776136665',
        '15 March,1985',
        'Maths',
        'Music',
        'picture.jpg',
        'Moscow',
        'NCR Noida'
    )
