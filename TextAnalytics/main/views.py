from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .utils import sumextract


def index(request):
    if request.method == 'POST':
        form = TextInp(request.POST)
        if form.is_valid():
            inp_text = form.cleaned_data['inp_text']
            sent_count = form.cleaned_data['inp_sent_count']
            out_text = sumextract(inp_text, sent_count).split('(?%)')
            return render(
                request,
                'main/index.html',
                context={
                    'form': form,
                    'inp_text': inp_text,
                    'out_text': out_text
                }
            )
        else:
            return HttpResponse("Ошибка введённых данных")
    else:
        form = TextInp()
        data = {'form': form}
        return render(request, 'main/index.html', context=data)