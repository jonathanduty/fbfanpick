from google.appengine.ext import db
from django.utils import simplejson



class ModelMixin(db.Model):
    
    def __get_key(self):
        return self.key()
    
    id_ = property(__get_key)


        
        
class GamePick(ModelMixin):
    
    
    fb_user_id = db.StringProperty()
    
    home_team = db.StringProperty()
    
    visitor_team = db.StringProperty()
    
    
    game_time = db.DateTimeProperty(required=False)
    
    home_team_winner = db.BooleanProperty()
    
    def to_json():
        return simplejson.dumps({"id":self.key(),
                    "visiting_team":self.visiting_team
                    "home_team":self.home_team,
                    "game_time":str(self.game_time),
                    "fb_user_id":self.fb_user_id
                    })
        
        
        
class GamePickResponse(ModelMixin):
    
    fb_user_id = db.StringProperty()
    
    db.ReferenceProperty(GamePick)
    
    agree = db.BooleanProperty()
    
    def to_json():
        return simplejson.dumps({"id":self.key(),
                    "agree":self.visiting_team
                    "home_team":self.home_team
                    "game_time":str(self.game_time),
                    "fb_user_id":self.fb_user_id
                    })
                    
                    