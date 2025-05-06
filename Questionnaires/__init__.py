import random
from otree.api import *



class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
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
    subsession.session.questionnairesLexi = Lexicon


def make_likert6():
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6],
        widget=widgets.RadioSelect,
    )


def make_likert10():
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelect,
    )

def comprehension_question_choices(player):
    Lexicon = player.session.questionnairesLexi
    comprehension_question_choices = [
        ["1", Lexicon.comprehension_answer_1],
        ["2", Lexicon.comprehension_answer_2],
        ["3", Lexicon.comprehension_answer_3],
        ["4", Lexicon.comprehension_answer_4],
        ]
    return comprehension_question_choices

def environmental_attitude_q1_choices(player):
    Lexicon = player.session.questionnairesLexi
    environmental_attitude_q1_choices = [
        ["1", Lexicon.environmental_attitude_q1a1],
        ["2", Lexicon.environmental_attitude_q1a2],
        ["3", Lexicon.environmental_attitude_q1a3],
        ["4", Lexicon.environmental_attitude_q1a4],
        ["5", Lexicon.environmental_attitude_q1a5],
        #["NA", Lexicon.environmental_attitude_q1a6]
    ]
    return environmental_attitude_q1_choices

def environmental_attitude_q2_choices(player):
    Lexicon = player.session.questionnairesLexi
    environmental_attitude_q2_choices = [
        ["1", Lexicon.environmental_attitude_q2a1],
        ["2", Lexicon.environmental_attitude_q2a2],
        ["3", Lexicon.environmental_attitude_q2a3],
        ["4", Lexicon.environmental_attitude_q2a4],
        ["5", Lexicon.environmental_attitude_q2a5],
        ["NA", Lexicon.environmental_attitude_q2a6]
    ]
    return environmental_attitude_q2_choices

def environmental_attitude_q3_choices(player):
    Lexicon = player.session.questionnairesLexi
    environmental_attitude_q3_choices = [
        ["1", Lexicon.environmental_attitude_q3a1],
        ["2", Lexicon.environmental_attitude_q3a2],
        ["3", Lexicon.environmental_attitude_q3a3],
        ["4", Lexicon.environmental_attitude_q3a4],
        ["5", Lexicon.environmental_attitude_q3a5],
        #["NA", Lexicon.environmental_attitude_q3a6]
    ]
    return environmental_attitude_q3_choices

def environmental_attitude_q4_choices(player):
    Lexicon = player.session.questionnairesLexi
    environmental_attitude_q4_choices = [
        ["1", Lexicon.environmental_attitude_q4a1],
        ["2", Lexicon.environmental_attitude_q4a2],
        ["3", Lexicon.environmental_attitude_q4a3],
        ["4", Lexicon.environmental_attitude_q4a4],
        ["5", Lexicon.environmental_attitude_q4a5],
        #["NA", Lexicon.environmental_attitude_q4a6]
    ]
    return environmental_attitude_q4_choices

def attention_check_2_choices(player):
    Lexicon = player.session.questionnairesLexi
    attention_check_2_choices = [
        ["Ford", Lexicon.ford],
        ["Volkswagen", Lexicon.volkswagen],
        ["Mercedes", Lexicon.mercedes],
        ["Toyota", Lexicon.toyota],
        ["Subaru", Lexicon.subaru],
        ]
    return attention_check_2_choices


def trust_in_government_q1_choices(player):
    Lexicon = player.session.questionnairesLexi
    trust_in_government_q1_choices = [
        ["1", Lexicon.trust_in_government_q1a1],
        ["2", Lexicon.trust_in_government_q1a2],
        ["3", Lexicon.trust_in_government_q1a3],
        ["4", Lexicon.trust_in_government_q1a4],
        ["5", Lexicon.trust_in_government_q1a5],
        #["NA", Lexicon.trust_in_government_q1a6]
    ]
    return trust_in_government_q1_choices

def trust_in_government_q2_choices(player):
    Lexicon = player.session.questionnairesLexi
    trust_in_government_q2_choices = [
        ["1", Lexicon.trust_in_government_q2a1],
        ["2", Lexicon.trust_in_government_q2a2],
        ["3", Lexicon.trust_in_government_q2a3],
        ["4", Lexicon.trust_in_government_q2a4],
        ["5", Lexicon.trust_in_government_q2a5],
        #["NA", Lexicon.trust_in_government_q2a6]
    ]
    return trust_in_government_q2_choices

def trust_in_government_q3_choices(player):
    Lexicon = player.session.questionnairesLexi
    trust_in_government_q3_choices = [
        ["1", Lexicon.trust_in_government_q3a1],
        ["2", Lexicon.trust_in_government_q3a2],
        ["3", Lexicon.trust_in_government_q3a3],
        ["4", Lexicon.trust_in_government_q3a4],
        ["5", Lexicon.trust_in_government_q3a5],
        #["NA", Lexicon.trust_in_government_q3a6]
    ]
    return trust_in_government_q3_choices

