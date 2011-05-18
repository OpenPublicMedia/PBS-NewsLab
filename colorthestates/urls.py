from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

urlpatterns = patterns("colorthestates.views",
    
    # The homepage
    url(r'^$', 'index', name='colorthestates-index'),
    
    #Base KML file that outlines all state polygons with templated conditionals so info only displayed if user picks that state
    url(r'^preview$', 'preview', name='colorthestates-preview'),
    
    #Detail page that allows user to specify color and opacity they want to use for states
    url(r'^color$', 'color', name='colorthestates-color'),
    
    #Generates file with user specified states and colors filled in
    url(r'^convertkml$', direct_to_template, {'template': 'colorthestates/color.html'}, name='colorthestates-color'),
    
    #Generates file with proper name and mimetype specified so user can download the KML
    url(r'^download$', 'download', name='colorthestates-download')
    )