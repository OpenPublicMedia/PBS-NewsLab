from django.views.generic.simple import direct_to_template
from base.models import BaseState as State
from django.shortcuts import render_to_response



#Home page where user can select states they are interested in outputting in a KML
def index(request):
    all_states = State.objects.all().order_by('full_name').exclude(full_name='Puerto Rico')
    return direct_to_template(request, 'colorthestates/index.html', {'all_states': all_states})

#Generates file to be displayed in Google map preview, and adjust states displayed and user-specified color and opacity
def preview(request):
    color1 = request.GET.get('color1', '')
    states = request.GET.getlist('states')
    return direct_to_template(request, 'colorthestates/preview.kml', {'color_1': color1, 'states':states})
    

#Detail page where user can choose the color/opacity they would like, and then download the completed file
def color(request):
    states = request.GET.getlist('states')
    if len(states) == 0:
        states=['TX']
    number = request.GET.get('number')
    if number:
        states_queryset=State.objects.all()[:int(number)]
        for i in states_queryset:
            states.append(i.abbrev)
    return direct_to_template(request, 'colorthestates/color.html', {'states': states})
    

#Generates a downloadable KML file with user preferences selected, adds metadata for simple download
def download(request):
    states = request.GET.getlist('states')
    number = request.GET.get('number')
    color1 = request.GET.get('color1', '')
    if number:
        states_queryset=State.objects.all()[:int(number)]
        for i in states_queryset:
            states.append(i.abbrev)
    r =  render_to_response('colorthestates/preview.kml', {"states": states, "color_1": color1, "number": number},
        mimetype="application/vnd.google-earth.kml+xml")
    r['Content-Disposition']='filename=state_backgrounds.kml'
    return r
