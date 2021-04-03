# -*- coding: utf-8 -*-

import asyncio
import time
import sys
from poke_env.player.player import Player
from poke_env.player.random_player import RandomPlayer
from tabulate import tabulate
from poke_env.player.utils import cross_evaluate
from poke_env.player_configuration import PlayerConfiguration
from poke_env.server_configuration import ShowdownServerConfiguration
from poke_env.server_configuration import LocalhostServerConfiguration
from poke_env.teambuilder.teambuilder import Teambuilder


class MetronomePlayerRL(Player):
    def __init__(self, **kwargs):
        super(MetronomePlayerRL, self).__init__(**kwargs, battle_format="gen8metronomebattle", max_concurrent_battles=1,
                                              avatar=129, start_timer_on_battle_start=True)
    # async def message(self):
    #     await self._send_message("dab dab dab")
    def choose_move(self, battle):
        # self.message()
        return self.choose_random_doubles_move(battle)



#Arrays
abilities = []
#Teams
mewTeam = """
Mew @ Leppa Berry  
Ability: Synchronize  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Quirky Nature  
- Metronome  

Mew @ Leppa Berry  
Ability: Synchronize  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Quirky Nature  
- Metronome  
"""

shayminTeam = """
vacation (Shaymin) @ Weakness Policy  
Ability: Flower Veil  
Happiness: 128  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Relaxed Nature  
IVs: 0 Spe  
- Metronome  

i am NOT on (Shaymin-Sky) @ Weakness Policy  
Ability: Simple  
Happiness: 128  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Sassy Nature  
- Metronome  

"""
stallTeam = """Dusclops @ Eviolite  
Ability: Neutralizing Gas  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Sassy Nature  
- Metronome  

Silvally-Ghost @ Steel Memory  
Ability: RKS System  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Relaxed Nature  
- Metronome  

"""

pikachuTeam = """PEKACHU (Pikachu-Starter) @ Light Ball  
Ability: Intrepid Sword  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Brave Nature  
- Metronome  

pekachu2 (Pikachu-Starter) @ Light Ball  
Ability: Download  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Serious Nature  
- Metronome  

"""
heracrossTeam = """Cerulean (Heracross-Mega) @ Choice Band  
Ability: Intrepid Sword  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Brave Nature  
- Metronome  

Fuchsia (Heracross-Mega) @ Choice Band  
Ability: Intrepid Sword  
Shiny: Yes  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Brave Nature  
IVs: 0 Spe  
- Metronome  
"""
fveilTeam = """Chungus (Venusaur-Mega) (M) @ Choice Specs  
Ability: Flower Veil  
Hidden Power: Grass  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Quiet Nature  
- Metronome  

Bride of Chungus (Necturna) @ Weakness Policy  
Ability: Thick Fat  
Shiny: Yes  
Hidden Power: Ghost  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Brave Nature  
IVs: 0 Spe  
- Metronome  """

mewCompTeam = """Mew @ Choice Specs  
Ability: Competitive  
Hidden Power: Psychic  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Quiet Nature  
- Metronome  

Mew @ Choice Band  
Ability: Defiant  
Shiny: Yes  
Hidden Power: Psychic  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Brave Nature  
- Metronome  """

bugTeam = """Snaelstrom @ Weakness Policy  
Ability: Unaware  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Relaxed Nature  
- Metronome  

Aurumoth @ Weakness Policy  
Ability: Magic Guard  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Hardy Nature  
- Metronome  

"""
sirfetchdTeam = """Brave (Sirfetch’d) (M) @ Leek  
Ability: Super Luck  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Brave Nature  
- Metronome  

Quiet (Sirfetch’d) (F) @ Leek  
Ability: Super Luck  
Shiny: Yes  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Quiet Nature  
- Metronome  

"""

gulpTeam = """Biased vapor (Cramorant-Gorging) @ Jaboca Berry  
Ability: Gulp Missile  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Relaxed Nature  
- Metronome  

Prejudiced air (Cramorant-Gorging) @ Rowap Berry  
Ability: Gulp Missile  
Shiny: Yes  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Sassy Nature  
- Metronome  

"""
sereneTeam = """Zeroara (Marshadow) @ King's Rock  
Ability: Serene Grace  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Quirky Nature  
- Metronome  

Marshodaw (Zeraora) @ King's Rock  
Ability: Serene Grace  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Quirky Nature  
- Metronome  

"""
steelTeam = """Leets (Silvally-Ghost) @ Steel Memory  
Ability: RKS System  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Relaxed Nature  
- Metronome  

normal type (Silvally-Fire) @ Steel Memory  
Ability: RKS System  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Relaxed Nature  
- Metronome  

"""
latiTeam = """TOP %AGE (Latios) (M) @ Weakness Policy  
Ability: Unaware  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Quiet Nature  
- Metronome  

: 42 (Latias) (F) @ Weakness Policy  
Ability: Magic Guard  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Relaxed Nature  
- Metronome  

"""
silvallyGhostTeam = """Silvally-Ghost @ Bright Powder  
Ability: Magic Bounce  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Sassy Nature  
- Metronome  

Silvally-Ghost @ Bright Powder  
Ability: Magic Bounce  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Sassy Nature  
- Metronome  

"""

