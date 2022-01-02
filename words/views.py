from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Letters
from .forms import LettersForm

from .data_processing import *



def letters_input(request):
    filled = False

    if request.method == 'POST':
        form = LettersForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            filled = True

            data = open_txt_file(r"C:\Users\PAWWYP\Desktop\literaki\list_of_words_pl.txt")
            result = find_word(data, cd['letters'])
            
            return HttpResponse("{}".format(result))

            
    else:
        form = LettersForm()

    return render(request, 'scrabble/main.html',
                                {'form': form,
                                'filled': filled})
        


