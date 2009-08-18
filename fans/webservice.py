import os
import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup

_abspath_to_here = os.path.abspath( os.path.dirname(__file__) )
_template_lookup = TemplateLookup(directories=[os.path.join(_abspath_to_here,'templates')],format_exceptions=True)


def render(template_path, **kwargs):
    """Renders mako template with given values"""
    template = _template_lookup.get_template(template_path)
    return template.render(**kwargs)
    
    

class FacebookAppController(object):
    
    
    def __init__(self):
        pass
        
        
    @cherrypy.expose
    def say_hello(self):
        return "<h3>Hello World</h3>"
        
    @cherrypy.expose
    def canvas(self,**kwargs):
        print kwargs
        return render("canvas.htm")
        
        