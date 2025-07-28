class Lexicon:
    # General
    next = "Weiter"
    yes = "Ja"
    no = "Nein"
    strongly_oppose = "Stark dagegen"
    oppose = "Dagegen"
    somewhat_oppose = "Eher dagegen"
    neutral = "Neutral"
    somewhat_support = "Eher dafür"
    support = "Dafür"
    strongly_support = "Stark dafür"
    very_unfair = "Sehr unfair"
    unfair = "Unfair"
    somewhat_unfair = "Eher unfair"
    neutral = "Neutral"
    somewhat_fair = "Eher fair"
    fair = "Fair"
    very_fair = "Sehr fair"
    button_start = "Aufgabe starten"

    # table titles
    ev_attribute = "Fahrzeugmerkmal"
    ev_attribute_level = "Merkmalsebene"
    policy = "Maßnahme"
    policy_level = "Maßnahmenebene"
    policy_outcome = "Auswirkung"
    policy_outcome_level = "Auswirkungsebene"

    # instruction_product
    product_intro_title = "Bitte lesen Sie den folgenden Text sorgfältig:"
    product_intro_text1 = "Auf den nächsten Seiten werden Ihnen 18 ausgedachte Kaufszenarien präsentiert. <b>Bitte stellen Sie sich vor, dass Sie ein neues Auto kaufen möchten.</b><br><br>"
    product_intro_text2 = "Ihre Aufgabe ist es, verschiedene Angebote für <b>Elektrofahrzeuge</b> zu bewerten und  zu entscheiden, ob Sie das angebotene Auto jeweils kaufen würden oder nicht.<br><br>"
    product_intro_text3 = "Berücksichtigen Sie die folgenden Merkmale, die sich zwischen den Angeboten unterscheiden:"

    investment_cost = "<u>Kaufpreis:</u>"
    electricity_cost = "<u>Stromkosten für das Fahren:</u>"
    gasoline_cost = "<u>Benzinkosten für vergleichbares Auto:</u>"
    range = "<u>Batteriereichweite:</u>"
    adopters = "<u>Verbreitung von Elektrofahrzeugen in Ihrer Einkommensgruppe:</u>"
    ice_sales_ban_adoption = "<u>Verkaufsverbot für neue Benzin- und Dieselfahrzeuge:</u>"

    investment_cost_text = "Dieses finanzielle Merkmal stellt den <b>Nettopreis des Elektroautos</b> dar. Es kann staatliche Subventionen geben, die den Preis direkt senken. Die Kosten hängen von der Automarke und den abgezogenen Subventionen/Rabatten ab."
    electricity_cost_text = "Ein Elektrofahrzeug benötigt Strom zum Fahren, was pro Kilometer meist günstiger ist als Benzin oder Diesel. Dieses Merkmal gibt die <b>Stromkosten pro 100 gefahrene Kilometer</b> mit diesem Elektrofahrzeug an. Die Gesamtkosten hängen von der Effizienz des Fahrzeugs, den Stromproduktions- und -verteilungskosten sowie Steuern ab."
    gasoline_cost_text = "Dieses Merkmal gibt die <b>Benzinkosten pro 100 gefahrene Kilometer</b> für ein benzinbetriebenes Fahrzeug vergleichbarer Größe an. Diese Kosten hängen von der typischen Kraftstoffeffizienz, den Produktions- und Vertriebskosten von Benzin und staatlichen Steuern ab. Durch den Vergleich mit den Stromkosten des Elektroautos können Sie berechnen, wie viel Sie monatlich mit einem Elektroauto sparen würden."
    savings_text = "Das Aufladen eines Elektroautos ist <b>günstiger als das Tanken eines Benzinautos</b>. Daher sind die Kosten pro Kilometer bei Elektrofahrzeugen niedriger. Die Ersparnis ergibt sich aus dem Vergleich der Strompreise mit den Benzinpreisen und der Effizienz. <b>Der angegebene Wert zeigt, wie viel Sie pro 100 Kilometer im Vergleich zu Benzin- und Dieselfahrzeugen sparen können.</b>"
    range_text = "Die Reichweite gibt an, <b>wie weit ein Elektroauto mit einer Batterieladung fahren kann</b>. Sie zeigt, wie viele Kilometer Sie fahren können, bevor Sie laden müssen."
    adopters_text = "Dieses Merkmal zeigt den <b>Prozentsatz der Menschen in Ihrer Einkommensgruppe, die ein Elektrofahrzeug fahren</b>."
    ice_sales_ban_adoption_text = "Dieses Attribut gibt an, ob es ab einem bestimmten Jahr ein <b>Verkaufsverbot für Benzin- und Dieselfahrzeuge</b> gibt. Beachten Sie, dass dieses Verbot nur für den <b>Verkauf</b> von Autos gilt und dass es weiterhin legal ist, Benzin- und Dieselfahrzeuge zu <b>fahren</b>."

    product_intro_text4 = "Jedes präsentierte Elektrofahrzeug ist so gestaltet, dass es den Merkmalen eines Autos entspricht, das Sie in Betracht ziehen würden. Dazu gehören Modell, Größe, Motorleistung und Anzahl der Türen."
    product_intro_text5 = "Wir bitten Sie, für jedes Angebot anzugeben, ob Sie sich vorstellen können das Elektroauto als <u>Hauptfahrzeug</u> zu kaufen."

    # instruction_policy
    policy_intro_title = "Bitte lesen Sie den folgenden Text sorgfältig:"
    policy_intro_text1 = "Auf den folgenden Seiten zeigen wir Ihnen 18 ausgedachte politischer Maßnahmenpakete. Diese Maßnahmen sollen die Verkaufszahlen von Elektrofahrzeugen erhöhen."
    policy_intro_text2 = "Wir bitten Sie nun darum, jede Maßnahme zu bewerten und anzugeben, ob Sie sie unterstützen würden oder nicht."
    policy_intro_text3 = "Jedes politische Maßnahmenpaket enthält verschiedene Kombinationen der folgenden Einzelmaßnahmen:"

    subsidy_new = "<u>Subventionen für neue Elektrofahrzeuge:</u>"
    subsidy_preowned = "<u>Subventionen für gebrauchte Elektrofahrzeuge:</u>"
    tax = "<u>CO2-Steuer auf Benzin und Diesel:</u>"
    ice_sales_ban = "<u>Verkaufsverbot für neue Benzin- und Dieselautos:</u>"

    subsidy_new_text = "Dieses Merkmal gibt an, ob <b>staatliche Subventionen (Preisnachlässe)</b> für Käufer eines neuen Elektrofahrzeugs gewährt werden. Diese Subventionen sollen die Attraktivität und Erschwinglichkeit von Elektroautos erhöhen. Allerdings stehen öffentliche Mittel dann möglicherweise nicht für andere Projekte zur Verfügung. Diese Subvention gilt nur für <b><u>neue</u></b> Fahrzeuge, und <b><u>nicht</u></b> für gebrauchte."
    subsidy_preowned_text = "Dieses Merkmal gibt an, ob <b>staatliche Subventionen (Preisnachlässe)</b> für Käufer eines neuen Elektrofahrzeugs gewährt werden. Diese Subventionen sollen die Attraktivität und Erschwinglichkeit von Elektroautos erhöhen. Allerdings stehen öffentliche Mittel dann möglicherweise nicht für andere Projekte zur Verfügung. Diese Subvention gilt nur für <b><u>gebrauchte</u></b> Fahrzeuge, und <b><u>nicht</u></b> für neue."
    tax_text = "Das Maßnahmenpaket kann eine CO2-Steuer auf Emissionen durch den Verbrauch von Benzin und Diesel enthalten. Die Verbrennung von Benzin und Diesel erzeugt CO2-Emissionen und trägt damit zum Klimawandel bei. Jeder Liter Kraftstoff produziert CO2, sodass die Steuer die Preise für Benzin und Diesel erhöht. Dadurch werden Elektrofahrzeuge im Vergleich attraktiver. Die Einnahmen erhöhen die öffentlichen Mittel."
    ice_sales_ban_text = "Diese Maßnahme verbietet den Verkauf von Benzin- und Dieselfahrzeugen ab einem bestimmten Jahr. Beachten Sie, dass dieses Verbot nur für den <b>Verkauf</b> von Autos gilt und dass es weiterhin legal ist, Benzin- und Dieselfahrzeuge zu <b>fahren</b>."

    policy_intro_text4 = "Bitte entscheiden Sie, ob Sie das jeweilige Maßnahmenpaket unterstützen würden. Mögliche Antworten reichen von ‚stark dagegen‘ bis ‚stark dafür‘."

    # instruction_fairness
    fairness_intro_title = "Bitte lesen Sie den folgenden Text sorgfältig:"
    fairness_intro_text1 = "Auf den folgenden Seiten zeigen wir Ihnen 18 hypothetische Auswirkungen von Maßnahmenpaketen. Ziel der Maßnahmen ist es, den Verkauf von Elektroautos zu steigern und CO2-Emissionen zu senken. Die Auswirkungen dieser Maßnahmen können sich jedoch je nach Einkommensgruppe unterscheiden."
    fairness_intro_text2 = "Wir bitten Sie nun darum zu bewerten, ob Sie die Auswirkungen der Maßnahmen als fair oder unfair empfinden."
    fairness_intro_text3 = "Die Auswirkungen bestehen aus einer Kombination folgender Merkmale:"

    total_co2_reduction = "<u>Gesamte CO2-Reduktion im Individualverkehr:</u>"
    policy_benefits_high_income = "<u>Durchschnittliche Subvention für Haushalte mit hohem Einkommen im letzten Jahr:</u>"
    policy_benefits_low_income = "<u>Durchschnittliche Subvention für Haushalte mit niedrigem Einkommen im letzten Jahr:</u>"
    policy_burden_high_income = "<u>Durchschnittlich gezahlte CO2-Steuer durch Haushalte mit hohem Einkommen im letzten Jahr:</u>"
    policy_burden_low_income = "<u>Durchschnittlich gezahlte CO2-Steuer durch Haushalte mit niedrigem Einkommen im letzten Jahr:</u>"

    total_co2_reduction_text = "Dieses Merkmal zeigt die gesamte CO2-Einsparung im privaten Verkehr durch den Umstieg von fossilen auf elektrische Antriebe. Größere Einsparungen bedeuten stärkere Beiträge zum Klimaschutz und zu besserer Luftqualität."
    policy_benefits_high_income_text = "Dieses Merkmal zeigt, wie viel staatliche Unterstützung Haushalte mit hohem Einkommen (über 56.000 € Nettoeinkommen pro Jahr) im Durchschnitt im letzten Jahr für den Kauf eines Elektrofahrzeugs erhalten haben. Die Angabe ergibt sich aus der Gesamtsumme der Förderungen für Käufer aus dieser Einkommensgruppe, geteilt durch die Gesamtzahl aller Haushalte mit hohem Einkommen – auch jener, die kein Elektrofahrzeug gekauft haben."
    policy_benefits_low_income_text = "Dieses Merkmal zeigt, wie viel staatliche Unterstützung Haushalte mit niedrigem Einkommen (unter 19.000 € Nettoeinkommen pro Jahr) im Durchschnitt im letzten Jahr für den Kauf eines Elektrofahrzeugs erhalten haben. Die Angabe ergibt sich aus der Gesamtsumme der Förderungen für Käufer aus dieser Einkommensgruppe, geteilt durch die Gesamtzahl aller Haushalte mit hohem Einkommen – auch jener, die kein Elektrofahrzeug gekauft haben."
    policy_burden_high_income_text = "Dieses Merkmal zeigt den durchschnittlichen Betrag, den Haushalte mit hohem Einkommen (über 56.000 € Nettoeinkommen pro Jahr) im letzten Jahr an CO2-Steuern für das Fahren benzin- oder dieselbetriebener Fahrzeuge gezahlt haben. Die Angabe ergibt sich aus der Gesamtsumme gezahlter CO2-Steuern in der Einkommensgruppe, die durch das Fahren solcher Fahrzeuge anfallen, und wird über alle Haushalte mit hohem Einkommen gemittelt – einschließlich jener, die Elektrofahrzeuge oder kein Auto besitzen."
    policy_burden_low_income_text = "Dieses Merkmal zeigt den durchschnittlichen Betrag, den Haushalte mit hohem Einkommen (unter 19.000 € Nettoeinkommen pro Jahr) im letzten Jahr an CO2-Steuern für das Fahren benzin- oder dieselbetriebener Fahrzeuge gezahlt haben. Die Angabe ergibt sich aus der Gesamtsumme gezahlter CO2-Steuern in der Einkommensgruppe, die durch das Fahren solcher Fahrzeuge anfallen, und wird über alle Haushalte mit niedrigem Einkommen gemittelt – einschließlich jener, die Elektrofahrzeuge oder kein Auto besitzen."

    fairness_intro_text4 = "Bitte geben Sie an, ob Sie die Auswirkungen der Maßnahmenpakete für fair oder unfair halten. Mögliche Antworten reichen von ‚sehr unfair‘ bis ‚sehr fair‘."

    # TaskPage
    policy_question = "Würden Sie dieses Maßnahmenpaket unterstützen?"
    fairness_question = "Halten Sie dieses Ergebnis für fair?"
    product_question = "Würden Sie dieses Elektrofahrzeug kaufen?"

    affirmative_text = 'Gut gemacht! Sie haben diesen Block abgeschlossen.'

    policy_package_no = "Maßnahmenpaket"
    product_offer_no = "Angebot Elektrofahrzeug"
    fairness_no = "Maßnahmenergebnis"

    # instruction_disruption
    disruption_intro_title = "Please read carefully:"
    disruption_intro_text = "Imagine that <b>a political crisis</b> has hit your country. Due to geopolitical tensions, tariffs have been implemented on electric vehicles and energy imports. This has led to supply chain disruptions and instable global energy markets. These factors have also contributed to increased costs for electric vehicles as well as gasoline and electricity prices. The extent of price increases varies, reflecting potential market responses to supply shortages, shifts in global demand, and government policies to counter high prices for consumers."
    disruption_intro_text1 = "In the upcoming pages, you will be presented with another 18 imaginary investment scenarios.<br><br>"
    disruption_intro_text2 = "Your role is to evaluate different offers for <b>electric vehicles</b> and decide whether or not you would choose to buy each car.<br><br>"
    disruption_intro_text3 = "Compared to the previous block of this study, several attributes have changed to reflect this disruptive environment:"

    investment_cost_high = "<u>Increased purchase price:</u>"
    electricity_gasoline_cost = "<u>Higher and more uncertain gasoline and electricity costs:</u>"

    investment_cost_high_text = "EV prices have risen due to tariffs."
    electricity_gasoline_cost_text = "Energy prices may increase due to tariffs and supply chain issues, which has impacted gasoline as well as electricity costs. Furthermore, both gasoline and electricity costs now include potential fluctuations and prices vary over time."

    disruption_intro_text4 = "Each electric car presented in an offer is designed to match the characteristics of a car you would consider buying. This includes factors such as model, size, engine power, and the number of doors."
    disruption_intro_disruption_text5 = "For each offer you will need to indicate whether you would accept the offer imagining that you are buying a new <u>main car under the current political crisis.</u>"

 

    # TaskPage disruption

    disruption_question = "Would you buy this electric vehicle?"

    affirmative_text = 'Well done on completing the block!'
  


    disruption_offer_no = "Electric Vehicle Offer"
