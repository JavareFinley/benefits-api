from screener.models import Screen
from programs.models import FederalPoveryLimit
from programs.util import Dependencies
from .eoc_income_limits import eoc_income_limits


class UrgentNeedFunction():
    dependencies = []

    @classmethod
    def calc(cls, screen: Screen, missing_dependencies: Dependencies):
        if not cls.can_calc(missing_dependencies):
            return False

        return cls.eligible(screen)

    @classmethod
    def eligible(cls, screen: Screen):
        return True

    @classmethod
    def can_calc(cls, missing_dependencies: Dependencies):
        if missing_dependencies.has(*cls.dependencies):
            return False

        return True


class LivesInDenver(UrgentNeedFunction):
    dependencies = ['county']

    @classmethod
    def eligible(cls, screen: Screen):
        '''
        Household lives in the Denver County
        '''
        return screen.county == 'Denver County'


class HelpkitchenZipcode(UrgentNeedFunction):
    dependencies = ['zipcode']

    @classmethod
    def eligible(cls, screen: Screen):
        '''
        Lives in a zipcode that is eligible for HelpKitchen
        '''
        zipcodes = [
            '80010',
            '80011',
            '80012',
            '80013',
            '80014',
            '80015',
            '80016',
            '80017',
            '80018',
            '80019',
            '80045',
            '80102',
            '80112',
            '80137',
            '80138',
            '80230',
            '80231',
            '80238',
            '80247',
            '80249',
        ]
        return screen.zipcode in zipcodes


class Child(UrgentNeedFunction):
    dependencies = ['age']

    @classmethod
    def eligible(cls, screen: Screen):
        '''
        Return True if someone is younger than 18
        '''
        return screen.num_children(child_relationship=['all']) >= 1


class BiaFoodDelivery(UrgentNeedFunction):
    dependencies = ['county']

    @classmethod
    def eligible(cls, screen: Screen):
        '''
        Return True if in Adams, Arapahoe, Denver or Jefferson county
        '''
        eligible_counties = [
            'Adams County',
            'Arapahoe County',
            'Denver County',
            'Jefferson County',
        ]
        return screen.county in eligible_counties


class Trua(UrgentNeedFunction):
    dependencies = ['household_size', 'income_amount', 'income_frequency']

    @classmethod
    def eligible(cls, screen: Screen):
        '''
        Return True if the household is below the income limit for their household size
        '''
        income_limits = {
            1: 66_300,
            2: 75_750,
            3: 85_200,
            4: 94_560,
            5: 102_250,
            6: 109_800,
            7: 117_400,
            8: 124_950
        }
        household_income = screen.calc_gross_income('yearly', ['all'])
        income_limit = income_limits[screen.household_size]
        return household_income <= income_limit


class Eoc(UrgentNeedFunction):
    dependencies = ['income_amount', 'income_frequency', 'household_size', 'county']

    @classmethod
    def eligible(cls, screen: Screen):
        '''
        Return True if the household is below the income limit for their county and household size
        '''
        household_income = screen.calc_gross_income('yearly', ['all'])
        if screen.county in eoc_income_limits:
            income_limit = eoc_income_limits[screen.county][screen.household_size]
        else:
            return False
        return household_income <= income_limit


class CoLegalServices(UrgentNeedFunction):
    dependencies = ['income_amount', 'income_frequency', 'household_size', 'age']

    @classmethod
    def eligible(cls, screen: Screen):
        '''
        Return True if the household is has an income bellow 200% FPL or someone in the household is over 60 years old
        '''
        fpl = FederalPoveryLimit.objects.get(year='THIS YEAR').as_dict()
        is_income_eligible = screen.calc_gross_income('yearly', ['all']) < fpl[screen.household_size]
        is_age_eligible = screen.num_adults(age_max=60)
        return is_income_eligible or is_age_eligible
