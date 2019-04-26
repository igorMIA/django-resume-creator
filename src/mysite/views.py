from django.shortcuts import render
from .models import Jobs, Lang, Edu, Achievements, Skills, ShowBlocks, BaseInfo


def index(request):
    context = {
        'show': ShowBlocks.objects.all(),
        'jobs': Jobs.objects.all(),
        'base_info': BaseInfo.objects.first(),
    }

    if ShowBlocks.objects.get(title='Навыки').show:
        context['skills'] = Skills.objects.all()

    if ShowBlocks.objects.get(title='Языки').show:
        context['languages'] = Lang.objects.all()

    if ShowBlocks.objects.get(title='Образование').show:
        context['univs'] = Edu.objects.all()

    if ShowBlocks.objects.get(title='Награды').show:
        context['achievements'] = Achievements.objects.all()

    return render(request, 'mysite/index.html', context)
