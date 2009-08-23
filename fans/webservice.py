import os
import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
from django.utils import simplejson

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
    def canvas(self,**kwargs):
        return render("canvas.htm",{})
    
    
    

        