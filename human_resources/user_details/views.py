from django.shortcuts import render


def user_details(request):
    context = {

    }
    return render(request, 'human_resources/user_details/user_details.html', context)
def add_user(request):
    context = {

    }
    return render(request, 'human_resources/user_details/add_user.html', context)
def user_accounts(request):
    context = {

    }
    return render(request, 'human_resources/user_details/user_accounts.html', context)
