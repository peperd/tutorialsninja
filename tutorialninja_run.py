from test import Test001

with Test001() as bot:
    bot.test_add_to_shopping_cart()
    bot.test_delete_from_shopping_cart()
    bot.test_my_account_register()
    bot.test_login()
    bot.test_broken_links_main_page()
