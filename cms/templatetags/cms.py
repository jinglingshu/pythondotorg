from django import template
from django.utils.dateformat import format
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
def iso_time_tag(date):
    """ Returns an ISO date, with the year tagged in a say-no-more span.

    This allows the date representation to shrink to just MM-DD. """
    date_templ = '<time datetime="{timestamp}"><span class="say-no-more">{year}-</span>{month}-{day}</time>'
    return mark_safe(date_templ.format(
        timestamp=format(date, 'c'),
        month=format(date, 'm'),
        day=format(date, 'd'),
        year=format(date, 'Y'),
    ))
