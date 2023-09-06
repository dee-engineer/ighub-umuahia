from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        input1 = request.POST.get('from')
        input2 = request.POST.get('to')

        print(input1 + input2)
    return render(request, 'index.html')
    