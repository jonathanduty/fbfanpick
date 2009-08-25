from google.appengine.ext import db
from django.utils import simplejson



class ModelMixin(db.Model):
    
    def __get_key(self):
        return self.key()
    
    id_ = property(__get_key)




class Game(ModelMixin):
    
    
    team_a = db.StringProperty()
    team_b = db.StringProperty()
    league = db.StringProperty()
    
    
    game_date = db.DateProperty(required=False)
    
    
    
    
class Pick(ModelMixin):
    
    
    fb_user_id = db.StringProperty()
    
    game = db.ReferenceProperty(Game)

    response_to = db.SelfReferenceProperty(collection_name="responses_set")
    
    home_a_winner = db.BooleanProperty()
    
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

                    
                    