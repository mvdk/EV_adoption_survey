from otree.api import *

author = 'Mart van der Kam & Anne Günther'

class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.session.config['language'] == 'de':
        from .lexicon_de import Lexicon
        subsession.session.myLangCode = "_de"
    elif subsession.session.config['language'] == 'sa':
        from .lexicon_sa import Lexicon
        subsession.session.myLangCode = "_sa"
    else:
        from .lexicon_usa import Lexicon
        subsession.session.myLangCode = "_usa"
    subsession.session.demographicsLexi = Lexicon


class Group(BaseGroup):
    pass


def make_likert10():
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelect,
    )


def education_choices(player):
    Lexicon = player.session.demographicsLexi
    if player.session.config['language'] == 'de':
        education_choices = [
            ["1", Lexicon.education_DE_1],
            ["2", Lexicon.education_DE_2],
            ["3", Lexicon.education_DE_3],
            ["4", Lexicon.education_DE_4],
            ["5", Lexicon.education_DE_5],
            ["6", Lexicon.education_DE_6],
            ["7", Lexicon.education_DE_7],
            ["8", Lexicon.education_DE_8],
            ["9", Lexicon.education_DE_9],
            ["10", Lexicon.education_DE_10],
            ["11", Lexicon.education_DE_11]
        ]
    else:
        education_choices = [
            ["none", Lexicon.none],
            ["obligatory", Lexicon.obligatory],
            ["high_school", Lexicon.high_school],
            ["college", Lexicon.college],
            ["university", Lexicon.university],
            ["doctor", Lexicon.doctor]
        ]

    return education_choices


def gender_choices(player):
    Lexicon = player.session.demographicsLexi
    gender_choices = [
        ["female", Lexicon.female],
        ["male", Lexicon.male],
        ["other", Lexicon.other],
        ["notsay", Lexicon.notsay]
    ]
    return gender_choices


def region_choices(player):
    Lexicon = player.session.demographicsLexi
    region_choices = [
        ["urban", Lexicon.urban],
        ["suburban", Lexicon.suburban],
        ["rural", Lexicon.rural]
    ]
    return region_choices


def income_choices(player):
    Lexicon = player.session.demographicsLexi
    income_choices = [
        ["1", Lexicon.income_quintile1],
        ["2", Lexicon.income_quintile2],
        ["3", Lexicon.income_quintile3],
        ["4", Lexicon.income_quintile4],
        ["5", Lexicon.income_quintile5]
    ]
    return income_choices

def attention_check_1_choices(player):
    Lexicon = player.session.demographicsLexi
    attention_check_1_choices = [
        ["Ford", Lexicon.ford],
        ["Volkswagen", Lexicon.volkswagen],
        ["Mercedes", Lexicon.mercedes],
        ["Toyota", Lexicon.toyota],
        ["Subaru", Lexicon.subaru],
        ]
    return attention_check_1_choices

def own_car_choices(player):
    Lexicon = player.session.demographicsLexi
    own_car_choices = [
        ["yes", Lexicon.yes],
        ["no", Lexicon.no]
    ]
    return own_car_choices

def car_type_choices(player):
    Lexicon = player.session.demographicsLexi
    car_type_choices = [
        ["gasoline", Lexicon.gasoline],
        ["diesel", Lexicon.diesel],
        ["ev", Lexicon.ev],
        ["hev", Lexicon.hev]
    ]
    return car_type_choices

def car_size_choices(player):
    Lexicon = player.session.demographicsLexi
    car_size_choices = [
        ["small", Lexicon.small],
        ["medium", Lexicon.medium],
        ["large", Lexicon.large]
    ]
    return car_size_choices

def car_size_future_choices(player):
    Lexicon = player.session.demographicsLexi
    car_size_future_choices = [
        ["small", Lexicon.small],
        ["medium", Lexicon.medium],
        ["large", Lexicon.large]
    ]
    return car_size_future_choices

def car_type_future_choices(player):
    Lexicon = player.session.demographicsLexi
    car_size_future_choices = [
        ["new_only", Lexicon.new_only],
        ["preowned_only", Lexicon.preowned_only],
        ["new_preowned", Lexicon.new_preowned]
    ]
    return car_size_future_choices

def own_car_future_choices(player):
    Lexicon = player.session.demographicsLexi
    own_car_future_choices = [
        ["yes", Lexicon.yes],
        ["no", Lexicon.no]
    ]
    return own_car_future_choices



