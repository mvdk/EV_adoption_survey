class Lexicon:
    # General
    instructions = "Anweisungen"
    next = "Weiter"
    no = "Nein"
    yes = "Ja"

    # Scales
    not_at_all = "überhaupt nicht"
    very_much = "sehr stark"

    completely_disagree = "stimme überhaupt nicht zu"
    completely_agree = "stimme voll und ganz zu"

    unlikely = "sehr unwahrscheinlich"
    likely = "sehr wahrscheinlich"

    # Transition
    transition_title = 'Willkommen im letzten Abschnitt der Studie'
    transition_thanks = 'Vielen Dank für die Bewertung der Elektrofahrzeugangebote sowie der politischen Maßnahmen und Auswirkungen!'
    transition_info_carbuyers = 'Wir stellen Ihnen noch ein paar generelle Fragen zu Ihren Meinungen. Bitte beantworten Sie die folgende zwei Fragen und klicken Sie dann auf "Weiter", um fortzufahren.'
    transition_info_no_carbuyers = 'Wir stellen Ihnen noch ein paar generelle Fragen zu Ihren Meinungen. Bitte beantworten Sie die folgende Verständnisfrage und klicken Sie dann auf "Weiter", um fortzufahren.'

    # Frage zum Verbot
    ban_question_label = "In den Angeboten für Elektrofahrzeuge haben wir ein Verbot für den Verkauf neuer Benzin- und Dieselfahrzeuge beginnedn in 1 oder 5 Jahren aufgenommen. Wie hat dieses Verbotsankündigung Ihre Bewertung der Angebote für Elektrofahrzeuge beeinflusst?"
    ban_answer_1 = "Hat mich deutlich eher dazu gebracht, ein Elektrofahrzeug zu kaufen."
    ban_answer_2 = "Hat mich etwas eher dazu gebracht, ein Elektrofahrzeug zu kaufen."
    ban_answer_3 = "Hatte keinen Einfluss auf meine Bereitschaft, ein Elektrofahrzeug zu kaufen."
    ban_answer_4 = "Hat mich etwas weniger dazu gebracht, ein Elektrofahrzeug zu kaufen."
    ban_answer_5 = "Hat mich deutlich weniger dazu gebracht, ein Elektrofahrzeug zu kaufen."

    # Verständnisfrage
    comprehension_question_label = 'Welche der folgenden Aussagen beschreibt am besten eine <b><i>CO2-Steuer</b></i>?'
    comprehension_answer_1 = 'Ein zusätzlicher Preis auf Treibhausgasemissionen von Kraftstoffen'
    comprehension_answer_2 = 'Eine direkte Zahlung der Regierung zur Unterstützung klimafreundlicher Projekte'
    comprehension_answer_3 = 'Ein zusätzlicher Preis auf Produkte, die Kinderarbeit beinhalten'
    comprehension_answer_4 = 'Eine zusätzliche Steuer auf hohe Einkommen'

    # Risks preferences (Arslan et al., 2020)
    risks_pref_title = "Risikopräferenzen"
    risks_pref_text = "Wie sehen Sie sich selbst: Sind Sie im Allgemeinen eine Person, die bereit ist, Risiken einzugehen, oder vermeiden Sie lieber Risiken?"
    unwilling_to_take_risks = "Nicht bereit, Risiken einzugehen"
    fully_prepared_to_take_risks = "Vollständig bereit, Risiken einzugehen"

    # Subjective Probability
    probability_title = 'Vorteile und Nachteile von Elektrofahrzeugen'
    intro_probability = 'Nachfolgend finden Sie einige allgemeine Fragen zu den Vor- und Nachteilen von Elektrofahrzeugen für Sie persönlich.'
    question_advantages = 'Wie wahrscheinlich ist es Ihrer Meinung nach, dass Sie beim Kauf eines Elektrofahrzeugs von den folgenden Vorteilen profitieren?'
    answer_intro_advantages = 'Der Kauf eines Elektrofahrzeugs würde mir ermöglichen...'
    question_disadvantages = 'Wie wahrscheinlich ist es Ihrer Meinung nach, dass Sie beim Kauf eines Elektrofahrzeugs die folgenden Nachteile erleben?'
    answer_intro_disadvantages = 'Der Kauf eines Elektrofahrzeugs würde zu...'

    ev_prob_benefits1_label = '...meine Ausgaben erheblich zu reduzieren.'
    ev_prob_benefits2_label = '...meine Unabhängigkeit erheblich zu erhöhen.'
    ev_prob_benefits3_label = '...meinen Einfluss auf das Klima erheblich zu verringern.'
    ev_prob_benefits4_label = '...Teil eines gemeinsamen Ziels oder Handelns zu sein, an dem auch andere beteiligt sind.'

    ev_prob_risks1_label = '...zu hohen Anschaffungskosten führen.'
    ev_prob_risks2_label = '...zu geringen Einsparungen führen.'
    ev_prob_risks3_label = '...einer zu geringen Reichweite führen.'

    # Perceived Risk and benefit
    risks_title = "Ihre Wahrnehmung von Risiken und Vorteilen von Elektrofahrzeugen"
    risk_agree = "Inwieweit stimmen Sie den folgenden Aussagen zu?"
    ev_perceived_risk1_label = "Der Kauf eines Elektrofahrzeugs ist für mich ein Risiko."
    ev_perceived_risk2_label = "Ich denke, der Kauf eines Elektrofahrzeugs ist mit zu vielen Risiken verbunden."
    ev_perceived_benefit1_label = "Der Kauf eines Elektrofahrzeugs ist für mich attraktiv."
    ev_perceived_benefit2_label = "Ich denke, der Kauf eines Elektrofahrzeugs bringt viele Vorteile mit sich."

    # Climate Change Concern (Tobler et al., 2012 & Shi et al., 2016)
    cc_concern_title = "Sorge um den Klimawandel"
    cc_concern_intro = "Inwieweit stimmen Sie den folgenden Aussagen zu?"
    cc_concern1_label = "Ich mache mir Sorgen, dass sich der Zustand des Klimas verändert."
    cc_concern2_label = "Klimaschutz ist wichtig für unsere Zukunft."
    cc_concern3_label = "Wir müssen das Gleichgewicht des Klimas schützen."
    cc_concern4_label = "Der Klimawandel hat schwerwiegende Folgen für Mensch und Natur."

    # Environmental attitude (Engel et al., 2023)
    environmental_attitude_title = "Einstellung zur Umwelt"

    environmental_attitude_q1 = "Welche der folgenden Aussagen beschreibt Sie persönlich am besten?"
    environmental_attitude_q1a1 = "Umweltschutz ist ein zentraler Lebensinhalt."
    environmental_attitude_q1a2 = "Ich sehe mich selbst als Umweltschützer:in."
    environmental_attitude_q1a3 = "Ich versuche, einen Kompromiss zwischen Umwelt schützen und mir etwas zu gönnen zu finden."
    environmental_attitude_q1a4 = "Da es technologische Lösungen zur Bekämpfung des Klimawandels geben wird, brauche ich mich nicht einzuschränken."
    environmental_attitude_q1a5 = "Umweltschutz interessiert mich nicht."
    environmental_attitude_q1a6 = "Ich kann mich mit keiner dieser Aussagen identifizieren."

    environmental_attitude_q2 = "Welche der folgenden Meinungen zu Umweltpolitik würden Sie am ehesten vertreten?"
    environmental_attitude_q2a1 = "Umweltschutz sollte im 21. Jahrhundert das zentrale Ziel politischen Handelns sein."
    environmental_attitude_q2a2 = "Eine effektive Umweltpolitik führt zu tiefgreifenden Einschränkungen."
    environmental_attitude_q2a3 = "Wir als wohlhabende Gesellschaft tragen die Verantwortung, den Klimaschutz in der Welt voranzubringen."
    environmental_attitude_q2a4 = "Es ist die Aufgabe der Regierung, etwas gegen den menschengemachten Klimawandel zu unternehmen."
    environmental_attitude_q2a5 = "Ich bin gegen politische Maßnahmen zum Schutz des Klimas."
    environmental_attitude_q2a6 = "Ich vertrete keine dieser Meinungen."

    environmental_attitude_q3 = "Welche der folgenden Meinungen zum Klimawandel würden Sie am ehesten vertreten?"
    environmental_attitude_q3a1 = "Der Klimawandel ist die größte Herausforderung der Menschheit."
    environmental_attitude_q3a2 = "Mich macht der Klimawandel persönlich betroffen."
    environmental_attitude_q3a3 = "Alle Menschen sollten ihren Teil zur Eindämmung des Klimawandels beitragen."
    environmental_attitude_q3a4 = "Der Klimawandel ist menschengemacht."
    environmental_attitude_q3a5 = "Der Klimawandel stellt kein wirkliches Problem dar."
    environmental_attitude_q3a6 = "Ich vertrete keine dieser Meinungen."

    environmental_attitude_q4 = "Welche der folgenden Aussagen beschreibt am besten Ihre Haltung zum Umweltschutz?"
    environmental_attitude_q4a1 = "Der Umweltschutz leitet mir wichtige Lebensentscheidungen, wie zum Beispiel Wohnsituation und Beruf."
    environmental_attitude_q4a2 = "Indem ich mich öffentlich für Umweltschutz einsetze, zeige ich anderen, wie wichtig	er ist."
    environmental_attitude_q4a3 = "Ich fühle mich verpflichtet, meinen Beitrag zum Umweltschutz zu leisten."
    environmental_attitude_q4a4 = "Umweltschutz ergibt nur Sinn, wenn auch die größten CO2-Emittenten, China und USA, Maßnahmen ergreifen."
    environmental_attitude_q4a5 = "Umweltschutz ist mir ziemlich egal."
    environmental_attitude_q4a6 = "Ich kann mich mit keiner dieser Aussagen identifizieren."

    # Trust in government
    trust_in_government_title = "Vertrauen in die Regierung"

    trust_in_government_q1 = "Welche der folgenden Aussagen beschreibt Ihre Meinung zu den Fähigkeiten der Regierung am besten?"
    trust_in_government_q1a1 = "Ich vertraue keiner Form von Regierung."
    trust_in_government_q1a2 = "Ich glaube, dass die Regierung Notfälle meistern kann."
    trust_in_government_q1a3 = "Ich denke, dass die Regierung in der Lage ist, gesellschaftliche Probleme anzugehen."
    trust_in_government_q1a4 = "Ich habe Vertrauen in den Weitblick der Regierung."
    trust_in_government_q1a5 = "Ich glaube, dass die Regierung weiß, was das Beste ist, selbst wenn ich anderer Meinung bin."
    trust_in_government_q1a6 = "Ich unterstütze keine dieser Aussagen."

    trust_in_government_q2 = "Welche der folgenden Aussagen beschreibt Ihre Meinung zu politischen Prozessen in der Regierung am besten?"
    trust_in_government_q2a1 = "Ich habe kein Vertrauen in irgendeine staatliche Institution."
    trust_in_government_q2a2 = "Ich glaube, dass Wahlen in meinem Land größtenteils fair ablaufen."
    trust_in_government_q2a3 = "Ich glaube, dass staatliche Maßnahmen nicht nur mir persönlich, sondern auch anderen zugutekommen."
    trust_in_government_q2a4 = "Ich denke, dass die Regierung Maßnahmen umsetzt, die den langfristigen Wohlstand der gesamten Gesellschaft sichern."
    trust_in_government_q2a5 = "Ich stelle politische Maßnahmen der Regierung nicht infrage."
    trust_in_government_q2a6 = "Ich kann mich mit keiner dieser Aussagen identifizieren."

    trust_in_government_q3 = "Welche der folgenden Aussagen beschreibt am besten Ihre Meinung dazu, wie die Regierung Ihr Leben beeinflusst?"
    trust_in_government_q3a1 = "Ich denke, dass Regierungen keinen positiven Einfluss haben können."
    trust_in_government_q3a2 = "Ich vertraue der Regierung, grundlegende Dienstleistungen wie Wasser und Strom bereitzustellen."
    trust_in_government_q3a3 = "Ich glaube, dass staatliche Maßnahmen meine Lebensqualität positiv beeinflussen."
    trust_in_government_q3a4 = "Ich vertraue den Entscheidungen der Regierung, auch wenn sie mich kurzfristig negativ beeinflussen."
    trust_in_government_q3a5 = "Die Regierung beschützt mich immer."
    trust_in_government_q3a6 = "Ich unterstütze keine dieser Aussagen."

    trust_in_government_q4 = "Welche der folgenden Aussagen beschreibt Ihre Beziehung zur Regierung am besten?"
    trust_in_government_q4a1 = "Ich ziehe es vor, unabhängig von jeder Einmischung der Regierung zu leben."
    trust_in_government_q4a2 = "Ich glaube, dass die Regierung die öffentliche Ordnung aufrechterhalten kann."
    trust_in_government_q4a3 = "Ich vertraue darauf, dass staatliche Prozesse fair und gerecht sind."
    trust_in_government_q4a4 = "Ich glaube, dass die Regierung gute Arbeit dabei leistet, aktuelle und zukünftige Perspektiven auszubalancieren."
    trust_in_government_q4a5 = "Ich denke, öffentliche Kontrolle der Regierung ist unnötig."
    trust_in_government_q4a6 = "Ich kann mich mit keiner dieser Aussagen identifizieren."

    # Attention Check

    attention_check_2_label = "Um zu zeigen, dass Sie die Anweisungen dieser Umfrage sorgfältig lesen, wählen Sie bei dieser Frage bitte Mercedes aus."
    ford = "Ford"
    volkswagen = "Volkswagen"
    mercedes = "Mercedes"
    toyota = "Toyota"
    subaru = "Subaru"

    # Political Orientation
    pol_orientation_title = "Politische Orientierung"
    pol_orientation_text = ("<b>Progressiv</b> und <b>konservativ</b> sind Begriffe, die häufig zur Beschreibung der politischen "
                            "Orientierung verwendet werden. Bitte geben Sie auf der folgenden Skala von 1 (extrem progressiv) bis 10 (extrem konservativ) an, wie Sie sich selbst politisch einordnen.")
    strongly_liberal = "Extrem progressiv"
    moderate = "Mittel"
    strongly_conservative = "Extrem konservativ"

    # Comments
    comments_title = "Möchten Sie uns einen Kommentar oder ein Feedback hinterlassen?"
    comments_instruction = "Bitte schreiben Sie Ihre Kommentare in das Feld oder lassen Sie es leer."
