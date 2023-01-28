from django.shortcuts import render


def user_details(request):
    context = {

    }
    return render(request, 'human_resources/user_details/user_details.html', context)
