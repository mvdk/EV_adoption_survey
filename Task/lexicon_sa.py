class Lexicon:
    # General
    next = "Next"
    yes = "Yes"
    no = "No"
    strongly_oppose = "Strongly oppose"
    oppose = "Oppose"
    somewhat_oppose = "Somewhat oppose"
    neutral = "Neutral"
    somewhat_support = "Somewhat support"
    support = "Support"
    strongly_support = "Strongly support"
    very_unfair = "Very unfair"
    unfair = "Unfair"
    somewhat_unfair = "Somewhat unfair"
    neutral = "Neutral"
    somewhat_fair = "Somewhat fair"
    fair = "Fair"
    very_fair = "Very fair"
    button_start = "Start Task"

    # instruction_product
    product_intro_title = "Please read carefully:"
    product_intro_text1 = "In the upcoming pages, you will be presented with various imaginary investment scenarios. <b>Please imagine that you would like to purchase a new car.</b><br><br>"
    product_intro_text2 = "Your role is to evaluate different offers for <b>electric vehicles</b> and decide whether or not you would choose to buy each car.<br><br>"
    product_intro_text3 = "Consider the following attributes that vary across the offers:"

    investment_cost = "<u>Purchase Price:</u>"
    electricity_cost = "<u>Electricity costs for driving:</u>"
    gasoline_cost = "<u>Gasoline costs for comparable car:</u>"
    new_used = "<u>New car or pre-owned car:</u>"
    range = "<u>Battery Range:</u>"
    adopters = "<u>Electric vehicle adoption in your income group:</u>"
    ice_sales_ban_adoption = "<u>Sales ban on new gasoline and diesel vehicles:</u>"

    investment_cost_text = "This financial attribute shows the <b>net price of the electric car</b>. There are government subsidies that can directly reduce the price. The cost depends on the car brand and the subsidies/discounts subtracted."
    electricity_cost_text = "An electric vehicle needs electricity for driving, which is typically cheaper per kilometer than gasoline and diesel. This attribute represents the <b>electricity costs per 100 kilometer driven</b> in this electric vehicle. The total costs are determined by the efficiency of the electric vehicle, the costs to produce and distribute the electricity, and governmental taxes."
    gasoline_cost_text = "This attribute represents the <b>gasoline costs per 100 kilometer driven</b> for a gasoline-fueled vehicle of comparable size to the electric vehicle of this offer. These costs are determined by the typical fuel efficiency of cars of this size, the costs to produce and distribute gasoline, and governmental taxes. By comparing the gasoline costs to the electricity costs of the electric vehicle, you can calculate how much money you would save each month by driving electric instead of gasoline."
    savings_text = "Charging an electric vehicles is <b>cheaper than fueling a gasoline car</b>. Therefore, the costs per kilometer are lower for electric vehicles than for gasoline cars. The savings are calculated by comparing electricity prices with gas prices and the efficiency of electric vehicles with traditional cars. <b>The value presented tells you how much you can save with this electric car for every 100 kilometers compared to gasoline and diesl vehicles.</b>"
    new_used_text = "This attribute specifies whether the electric car is being sold <b>as a new or used vehicle</b>. A new electric car has not been previously owned or used, whereas a used electric car has had a previous owner. Used cars often have a lower purchase price compared to the original model, but may involve some wear."
    range_text = "The battery range indicates the <b>distance an electric vehicle can travel on a single battery charge</b>. It indicates how many kilometers you can drive before you have to stop to charge the battery."
    adopters_text = "This attribute represents the <b>percentage of people within your income group who currently drive a electric car</b>."
    ice_sales_ban_adoption_text = "This attribute indicates whether there is a <b>sales ban on gasoline and diesel vehicles</b> starting from a certain year. Note that this ban will only apply to car <b>sales</b> and that it will still be legal to <b>drive</b> gasoline and diesel vehicles."

    product_intro_text4 = "Each electric car presented in an offer is designed to match the characteristics of a car you would consider buying. This includes factors such as model, size, engine power, and the number of doors."
    product_intro_text5 = "For each offer you will need to indicate whether you would accept the offer imagining that you need to <i>replace your main car</i>."

    # instruction_policy
    policy_intro_title = "Please read carefully:"
    policy_intro_text1 = "In the following pages, we will present you with a series of imaginary policy packages. The policies are designed to foster the uptake of electric vehicles."
    policy_intro_text2 = "Your task is to evaluate and express your support or non-support for each policy proposal."
    policy_intro_text3 = "Each policy package will consist of different combinations of the following policies:"

    
    subsidy_new = "<u>Subsidies on investment costs of new electric vehicles:</u>"
    subsidy_preowned = "<u>Subsidies on investment costs of pre-owned electric vehicles:</u>"
    tax = "<u>Carbon tax on gasoline and diesel:</u>"
    ice_sales_ban = "<u>A sales ban on new gasoline and diesel vehicles:</u>"

    subsidy_new_text = "This attribute indicates whether there are <b>government subsidies (price discounts)</b> provided to buyers of a new electric vehicle. Subsidies on investment costs are designed to make electric vehicles more financially attractive and affordable for consumers, and promote their adoption. However, it is important to note that these subsidies might also mean that the public funds are not available for other projects. Furthermore, this subsidy is only valid for sales of <b><u>new</u></b> electric vehicles, and will <b><u>not</b></u> be available for the purchase of pre-owned electric vehicles" 
    subsidy_preowned_text = "This attribute indicates whether there are <b>government subsidies (price discounts)</b> provided to buyers of a pre-owned electric vehicle. Subsidies on investment costs are designed to make electric vehicles more financially attractive and affordable for consumers, and promote their adoption. However, it is important to note that these subsidies might also mean that the public funds are not available for other projects. Furthermore, this subsidy only on sales of <b><u>pre-owned</u></b> electric vehicles, and will <b><u>not</b></u> be available for the purchase of new electric vehicles"
    tax_text = "The policy package can include a carbon tax on CO2 emissions of gasoline and diesel. Combustion of gasoline and diesel causes CO2 emissions, contributing to climate change. Each gallon of gasoline and diesel burned produces CO2, so the carbon tax would increase the price of these fuels. As a result, the savings from driving an electric vehicle would be higher compared to gasoline and diesel cars. The tax revenue increases the government budget to spend on other projects."
    ice_sales_ban_text = "This policy bans the sale of gasoline and diesel vehicles starting from a certain year. Note that this ban will only apply to car <b>sales</b> and that it will still be legal to <b>drive</b> gasoline and diesel vehicles."

    policy_intro_text4 = "Please decide whether you would support each policy package presented."

    # instruction_fairness
    fairness_intro_title = "Please read carefully:"
    fairness_intro_text1 = "In the following pages, we will present you with a series of imaginary outcomes of policy packages. The goal of these policies is to stimulate the sales of electric vehicles to achieve reductions of CO2 emissions. However, the impact of these policies may differ between groups of households with different incomes. Even when electric vehicle policies can provide societal benefits such as pollution reduction, some groups may benefit more from these policies than others."
    fairness_intro_text2 = "Your task is to evaluate and express whether you find the outcome of the electric vehicle policies fair or unfair."
    fairness_intro_text3 = "Each policy outcome will consist of different combinations of the following attributes:"


    total_co2_reduction = "<u>Total CO2 reduction personal transportation:</u>"
    policy_benefits_high_income = "<u>Average electric vehicle subsidy received last year by high-income households:</u>"
    policy_benefits_low_income = "<u>Average electric vehicle subsidy received last year by low-income households:</u>"
    policy_burden_high_income = "<u>Average CO2 tax paid last year by high-income households:</u>"
    policy_burden_low_income = "<u>Average CO2 tax paid last year by low-income households:</u>"

    total_co2_reduction_text = "This attribute measures the total reduction in CO2 emissions from personal vehicles as a result of households switching from fossil-fuel based vehicles to electric vehicles. It reflects the overall environmental impact of personal transportations, with larger reductions indicating greater contributions to mitigating climate change and improving air quality."
    policy_benefits_high_income_text = "This attribute represents the average subsidy received by high-income households (more than R240,000 post-tax annual income) for the adoption of an electric vehicle in the last year."
    policy_benefits_low_income_text = "This attribute represents the average subsidy received by low-income households (less than R20,000 post-tax annual income) for the adoption of an electric vehicle in the last year."
    policy_burden_high_income_text = "This attribute indicates how much CO2 tax on emissions from gasoline and diesel had to be paid by high-income households (more than R240,000 post-tax annual income) in the last year. This tax was on the total amount of gasoline or diesel that these households used for driving their personal vehicle."
    policy_burden_low_income_text = "This attribute indicates how much CO2 tax on emissions from gasoline and diesel had to be paid by low-income households (less than R20,000 post-tax annual income) in the last year. This tax was on the total amount of gasoline or diesel that these households used for driving their personal vehicle."
 
    fairness_intro_text4 = "Please decide whether you would support each policy package presented."

    # TaskPage

    policy_question = "Would you support this policy package?"
    fairness_question = "Do you think this policy outcome is fair?"
    product_question = "Would you buy this electric vehicle?"

    affirmative_text = 'Well done on completing the block!'
  


    policy_package_no = "Policy Package"
    product_offer_no = "Electric Vehicle Offer"
    fairness_no = "Policy Outcome"
