import fire
import util


SafeTextRegex = "^[a-zA-Z0-9 .-]+$"
SQLRegex = ".*(drop table|update|select|insert|delete|from|count\(| truncate|asc\(|mid\(|char\(|xp_cmdshell|exec master|:|net user|’|or|and|1=1|).*"
URLRegex = "^((((https?|ftps?|gopher|telnet|nntp)://)|(mailto:|news:))(%[0-9A-Fa-f]{2}|[-()_.!~*';/?:@&=+$,A-Za-z0-9])+)([).!';/?:,][[:blank:|:blank:]])?$"
IPRegex = "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
EmailRegex = "^[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}$"
CreditCardNumRegex = "^((4\d{3})|(5[1-5]\d{2})|(6011)|(7\d{3}))-?\d{4}-?\d{4}-?\d{4}|3[4,7]\d{13}$"
USZipRegex = "^\d{5}(-\d{4})?$"
USPhoneRegex = "^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$"
SSNRegex = "^\d{3}-\d{2}-\d{4}$"


def safe_text(input:str, min=1, max=200):
    if util.lenInRange(min, max, input) and util.isMatch(SafeTextRegex, input):
        print("{0} is valid safe text".format(input))
        return True
    else:
        print("{0} is invalid safe text".format(input))
        return False


def sql(input:str, min=0, max=1024):
    if util.lenInRange(min, max, input) and not util.isMatch(SQLRegex, input) or input == "":
        print("{0} is a valid sql query".format(input))
        return True
    else:
        print("{0} is a potential sql injection attack".format(input))
        return False


def url(input:str, min=2, max=2048):
    if util.lenInRange(min, max, input) and util.isMatch(URLRegex, input):
        print("{0} is a valid url".format(input))
        return True
    else:
        print("{0} is a invalid url".format(input))
        return False


def ip(input:str, min=7, max=15):
    if util.lenInRange(min, max, input) and util.isMatch(IPRegex, input):
        print("{0} is a valid ip address".format(input))
        return True
    else:
        print("{0} is a invalid ip address".format(input))
        return False


def email(input:str, min=3, max=320):
    if util.lenInRange(min, max, input) and util.isMatch(EmailRegex, input):
        print("{0} is a valid email".format(input))
        return True
    else:
        print("{0} is a invalid email".format(input))
        return False


def credit_card_number(input:str, min=13, max=19):
    if util.lenInRange(min, max, input) and util.isMatch(CreditCardNumRegex, input):
        print("{0} is a valid credit card number".format(input))
        return True
    else:
        print("{0} is a invalid credit card number".format(input))
        return False


def zip(input:str, min=5, max=10):
    if util.lenInRange(min, max, input) and util.isMatch(USZipRegex, input):
        print("{0} is a valid US zip code".format(input))
        return True
    else:
        print("{0} is a invalid US zip code".format(input))
        return False


def phone(input:str, min=4, max=13):
    if util.lenInRange(min, max, input) and util.isMatch(USPhoneRegex, input):
        print("{0} is a valid US phone number".format(input))
        return True
    else:
        print("{0} is a invalid US phone number".format(input))
        return False


def ssn(input:str, min=11, max=11):
    if util.lenInRange(min, max, input) and util.isMatch(SSNRegex, input):
        print("{0} is a valid social security number".format(input))
        return True
    else:
        print("{0} is a invalid social security number".format(input))
        return False


if __name__ == '__main__':
  fire.Fire()