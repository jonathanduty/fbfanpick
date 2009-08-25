import sys
import platform
from metamake import task, shell, path, bootstrap, Flag



@task
def generate_nfl_schedule():
    from fans.football import parse_nfl
    
    parse_nfl("/tmp/games.csv")


