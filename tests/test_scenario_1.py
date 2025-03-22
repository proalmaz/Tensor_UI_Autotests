from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage
from pages.about_page import AboutPage

def test_compare_img_sizes(driver):
    main_page = MainPage(driver)
    main_page.open("https://sbis.ru/")

    main_page.go_to_contacts()

    contacts_page = ContactsPage(driver)
    contacts_page.click_tensor_banner()

    tensor_page = TensorPage(driver)

    assert "https://tensor.ru/" == driver.current_url, "Переход на tensor.ru не произошел"
    assert tensor_page.check_power_in_people_block(), "Блок 'Сила в людях' не найден"

    tensor_page.click_about()

    assert "https://tensor.ru/about" == driver.current_url, "Не удалось перейти в 'Подробнее'"

    about_page = AboutPage(driver)

    assert about_page.check_images_size(), "Изображения в блоке 'Работаем' имеют разный размер!"
