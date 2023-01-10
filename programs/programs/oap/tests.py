from django.test import TestCase
from programs.programs.oap.oap import OldAge
from screener.models import Screen, HouseholdMember, IncomeStream


class TestOldAgePension(TestCase):
    def setUp(self):
        self.screen1 = Screen.objects.create(
            agree_to_tos=True,
            zipcode='80205',
            county='Denver County',
            household_size=2,
            household_assets=0,
            has_tanf=False,
            has_ssi=False
        )
        self.person1 = HouseholdMember.objects.create(
            screen=self.screen1,
            relationship='headOfHousehold',
            age=60,
            student=False,
            student_full_time=False,
            pregnant=False,
            unemployed=False,
            worked_in_last_18_mos=True,
            visually_impaired=False,
            disabled=False,
            veteran=False,
            has_income=False,
            has_expenses=False,
        )

    def test_oap_visualy_impaired_is_eligible(self):
        oap = OldAge(self.screen1)
        eligibility = oap.eligibility

        self.assertTrue(eligibility["eligible"])

    def test_oap_failed_all_conditions(self):
        self.screen1.has_ssi = True
        self.screen1.has_tanf = True
        self.screen1.household_assets = 2000
        self.screen1.save()
        self.person1.age = 30
        self.person1.save()

        oap = OldAge(self.screen1)
        eligibility = oap.eligibility

        self.assertFalse(eligibility["eligible"])

    def test_oap_failed_income_condition(self):
        income = IncomeStream.objects.create(
            screen=self.screen1,
            household_member=self.person1,
            type='wages',
            amount=2000,
            frequency='monthly'
        )
        oap = OldAge(self.screen1)
        eligibility = oap.eligibility

        self.assertFalse(eligibility["eligible"])
