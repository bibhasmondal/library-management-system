from django import template
register = template.Library()


@register.filter(name='sf')
def short_form(data):
    sf = ""
    try:
        for word in str(data).split(" "):
            sf += word[0].upper()
    except:
        pass
    return sf


@register.filter()
def isappview(request):
    try:
        if request.GET['appName'] == 'VCWeb':
            return True
    except:
        pass
    return False