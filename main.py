import phonenumbers
from test import number

from phonenumbers import geocoder

ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))

from phonenumbers import timezone

gb_number=phonenumbers.parse(number,"GB")
print(timezone.time_zones_for_geographical_number(gb_number))

text="Contact us at +254745638455 or +254739063461"
num=phonenumbers.PhoneNumberMatcher(text,"IN")

for numbs in num:
    print(numbs)

phone=phonenumbers.parse(number)
valid=phonenumbers.is_valid_number(phone)
possible=phonenumbers.is_possible_number(phone)
print(valid)
print(possible)