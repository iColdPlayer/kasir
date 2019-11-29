from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileUpdateForm, UserUpdateForm
from accounts.models import Profile

def Register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun baru telah berhasil dibuat, dengan username: {username}!')
            password = form.cleaned_data.get('password1')
            return redirect("/")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "accounts/register.html",
                          context={"form":form})

    form = SignUpForm
    return render(request = request,
                  template_name = "accounts/register.html",
                  context={"form":form})

@login_required
def Account(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                     request.FILES,
                                     instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account information has been updated successfully!')
            return redirect('Account')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        data_user = Profile.objects.filter(user_id=request.user.id)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'data_user': data_user
    }
    return render(request, 'accounts/account.html', context)