class Player(BasePlayer):

    # Demographics
    age = models.IntegerField(min=1, max=99)
    gender = models.StringField(widget=widgets.RadioSelect,)
    education = models.StringField(widget=widgets.RadioSelect,)
    income = models.StringField(widget=widgets.RadioSelect,)
    household = models.IntegerField(min=1, max=12)
    region = models.StringField(widget=widgets.RadioSelect,)
    zip_code = models.StringField(blank=True)
    attention_check_1 = models.StringField(widget=widgets.RadioSelect,)

    # Car_questions
    own_car = models.StringField(widget=widgets.RadioSelect,)
    own_car_future = models.StringField(widget=widgets.RadioSelect,)

    # car_owner
    car_type = models.StringField(widget=widgets.RadioSelect,)
    car_size = models.StringField(widget=widgets.RadioSelect,)
    car_number = models.IntegerField(min=1, max=8)
    km_day = models.IntegerField(min=0, max=1000)
    km_year = models.IntegerField(min=0, max=100000)
    car_age = models.IntegerField(min=1, max=30)
    car_replace = models.IntegerField(min=1, max=20)
    car_size_future = models.StringField(widget=widgets.RadioSelect,)
    car_type_future = models.StringField(widget=widgets.RadioSelect,)

    # no_car_owner
    own_car_future = models.StringField(widget=widgets.RadioSelect,)

    # affect
    affect_ev = make_likert10()
    affect_ice = make_likert10()


# Demographics Page class
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'income', 'household', 'region', 'zip_code','attention_check_1']

    @staticmethod
    def error_message(player: Player, values):
        Lexicon = player.session.demographicsLexi
        if values['age'] < 18:
            return Lexicon.age_error_label

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['age', 'gender', 'education', 'income', 'household', 'region', 'zip_code','attention_check_1'],
            form_field_labels=[Lexicon.age_label, Lexicon.gender_label, Lexicon.education_label,
                               Lexicon.income_label, Lexicon.household_label, Lexicon.region_label,
                               Lexicon.zip_code_label,Lexicon.attention_check_1_label],
        )


class Car_questions(Page):
    form_model = 'player'
    form_fields = ['own_car']

    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['own_car'] = player.own_car

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['own_car'],
            form_field_labels=[Lexicon.own_car_label]
        )


class car_owner(Page):
    form_model = 'player'
    form_fields = ['car_number', 'car_type', 'car_size','km_day', 'km_year', 'car_age', 'car_replace', 'car_size_future',  'car_type_future']

    def is_displayed(player):
        return player.participant.vars['own_car'] == 'yes'
    
    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['car_size_future'] = player.car_size_future

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['car_number', 'car_type', 'car_size','km_day', 'km_year', 'car_age', 'car_replace', 'car_size_future',  'car_type_future'],
            form_field_labels=[Lexicon.car_number_label, Lexicon.car_type_label, Lexicon.car_size_label,Lexicon.km_day_label, Lexicon.km_year_label,
                               Lexicon.car_age_label, Lexicon.car_replace_label,Lexicon.car_size_future_label,Lexicon.car_type_future_label]
        )


class no_car_owner(Page):
    form_model = 'player'
    form_fields = ['own_car_future']

    def is_displayed(player):
        return player.participant.vars['own_car'] == 'no'
    
    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['own_car_future'] = player.own_car_future
        if player.participant.vars['own_car_future'] == 'no':
            player.participant.vars['car_size_future'] = 'none'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['own_car_future'],
            form_field_labels=[Lexicon.own_car_future_label]
        )
    
class future_car_owner(Page):
    form_model = 'player'
    form_fields = ['car_size_future',  'car_type_future']

    def is_displayed(player):
        return player.participant.vars['own_car'] == 'no' and player.participant.vars['own_car_future'] == 'yes'
    
    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['car_size_future'] = player.car_size_future

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['car_size_future',  'car_type_future'],
            form_field_labels=[Lexicon.car_size_future_label, Lexicon.car_type_future_label]
        )

class affect(Page):
    form_model = 'player'
    form_fields = ['affect_ev','affect_ice']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)  

class pre_transition(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

# Page sequence
page_sequence = [
    Demographics,
    Car_questions,
    car_owner,
    no_car_owner,
    future_car_owner,
    affect,
    pre_transition
]
