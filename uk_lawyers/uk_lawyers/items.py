# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

class UkLawyersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def extract_address(value):
    if len(value) > 0:
        # Filter out empty strings and whitespace from the list
        value = [line.strip() for line in value if line.strip()]
        if value:
            # The address should be the last non-empty string in the list
            address = value[-1]
            return address
        else:
            return None
    else:
        return None

def extract_date(value):
    if len(value) > 0:
        # Split the string by ':'
        parts = value[0].split(':')
        if len(parts) > 1:
            # Get the last part after splitting
            date_part = parts[-1].strip()
            return date_part
        else:
            return None
    else:
        return None
    
def concatenate_values(value):
    if len(value) > 0:
        # Filter out empty strings and whitespace
        cleaned_values = [v.strip() for v in value if v.strip()]
        # Join the cleaned values with a comma
        concatenated_value = ', '.join(cleaned_values)
        return concatenated_value
    else:
        return None

class LawyerItem(scrapy.Item):
    Name = scrapy.Field(default=None)
    Sra_id = scrapy.Field(default=None, output_processor = TakeFirst())
    Phone = scrapy.Field(default=None, output_processor = TakeFirst())
    Email = scrapy.Field(default=None)
    Org_name = scrapy.Field(default=None)
    Org_addr = scrapy.Field(default=None, input_processor = Compose(extract_address))
    Position = scrapy.Field(default=None)
    Date = scrapy.Field(default=None, input_processor = Compose(extract_date))
    Area_Of_Practice = scrapy.Field(default=None, input_processor = Compose(concatenate_values))
    Url = scrapy.Field(default=None)
