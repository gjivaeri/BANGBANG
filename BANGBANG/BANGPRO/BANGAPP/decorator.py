from django.shortcuts import redirect

def login_required(function):
    # wrapping한 함수와 기존 함수의 인자값을 맞춰 줘야 한다
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('registration/login')
        return function(request, *args, **kwargs)

    return wrap