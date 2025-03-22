import pytest
import logging
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage

logging.basicConfig(level=logging.INFO)

@pytest.mark.parametrize("src_local_region, target_region_name, region_url_part, region_title", [
    ("Республика Татарстан", "Камчатский край", "kamchatskij-kraj", "Saby Контакты — Камчатский край"),
], ids=["Tatarstan -> Kamchatka"])
def test_functionality_of_change_region(driver, src_local_region, target_region_name, region_url_part, region_title):
    main_page = MainPage(driver)

    logging.info("Открываем главную страницу СБИС")
    main_page.open("https://sbis.ru/")

    logging.info("Переходим в раздел 'Контакты'")
    main_page.go_to_contacts()

    contacts_page = ContactsPage(driver)
    local_region = contacts_page.get_region()
    local_partners = contacts_page.get_partners_list()

    logging.info(f"Текущий регион: {local_region}")
    logging.info(f"Количество партнеров: {len(local_partners)}")

    assert local_region == src_local_region, "Неверный регион"
    assert len(local_partners) > 0, 'Партнеры для данного региона не найдены'

    contacts_page.change_region(target_region_name)
    contacts_page.wait_for_page_load(region_url_part, region_title)

    new_region = contacts_page.get_region()

    assert new_region == target_region_name, f"Регион после изменения неверный: {new_region}"

    new_partners = contacts_page.get_partners_list()

    logging.info(f"Новый регион: {new_region}")
    logging.info(f"Количество партнеров после смены региона: {len(new_partners)}")

    assert len(new_partners) > 0, "Список партнеров пуст!"
    assert local_partners != new_partners, "Список партнеров не изменился!"
