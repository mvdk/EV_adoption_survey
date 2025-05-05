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

    # instruction_product
    product_intro_title = "Bitte lesen Sie den folgenden Text sorgfältig:"
    product_intro_text1 = "Auf den nächsten Seiten werden Ihnen verschiedene ausgedachte Kaufszenarien präsentiert. <b>Bitte stellen Sie sich vor, dass Sie ein neues Auto kaufen möchten.</b><br><br>"
    product_intro_text2 = "Ihre Aufgabe ist es, verschiedene Angebote für <b>Elektrofahrzeuge</b> zu bewerten und  zu entscheiden, ob Sie das angebotene Auto jeweils kaufen würden oder nicht.<br><br>"
    product_intro_text3 = "Berücksichtigen Sie die folgenden Merkmale, die sich zwischen den Angeboten unterscheiden:"

    investment_cost = "<u>Kaufpreis:</u>"
    electricity_cost = "<u>Stromkosten für das Fahren:</u>"
    gasoline_cost = "<u>Benzinkosten für vergleichbares Auto:</u>"
    new_used = "<u>Neuwagen oder Gebrauchtwagen:</u>"
    range = "<u>Batteriereichweite:</u>"
    adopters = "<u>Verbreitung von Elektrofahrzeugen in Ihrer Einkommensgruppe:</u>"
    ice_sales_ban_adoption = "<u>Verkaufsverbot für neue Benzin- und Dieselfahrzeuge:</u>"

    investment_cost_text = "Dieses finanzielle Merkmal stellt den <b>Nettopreis des Elektroautos</b> dar. Es kann staatliche Subventionen geben, die den Preis direkt senken. Die Kosten hängen von der Automarke und den abgezogenen Subventionen/Rabatten ab."
    electricity_cost_text = "Ein Elektrofahrzeug benötigt Strom zum Fahren, was pro Kilometer meist günstiger ist als Benzin oder Diesel. Dieses Merkmal gibt die <b>Stromkosten pro 100 gefahrene Kilometer</b> mit diesem Elektrofahrzeug an. Die Gesamtkosten hängen von der Effizienz des Fahrzeugs, den Stromproduktions- und -verteilungskosten sowie Steuern ab."
    gasoline_cost_text = "Dieses Merkmal gibt die <b>Benzinkosten pro 100 gefahrene Kilometer</b> für ein benzinbetriebenes Fahrzeug vergleichbarer Größe an. Diese Kosten hängen von der typischen Kraftstoffeffizienz, den Produktions- und Vertriebskosten von Benzin und staatlichen Steuern ab. Durch den Vergleich mit den Stromkosten des Elektroautos können Sie berechnen, wie viel Sie monatlich mit einem Elektroauto sparen würden."
    savings_text = "Das Aufladen eines Elektroautos ist <b>günstiger als das Tanken eines Benzinautos</b>. Daher sind die Kosten pro Kilometer bei Elektrofahrzeugen niedriger. Die Ersparnis ergibt sich aus dem Vergleich der Strompreise mit den Benzinpreisen und der Effizienz. <b>Der angegebene Wert zeigt, wie viel Sie pro 100 Kilometer im Vergleich zu Benzin- und Dieselfahrzeugen sparen können.</b>"
    new_used_text = "Dieses Merkmal gibt an, ob das Elektrofahrzeug <b>neu oder gebraucht</b> verkauft wird. Ein neues Fahrzeug wurde noch nie benutzt, ein gebrauchtes hatte bereits einen Vorbesitzer. Gebrauchtwagen sind oft günstiger, können aber Gebrauchsspuren aufweisen."
    range_text = "Die Reichweite gibt an, <b>wie weit ein Elektroauto mit einer Batterieladung fahren kann</b>. Sie zeigt, wie viele Kilometer Sie fahren können, bevor Sie laden müssen."
    adopters_text = "Dieses Merkmal zeigt den <b>Prozentsatz der Menschen in Ihrer Einkommensgruppe, die derzeit ein Elektrofahrzeug fahren</b>."
    ice_sales_ban_adoption_text = "Dieses Attribut gibt an, ob es ab einem bestimmten Jahr ein <b>Verkaufsverbot für Benzin- und Dieselfahrzeuge</b> gibt. Beachten Sie, dass dieses Verbot nur für den <b>Verkauf</b> von Autos gilt und dass es weiterhin legal ist, Benzin- und Dieselfahrzeuge zu <b>fahren</b>."

    product_intro_text4 = "Jedes präsentierte Elektrofahrzeug ist so gestaltet, dass es den Merkmalen eines Autos entspricht, das Sie in Betracht ziehen würden. Dazu gehören Modell, Größe, Motorleistung und Anzahl der Türen."
    product_intro_text5 = "Wir bitten Sie, für jedes Angebot anzugeben, ob Sie sich vorstellen können das Elektroauto zu kaufen, wenn Sie Ihr aktuelles <b><i>Hauptfahrzeug</b></i> ersetzen müssten."

    # instruction_policy
    policy_intro_title = "Bitte lesen Sie den folgenden Text sorgfältig:"
    policy_intro_text1 = "Auf den folgenden Seiten zeigen wir Ihnen eine Reihe ausgedachte politischer Maßnahmenpakete. Diese Maßnahmen sollen die Verkaufszahlen von Elektrofahrzeugen erhöhen."
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
    fairness_intro_text1 = "Auf den folgenden Seiten zeigen wir Ihnen die hypothetische Auswirkungen, wenn die von Ihnen vorher bewerteten Maßnahmenpaketen eingeführt werden. Ziel der Maßnahmen ist es, den Verkauf von Elektroautos zu steigern und CO2-Emissionen zu senken. Die Auswirkungen dieser Maßnahmen können sich jedoch je nach Einkommensgruppe unterscheiden."
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
