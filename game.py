import random

# Monsterklasse
class Monster:
    def __init__(self, name, hp, dmg, art):
        self.name = name  # Navn på monsteret
        self.hp = hp  # Monsterets helsepoeng
        self.dmg = dmg  # Skade monsteret gjør per angrep
        self.art = art  # ASCII-kunst av monsteret

    def present_monster(self):
        print(self.art)  # Skriver ut ASCII-kunsten av monsteret
        # Skriver ut beskrivelse av monsteret
        print(
            f"Du møtte en {self.name} med totalt {self.hp} HP, som gjør {self.dmg} skade per angrep."
        )

# ASCII-kunst for ulike monstre
bat_art = '''
___________________               ___________________
~-.             \\  |\\___/|  //              .-~
 ~-.           \\ / o o \\ /           .-~
    >           \\\\  W  //           <
   /             /~---~\\             \\
  /_            |       |            _\\
     ~-.        |       |        .-~
        ;        \\     /        i
       /___      /\\   /\\      ___\\
            ~-. /  \\_/  \\ .-~
               V         V
'''

dragon_art = '''
                   __====-_  _-====___
         _--^^^#####//      \\#####^^^--_
      _-^##########// (    ) \\##########^-_
     -############//  |\\^^/|  \\############-
   _/############//   (@::@)   \\############\\_
  /#############((     \\//     ))#############\\
 -###############\\    (oo)    //###############-
-#################\\  / " " \\  //#################-
-###################\\/  (   )  \\//###################-
_#/|##########/\\######(   /   \\   )######/\\##########|\\#_
|/  |/  |/  |/  |/  |/  |/  |/  |/  |/  |/  |/  |/  |/  |/
'''

skeleton_art = '''
  _____
/     \\
|       |
| X   X |
|   ∆   |
\\_____/
  | |
__| |__
/  | |  \\
|___| |___|
'''

goblin_art = '''
 ,     ,     
 |\\.\\\\ //|     
 ) _     _ (   
/   \\ . /   \\  
|   o     o   |  
(   \\ (_) /   )  
 \\           /   
  `.  -----  .'  
    `-------'    
'''

vampire_art = '''
               /######\\
             /##########\\
            /   \\###/    \\
           /     \\#/      \\
        /\\|               |/\\
        | | \\ ==\\    /== / | |
         \\|  \\<|>\\  /<|>/  |/     /|
  \\__     |    -   \\  -    |     /#|
   \\#\\    |        |      |    /###|
    \\##\\  |       \\|     |  /#####|
     \\###\\  |   _______  | /######|
      \\####\\ | / \\/ \\/| /#######|
      |######\\|         | #########|
      |########\\_______/##########|
      |#########\\    /##########/\\
      /###########\\/########/###\\
  /################\\######/########\\
 /##################\\###/###########\\
/###################\\#/##############\\
/####################/#################\\
/###################/####################\\
'''

fighter_art = """
      ,  /\\  .
     //`-||-'\\\\
    (| -=||=- |)
     \\\\,-||-.//
      `  ||  '
         ||
         ||
         ||
         ||
         ||
    hjm  ()
"""

mage_art = """
                 *
           *   *
         *    \\* / *
           * --.:. *
          *   * :\\ -
            .*  | \\
           * *     \\
         .  *       \\
          ..        /\\.
         *          |\\)|
       .   *         \\ |
      . . *           |\\/\\
         .* *         /  \\
       *              \\ / \\
     *  .  *           \\   \\
        * .  
       *    *    
      .   *    *  
"""

# Opprettelse av monsterinstanser
vampire = Monster("vampyr", 600, 10, vampire_art)
dragon = Monster("drage", 1000, 10, dragon_art)
bat = Monster("flaggermus", 100, 2, bat_art)
skeleton = Monster("skjelett", 50, 1, skeleton_art)
goblin = Monster("goblin", 150, 2, goblin_art)

# Liste over alle monsterinstanser
monster_manual = [bat, skeleton, goblin, dragon, vampire]

# Liste med morsomme meldinger
funny_messages = [
    "Det monsteret så det aldri komme!",
    "En til biter i støvet!",
    "Du er på brann!",
    "Monstre, pass dere!",
    "Er det alt du har?",
    "Du får det til å se lett ut!",
    "En ny dag, et nytt monster!",
    "Du er ustoppelig!",
    "Lett som en plett!",
    "Du burde kalles monsterslakteren!",
    "Er det ingen som kan utfordre deg?",
    "De kommer, du vinner!",
    "Monsterfest? Mer som monsterkrasj!",
    "Du er et monsters verste mareritt!",
    "De hadde ingen sjanse!",
    "Du er sjefen nå!",
    "Hvem er neste?",
    "For enkelt!",
    "Du er en legende!",
    "Monster beseiret! Hvem ler nå?"
]

# Initialisering av spillerstatistikk
player_hp = 100
player_dmg = 100
alt_dmg = 0
monsters_defeated = 0

# Funksjon for å lage en spiller
def create_player():
    global player_hp
    global player_dmg
    global alt_dmg
    player_name = input("Hva er navnet ditt? ")
    stre = int(input("Hvor mange push-ups kan du ta på en time? "))
    mag = int(input("Hvor mange bøker har du lest? "))

    player_hp = 30 + stre + 100
    player_dmg = stre + 100
    alt_dmg = mag + 10

    # Bestemmer spillerens type basert på statistikk
    if player_dmg > alt_dmg:
        print(
            f"Du er den mektige {player_name}, en øksebærende kriger {fighter_art} som gjør {player_dmg} skadepoeng!"
        )
    else:
        player_dmg = alt_dmg
        print(
            f"Du er en kraftfull trollmann kalt {player_name}-Sama med en magisk stav {mage_art} som gjør {player_dmg} skadepoeng!"
        )

# Funksjon for å simulere kampen
def fight():
    global player_hp
    global player_dmg
    global monsters_defeated
    while player_hp > 0:
        encounter = random.choice(monster_manual)
        encounter.present_monster()
        while encounter.hp > 0 and player_hp > 0:
            player_hp -= encounter.dmg
            print(
                f"Monsteret angrep deg for {encounter.dmg} skade. Du har {max(player_hp, 0)} HP igjen."
            )
            input("Angrip tilbake! (Trykk på en tast)")
            encounter.hp -= player_dmg
            print(f"Monsteret har {max(encounter.hp, 0)} HP igjen.")
            if encounter.hp <= 0:
                print("Gratulerer, du har beseiret monsteret!")
                monsters_defeated += 1
                # Vis en tilfeldig morsom melding
                funny_message = random.choice(funny_messages)
                print(f"\n*** {funny_message} ***\n")
                f_choice = input("Vil du kjempe mot flere monstre? J/N ").lower()
                if f_choice == "j":
                    break  # Gå til neste monster
                else:
                    print(f"Du beseiret totalt {monsters_defeated} monstre! Takk for at du spilte!")
                    return
            elif player_hp <= 0:
                break
        if player_hp <= 0:
            print("Du har gått tom for HP!")
            game_over = input("Du døde. Vil du prøve igjen? J/N ").lower()
            if game_over == "j":
                player_hp = 100
                player_dmg = 100
                monsters_defeated = 0
                create_player()
            else:
                print(f"Du beseiret totalt {monsters_defeated} monstre! Takk for at du spilte!")
                break

# Start spillet
create_player()
fight()
