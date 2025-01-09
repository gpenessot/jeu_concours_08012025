import random
import time
import sys
from datetime import datetime

# Liste des participants
participants = [
    "Alain E.",
    "SYLVAIN GAYCHET",
    "Ahmed Ibnabasse",
    "Charles RANDRIATAHINA",
    "Mialy TSIRINATSIVA",
    "Raphaël Rougis",
    "Marland Lynval",
    "Augustin MADET",
    "Afdel Desmond KOMBOU",
    "Victory MBANZILA DIMBOU",
    "Laetitia MOREL",
    "Zakaria El Hayani",
    "Xavier Leclercq",
    "Christian KUATE",
    "Richard Toulou",
    "Emilie GROSCHENE",
    "Mélanie Bessonnier",
    "François Vercellotti",
    "Jezabel MONTIGNY",
    "DATANOSCO",
    "Ruddy Nzita-Baku",
    "Méline Bourquin",
    "Khady DIAGNE",
    "Geoffroy KOUACOU",
    "Aurélien Segura",
    "Sabrina NAINE",
    "Youh Essoh",
    "Lucie Camanez",
    "Xuan NGUYEN",
    "François-Xavier Ribeiro",
    "Abdel Oulali",
    "Giovanny LAURET",
    "Maihdi Elfassi-Fihri",
    "Moktar Yacin Abdillahi",
    "B R.Consult",
    "Manuella Feujio",
    "Lydie-Laure Tajiona Manguesso",
    "Alimatou Seck",
    "Thelma Sandra LUM",
    "Ben Rebah Maher",
    "Ilias EL AMRANI EL IDRISSI",
    "Claude Stein",
    "Essè Alexis TABO",
    "Israël Toubol",
    "Gaëtan W.",
    "Etienne Coudron",
    "BISSIRIOU Cherif A. A.",
    "Jérémie QUERET",
    "Amadou TAMBOURA",
    "Jean Lhuillier",
    "Hugo LESCURE",
    "Ludovic Cancy Ross",
    "Christ Leckossa",
    "Lea Cruder",
    "Issifou BARO",
    "Abdoulaye Dabo",
    "Bernard PERON",
    "Aboubakar Ibrahime",
    "Omar Bouziane",
    "Lanto RAKOTOSOLOFO",
    "Emmanuel Said",
    "Sidi M. T.",
    "Georges LEMOKEM ZEBAZE",
    "Nacereddine MOUMAI",
    "Leclaire ANJIPU",
    "Marylène Henry",
    "Adil EL ALAMI",
    "Corinne MAZALEIGUE",
    "Jean-Baptiste CASSIN",
    "Houssem SWAIEH ROUIS",
    "Jérémy BRODIER",
    "Julien BIDIAS",
    "NAWAL Benhamouche",
    "Charly D.",
    "Yaya Diallo",
    "Adoum MAHAMAT A.",
    "samba ka",
    "Frédéric Zogbelemou",
    "Adama Boune",
    "Vincent Barrano",
    "Sionceligame Sekongo",
    "Traoré El-Kaher ISSAKA MOUSSA",
    "Alexandre Boullen",
    "Albert Sandokh Bakhoum",
    "willy Kouongni",
    "Stéphanie RAMPNOUX",
    "Blandine Jatsa Nguetse",
    "François TASTET",
    "Ousmane Barry",
    "Inty NAVARRO",
    "Olivier BERSOT",
    "Siangba MANGA-MABADA",
    "Abdoul Karim SOUMAHORO",
    "Sokhna Magné MBOUP",
    "Sébastien Lions",
    "Mohamed Drame",
    "mohamed hamza haouane",
    "Yassin CHAAIRATE",
    "Aurélien Dieu",
    "Patrick BAYO",
    "Yaya SYLLA",
    "Dr. Michel MAMA TOULOU",
    "Tantely Rivoniaina RABEMANANJARA",
    "Roland PENA",
    "Cédric Roussel",
    "Gabrielle Devaux",
    "Denis DARBAS",
    "Galaad Bastos",
    "Mohamed Foupoua",
    "Sékou BERTHE",
    "Amina MARIE",
    "Romain Dubreil",
    "Nathalie Moutreux-Brissaud",
    "Alpha DIALLO",
    "ali meziani",
    "Tanguy Boris Romuald YAO",
    "Yohann Mansiaux",
    "Pascal Tartarin",
    "Jean Christian YAPO",
    "Miguel Palencia-Olivar",
    "Tetyana TARASENKO"
]

def clear_line():
    """Efface la ligne courante"""
    sys.stdout.write('\r')
    sys.stdout.write(' ' * 80)
    sys.stdout.write('\r')

def animate_countdown(seconds):
    """Affiche un compte à rebours animé"""
    for i in range(seconds, 0, -1):
        clear_line()
        print(f"🎲 Tirage dans {i} secondes...", end='', flush=True)
        time.sleep(1)
    clear_line()

def main():
    # Fixe la seed pour la reproductibilité
    # Utilisation de la date du jour pour avoir une seed différente chaque jour
    today = datetime.now()
    random.seed(21) # Département de la Côte d'Or ❤️
    
    # En-tête
    print("\n🎉 TIRAGE AU SORT DU LIVRE 'BUSINESS INTELLIGENCE AVEC PYTHON' 🎉\n", flush=True)
    time.sleep(2)
    
    print(f"Nombre de participants: {len(participants)}\n", flush=True)
    time.sleep(1)
    
    print("Lancement du tirage...\n", flush=True)
    time.sleep(1)
    
    # Compte à rebours
    animate_countdown(10)
    
    # Tirage au sort
    winner = random.choice(participants)
    
    # Annonce du gagnant
    print("\n🎊 Et le(la) gagnant(e) est... 🎊", flush=True)
    time.sleep(2)
    print(f"🏆 {winner.upper()} 🏆")
    
    # Pied de page
    print("\nFélicitations au gagnant ! 🎉")
    print("\nTirage réalisé le:", today.strftime("%d/%m/%Y"))

if __name__ == "__main__":
    main()