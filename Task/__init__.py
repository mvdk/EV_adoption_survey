from otree.api import *
import random

author = 'Mart van der Kam & Anne Günther'

doc = """
Choice experiment task
"""


# Constants
class Constants(BaseConstants):
    name_in_url = 'Task'
    players_per_group = None
    blocks = ['product_v1', 'product_v2', 'policy_mix_support','policy_outcome_fairness']
    trials_per_block = 18
    num_rounds = 54
    possible_orders = [
        ['product_v1','policy_mix_support','policy_outcome_fairness'],
        ['product_v2','policy_mix_support','policy_outcome_fairness'],
        ['product_v1','policy_outcome_fairness','policy_mix_support'],
        ['product_v2','policy_outcome_fairness','policy_mix_support'],
        ['policy_mix_support','product_v1','policy_outcome_fairness'],
        ['policy_mix_support','product_v2','policy_outcome_fairness'],
        ['policy_mix_support','policy_outcome_fairness','product_v1'],
        ['policy_mix_support','policy_outcome_fairness','product_v2'],
        ['policy_outcome_fairness','product_v1','policy_mix_support'],
        ['policy_outcome_fairness','product_v2','policy_mix_support'],
        ['policy_outcome_fairness','policy_mix_support','product_v1'],
        ['policy_outcome_fairness','policy_mix_support','product_v2'],
    ]

    from .attributes_usa import (
        attributes_version_1_small as attributes_version_1_small_usa,
        attributes_version_2_small  as attributes_version_2_small_usa,
        attributes_version_1_medium  as attributes_version_1_medium_usa,
        attributes_version_2_medium  as attributes_version_2_medium_usa,
        attributes_version_1_large  as attributes_version_1_large_usa,
        attributes_version_2_large  as attributes_version_2_large_usa,
        attributes_version_1_small  as attributes_version_1_listA_none_usa,
        attributes_version_2_small  as attributes_version_2_listB_none_usa,
        attributes_policy_mix_support as attributes_policy_mix_support_usa,
        attributes_policy_outcome_fairness as attributes_policy_outcome_fairness_usa
    )

    from .attributes_de import (
        attributes_version_1_small as attributes_version_1_small_de,
        attributes_version_2_small  as attributes_version_2_small_de,
        attributes_version_1_medium  as attributes_version_1_medium_de,
        attributes_version_2_medium  as attributes_version_2_medium_de,
        attributes_version_1_large  as attributes_version_1_large_de,
        attributes_version_2_large  as attributes_version_2_large_de,
        attributes_version_1_small  as attributes_version_1_listA_none_de,
        attributes_version_2_small  as attributes_version_2_listB_none_de,
        attributes_policy_mix_support as attributes_policy_mix_support_de,
        attributes_policy_outcome_fairness as attributes_policy_outcome_fairness_de
    )
    
    from .attributes_sa import (
        attributes_version_1_small as attributes_version_1_small_sa,
        attributes_version_2_small  as attributes_version_2_small_sa,
        attributes_version_1_medium  as attributes_version_1_medium_sa,
        attributes_version_2_medium  as attributes_version_2_medium_sa,
        attributes_version_1_large  as attributes_version_1_large_sa,
        attributes_version_2_large  as attributes_version_2_large_sa,
        attributes_version_1_small  as attributes_version_1_listA_none_sa,
        attributes_version_2_small  as attributes_version_2_listB_none_sa,
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
        choices=["Yes", "No","Somewhat",
                 "Strongly oppose","Oppose","Somewhat oppose","Neutral","Somewhat support","Support","Strongly support",
                 "Very unfair","Unfair","Somewhat unfair","Neutral","Somewhat fair","Fair","Very fair",
                 "choice1", "choice2","choice3","choice4","choice5","choice6","choice7"],
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
    subsession.session.taskLexi = Lexicon
    

    if subsession.round_number == 1:
        for p in subsession.get_players():
            tasks = ['TaskPage'] * Constants.num_rounds
            random.shuffle(tasks)
            task_rounds = dict(zip(tasks, range(1, len(tasks) + 1)))
            p.participant.task_rounds = task_rounds

    if subsession.round_number <= Constants.num_rounds:
        trials_per_block = Constants.trials_per_block

        for p in subsession.get_players():
            possible_orders = Constants.possible_orders.copy()

            block_order = random.choice(possible_orders)

            randomized_sequence = []

            # Generate a sequence that completes all trials for each block before moving on to the next block
            for block in block_order:
                block_sequence = [(block, trial_number) for trial_number in range(1, trials_per_block + 1)]
                random.shuffle(block_sequence)
                randomized_sequence.extend(block_sequence)

            p.participant.task_rounds = randomized_sequence
            p.participant.vars['randomized_sequence'] = randomized_sequence


# Page with Blocks A, B, C, D, E
class TaskPage(Page):
    form_model = 'player'
    form_fields = ['choice']

    def is_displayed(player):
        return player.participant.vars['own_car'] == 'yes' or player.participant.vars['own_car_future'] == 'yes'

    @staticmethod
    def vars_for_template(player: Player):
        # Ensure that randomized_sequence is set before trying to access it
        if player.session.config['language'] == "de":
            attributes_version_1_small = Constants.attributes_version_1_small_de
            attributes_version_2_small = Constants.attributes_version_1_small_de
            attributes_version_1_medium = Constants.attributes_version_1_medium_de
            attributes_version_2_medium = Constants.attributes_version_2_medium_de
            attributes_version_1_large = Constants.attributes_version_1_large_de
            attributes_version_2_large = Constants.attributes_version_2_large_de
            attributes_policy_mix_support = Constants.attributes_policy_mix_support_de
            attributes_policy_outcome_fairness = Constants.attributes_policy_outcome_fairness_de
        elif player.session.config['language'] == "sa":
            attributes_version_1_small = Constants.attributes_version_1_small_sa
            attributes_version_2_small = Constants.attributes_version_1_small_sa
            attributes_version_1_medium = Constants.attributes_version_1_medium_sa
            attributes_version_2_medium = Constants.attributes_version_2_medium_sa
            attributes_version_1_large = Constants.attributes_version_1_large_sa
            attributes_version_2_large = Constants.attributes_version_2_large_sa
            attributes_policy_mix_support = Constants.attributes_policy_mix_support_sa
            attributes_policy_outcome_fairness = Constants.attributes_policy_outcome_fairness_sa
        else:
            attributes_version_1_small = Constants.attributes_version_1_small_usa
            attributes_version_2_small = Constants.attributes_version_1_small_usa
            attributes_version_1_medium = Constants.attributes_version_1_medium_usa
            attributes_version_2_medium = Constants.attributes_version_2_medium_usa
            attributes_version_1_large = Constants.attributes_version_1_large_usa
            attributes_version_2_large = Constants.attributes_version_2_large_usa
            attributes_policy_mix_support = Constants.attributes_policy_mix_support_usa
            attributes_policy_outcome_fairness = Constants.attributes_policy_outcome_fairness_usa
        Lexicon = player.session.taskLexi

        if 'randomized_sequence' not in player.participant.vars:
            print("DEBUG: 'randomized_sequence' not found in participant.vars. Calling creating_session.")

        print(player.round_number)
        current_task_tuple = player.participant.task_rounds[player.round_number - 1]

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
        product_block = player.block in ['product_v1', 'product_v2']

        round_number = player.round_number

        # Specify the rounds where the message is supposed to be visually attractive -> first trials of each block
        attractive_rounds = {1, 19, 37}
        # Check if trial_number is in attractive_rounds = first trial of the block
        is_first_trial_of_block = player.round_number in attractive_rounds

        # Well done rounds
        well_done = {19, 37}
        completed_block = player.round_number in well_done

        # Conditionally choose the attributes lists based on the "car_size_future" value and block
        if player.participant.vars['car_size_future'] == 'small':
            attributes_list = {
                'product_v1': attributes_version_1_small,
                'product_v2': attributes_version_2_small,
                'policy_mix_support': attributes_policy_mix_support,
                'policy_outcome_fairness': attributes_policy_outcome_fairness
            }
        elif player.participant.vars['car_size_future'] == 'medium':
            attributes_list = {
                'product_v1': attributes_version_1_medium,
                'product_v2': attributes_version_2_medium,
                'policy_mix_support': attributes_policy_mix_support,
                'policy_outcome_fairness': attributes_policy_outcome_fairness
            }
        elif player.participant.vars['car_size_future'] == 'large':
            attributes_list = {
                'product_v1': attributes_version_1_large,
                'product_v2': attributes_version_2_large,
                'policy_mix_support': attributes_policy_mix_support,
                'policy_outcome_fairness': attributes_policy_outcome_fairness
            }
        else:
            attributes_list = {
                'product_v1': attributes_version_1_large,
                'product_v2': attributes_version_2_large,
                'policy_mix_support': attributes_policy_mix_support,
                'policy_outcome_fairness': attributes_policy_outcome_fairness
            }

        try:
            if block == 'policy_mix_support':
                attributes = attributes_policy_mix_support[trial_number - 1]
                if 'shuffled_attributes_policy' not in player.participant.vars:
                    keys_list_policy = list(attributes.keys())
                    # UNCOMMENT FUNCTION BELOW TO RANDOMIZE ATTRIBUTE ORDER
                    #random.shuffle(keys_list_policy)
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
                        #random.shuffle(keys_list_fairness)
                        player.participant.vars['keys_list_fairness'] = keys_list_fairness
                        shuffled_attributes = {key: attributes[key] for key in keys_list_fairness}
                        player.participant.vars['shuffled_attributes_fairness'] = shuffled_attributes
                    else:
                        shuffled_attributes = {key: attributes[key] for key in player.participant.vars['keys_list_fairness']}
                else:
                    # Retrieve the attributes_list for the given block
                    current_attributes_list = attributes_list[block]
                    if not current_attributes_list:
                        print("DEBUG: current_attributes_list is empty. Available blocks:", attributes_list.keys())
                        raise KeyError(f"Block {block} not found in attributes_list")
                    # Retrieve the attributes for the given trial_number
                    attributes = current_attributes_list[trial_number - 1]
                    if 'shuffled_attributes_product' not in player.participant.vars:
                        keys_list = list(attributes.keys())
                        # UNCOMMENT FUNCTION BELOW TO RANDOMIZE ATTRIBUTE ORDER
                        #random.shuffle(keys_list)
                        player.participant.vars['keys_list'] = keys_list
                        shuffled_attributes = {key: attributes[key] for key in keys_list}
                        player.participant.vars['shuffled_attributes_product'] = shuffled_attributes
                    else:
                        shuffled_attributes = {key: attributes[key] for key in player.participant.vars['keys_list']}
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
            "product_block": product_block,
            "Lexicon": Lexicon,
        }

# Page sequence
page_sequence = [TaskPage]