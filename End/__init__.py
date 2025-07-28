import random
from otree.api import *

author = 'Mart van der Kam & Anne Günther'

class C(BaseConstants):
    NAME_IN_URL = 'end'
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
    subsession.session.endLexi = Lexicon


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class end_wave2(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(player):
        return player.participant.vars['own_car'] == 'yes' or player.participant.vars['own_car_future'] == 'yes'

    @staticmethod
    def vars_for_template(player: Player):
        lang = player.subsession.session.config['language']
        if lang == 'de':
            redirect_url = "https://app.prolific.com/submissions/complete?cc=C6YZKL0V"
        elif lang == 'sa':
            redirect_url = "https://app.prolific.com/submissions/complete?cc=CRHM9MJH"
        else:
            redirect_url = "https://app.prolific.com/submissions/complete?cc=C1DYB08Q"

        return {
            'redirect_url': redirect_url,
            'Lexicon': player.session.endLexi,
        }
    
class end_no_wave2(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(player):
        return player.participant.vars['own_car'] == 'no' and player.participant.vars['own_car_future'] == 'no'

    @staticmethod
    def vars_for_template(player: Player):
        lang = player.subsession.session.config['language']
        if lang == 'de':
            redirect_url = "https://app.prolific.com/submissions/complete?cc=C6YZKL0V"
        elif lang == 'sa':
            redirect_url = "https://app.prolific.com/submissions/complete?cc=CRHM9MJH"
        else:
            redirect_url = "https://app.prolific.com/submissions/complete?cc=C1DYB08Q"

        return {
            'redirect_url': redirect_url,
            'Lexicon': player.session.endLexi,
        }


# Page sequence
page_sequence = [
    end_wave2,
    end_no_wave2
]