def trust_in_government_q4_choices(player):
    Lexicon = player.session.questionnairesLexi
    trust_in_government_q4_choices = [
        ["1", Lexicon.trust_in_government_q4a1],
        ["2", Lexicon.trust_in_government_q4a2],
        ["3", Lexicon.trust_in_government_q4a3],
        ["4", Lexicon.trust_in_government_q4a4],
        ["5", Lexicon.trust_in_government_q4a5],
        #["NA", Lexicon.trust_in_government_q4a6]
    ]
    return trust_in_government_q4_choices

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # questionnaire

    comprehension_question = models.StringField(widget=widgets.RadioSelect,)
    attention_check_2 = models.StringField(widget=widgets.RadioSelect,)
    
    risks_pref = make_likert10()
    conservative_liberal = make_likert10()

    environmental_attitude_q1 = models.StringField(widget=widgets.RadioSelect,)
    environmental_attitude_q2 = models.StringField(widget=widgets.RadioSelect,)
    environmental_attitude_q3 = models.StringField(widget=widgets.RadioSelect,)
    environmental_attitude_q4 = models.StringField(widget=widgets.RadioSelect,)

    trust_in_government_q1 = models.StringField(widget=widgets.RadioSelect,)
    trust_in_government_q2 = models.StringField(widget=widgets.RadioSelect,)
    trust_in_government_q3 = models.StringField(widget=widgets.RadioSelect,)
    trust_in_government_q4 = models.StringField(widget=widgets.RadioSelect,)

    ev_prob_benefits1 = make_likert6()
    ev_prob_benefits2 = make_likert6()
    ev_prob_benefits3 = make_likert6()
    ev_prob_benefits4 = make_likert6()

    ev_prob_risks1 = make_likert6()
    ev_prob_risks2 = make_likert6()
    ev_prob_risks3 = make_likert6()

    ev_perceived_benefit1 = make_likert6()
    ev_perceived_benefit2 = make_likert6()

    ev_perceived_risk1 = make_likert6()
    ev_perceived_risk2 = make_likert6()


    comment = models.StringField(
        blank=True,
    )

class transition(Page):
    form_model = 'player'
    form_fields = ['comprehension_question']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)
    
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['comprehension_question'],
            form_field_labels=[Lexicon.comprehension_question_label]
        )

class risks_preferences(Page):
    form_model = 'player'
    form_fields = ['risks_pref']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

class probability(Page):
    form_model = 'player'
    form_fields = ['ev_prob_benefits1', 'ev_prob_benefits2', 'ev_prob_benefits3', 'ev_prob_benefits4',
                   'ev_prob_risks1', 'ev_prob_risks2','ev_prob_risks3']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['ev_prob_benefits1', 'ev_prob_benefits2', 'ev_prob_benefits3', 'ev_prob_benefits4',
                         'ev_prob_risks1', 'ev_prob_risks2','ev_prob_risks3'],
            form_field_labels=[Lexicon.ev_prob_benefits1_label, Lexicon.ev_prob_benefits2_label,
                           Lexicon.ev_prob_benefits3_label, Lexicon.ev_prob_benefits4_label,
                           Lexicon.ev_prob_risks1_label, Lexicon.ev_prob_risks2_label,
                           Lexicon.ev_prob_risks3_label]
        )


class environmental_attitude(Page):
    form_model = 'player'
    form_fields = ['environmental_attitude_q1','environmental_attitude_q2','attention_check_2','environmental_attitude_q3','environmental_attitude_q4']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['environmental_attitude_q1','environmental_attitude_q2','attention_check_2','environmental_attitude_q3','environmental_attitude_q4'],
            form_field_labels=[Lexicon.environmental_attitude_q1,
                               Lexicon.environmental_attitude_q2,
                               Lexicon.attention_check_2_label,                               
                               Lexicon.environmental_attitude_q3,
                               Lexicon.environmental_attitude_q4
                               ]
        )
    
class trust_in_government(Page):
    form_model = 'player'
    form_fields = ['trust_in_government_q1','trust_in_government_q2','trust_in_government_q3','trust_in_government_q4']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['trust_in_government_q1','trust_in_government_q2','trust_in_government_q3','trust_in_government_q4'],
            form_field_labels=[Lexicon.trust_in_government_q1,
                               Lexicon.trust_in_government_q2,
                               Lexicon.trust_in_government_q3,
                               Lexicon.trust_in_government_q4
                               ]
        )


class pol_orientation(Page):
    form_model = 'player'
    form_fields = ['conservative_liberal']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)


class risks_EV(Page):
    form_model = 'player'
    form_fields = ['ev_perceived_risk1', 'ev_perceived_risk2', 'ev_perceived_benefit1', 'ev_perceived_benefit2']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['ev_perceived_risk1', 'ev_perceived_risk2', 'ev_perceived_benefit1', 'ev_perceived_benefit2'],
            form_field_labels=[Lexicon.ev_perceived_risk1_label, Lexicon.ev_perceived_risk2_label,
                               Lexicon.ev_perceived_benefit1_label, Lexicon.ev_perceived_benefit2_label]
        )


class comments(Page):
    form_model = 'player'
    form_fields = ['comment']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)


# Page sequence
page_sequence = [
    transition,
    risks_preferences,
    probability,
    #risks_EV,
    environmental_attitude,
    trust_in_government,
    pol_orientation,
    comments
]
