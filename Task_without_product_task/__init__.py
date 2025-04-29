from otree.api import *
import random

author = 'Mart van der Kam & Anne Günther'

doc = """
Choice experiment task
"""


# Constants
class Constants(BaseConstants):
    name_in_url = 'Task_v2'
    players_per_group = None
    blocks = ['policy_mix_support','policy_outcome_fairness']
    trials_per_block = 18
    num_rounds = 36

    possible_orders_without_product_task = [
        ['policy_mix_support','policy_outcome_fairness'],
        ['policy_outcome_fairness','policy_mix_support']
    ]

    from .attributes_usa import (
        attributes_policy_mix_support as attributes_policy_mix_support_usa,
        attributes_policy_outcome_fairness as attributes_policy_outcome_fairness_usa
    )

    from .attributes_de import (
        attributes_policy_mix_support as attributes_policy_mix_support_de,
        attributes_policy_outcome_fairness as attributes_policy_outcome_fairness_de
    )

    from .attributes_sa import (
        attributes_policy_mix_support as attributes_policy_mix_support_sa,
        attributes_policy_outcome_fairness as attributes_policy_outcome_fairness_sa
    )


# Subsession
class Subsession(BaseSubsession):
    pass


# Group
class Group(BaseGroup):
    pass


# Player
class Player(BasePlayer):

    # Add a field to store the radio button decision
    choice = models.StringField(
        choices=[
                 "Strongly oppose","Oppose","Somewhat oppose","Neutral","Somewhat support","Support","Strongly support",
                 "Very unfair","Unfair","Somewhat unfair","Neutral","Somewhat fair","Fair","Very fair"],
        widget=widgets.RadioSelectHorizontal,
    )

    current_task = models.IntegerField(initial=0)
    block = models.StringField()
    current_task_pol = models.IntegerField(initial=0)



def creating_session(subsession: Subsession):
    if subsession.session.config['language'] == 'de':
        from .lexicon_de import Lexicon
        subsession.session.myLangCode = "_de"
    elif subsession.session.config['language'] == "sa":
        from .lexicon_sa import Lexicon
        subsession.session.myLangCode = "_sa"
    else:
        from .lexicon_usa import Lexicon
        subsession.session.myLangCode = "_usa"
    subsession.session.taskWithoutProductTaskLexi = Lexicon

    if subsession.round_number == 1:
        for p in subsession.get_players():
            tasks_without_product_task = ['TaskPage_v2'] * Constants.num_rounds
            random.shuffle(tasks_without_product_task)
            task_rounds_without_product_task = dict(zip(tasks_without_product_task, range(1, len(tasks_without_product_task) + 1)))
            p.participant.task_rounds_without_product_task = task_rounds_without_product_task

    if subsession.round_number <= Constants.num_rounds:
        trials_per_block = Constants.trials_per_block

        for p in subsession.get_players():
            possible_orders_without_product_task = Constants.possible_orders_without_product_task.copy()

            block_order_without_product_task = random.choice(possible_orders_without_product_task)

            randomized_sequence_without_product_task = []

            # Generate a sequence that completes all trials for each block before moving on to the next block
            for block in block_order_without_product_task:
                block_sequence_without_product_task = [(block, trial_number) for trial_number in range(1, trials_per_block + 1)]
                random.shuffle(block_sequence_without_product_task)
                randomized_sequence_without_product_task.extend(block_sequence_without_product_task)

            p.participant.task_rounds_without_product_task = randomized_sequence_without_product_task
            p.participant.vars['randomized_sequence_without_product_task'] = randomized_sequence_without_product_task


