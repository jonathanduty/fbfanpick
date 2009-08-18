from google.appengine.ext import db
from django.utils import simplejson

class League(db.Model):
    
    name = db.StringProperty(required=True)
    
    
    def to_json(self):
        return simplejson.dumps({"id":self.key(),"name":self.name})
        
    
class Team(db.Model):
    
    name = db.StringProperty(required=True)
    league = db.ReferenceProperty(League)
    
    
    def to_json():
        return simplejson.dumps({"id":self.key(),"name":self.name,"league":self.league.to_json()})
        
# class Game(db.Model):
#     
#     
#     home_team = db.ReferenceProperty(Team)
#     
#     visiting_team = db.ReferenceProperty(Team)
#     
#     game_time = db.DateTimeProperty(required=False)
#     
#     def to_json():
#         return simplejson.dumps({"id":self.key(),
#                     "visiting_team":self.visiting_team.to_json(),
#                     "home_team":self.home_team.to_json(),
#                     "game_time":str(self.game_time)})
        