from database import BaseModel
from peewee import *

class Donation(BaseModel):
    amount = IntegerField(verbose_name="Amount")
    first_name = CharField(64, verbose_name="First name")
    last_name = CharField(64, verbose_name="Last name")
    street_address = CharField(128, verbose_name="Address")
    city = CharField(64, verbose_name="City")
    state = CharField(2, verbose_name="State code")
    postal_code = CharField(5, verbose_name="ZIP code")
    email = CharField(64, verbose_name="Email address")
    occupation = CharField(64, default="", verbose_name="Occupation")
    employer = CharField(64, default="", verbose_name="Employer")
    recurring = BooleanField(default=False, verbose_name="Recurring Donation")
    agreed = BooleanField(default=True, verbose_name="Agree to Conditions")
    stripe_success = BooleanField(default=False, verbose_name="Charge successful")
