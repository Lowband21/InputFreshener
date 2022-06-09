import unittest
import freshener

class Testfreshener(unittest.TestCase):
    def test_safe_text(self):
        self.assertTrue(freshener.safe_text("Some text with numbers123"))
        self.assertTrue(freshener.safe_text("A long string with lots of characters. I will have to count these. Ill probably just use the len function in the python interpreter. I was short so now Im typing about 50 more words and 12345678901"))
        self.assertFalse(freshener.safe_text("This - won't * work"))
        self.assertFalse(freshener.safe_text("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    def test_sql(self):
        self.assertFalse(freshener.sql("SELECT * from userstable"))
        self.assertFalse(freshener.sql("*"))
        self.assertFalse(freshener.sql("user' or 1=1--"))
        self.assertFalse(freshener.sql(" ' or ''='"))
        self.assertFalse(freshener.sql("CAST('smartbear' AS SIGNED INTEGER)"))
        self.assertTrue(freshener.sql(""))
    def test_url(self):
        self.assertTrue(freshener.url("https://www.google.com/"))
        self.assertTrue(freshener.url("https://canvas.du.edu/courses/137501"))
        self.assertFalse(freshener.url("`"))
        self.assertFalse(freshener.url("com.goog,https"))
    def test_ip(self):
        self.assertTrue(freshener.ip("192.168.0.0"))
        self.assertTrue(freshener.ip("255.255.255.255"))
        self.assertFalse(freshener.ip("400.440.230.1000"))
        self.assertFalse(freshener.ip("1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"))
    def test_email(self):
        self.assertTrue(freshener.email("johndoe@gmail.com"))
        self.assertTrue(freshener.email("miles.ji._.ji@fosije.lom"))
        self.assertFalse(freshener.email("JI!@gma.ji"))
        self.assertFalse(freshener.email("!@#$%^&*"))
    def test_credit_card_number(self):
        self.assertTrue(freshener.credit_card_number("5105105105105100"))
        self.assertTrue(freshener.credit_card_number("4111111111111111"))
        self.assertFalse(freshener.credit_card_number("This is not a num"))
        self.assertFalse(freshener.credit_card_number("149875293841093840192840193801938019823"))
    def test_zip(self):
        self.assertTrue(freshener.zip("46545"))
        self.assertTrue(freshener.zip("38539-4839"))
        self.assertFalse(freshener.zip("Not a num"))
        self.assertFalse(freshener.zip("019348203985209385209384"))
    def test_phone(self):
        self.assertTrue(freshener.phone("582-284-2389"))
        self.assertTrue(freshener.phone("111-111-1111"))
        self.assertFalse(freshener.phone("Not a num"))
        self.assertFalse(freshener.phone("019248198732987140998429"))
    def test_ssn(self):
        self.assertTrue(freshener.ssn("238-53-9539"))
        self.assertTrue(freshener.ssn("999-99-9999"))
        self.assertFalse(freshener.ssn("Not a num"))
        self.assertFalse(freshener.ssn("101010101010101010101010101010101010101010101010101010101010101010"))


if __name__ == '__main__':
    unittest.main()