# Page with Blocks 'policy_mix_support' and 'policy_outcome_fairness'
class TaskPage_v2(Page):
    form_model = 'player'
    form_fields = ['choice']

    def is_displayed(player):
        return player.participant.vars['own_car'] != 'yes' and player.participant.vars['own_car_future'] != 'yes'

    @staticmethod
    def vars_for_template(player: Player):
        if player.session.config['language'] == "de":
            attributes_policy_mix_support = Constants.attributes_policy_mix_support_de
            attributes_policy_outcome_fairness = Constants.attributes_policy_outcome_fairness_de
        elif player.session.config['language'] == "sa":
            attributes_policy_mix_support = Constants.attributes_policy_mix_support_sa
            attributes_policy_outcome_fairness = Constants.attributes_policy_outcome_fairness_sa
        else:
            attributes_policy_mix_support = Constants.attributes_policy_mix_support_usa
            attributes_policy_outcome_fairness = Constants.attributes_policy_outcome_fairness_usa
        Lexicon = player.session.taskWithoutProductTaskLexi

        if 'randomized_sequence_without_product_task' not in player.participant.vars:
            print("DEBUG: 'randomized_sequence_without_product_task' not found in participant.vars. Calling creating_session.")

        print(player.round_number)
        current_task_tuple = player.participant.task_rounds_without_product_task[player.round_number - 1]

        if not isinstance(current_task_tuple, tuple) or len(current_task_tuple) != 2:
            # Handle the case where current_task_tuple is not a tuple of length 2
            current_task_tuple = ('', 0)

        block, trial_number = current_task_tuple
        print(f"DEBUG: current_task_tuple: {current_task_tuple}, block: {block}, trial_number: {trial_number}")

        player.block = block
        player.current_task = trial_number

        # Define which blocks are product choice and which is the policy block
        policy_block = block == 'policy_mix_support'
        fairness_block = block == 'policy_outcome_fairness'

        round_number = player.round_number

        # Specify the rounds where the message is supposed to be visually attractive -> first trials of each block
        attractive_rounds = {1, 19}
        # Check if trial_number is in attractive_rounds = first trial of the block
        is_first_trial_of_block = player.round_number in attractive_rounds

        # Well done rounds
        well_done = {19}
        completed_block = player.round_number in well_done


        # Conditionally choose the attributes lists based on the "car_size_future" value and block
        if player.participant.vars['car_size_future'] == 'small':
            attributes_list = {
                'policy_mix_support': attributes_policy_mix_support,
                'policy_outcome_fairness': attributes_policy_outcome_fairness
            }
        elif player.participant.vars['car_size_future'] == 'medium':
            attributes_list = {
                'policy_mix_support': attributes_policy_mix_support,
                'policy_outcome_fairness': attributes_policy_outcome_fairness
            }
        elif player.participant.vars['car_size_future'] == 'large':
            attributes_list = {
                'policy_mix_support': attributes_policy_mix_support,
                'policy_outcome_fairness': attributes_policy_outcome_fairness
            }
        else:
            attributes_list = {
                'policy_mix_support': attributes_policy_mix_support,
                'policy_outcome_fairness': attributes_policy_outcome_fairness
            }

        try:
            if block == 'policy_mix_support':
                attributes = attributes_policy_mix_support[trial_number - 1]
                if 'shuffled_attributes_policy' not in player.participant.vars:
                    keys_list_policy = list(attributes.keys())
                    # UNCOMMENT FUNCTION BELOW TO RANDOMIZE ATTRIBUTE ORDER
                    # random.shuffle(keys_list_policy)
                    player.participant.vars['keys_list_policy'] = keys_list_policy
                    shuffled_attributes = {key: attributes[key] for key in keys_list_policy}
                    player.participant.vars['shuffled_attributes_policy'] = shuffled_attributes
                else:
                    shuffled_attributes = {key: attributes[key] for key in player.participant.vars['keys_list_policy']}
            else:
                if block == 'policy_outcome_fairness':
                    attributes = attributes_policy_outcome_fairness[trial_number - 1]
                    if 'shuffled_attributes_fairness' not in player.participant.vars:
                        keys_list_fairness = list(attributes.keys())
                        # UNCOMMENT FUNCTION BELOW TO RANDOMIZE ATTRIBUTE ORDER
                        # random.shuffle(keys_list_fairness)
                        player.participant.vars['keys_list_fairness'] = keys_list_fairness
                        shuffled_attributes = {key: attributes[key] for key in keys_list_fairness}
                        player.participant.vars['shuffled_attributes_fairness'] = shuffled_attributes
                    else:
                        shuffled_attributes = {key: attributes[key] for key in player.participant.vars['keys_list_fairness']}
        except KeyError:
            print("DEBUG: KeyError occurred. Available blocks:", attributes_list.keys())
            raise

        return {
            "attributes": shuffled_attributes,
            "current_task": trial_number,  # Set current_task to the extracted trial_number
            "block": block,  # Include the block information
            "round_number": round_number,
            "is_first_trial_of_block": is_first_trial_of_block,
            "completed_block": completed_block,
            "policy_block": policy_block,
            "fairness_block": fairness_block,
            "Lexicon": Lexicon,
        }

# Page sequence
page_sequence = [TaskPage_v2]