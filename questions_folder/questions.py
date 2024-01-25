import random

questions_dict = {
    1: {
        'question': 'Welches Land ist aktuell Fußballrekordweltmeister? (Stand 01.2024)',
        'first_possible_answer': 'Italien',
        'second_possible_answer': 'Frankreich',
        'third_possible_answer': 'Brasilien',
        'fourth_possibe_answer': 'Deutschland',
        'question_answer': 'Brasilien',
        'question_category': 'Sport',
        'category_picture': 'sports.jpg'
    },
    2: {
        'question': 'Welcher Tennisspieler steht aktuell auf dem ersten PLatz der ATP-Waltrangliste? (Stand 01.2024)',
        'possible_answers': ['Novak Đoković', 'Roger Federer', 'Boris Becker', 'Alexander Zverev'],
        'right_answer': 'Novak Đoković',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    3: {
        'question': 'Welche beiden NFL-Teams haben die meisten Super-Bowl Siege?',
        'possible_answers': ['Kansas City Chiefs und Green Bay Packers', 'San Francisco 49ers und Kansas City Chiefs', 'New England Patriots und New York Jets', 'Pittsburgh Steelers und New England Patriots'],
        'right_answer': 'Pittsburgh Steelers und New England Patriots',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    4: {
        'question': 'Wie viele Siege hat Wladimir Klitschko in seiner Boxkarriere einfahren können?',
        'possible_answers': ['53', '64', '77', '49'],
        'right_answer': '64',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    5: {
        'question': 'Wie heißt der Fußballspieler, der auf Vereins- und Notionalmannschaftsebene die meisten Titel gewonnen hat? (Stand 01.2024)',
        'possible_answers': ['Dani Alves', 'Andrés Iniesta', 'Lionel Messi', 'David Beckham'],
        'right_answer': 'Dani Alves',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    6: {
        'question': 'Für welches NBA-Team bestritt Kobe Bryant 2016 das letzte Spiel seiner Karriere?',
        'possible_answers': ['Los Angeles Clippers', 'Bosten Celtics', 'Denver Nuggets', 'Los Angeles Lakers'],
        'right_answer': 'Los Angeles Lakers',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    7: {
        'question': 'Welcher Fußballspieler ist Deutschlands Rekordnationalspieler? (Stand 01.2024)',
        'possible_answers': ['Franz Beckanbauer', 'Philipp Lahm', 'Lothar Matthäus', 'Diege Maradonna'],
        'right_answer': 'Lothar Matthäus',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    8: {
        'question': 'Welcher NFL-Quarterback hat in seier Karriere die meisten Touchdowns geworfen? (Stand 01.2024)',
        'possible_answers': ['Joe Montana', 'Jimmy Garoppolo', 'Patrick Mahomes', 'Tom Brady'],
        'right_answer': 'Tom Brady',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    9: {
        'question': 'Mit welchem Formel 1-Team ist Michael Schumacher 5 mal in Folge Weltmeister geworden?',
        'possible_answers': ['Ferarri', 'Mercedes', 'Red Bull', 'BMW'],
        'right_answer': 'Ferrari',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    10: {
        'question': 'Wie heißt der Golfer mit den meisten Major-Siegen?',
        'possible_answers': ['Jack Nicklaus', 'Tiger Woods', 'Brooks Koepka', 'Martin Kaymar'],
        'right_answer': 'Jack Nicklaus',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    11: {
        'question': 'Wer war der erste deutsche Bundeskanzler?',
        'possible_answers': ['Wolfgang Schäuble', 'Konrad Adenauer', 'Helmut Schmidt', 'Joachim Gauck'],
        'right_answer': 'Konrad Adenauer',
        'picture': '',
        'cotegory': 'Allgemeinbildung'
    },
    12: {
        'question': 'Welches Amt hat Frank Walter Steinmeier seit 2017 in Deutschland inne? (Stand 01.2024)',
        'possible_answers': ['Bundes Verteidigungsminister', 'Bundes Wirtschaftsminster', 'Bundeskanzler', 'Bundespräsident'],
        'right_answer': 'Bundespräsident',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    13: {
        'question': 'Wie viele Nachbarländer hat Deutschland',
        'possible_answers': ['7', '11', '5', '9'],
        'right_answer': '9',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    14: {
        'question': 'Welche Supermarktkette hat die meisten Filialen in Deutschland?',
        'possible_answers': ['Edeka', 'Rewe', 'Lidl', 'Aldi'],
        'right_answer': 'Edeka',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    15: {
        'question': 'Aus wie vielen Felder besteht ein Schachbrett?',
        'possible_answers': ['64', '32', '56', '49'],
        'right_answer': '64',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    16: {
        'question': 'Wie viele Länder sind Mitglied in der NATO? (Stand 01.2024)',
        'possible_answers': ['27', '32', '31', '19'],
        'right_answer': '31',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    17: {
        'question': 'In welcher Stadt ist der eigentliche Hauptsitz des EU-Parlaments?',
        'possible_answers': ['Genf', 'Straßburg', 'Brüssel', 'Kopenhagen'],
        'right_answer': 'Straßburg',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    18: {
        'question': 'Welcher Schriftzug steht über dem deutschen Bundestag?',
        'possible_answers': ['Einigkeit, Recht, Freiheit', '1894 (Baujahr)', 'Deutsches Vaterland', 'Dem Deutschen Volke'],
        'right_answer': 'Dem deutschen Volke',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    19: {
        'question': 'Was ist die Hauptkomponente von Luft?',
        'possible_answers': ['Sauerstoff', 'Stickstoff', 'Kohlendioxid', 'Wasserstoff'],
        'right_answer': 'Stickstoff',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    20: {
        'question': 'Wie heißt der profitabelste deutsch Autokonzern? (Stand 01.2024)',
        'possible_answers': ['Volkswagen', 'Mercedes', 'BMW', 'Audi'],
        'right_answer': 'Mercedes',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    21: {
        'question': 'Welcher Regisseur war für die Star Wars Filmreihe verantwortlich?',
        'possible_answers': ['George Lucas', 'Cristopher Nolan', 'Steven Spielberg', 'James Cameron'],
        'right_answer': 'George Lucas',
        'picture': '',
        'category': 'Filme/Comics'
    },
    22: {
        'question': 'Wann wurde Disney gegründet?',
        'possible_answers': ['1922', '1873', '1923', '1898'],
        'right_answer': '1923',
        'picture': '',
        'category': 'Filme/Comics'
    },
    23: {
        'question': 'Welches ist der erfolgreichste Film aller Zeiten? (Stand 01.2024)',
        'possible_answers': ['Avengers: Endgame', 'Avatar', 'Titanic', 'Ben-Hur'],
        'right_answer': 'Avatar',
        'picture': '',
        'category': 'Filme/Comics'
    },
    24: {
        'question': 'Welches ist der teuerste Film aller Zeiten? (Stand 01.2024)',
        'possible_answers': ['Titanic', 'Der Pate', 'Vom Winde verweht', 'Avatar: The Way of Water'],
        'right_answer': 'Avatar: The Way of Water',
        'picture': '',
        'category': 'Filme/Comics'
    },
    25: {
        'question': 'Welcher Schauspieler verkörpert die Rolle von Iron Man im Marvel Cinematic Universe?',
        'possible_answers': ['Chris Evans', 'Chris Hemsworth', 'Robert Downey Jr.', 'Mark Ruffalo'],
        'right_answer': 'Robert Downey Jr.',
        'picture': '',
        'category': 'Filme/Comics'
    },
    26: {
        'question': 'Wie viele Teile gibt es in der originalen "Star Wars"-Trilogie von 1977 bis 1983?',
        'possible_answers': ['2', '3', '4', '5'],
        'right_answer': '3',
        'picture': '',
        'category': 'Filme/Comics'
    },
    27: {
        'question': 'Welcher Schauspieler spielt die Hauptrolle in der "Harry Potter" -Filmreihe?',
        'possible_answers': ['Daniel Radcliffe', 'Rupert Grint', 'Emma Watson', 'Tom Felton'],
        'right_answer': 'Daniel Radcliffe',
        'picture': '',
        'category': 'Filme/Comics'
    },
    28: {
        'question': 'Welcher Schauspieler spielt die Hauptrolle in der "John Wick"-Filmreihe?',
        'possible_answers': ['Tom Hardy', 'Keanu Reeves', 'Liam Neeson', 'Jason Statham'],
        'right_answer': 'Keanu Reeves',
        'picture': '',
        'category': 'Filme/Comics'
    },
    29: {
        'question': 'In welchem Jahr wurde der Oscar für den Besten Animationsfilm zum ersten Mal verliehen?',
        'possible_answers': ['1995', '2006', '2001', '2010'],
        'right_answer': '2001',
        'picture': '',
        'category': 'Filme/Comics'
    },
    30: {
        'question': 'Welcher Schauspieler verstarb im Jahr 2013 bei einem Autounfall?',
        'possible_answers': ['Robin Williams', 'Philip Seymour Hoffman', 'Paul Walker', 'Philip Seymour Hoffman'],
        'right_answer': 'Paul Walker',
        'picture': '',
        'category': 'Filme/Comics'
    },
    31: {
        'question': 'Wann endete der Erste Weltkrieg?',
        'possible_answers': ['1918', '1917', '1921', '1914'],
        'right_answer': '1918',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    32: {
        'question': 'Welches Ereignis markiert das Ende des Römischen Reiches?',
        'possible_answers': ['Schlacht von Cannae', 'Fall von Konstantinopel', 'Schlacht im Teutoburger Wald', 'Untergang von Rom'],
        'right_answer': 'Fall von Konstantinopel',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    33: {
        'question': 'Wann wurde die Berliner Mauer errichtet?',
        'possible_answers': ['1945', '1946', '1973', '1961'],
        'right_answer': '1961',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    34: {
        'question': 'Wann endete der Korea-Krieg?',
        'possible_answers': ['1953', '1952', '1951', '1956'],
        'right_answer': '1953',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    35: {
        'question': 'Welche Stadt wurde im Jahr 79 n. Chr. durch den Ausbruch des Vesuvs zerstört?',
        'possible_answers': ['Rom', 'Pompeji', 'Alexandria', 'Athen'],
        'right_answer': 'Pompeji',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    36: {
        'question': 'Welche Schlacht markiert das Ende der Napoleonischen Kriege in Europa?',
        'possible_answers': ['Schlacht von Austerlitz', 'Schlacht von Leipzig', 'Schlacht von Waterloo', 'Schlacht von Borodino'],
        'right_answer': 'Schlacht von Waterloo',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    37: {
        'question': 'Welcher berühmte Seefahrer führte die erste dokumentierte Reise um die Welt an?',
        'possible_answers': ['Marco Polo', 'Ferdinand Magellan', 'Christopher Kolumbus', 'James Cook'],
        'right_answer': 'Ferdinand Magellan',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    38: {
        'question': 'Welcher berühmte Herrscher führte das Römische Reich zur größten Ausdehnung?',
        'possible_answers': ['Augustus', 'Nero', 'Trajan', 'Julius Caesar'],
        'right_answer': 'Julius Caesar',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    39: {
        'question': 'Welche antike Zivilisation entwickelte die Demokratie in der Stadt Athen?',
        'possible_answers': ['Römisches Reich', 'Ägyptische Zivilisation', 'Griechisches Reich', 'Persisches Reich'],
        'right_answer': 'Griechisches Reich',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    40: {
        'question': 'Welcher antike Herrscher führte die mächtige persische Armee in den Kriegen gegen die Griechen, einschließlich der Schlacht bei den Thermopylen?',
        'possible_answers': ['Xerxes I.', 'Artaxerxes I.', 'Cyrus der Große', 'Darius I.'],
        'right_answer': 'Xerxes I.',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    41: {
        'question': 'Welches nordische Land wird auch als "Land der Mitternachtssonne" bezeichnet',
        'possible_answers': ['Russland', 'Island', 'Schweden', 'Norwegen'],
        'right_answer': 'Norwegen',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    42: {
        'question': 'Welche Inselgruppe gehört zu Dänemark und ist für ihre einzigartige Natur bekannt?',
        'possible_answers': ['Färöer-Inseln', 'Südliche Sandwichinseln', 'Azoren', 'Helgoland'],
        'right_answer': 'Färöer-Inseln',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    43: {
        'question': 'Wie heißt der längste Fluss der durch Deutschland fließt?',
        'possible_answers': ['Neckar', 'Rhein', 'Donau', 'Weser'],
        'right_answer': 'Rhein',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    44: {
        'question': 'In welchem Land befindet sich der Kilimandscharo, der höchste Berg Afrikas?',
        'possible_answers': ['Kenia', 'Äthiopien', 'Tansania', 'Uganda'],
        'right_answer': 'Tansania',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    45: {
        'question': 'Welcher Kontinent ist auch als "Down Under" bekannt?',
        'possible_answers': ['Südamerika', 'Australien', 'Afrika', 'Asien'],
        'right_answer': 'Australien',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    46: {
        'question': 'Welcher Fluss fließt durch Kairo?',
        'possible_answers': ['Nil', 'Euphrat', 'Tigris', 'Jordan'],
        'right_answer': 'Nil',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    47: {
        'question': 'Welches Gebirge trennt Europa von Asien?',
        'possible_answers': ['Die Anden', 'Die Rocky Mountains', 'Der Himalaya', 'Das Uralgebirge'],
        'right_answer': 'Das Uralgebirge',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    48: {
        'question': 'Welches Land wird als "Land der aufgehenden Sonne" bezeichnet?',
        'possible_answers': ['China', 'Japan', 'Südkorea', 'Vietnam'],
        'right_answer': 'Japan',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    49: {
        'question': 'Welches Land hat die längste Küstenlinie der Welt?',
        'possible_answers': ['Brasilien', 'Australien', 'Russland', 'Kanada'],
        'right_answer': 'Kanada',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    50: {
        'question': 'Welches Land wird als "Land der tausend Seen" bezeichnet?',
        'possible_answers': ['Finnland', 'Kanada', 'Kenia', 'Amerika'],
        'right_answer': 'Finnland',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    51: {
        'question':'Wie heißt der größte Planet unseres Sonnensystems?',
        'possible_answers':['Jupter', 'Uranus', 'Venus', 'Mars'],
        'right_answer':'Jupiter',
        'picture':'',
        'category':'Astronomie'
    },
    52: {
        'question':'Was ist ein Komet',
        'possible_answers':['Ein kleiner Planet', 'Eine schmutzige Schneekugel aus Eis und Staub', 'Ein felsiger Himmeslkörper', 'Ein wandelnder Stern'],
        'right_answer':'Eine schmutzige Schneekugel aus Eis und Staub',
        'picture':'',
        'category':'Astronomie'
    },
    53: {
        'question':'Welcher Planet hat deutlich sichtbare Ringe?',
        'possible_answers':['Mars', 'Venus', 'Saturn', 'Uranus'],
        'right_answer':'Saturn',
        'picture':'',
        'category':'Astronomie'
    },
    54: {
        'question':'Was verursacht eine Supernova?',
        'possible_answers':['Kollision von Planeten', 'Kollision von Galaxien', 'Erlöschung eines schwarzen Lochs', 'Explosion eines massiven Sterns'],
        'right_answer':'Explosion eines massiven Sterns',
        'picture':'',
        'category':'Astronomie'
    },
    55: {
        'question':'Welche Galaxie ist die nächste zu unserer Milchstraße?',
        'possible_answers':['Andromeda-Galaxie', 'Sombrero-Galaxie', 'Socratis-Galaxie', 'Dreiecks-Galaxie'],
        'right_answer':'Andromeda-Galaxie',
        'picture':'',
        'categoy':'Astronomie'
    },
    56: {
        'question':'Welches Sternbild enthält den Polarstern?',
        'possible_answers':['Orion', 'Ursa (Großer Bär)', 'Scorpius (Skorpion)', 'Leo (Löwe)'],
        'right_answer':'Ursa (Großer Bär)',
        'picture':'',
        'category':'Astronomie'
    },
    57: {
        'question':'Was ist ein Exoplanet',
        'possible_answers':['Ein nicht entwickelter Planet', 'Ein Mond eines anderen Planeten', 'Ein Planet außerhalb unseres Sonnensystems', 'Ein künstlich geschaffener Himmelskörper'],
        'right_answer':'Ein Planet außerhalb unseres Sonnensystems',
        'picture':'',
        'categoy':'Astronomie'
    },
    58: {
        'question':'Welches Phänomen tritt ein, wenn ein kleiner Himmelskörper in die Erdatmosphäre eintritt und verglüht?',
        'possible_answers':['Meteoriteneinschlag', 'Komet', 'Asteroid', 'Meteor'],
        'right_answer':'Meteor',
        'picture':'',
        'category':'Astronomie'
    },
    59: {
        'question':'Wie heißt das leistungsstärkste Weltraumteleskop, das für Infrarotbeobachtungen konzipiert wurde?',
        'possible_answers':['Hubble-Teleskop', 'James Webb Space Telescope', 'Kepler-Telescope', 'Spitzer-Telescope'],
        'right_answer':'James Webb Space Telescope',
        'picture':'',
        'category':'Astronomie'
    },
    60: {
        'question':'Welches Ereignis tritt aus, wenn die Erde den küzesten Tag des Jahres hat?',
        'possible_answers':['Herbstsonnenwende', 'Sommeranfang', 'Wintersonnenwende', 'Frühlingsanfang'],
        'right_answer':'Wintersonnenwende',
        'picture':'',
        'category':'Astronomie'
    },
    61: {
        'question':'Welches ist das härteste natürliche Material auf der Erde?',
        'possible_answers':['Diamant', 'Quarz', 'Obsidian', 'Stahl'],
        'right_answer':'Diamant',
        'picture':'',
        'category':'Natur'
    },
    62: {
        'question':'Welches ist das größte Ökosystem aud der Erde?',
        'possible_answers':['Regenwald', 'Wüste', 'Tundra', 'Ozean'],
        'right_answer':'Ozean',
        'picture':'',
        'category':'Natur'
    },
    63: {
        'question':'Welches ist das älteste lebende Baumsystem der Welt?',
        'possible_answers':['Bristelcone-Kiefern', 'Eukalyptus-Bäume', 'Ginkgo-Bäume', 'Redwood-Bäume'],
        'right_answer': 'Bristlecone-Bäume',
        'picture':'',
        'category':'Natur'
    },
    64: {
        'question':'Welches ist das größste Riff-Ökosystem der Welt?',
        'possible_answers':['floida Keys Reef', 'Maldives Coral Reef', 'Great Barrier Reef', 'Belize Barrier Reef'],
        'right_answer':'Great Barrier Reef',
        'picture':'',
        'category':'Natur'
    },
    65: {
        'question':'Welches Gas ist für die grüne Farbe in Pflanzen verantwortlich',
        'possible_answers':['Chlorophyl', 'Kohlenstoff', 'Sauerstoff', 'Stickstoff'],
        'right_answer':'Chlorophyl',
        'picture':'',
        'category':'Natur'
    },
    66: {
        'question':'Welche der folgenden Blumen repräsentiert normalerweise Frieden und Ruhe?',
        'possible_answers':['rose', 'Tulpe', 'Lilie', 'Kamille'],
        'right_answer':'Lilie',
        'picture':'',
        'category':'Natur'
    },
    67: {
        'question':'Welches ist der größte Wüstentyp der Welt?',
        'possible_answers':['Sahare-Wüste', 'Gobi-Wüste', 'Antarktische-Wüste', 'Mojave-Wüste'],
        'right_answer':'Antarktische Wüste',
        'picture':'',
        'category':'Natur'
    },
    68: {
        'question':'Welches ist das größte Lebewesen auf dem Land?',
        'possible_answers':['Giraffe', 'Elefant', 'Blauwal', 'Sequioa-Baum'],
        'right_answer':'Sequioa-Baum',
        'picture':'',
        'category':'Natur'
    },
    69: {
        'question':'Wie heißt der größte Ozean unseres Planeten?',
        'possible_answers':['Pazifischer Ozean', 'Indischer Ozean', 'Südlicher Ozean', 'Atlantischer Ozean'],
        'right_answer':'Pazifischer Ozean',
        'picture':'',
        'category':'Natur'
    },
    70: {
        'question':'Was ist ein Tundra-Ökosystem?',
        'possible_answers':['Ein Gebiet mit ewigem Eis', 'Eine große Wüste', 'Ein trockenes Grasland', 'Ein Baumbestand aus Nadelbäumen'],
        'right_answer':'Ein Gebiet mit ewigem Eis',
        'picture':'',
        'category':'Natur'
    },
    71: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    72: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    73: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    74: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    75: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    76: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    77: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    78: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    79: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    80: {
        'question':'',
        'possible_answers':['', '', '', ''],
        'right_answer':'',
        'picture':'',
        'category':'Informatik'
    },
    81: {
        'question':'Welcher Vogel hat den längesten jährlichen Zugweg?',
        'possible_answers':['Kolibri', 'Kondor', 'Albatros', 'Storch'],
        'right_answer':'Albatros',
        'picture':'',
        'category':'Tiere'
    },
    82: {
        'question':'Welches Tier kann durch Mimkry das Aussehen von anderen gefährlichen Tieren imitieren?',
        'possible_answers':['Chamäleon', 'Oktopus', 'Fledermaus', 'Pfeilgiftfrosch'],
        'right_answer':'Pfeilgiftfrosch',
        'picture':'',
        'category':'Tiere'
    },
    83: {
        'question':'In welchem natürlichen Lebensraum leben Kängurus typischerweise?',
        'possible_answers':['Wüste', 'Tundra', 'Regenwald', 'Grasland'],
        'right_answer':'Grasland',
        'picture':'',
        'category':'Tiere'
    },
    84: {
        'question':'Welches Tier hält den längesten Winterschlaf?',
        'possible_answers':['Bär', 'Fledermaus', 'Igel', 'Eichhörnchen'],
        'right_answer':'Fledermaus',
        'picture':'',
        'category':'Tiere'
    },
    85: {
        'question':'Welches Reptil kann am längesten ohne Nahrung überleben?',
        'possible_answers':['Schlange', 'Leguan', 'Schildkröte', 'Krokodil'],
        'right_answer':'Krokodil',
        'picture':'',
        'category':'Tiere'
    },
    86: {
        'question':'Wie heißt das schnellste Meerestier?',
        'possible_answers':['Orca', 'Weißer Hai', 'Thunfisch', 'Delfin'],
        'right_answer':'Thunfisch',
        'picture':'',
        'category':'Tiere'
    },
    87: {
        'question':'Wie heißt das einzige Flugfähige Säugetier?',
        'possible_answers':['Flughund', 'Pinguin', 'Mistkäfer', 'Fledermaus'],
        'right_answer':'Fledermaus',
        'picture':'',
        'category':'Tiere'
    },
    88: {
        'question':'Welches Tier kann seinen Schwanz abwerfen, um Feinde zu täuschen?',
        'possible_answers':['Gecko', 'Leguan', 'Eidechse', 'Lalamander'],
        'right_answer':'',
        'picture':'',
        'category':'Tiere'
    },
    89: {
        'question':'Welche beiden Säugetiere legen Eier?',
        'possible_answers':['', 'Schnabeltiere und Ameisenigel', '', ''],
        'right_answer':'Schnabeltiere und Ameisenigel',
        'picture':'',
        'category':'Tiere'
    },
    90: {
        'question':'Welcher Vogel ist für seinen kunstvollen Nestbau in Form einer Tasche bekannt?',
        'possible_answers':['Elster', 'Webervogel', 'Spatz', 'Storch'],
        'right_answer':'Webervogel',
        'picture':'',
        'category':'Tiere'
    },
    91: {
        'question':'Was ist die Einheit der elektrischen Spannung',
        'possible_answers':['Watt', 'Volt', 'Ampere', 'Ohm'],
        'right_answer':'Volt',
        'picture':'',
        'category':'Wisschenschaft'
    },
    92: {
        'question':'Welche Einheit wird verwendet um Radioaktivität zu messen?',
        'possible_answers':['Sievert', 'Rad', 'Rem', 'Gray'],
        'right_answer':'Sievert',
        'picture':'',
        'category':'Wisschenschaft'
    },
    93: {
        'question':'Welches Element hat die chemische Bezeichnung "FE"?',
        'possible_answers':['Kalzium', 'Flur', 'Kalium', 'Eisen'],
        'right_answer':'Eisen',
        'picture':'',
        'category':'Wisschenschaft'
    },
    94: {
        'question':'Wer formulierte die Theorie der Evolution durch natürliche Auslese?',
        'possible_answers':['Gregor Mendel', 'Alfred Wegener', 'Charles Darwin', 'Linus Pauling'],
        'right_answer':'Charles Darwin',
        'picture':'',
        'category':'Wisschenschaft'
    },
    95: {
        'question':'Welches Organ im menschlichen Körper ist für die Blutbildung verantwortlich?',
        'possible_answers':['Knochenmark', 'Herz', 'Leber', 'Niere'],
        'right_answer':'Knochenmark',
        'picture':'',
        'category':'Wisschenschaft'
    },
    96: {
        'question':'Welches Organ ist für die Regulation des Blutzuckerspiegels verantwortlich?',
        'possible_answers':['Niere', 'Bauchspeicheldrüse', 'Leber', 'Darm'],
        'right_answer':'Bauchspeicheldrüse',
        'picture':'',
        'category':'Wisschenschaft'
    },
    97: {
        'question':'Welches Vitamin wird als "Sonnenvitamin" bezeichnet?',
        'possible_answers':['Vitamin A', 'Vitamin B', 'Vitamin D', 'Vitamin K'],
        'right_answer':'Vitamin D',
        'picture':'',
        'category':'Wisschenschaft'
    },
    98: {
        'question':'Welches ist das häufigste Edelgas in der Erdkruste?',
        'possible_answers':['Helium', 'Neon', 'Krypton', 'Argon'],
        'right_answer':'Argon',
        'picture':'',
        'category':'Wisschenschaft'
    },
    99: {
        'question':'Welcher Wissenschaftler entwickelte die Theorie der Quantentechnik?',
        'possible_answers':['Albert Einstein', 'Erwin Schrödinger', 'Niels Rohr', 'Max Planck'],
        'right_answer':'Max Planck',
        'picture':'',
        'category':'Wisschenschaft'
    },
    100: {
        'question':'Welches ist das erste kommerzielle Elektroauto, das weltweit anerkannt wurde?',
        'possible_answers':['Nissan Leaf', 'Tesla Roadster', 'Toyota Pirus', 'Chevrolet Volt'],
        'right_answer':'Tesla Roadster',
        'picture':'',
        'category':'Wisschenschaft'
    },
}

# Funktion um zufällig 10 Fragen auszuwählen
def get_random_questions():
    questions_keys = list(questions_dict.keys()) # holt die Fragen durch die Nummerierung (Schlüssel) aus dem Dictionary
    random_questions_keys = random.sample(questions_keys, 10) # zufällige Auswahl von 10 Fragen
    random_questions = {key: questions_dict[key] for key in random_questions_keys} # erstellt neues Dictionary mit den ausgewählten 10 Fragen
    return random_questions # neues Dictionary wird zurückgegeben
