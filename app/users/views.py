from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from footprints.models import UserChoice, Choice
from footprints.serializers import UserChoiceSerializer
from .serializers import UserSerializer
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import BadHeaderError
from django.template import loader
from django.db.models import Sum
from .models import User as CustomUser

# Create your views here.
User = get_user_model()


def update_user_total_footprint(user):
    total = UserChoice.objects.filter(user=user).aggregate(total=Sum('choice__carbon'))['total'] or 0
    user.total_footprint = total
    user.save(update_fields=['total_footprint'])
    return total

def register(request):
    next = request.GET.get('next', '/')
    try:
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(request, username=username, password=password)
        try:
            login(request, auth_user)
            return HttpResponseRedirect(next)
        except:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect(next)
    except (KeyError):
        messages.error(request, 'Invalid credentials')
        #return render(request, '/', { 'message': "Invalid username or password. Please try again." })


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        print("----------------- register called")
        print(username)
        print(password)
        print(firstname)
        print(lastname)
        print(email)

        # try:
        #     user = get_object_or_404(User, username=username)
        # except:
        #     pass

        messages.success(request,
                         f'Your account has been created! You can now login!')
        return redirect('login')
    else:
        return render(request, 'users/register.html')


@api_view(['GET'])
def user_list(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_choices(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'GET':
        user_choices = UserChoice.objects.filter(user=user).select_related('choice', 'choice__lifestyle')
        serializer = UserChoiceSerializer(user_choices, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        choice_id = request.data.get('choice_id')
        if not choice_id:
            return Response({'error': 'choice_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        choice = get_object_or_404(Choice, id=choice_id)
        user_choice, created = UserChoice.objects.get_or_create(user=user, choice=choice)
        updated_total = update_user_total_footprint(user)
        serializer = UserChoiceSerializer(user_choice)
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response({
            'user_choice': serializer.data,
            'total_footprint': updated_total,
        }, status=status_code)


@api_view(['POST'])
def user_total_footprint(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    total = update_user_total_footprint(user)
    return Response({'user_id': user.id, 'total_footprint': user.total_footprint}, status=status.HTTP_200_OK)