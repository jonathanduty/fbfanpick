from google.appengine.ext import db
from google.appengine.api import memcache
from django.utils import simplejson
import datetime


_GAME_CACHE_KEY = "games"


class ModelMixin(db.Model):
    
    def __get_key(self):
        return self.key().id()
    
    id_ = property(__get_key)
  

class Game(ModelMixin):
    
    
    home_team =  db.StringProperty()
    visiting_team =  db.StringProperty()
    
    home_score = db.IntegerProperty()
    visiting_score = db.IntegerProperty()
    
    league = db.StringProperty()
    
    game_date = db.DateProperty(required=False)
    
    game_title =  db.StringProperty()
    
    game_recorded =  db.BooleanProperty(default=False)
    
    
    def to_json_map(self):
        return {"id":self.id_,
                    "visiting_team":self.visiting_team,
                    "home_team":self.home_team,
                    "game_time":str(self.game_date),
                    "game_title":self.game_title,
                    "league":self.league,
                    "search_data":"%s %s" % (self.visiting_team,self.home_team),
                    }
    
    def to_json(self):
        return simplejson.dumps(self.to_json_map())
        
        
    
    @classmethod
    def generate_monthly_json_cache(klass):
        
        today = datetime.date.today()
        future = today + datetime.timedelta(days=31)

        # select all games 1 month into the future.
        games = Game.gql("where game_date < :1",future).fetch(limit=1000)
        
        
        json = simplejson.dumps([game.to_json_map() for game in games])
        memcache.set(_GAME_CACHE_KEY,json)
        return json
        
    @classmethod
    def get_cached_games_json(klass):
        json = memcache.get(_GAME_CACHE_KEY)
        if json is None:
            json = klass.generate_monthly_json_cache()
        return json
        
    
class Pick(ModelMixin):
    
    
    fb_user_id = db.StringProperty()
    
    game = db.ReferenceProperty(Game)

    response_to = db.SelfReferenceProperty(collection_name="responses_set")
    
    home_winner = db.BooleanProperty()
    
    
    
    def to_json():
        return simplejson.dumps({"id":self.key(),
                    "visiting_team":self.visiting_team,
                    "home_team":self.home_team,
                    "game_time":str(self.game_time),
                    "fb_user_id":self.fb_user_id
                    })
        
        
    def __agree_with_parent(self):
        if response_to is not None:
            return self.home_a_winner == response_to.home_a_winner
        return False
    
    agree = property(__agree_with_parent)

                    
                    