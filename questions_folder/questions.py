import random

questions_dict = {
    1: {
        'question': 'Welches Land ist aktuell Fußballrekordweltmeister? (Stand 01.2024)',
        'possible_answers': ['Italien', 'Frankreich', 'Brasilien', 'Deutschland'],
        'question_answer': 'Brasilien',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    2: {
        'question': 'Welcher Tennisspieler steht aktuell auf dem ersten PLatz der ATP-Waltrangliste? (Stand 01.2024)',
        'possible_answers': ['Novak Đoković', 'Roger Federer', 'Boris Becker', 'Alexander Zverev'],
        'question_answer': 'Novak Đoković',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    3: {
        'question': 'Welche beiden NFL-Teams haben die meisten Super-Bowl Siege?',
        'possible_answers': ['Kansas City Chiefs, \nGreen Bay Packers', 'San Francisco 49ers, \nKansas City Chiefs', 'New England Patriots, \nNew York Jets', 'Pittsburgh Steelers, \nNew England Patriots'],
        'question_answer': 'Pittsburgh Steelers und New England Patriots',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    4: {
        'question': 'Wie viele Siege hat Wladimir Klitschko in seiner Boxkarriere einfahren können?',
        'possible_answers': ['53', '64', '77', '49'],
        'question_answer': '64',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    5: {
        'question': 'Wie heißt der Fußballspieler, der auf Vereins- und \nNotionalmannschaftsebene die meisten Titel gewonnen hat? (Stand 01.2024)',
        'possible_answers': ['Dani Alves', 'Andrés Iniesta', 'Lionel Messi', 'David Beckham'],
        'question_answer': 'Dani Alves',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    6: {
        'question': 'Für welches NBA-Team bestritt Kobe Bryant 2016 das letzte Spiel seiner Karriere?',
        'possible_answers': ['Los Angeles Clippers', 'Bosten Celtics', 'Denver Nuggets', 'Los Angeles Lakers'],
        'question_answer': 'Los Angeles Lakers',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    7: {
        'question': 'Welcher Fußballspieler ist Deutschlands Rekordnationalspieler? (Stand 01.2024)',
        'possible_answers': ['Franz Beckanbauer', 'Philipp Lahm', 'Lothar Matthäus', 'Diege Maradonna'],
        'question_answer': 'Lothar Matthäus',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    8: {
        'question': 'Welcher NFL-Quarterback hat in seiner Karriere die meisten Touchdowns geworfen? (Stand 01.2024)',
        'possible_answers': ['Joe Montana', 'Jimmy Garoppolo', 'Patrick Mahomes', 'Tom Brady'],
        'question_answer': 'Tom Brady',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    9: {
        'question': 'Mit welchem Formel 1-Team ist Michael Schumacher 5 mal in Folge Weltmeister geworden?',
        'possible_answers': ['Ferrari', 'Mercedes', 'Red Bull', 'BMW'],
        'question_answer': 'Ferrari',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    10: {
        'question': 'Wie heißt der Golfer mit den meisten Major-Siegen?',
        'possible_answers': ['Jack Nicklaus', 'Tiger Woods', 'Brooks Koepka', 'Martin Kaymar'],
        'question_answer': 'Jack Nicklaus',
        'picture': 'sports.jpg',
        'current_category': 'Sport'
    },
    11: {
        'question': 'Wer war der erste deutsche Bundeskanzler?',
        'possible_answers': ['Wolfgang Schäuble', 'Konrad Adenauer', 'Helmut Schmidt', 'Joachim Gauck'],
        'question_answer': 'Konrad Adenauer',
        'picture': 'general_knowledge.jpg',
        'cotegory': 'Allgemeinbildung'
    },
    12: {
        'question': 'Welches Amt hat Frank Walter Steinmeier seit 2017 in Deutschland inne? (Stand 01.2024)',
        'possible_answers': ['Bundes Verteidigungsminister', 'Bundes Wirtschaftsminster', 'Bundeskanzler', 'Bundespräsident'],
        'question_answer': 'Bundespräsident',
        'picture': 'general_knowledge.jpg',
        'current_category': 'Allgemeinbildung'
    },
    13: {
        'question': 'Wie viele Nachbarländer hat Deutschland',
        'possible_answers': ['7', '11', '5', '9'],
        'question_answer': '9',
        'picture': 'general_knowledge.jpg',
        'current_category': 'Allgemeinbildung'
    },
    14: {
        'question': 'Welche Supermarktkette hat die meisten Filialen in Deutschland?',
        'possible_answers': ['Edeka', 'Rewe', 'Lidl', 'Aldi'],
        'question_answer': 'Edeka',
        'picture': 'general_knowledge.jpg',
        'current_category': 'Allgemeinbildung'
    },
    15: {
        'question': 'Aus wie vielen Felder besteht ein Schachbrett?',
        'possible_answers': ['64', '32', '56', '49'],
        'question_answer': '64',
        'picture': 'general_knowledge.jpg',
        'current_category': 'Allgemeinbildung'
    },
    16: {
        'question': 'Wie viele Länder sind Mitglied in der NATO? (Stand 01.2024)',
        'possible_answers': ['27', '32', '31', '19'],
        'question_answer': '31',
        'picture': 'general_knowledge.jpg',
        'current_category': 'Allgemeinbildung'
    },
    17: {
        'question': 'In welcher Stadt ist der eigentliche Hauptsitz des EU-Parlaments?',
        'possible_answers': ['Genf', 'Straßburg', 'Brüssel', 'Kopenhagen'],
        'question_answer': 'Straßburg',
        'picture': 'general_knowledge.jpg',
        'current_category': 'Allgemeinbildung'
    },
    18: {
        'question': 'Welcher Schriftzug steht über dem deutschen Bundestag?',
        'possible_answers': ['Einigkeit, Recht, Freiheit', '1894 (Baujahr)', 'Deutsches Vaterland', 'Dem deutschen Volke'],
        'question_answer': 'Dem deutschen Volke',
        'picture': 'general_knowledge.jpg',
        'current_category': 'Allgemeinbildung'
    },
    19: {
        'question': 'Was ist die Hauptkomponente von Luft?',
        'possible_answers': ['Sauerstoff', 'Stickstoff', 'Kohlendioxid', 'Wasserstoff'],
        'question_answer': 'Stickstoff',
        'picture': 'general_knowledge.jpg',
        'current_category': 'Allgemeinbildung'
    },
    20: {
        'question': 'Wie heißt der profitabelste deutsch Autokonzern? (Stand 01.2024)',
        'possible_answers': ['Volkswagen', 'Mercedes', 'BMW', 'Audi'],
        'question_answer': 'Mercedes',
        'picture': 'general_knowledge.jpg',
        'current_category': 'Allgemeinbildung'
    },
    21: {
        'question': 'Welcher Regisseur war für die Star Wars Filmreihe verantwortlich?',
        'possible_answers': ['George Lucas', 'Cristopher Nolan', 'Steven Spielberg', 'James Cameron'],
        'question_answer': 'George Lucas',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    22: {
        'question': 'Wann wurde Disney gegründet?',
        'possible_answers': ['1922', '1873', '1923', '1898'],
        'question_answer': '1923',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    23: {
        'question': 'Welches ist der erfolgreichste Film aller Zeiten? (Stand 01.2024)',
        'possible_answers': ['Avengers: Endgame', 'Avatar', 'Titanic', 'Ben-Hur'],
        'question_answer': 'Avatar',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    24: {
        'question': 'Welches ist der teuerste Film aller Zeiten? (Stand 01.2024)',
        'possible_answers': ['Titanic', 'Der Pate', 'Vom Winde verweht', 'Avatar: The Way of Water'],
        'question_answer': 'Avatar: The Way of Water',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    25: {
        'question': 'Welcher Schauspieler verkörpert die Rolle von Iron Man im Marvel Cinematic Universe?',
        'possible_answers': ['Chris Evans', 'Chris Hemsworth', 'Robert Downey Jr.', 'Mark Ruffalo'],
        'question_answer': 'Robert Downey Jr.',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    26: {
        'question': 'Wie viele Teile gibt es in der originalen "Star Wars"-Trilogie von 1977 bis 1983?',
        'possible_answers': ['2', '3', '4', '5'],
        'question_answer': '3',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    27: {
        'question': 'Welcher Schauspieler spielt die Hauptrolle in der "Harry Potter" -Filmreihe?',
        'possible_answers': ['Daniel Radcliffe', 'Rupert Grint', 'Emma Watson', 'Tom Felton'],
        'question_answer': 'Daniel Radcliffe',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    28: {
        'question': 'Welcher Schauspieler spielt die Hauptrolle in der "John Wick"-Filmreihe?',
        'possible_answers': ['Tom Hardy', 'Keanu Reeves', 'Liam Neeson', 'Jason Statham'],
        'question_answer': 'Keanu Reeves',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    29: {
        'question': 'In welchem Jahr wurde der Oscar für den Besten Animationsfilm zum ersten Mal verliehen?',
        'possible_answers': ['1995', '2006', '2001', '2010'],
        'question_answer': '2001',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    30: {
        'question': 'Welcher Schauspieler verstarb im Jahr 2013 bei einem Autounfall?',
        'possible_answers': ['Robin Williams', 'Philip Seymour Hoffman', 'Paul Walker', 'Philip Seymour Hoffman'],
        'question_answer': 'Paul Walker',
        'picture': 'movies.jpg',
        'current_category': 'Filme'
    },
    31: {
        'question': 'Wann endete der Erste Weltkrieg?',
        'possible_answers': ['1918', '1917', '1921', '1914'],
        'question_answer': '1918',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    32: {
        'question': 'Welches Ereignis markiert das Ende des Römischen Reiches?',
        'possible_answers': ['Schlacht von Cannae', 'Fall von Konstantinopel', 'Schlacht im Teutoburger Wald', 'Untergang von Rom'],
        'question_answer': 'Fall von Konstantinopel',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    33: {
        'question': 'Wann wurde die Berliner Mauer errichtet?',
        'possible_answers': ['1945', '1946', '1973', '1961'],
        'question_answer': '1961',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    34: {
        'question': 'Wann endete der Korea-Krieg?',
        'possible_answers': ['1953', '1952', '1951', '1956'],
        'question_answer': '1953',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    35: {
        'question': 'Welche Stadt wurde im Jahr 79 n. Chr. durch den Ausbruch des Vesuvs zerstört?',
        'possible_answers': ['Rom', 'Pompeji', 'Alexandria', 'Athen'],
        'question_answer': 'Pompeji',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    36: {
        'question': 'Welche Schlacht markiert das Ende der Napoleonischen Kriege in Europa?',
        'possible_answers': ['Schlacht von Austerlitz', 'Schlacht von Leipzig', 'Schlacht von Waterloo', 'Schlacht von Borodino'],
        'question_answer': 'Schlacht von Waterloo',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    37: {
        'question': 'Welcher berühmte Seefahrer führte die erste dokumentierte Reise um die Welt an?',
        'possible_answers': ['Marco Polo', 'Ferdinand Magellan', 'Christopher Kolumbus', 'James Cook'],
        'question_answer': 'Ferdinand Magellan',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    38: {
        'question': 'Auf welche japanische Stadt wurde die erste Atombombe am 06. August 1945 abgeworfen?',
        'possible_answers': ['Nagasaki', 'Tschernobyl', 'Yokohama', 'Hiroshima'],
        'question_answer': 'Hiroshima',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    39: {
        'question': 'Welche antike Zivilisation entwickelte die Demokratie in der Stadt Athen?',
        'possible_answers': ['Römisches Reich', 'Ägyptische Zivilisation', 'Griechisches Reich', 'Persisches Reich'],
        'question_answer': 'Griechisches Reich',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    40: {
        'question': 'Welcher antike Herrscher führte die mächtige persische Armee in den Kriegen \ngegen die Griechen, einschließlich der Schlacht bei den Thermopylen?',
        'possible_answers': ['Xerxes I.', 'Artaxerxes I.', 'Cyrus der Große', 'Darius I.'],
        'question_answer': 'Xerxes I.',
        'picture': 'history.jpg',
        'current_category': 'Geschichte'
    },
    41: {
        'question': 'Welches nordische Land wird auch als "Land der Mitternachtssonne" bezeichnet',
        'possible_answers': ['Russland', 'Island', 'Schweden', 'Norwegen'],
        'question_answer': 'Norwegen',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    42: {
        'question': 'Welche Inselgruppe gehört zu Dänemark und ist für ihre einzigartige Natur bekannt?',
        'possible_answers': ['Färöer-Inseln', 'Südliche Sandwichinseln', 'Azoren', 'Helgoland'],
        'question_answer': 'Färöer-Inseln',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    43: {
        'question': 'Wie heißt der längste Fluss der durch Deutschland fließt?',
        'possible_answers': ['Neckar', 'Rhein', 'Donau', 'Weser'],
        'question_answer': 'Rhein',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    44: {
        'question': 'In welchem Land befindet sich der Kilimandscharo, der höchste Berg Afrikas?',
        'possible_answers': ['Kenia', 'Äthiopien', 'Tansania', 'Uganda'],
        'question_answer': 'Tansania',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    45: {
        'question': 'Welcher Kontinent ist auch als "Down Under" bekannt?',
        'possible_answers': ['Südamerika', 'Australien', 'Afrika', 'Asien'],
        'question_answer': 'Australien',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    46: {
        'question': 'Welcher Fluss fließt durch Kairo?',
        'possible_answers': ['Nil', 'Euphrat', 'Tigris', 'Jordan'],
        'question_answer': 'Nil',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    47: {
        'question': 'Welches Gebirge trennt Europa von Asien?',
        'possible_answers': ['Die Anden', 'Die Rocky Mountains', 'Der Himalaya', 'Das Uralgebirge'],
        'question_answer': 'Das Uralgebirge',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    48: {
        'question': 'Welches Land wird als "Land der aufgehenden Sonne" bezeichnet?',
        'possible_answers': ['China', 'Japan', 'Südkorea', 'Vietnam'],
        'question_answer': 'Japan',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    49: {
        'question': 'Welches Land hat die längste Küstenlinie der Welt?',
        'possible_answers': ['Brasilien', 'Australien', 'Russland', 'Kanada'],
        'question_answer': 'Kanada',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    50: {
        'question': 'Welches Land wird als "Land der tausend Seen" bezeichnet?',
        'possible_answers': ['Finnland', 'Kanada', 'Kenia', 'Amerika'],
        'question_answer': 'Finnland',
        'picture': 'geography.jpg',
        'current_category': 'Geographie'
    },
    51: {
        'question': 'Wie heißt der größte Planet unseres Sonnensystems?',
        'possible_answers': ['Jupter', 'Uranus', 'Venus', 'Mars'],
        'question_answer': 'Jupiter',
        'picture': 'astronomy.jpg',
        'current_category': 'Astronomie'
    },
    52: {
        'question': 'Was ist ein Komet',
        'possible_answers': ['Ein kleiner Planet', 'Eine schmutzige Schneekugel \naus Eis und Staub', 'Ein felsiger Himmeslkörper', 'Ein wandelnder Stern'],
        'question_answer': 'Eine schmutzige Schneekugel aus Eis und Staub',
        'picture': 'astronomy.jpg',
        'current_category': 'Astronomie'
    },
    53: {
        'question': 'Welcher Planet hat deutlich sichtbare Ringe?',
        'possible_answers': ['Mars', 'Venus', 'Saturn', 'Uranus'],
        'question_answer': 'Saturn',
        'picture': 'astronomy.jpg',
        'current_category': 'Astronomie'
    },
    54: {
        'question': 'Was verursacht eine Supernova?',
        'possible_answers': ['Kollision von Planeten', 'Kollision von Galaxien', 'Erlöschung eines \nschwarzen Lochs', 'Explosion eines massiven Sterns'],
        'question_answer': 'Explosion eines massiven Sterns',
        'picture': 'astronomy.jpg',
        'current_category': 'Astronomie'
    },
    55: {
        'question': 'Welche Galaxie ist die nächste zu unserer Milchstraße?',
        'possible_answers': ['Andromeda-Galaxie', 'Sombrero-Galaxie', 'Socratis-Galaxie', 'Dreiecks-Galaxie'],
        'question_answer': 'Andromeda-Galaxie',
        'picture': 'astronomy.jpg',
        'categoy': 'Astronomie'
    },
    56: {
        'question': 'Welches Sternbild enthält den Polarstern?',
        'possible_answers': ['Orion', 'Ursa (Großer Bär)', 'Scorpius (Skorpion)', 'Leo (Löwe)'],
        'question_answer': 'Ursa (Großer Bär)',
        'picture': 'astronomy.jpg',
        'current_category': 'Astronomie'
    },
    57: {
        'question': 'Was ist ein Exoplanet',
        'possible_answers': ['Ein nicht entwickelter \nPlanet', 'Ein Mond eines \nanderen Planeten', 'Ein Planet außerhalb \nunseres Sonnensystems', 'Ein künstlich geschaffener \nHimmelskörper'],
        'question_answer': 'Ein Planet außerhalb unseres Sonnensystems',
        'picture': 'astronomy.jpg',
        'categoy': 'Astronomie'
    },
    58: {
        'question': 'Welches Phänomen tritt ein, wenn ein kleiner Himmelskörper in die Erdatmosphäre eintritt und verglüht?',
        'possible_answers': ['Meteoriteneinschlag', 'Komet', 'Asteroid', 'Meteor'],
        'question_answer': 'Meteor',
        'picture': 'astronomy.jpg',
        'current_category': 'Astronomie'
    },
    59: {
        'question': 'Wie heißt das leistungsstärkste Weltraumteleskop, das für Infrarotbeobachtungen konzipiert wurde?',
        'possible_answers': ['Hubble-Teleskop', 'James Webb Space Telescope', 'Kepler-Telescope', 'Spitzer-Telescope'],
        'question_answer': 'James Webb Space Telescope',
        'picture': 'astronomy.jpg',
        'current_category': 'Astronomie'
    },
    60: {
        'question': 'Welches Ereignis tritt aus, wenn die Erde den küzesten Tag des Jahres hat?',
        'possible_answers': ['Herbstsonnenwende', 'Sommeranfang', 'Wintersonnenwende', 'Frühlingsanfang'],
        'question_answer': 'Wintersonnenwende',
        'picture': 'astronomy.jpg',
        'current_category': 'Astronomie'
    },
    61: {
        'question': 'Welches ist das härteste natürliche Material auf der Erde?',
        'possible_answers': ['Diamant', 'Quarz', 'Obsidian', 'Stahl'],
        'question_answer': 'Diamant',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    62: {
        'question': 'Welches ist das größte Ökosystem aud der Erde?',
        'possible_answers': ['Regenwald', 'Wüste', 'Tundra', 'Ozean'],
        'question_answer': 'Ozean',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    63: {
        'question': 'Welches ist das älteste lebende Baumsystem der Welt?',
        'possible_answers': ['Bristelcone-Kiefern', 'Eukalyptus-Bäume', 'Ginkgo-Bäume', 'Redwood-Bäume'],
        'question_answer': 'Bristlecone-Bäume',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    64: {
        'question': 'Welches ist das größste Riff-Ökosystem der Welt?',
        'possible_answers': ['floida Keys Reef', 'Maldives Coral Reef', 'Great Barrier Reef', 'Belize Barrier Reef'],
        'question_answer': 'Great Barrier Reef',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    65: {
        'question': 'Welches Gas ist für die grüne Farbe in Pflanzen verantwortlich',
        'possible_answers': ['Chlorophyl', 'Kohlenstoff', 'Sauerstoff', 'Stickstoff'],
        'question_answer': 'Chlorophyl',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    66: {
        'question': 'Welche der folgenden Blumen repräsentiert normalerweise Frieden und Ruhe?',
        'possible_answers': ['rose', 'Tulpe', 'Lilie', 'Kamille'],
        'question_answer': 'Lilie',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    67: {
        'question': 'Welches ist der größte Wüstentyp der Welt?',
        'possible_answers': ['Sahare-Wüste', 'Gobi-Wüste', 'Antarktische-Wüste', 'Mojave-Wüste'],
        'question_answer': 'Antarktische Wüste',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    68: {
        'question': 'Welches ist das größte Lebewesen auf dem Land?',
        'possible_answers': ['Giraffe', 'Elefant', 'Blauwal', 'Sequioa-Baum'],
        'question_answer': 'Sequioa-Baum',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    69: {
        'question': 'Wie heißt der größte Ozean unseres Planeten?',
        'possible_answers': ['Pazifischer Ozean', 'Indischer Ozean', 'Südlicher Ozean', 'Atlantischer Ozean'],
        'question_answer': 'Pazifischer Ozean',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    70: {
        'question': 'Was ist ein Tundra-Ökosystem?',
        'possible_answers': ['Ein Gebiet mit ewigem Eis', 'Eine große Wüste', 'Ein trockenes Grasland', 'Ein Baumbestand aus Nadelbäumen'],
        'question_answer': 'Ein Gebiet mit ewigem Eis',
        'picture': 'nature.jpg',
        'current_category': 'Natur'
    },
    71: {
        'question': 'Welche Datenstruktur verwendet einen Last-In-First-Out (LIFO) Ansatz?',
        'possible_answers': ['Schlange (Queue)', 'Liste (List)', 'Stapel (Stack)', 'Baum (Tree)'],
        'question_answer': 'Stapel (Stack)',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    72: {
        'question': 'Was ist der Zweck eines Betriebssystems?',
        'possible_answers': ['Ausführung von Anwendungsprogrammen', 'Verwaltung von \nHardware-Ressourcen', 'Darstellung von grafischen \nBenutzeroberflächen', 'Netzwerkkommunikation'],
        'question_answer': 'Verwaltung von Hardware-Ressourcen',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    73: {
        'question': 'Was ist eine Firewall in Bezug auf Computersicherheit?',
        'possible_answers': ['Ein Hardware-Tool zum \nVerbinden von Computern', 'Ein Schutzprogramm gegen \nViren und Malware', 'Ein Sicherheitsprotokoll für \ndrahtlose Netzwerke', 'Eine Sicherheitsbarriere zwischen einem \ninternen Netzwerk und externen Netzwerken'],
        'question_answer': 'Eine Sicherheitsbarriere zwischen einem internen Netzwerk und externen Netzwerken',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    74: {
        'question': 'Was ist ein Byte in der Informatik?',
        'possible_answers': ['4 Bits', '8 Bits', '16 Bits', '32 Bits'],
        'question_answer': '8 Bits',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    75: {
        'question': ' Welche Programmiersprache wird häufig für die Entwicklung von mobilen Anwendungen verwendet,\ninsbesondere für iOS-Geräte?',
        'possible_answers': ['Java', 'Swift', 'Python', 'C#'],
        'question_answer': 'Swift',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    76: {
        'question': 'Was ist ein DNS (Domain Name System)?',
        'possible_answers': ['Ein Netzwerkprotokoll zur \nsicheren Datenübertragung', 'Ein Datenbankmanagementsystem', 'Ein Protokoll für die \nE-Mail-Kommunikation', 'Ein System zur Auflösung von \nDomainnamen in IP-Adressen'],
        'question_answer': 'Ein System zur Auflösung von Domainnamen in IP-Adressen',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    77: {
        'question': 'Was ist ein Stack Overflow in der Informatik?',
        'possible_answers': ['Ein Speicherüberlauffehler', 'Ein Algorithmus für Stapeloperationen', 'Ein spezieller Netzwerkdienst', 'Ein Sicherheitsprotokoll'],
        'question_answer': 'Ein Speicherüberlauffehler',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    78: {
        'question': 'Was ist ein Compiler in der Informatik?',
        'possible_answers': ['Ein Gerät zur Datenkompression', 'Ein Programm, das Code in \nMaschinensprache übersetzt', 'Ein Sicherheitsprogramm gegen Malware', 'Ein Netzwerkprotokoll für \nsichere Verbindungen'],
        'question_answer': 'Ein Programm, das Code in Maschinensprache übersetzt',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    79: {
        'question': 'Welcher Begriff beschreibt die Überprüfung von Quellcode auf Fehler und Unregelmäßigkeiten?',
        'possible_answers': ['Codierung', 'Testing', 'Debugging', 'Kompilierung'],
        'question_answer': 'Debugging',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    80: {
        'question': 'Welcher Begriff beschreibt eine Sammlung von Anweisungen oder Befehlen,\ndie eine bestimmte Aufgabe oder Funktion ausführen?',
        'possible_answers': ['Funktion', ' Klasse', 'Methode', 'Algorithmus'],
        'question_answer': 'Funktion',
        'picture': 'informatics.jpg',
        'current_category': 'Informatik'
    },
    81: {
        'question': 'Welcher Vogel hat den längesten jährlichen Zugweg?',
        'possible_answers': ['Kolibri', 'Kondor', 'Albatros', 'Storch'],
        'question_answer': 'Albatros',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    82: {
        'question': 'Welches Tier kann durch Mimkry das Aussehen von anderen gefährlichen Tieren imitieren?',
        'possible_answers': ['Chamäleon', 'Oktopus', 'Fledermaus', 'Pfeilgiftfrosch'],
        'question_answer': 'Pfeilgiftfrosch',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    83: {
        'question': 'In welchem natürlichen Lebensraum leben Kängurus typischerweise?',
        'possible_answers': ['Wüste', 'Tundra', 'Regenwald', 'Grasland'],
        'question_answer': 'Grasland',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    84: {
        'question': 'Welches Tier hält den längesten Winterschlaf?',
        'possible_answers': ['Bär', 'Fledermaus', 'Igel', 'Eichhörnchen'],
        'question_answer': 'Fledermaus',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    85: {
        'question': 'Welches Reptil kann am längesten ohne Nahrung überleben?',
        'possible_answers': ['Schlange', 'Leguan', 'Schildkröte', 'Krokodil'],
        'question_answer': 'Krokodil',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    86: {
        'question': 'Wie heißt das schnellste Meerestier?',
        'possible_answers': ['Orca', 'Weißer Hai', 'Thunfisch', 'Delfin'],
        'question_answer': 'Thunfisch',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    87: {
        'question': 'Wie heißt das einzige Flugfähige Säugetier?',
        'possible_answers': ['Flughund', 'Pinguin', 'Mistkäfer', 'Fledermaus'],
        'question_answer': 'Fledermaus',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    88: {
        'question': 'Welches Tier kann seinen Schwanz abwerfen, um Feinde zu täuschen?',
        'possible_answers': ['Gecko', 'Leguan', 'Eidechse', 'Salamander'],
        'question_answer': 'Eidechse',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    89: {
        'question': 'Welche beiden Säugetiere legen Eier?',
        'possible_answers': ['Igel und Maulwurf', 'Schnabeltiere und Ameisenigel', 'Rotkehlchen und Kaiserpinguin', 'Gans und Ente'],
        'question_answer': 'Schnabeltiere und Ameisenigel',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    90: {
        'question': 'Welcher Vogel ist für seinen kunstvollen Nestbau in Form einer Tasche bekannt?',
        'possible_answers': ['Elster', 'Webervogel', 'Spatz', 'Storch'],
        'question_answer': 'Webervogel',
        'picture': 'animals.jpg',
        'current_category': 'Tiere'
    },
    91: {
        'question': 'Was ist die Einheit der elektrischen Spannung',
        'possible_answers': ['Watt', 'Volt', 'Ampere', 'Ohm'],
        'question_answer': 'Volt',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
    92: {
        'question': 'Welche Einheit wird verwendet um Radioaktivität zu messen?',
        'possible_answers': ['Sievert', 'Rad', 'Rem', 'Gray'],
        'question_answer': 'Sievert',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
    93: {
        'question': 'Welches Element hat die chemische Bezeichnung "FE"?',
        'possible_answers': ['Kalzium', 'Flur', 'Kalium', 'Eisen'],
        'question_answer': 'Eisen',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
    94: {
        'question': 'Wer formulierte die Theorie der Evolution durch natürliche Auslese?',
        'possible_answers': ['Gregor Mendel', 'Alfred Wegener', 'Charles Darwin', 'Linus Pauling'],
        'question_answer': 'Charles Darwin',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
    95: {
        'question': 'Welches Organ im menschlichen Körper ist für die Blutbildung verantwortlich?',
        'possible_answers': ['Knochenmark', 'Herz', 'Leber', 'Niere'],
        'question_answer': 'Knochenmark',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
    96: {
        'question': 'Welches Organ ist für die Regulation des Blutzuckerspiegels verantwortlich?',
        'possible_answers': ['Niere', 'Bauchspeicheldrüse', 'Leber', 'Darm'],
        'question_answer': 'Bauchspeicheldrüse',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
    97: {
        'question': 'Welches Vitamin wird als "Sonnenvitamin" bezeichnet?',
        'possible_answers': ['Vitamin A', 'Vitamin B', 'Vitamin D', 'Vitamin K'],
        'question_answer': 'Vitamin D',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
    98: {
        'question': 'Welches ist das häufigste Edelgas in der Erdkruste?',
        'possible_answers': ['Helium', 'Neon', 'Krypton', 'Argon'],
        'question_answer': 'Argon',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
    99: {
        'question': 'Welcher Wissenschaftler entwickelte die Theorie der Quantentechnik?',
        'possible_answers': ['Albert Einstein', 'Erwin Schrödinger', 'Niels Rohr', 'Max Planck'],
        'question_answer': 'Max Planck',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
    100: {
        'question': 'Welches ist das erste kommerzielle Elektroauto, das weltweit anerkannt wurde?',
        'possible_answers': ['Nissan Leaf', 'Tesla Roadster', 'Toyota Pirus', 'Chevrolet Volt'],
        'question_answer': 'Tesla Roadster',
        'picture': 'science.jpg',
        'current_category': 'Wisschenschaft'
    },
}

# Funktion um zufällig 10 Fragen auszuwählen
def get_random_questions():
    questions_keys = list(questions_dict.keys()) # holt die Fragen durch die Nummerierung (Schlüssel) aus dem Dictionary
    random_questions_keys = random.sample(questions_keys, 10) # zufällige Auswahl von 10 Fragen
    random_questions = {key: questions_dict[key] for key in random_questions_keys} # erstellt neues Dictionary mit den ausgewählten 10 Fragen
    return random_questions_keys ,random_questions # neues Dictionary wird zurückgegeben
