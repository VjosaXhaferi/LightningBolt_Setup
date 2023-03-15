import random
import string


class Personnel:
    url = "https://s2.usw2.qa.lightning-bolt.com/Setup.aspx?page=personnel"
    LastName = "Adams"
    FirstName = "Ken"
    # DisplayNameGenerator = random.choices(string.ascii_lowercase, k=5)
    # DisplayName = ''.join(DisplayNameGenerator)
    DisplayName = "Ken Adams"
    CompactName = random.choices(string.ascii_lowercase, k=5)


