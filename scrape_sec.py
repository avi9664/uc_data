# to run this you need to pip install secedgar

from secedgar import filings

my_filings = filings(cik_lookup='0000315054',
                     user_agent="[email address]")

# easy access to methods shared across all 4 different filing classes
my_filings_urls = my_filings.get_urls()
my_filings.save("/")