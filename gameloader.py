import datetime
from google.appengine.ext import db
from google.appengine.tools import bulkloader
from fans.model import Game



class GameLoader(bulkloader.Loader):
    
    def __init__(self):
        bulkloader.Loader.__init__(self,'Game',
                                [('league',str),
                                ('game_date',lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').date()),
                                 ('home_team',str),
                                 ('visiting_team',str),]
                                 )
                                




loaders = [GameLoader]