# This will work on servers that do not require authentication, which is the
# case of the server launched in our 'Getting Started' section
#Configs
mewConfig = PlayerConfiguration("mew", None)
shayminConfig = PlayerConfiguration("shaymin", None)
stallConfig = PlayerConfiguration("stall", None)
pikachuConfig = PlayerConfiguration("pikachu", None)
heracrossConfig = PlayerConfiguration("heracross", None)
fveilConfig = PlayerConfiguration("fveilSample", None)
mewCompConfig = PlayerConfiguration("mewSample", None)
bugConfig = PlayerConfiguration("bugs", None)
sirfetchdConfig = PlayerConfiguration("sirfetch", None)
gulpConfig = PlayerConfiguration("gulp", None)
sereneConfig = PlayerConfiguration("serene", None)
steelConfig = PlayerConfiguration("steels", None)
latisConfig = PlayerConfiguration("latis", None)
silvallyGhostConfig = PlayerConfiguration("silvallyghost", None)
async def main():
    start = time.time()

    # We create players.
    mew_player = MetronomePlayerRL(
        team=mewTeam, player_configuration=mewConfig,
    )
    shaymin_player = MetronomePlayerRL(
        team=shayminTeam, player_configuration=shayminConfig
    )
    stall_player = MetronomePlayerRL(
        team=stallTeam, player_configuration=stallConfig
    )
    pikachu_player = MetronomePlayerRL(
        team=pikachuTeam, player_configuration=pikachuConfig
    )
    heracross_player = MetronomePlayerRL(
        team=heracrossTeam, player_configuration=heracrossConfig
    )
    fveil_player = MetronomePlayerRL(
        team=fveilTeam, player_configuration=fveilConfig
    )
    mewComp_player = MetronomePlayerRL(
        team=mewCompTeam, player_configuration=mewCompConfig
    )
    bug_player = MetronomePlayerRL(
        team=bugTeam, player_configuration=bugConfig
    )
    sirfetchd_player = MetronomePlayerRL(
        team = sirfetchdTeam, player_configuration=sirfetchdConfig
    )
    gulp_player = MetronomePlayerRL(
        team = gulpTeam, player_configuration=gulpConfig
    )
    serene_player = MetronomePlayerRL(
        team = sereneTeam, player_configuration=sereneConfig
    )
    steel_player = MetronomePlayerRL(
        team = steelTeam, player_configuration=steelConfig
    )
    latis_player = MetronomePlayerRL(
        team=latiTeam, player_configuration = latisConfig
    )
    silvallyGhost_player = MetronomePlayerRL(
        team=silvallyGhostTeam, player_configuration = silvallyGhostConfig
    )
    #Assign players
    # players = [heracross_player, fveil_player]
    # battleCount = 100
    # # Now, let's evaluate our players
    # await players[0].battle_against(players[1], n_battles=battleCount)
    #
    # if players[0].n_won_battles >= players[1].n_won_battles:
    #     winner = players[0]
    #     loser = players[1]
    # else:
    #     winner = players[1]
    #     loser = players[0]
    # print(
    #     "%s won %d / %d battles against %s [this took %f seconds]"
    #     % (winner.username, winner.n_won_battles, battleCount, loser.username, time.time() - start)
    # )

    # # Now, we can cross evaluate them: every player will play 20 games against every
    # # other player.
    # cross_evaluation = await cross_evaluate(players, n_challenges=battleCount)
    #
    # # Defines a header for displaying results
    # table = [["-"] + [p.username for p in players]]
    #
    # # Adds one line per player with corresponding results
    # for p_1, results in cross_evaluation.items():
    #     table.append([p_1] + [cross_evaluation[p_1][p_2] for p_2 in results])
    #
    # # Displays results in a nicely formatted table.
    # print(tabulate(table))

    with open(sys.path[0] + "\\id.txt") as logfile:
        username = logfile.readline()[:-1]
        password = logfile.readline()[:-1]
    player = MetronomePlayerRL( #Real Ladder
        player_configuration=PlayerConfiguration(username, password),
        server_configuration=ShowdownServerConfiguration,
        team = shayminTeam,
    )
    # await player.send_challenges("Flametix", n_challenges=1)
    await player.ladder(1)

    # Print the rating of the player and its opponent after each battle
    for battle in player.battles.values():
        print(battle.rating, battle.opponent_rating)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())