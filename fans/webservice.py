import os
import logging
import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
from django.utils import simplejson
from fans.model import Game,Pick,FacebookUser     
import datetime
_abspath_to_here = os.path.abspath( os.path.dirname(__file__) )
_template_lookup = TemplateLookup(directories=[os.path.join(_abspath_to_here,'templates')],format_exceptions=True)


def render(template_path, params):
    """Renders mako template with given values"""
    template = _template_lookup.get_template(template_path)
    return template.render(**params)    
    
    

class FacebookAppController(object):
    
    
    def __init__(self):
        pass
    
    
    
    @cherrypy.expose
    def authorize(self,fb_sig_user,fb_sig_time,fb_sig_authorize,fb_sig):
        
        user = FacebookUser.get_by_uid(fb_sig_user)
        if user is None:
            user = FacebookUser(uid=fb_sig_user,
                            active=True,
                    )
        
    @cherrypy.expose
    def remove(self,fb_sig_user,**kwargs):
        user = FacebookUser.get_by_uid(fb_sig_user)
        if user is not None:
            user.active = False
            user.put()
        
        
    @cherrypy.expose
    def canvas(self,parent_id=None,**kwargs):
        
        # assign parent to javascript null
        parent = None
        parent_json = "null"
        
        if parent_id is not None:
            parent = Pick.get_by_id(int(parent_id))
            parent_json = parent.to_json()

             
        logging.info( parent_json)
        logging.info(simplejson.dumps({"test":"jonathan"}))
        return render("canvas.htm",{"parent_json":parent_json,
                                    "parent":parent})
    
    
    @cherrypy.expose
    def games(self,year,month,day):
        
        date = datetime.date(year=int(year),month=int(month),day=int(day))
        json = Game.get_games_by_day(date)
        return json
        
    @cherrypy.expose
    def submit(self,game_id,home_win,userid,**kvargs):
        
        home_win = ("true","false")[home_win == "false"]
        
        parent = None
        if "parent_id" in kvargs.keys():
            parent = Pick.get_by_id(int(kvargs["parent_id"]))
            
        game = Game.get_by_id(int(game_id))
        pick = Pick(
            game=game,
            response_to=parent,
            fb_user_id= userid,
            home_winner=bool(home_win))
        
        pick.put()
        return pick.to_json()
        