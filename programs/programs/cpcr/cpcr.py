from django.db.models import Q


def calculate_property_credit_rebate(screen, data):
    cpcr = PropertyCreditRebate(screen)
    eligibility = cpcr.eligibility
    value = cpcr.value

    calculation = {
        'eligibility': eligibility,
        'value': value
    }

    return calculation


class PropertyCreditRebate():
    amount = 976
    min_age = 65
    income_limit = {"single": 15831, "married": 21381}

    def __init__(self, screen):
        self.screen = screen

        self.eligibility = {
            "eligible": True,
            "passed": [],
            "failed": []
        }

        self.calc_eligibility()

        self.calc_value()

    def calc_eligibility(self):
        # Someone is disabled
        people_disabled = self.screen.household_members.filter(Q(disabled=True) | Q(visually_impaired=True))
        someone_disabled = len(people_disabled) >= 1

        # Someone is old enough
        someone_old_enough = self.screen.num_adults(age_max=65) >= 1

        self._condition(someone_disabled or someone_old_enough,
                        f"Someone in the household must be disabled or over the age of {PropertyCreditRebate.min_age}")

        # Income test
        relationship_status = 'single'
        for member_id, married_to in self.screen.relationship_map().items():
            if married_to is not None:
                relationship_status = 'married'

        gross_income = self.screen.calc_gross_income('yearly', ['all'])
        self._condition(gross_income <= PropertyCreditRebate.income_limit[relationship_status],
                        f"Gross annual income must be less than {PropertyCreditRebate.income_limit[relationship_status]}")

    def calc_value(self):
        self.value = PropertyCreditRebate.amount

    def _failed(self, msg):
        self.eligibility["eligible"] = False
        self.eligibility["failed"].append(msg)

    def _passed(self, msg):
        self.eligibility["passed"].append(msg)

    def _condition(self, condition, msg):
        if condition is True:
            self._passed(msg)
        else:
            self._failed(msg)
