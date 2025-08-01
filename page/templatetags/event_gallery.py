from django import template
from ..models import Event
from datetime import date, timedelta
from random import sample

register = template.Library()

@register.inclusion_tag('partials/gallery_section.html')
def render_event_gallery(limit=3):
    today = date.today()
    end_week = today + timedelta(days=6 - today.weekday())
    
    events_qs = Event.objects.filter(
        published=True,
        date__range=(today, end_week)
    )

    events = list(events_qs)
    if len(events) > limit:
        events = sample(events, limit)
        
    return {'gallery_events': events}
