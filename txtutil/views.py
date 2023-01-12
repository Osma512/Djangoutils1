#This file is developer created
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact us.html')


def analyze(request):
    text1 = request.POST.get('text', 'Default')
    check1 = request.POST.get('Remove Punctuation', 'off')
    check2 = request.POST.get('uppercase', 'off')
    check3 = request.POST.get('charcount', 'off')
    punctu = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed_text = ""
    purpose_1 = ""
    if check1 == 'on':
        for char in text1:
            if char not in punctu:
                analyzed_text = analyzed_text + char
        text1 = analyzed_text
        purpose_1 = purpose_1 +" Remove Punctuations"
    if check2 == 'on':
        analyzed_text = ""
        for char in text1:
            char = char.upper()
            analyzed_text = analyzed_text + char
        text1 = analyzed_text
        purpose_1 = purpose_1 +", Capitalize"
    if check3 == 'on':
        analyzed_text = ""
        i = 0
        for char in text1:
            if char is not " ":
                i+=1
        analyzed_text = f"{text1}\nTotal characters in string are: {i}"
        purpose_1 = purpose_1 +", No. of Strings"
    if check1 != 'on' and check2 != 'on' and check3 != 'on':
        return render(request, 'error.html')
    params = {'Purpose': purpose_1, 'analyzed_text': analyzed_text}
    return render(request, 'analyze.html', params)
