from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Choice, Lifestyle
from .serializers import ChoiceSerializer, LifestyleSerializer
from rest_framework.decorators import api_view

def index(request):
    print("------------------------- I AM HERE")
    queryset = Choice.objects.all()
    return render(request, "footprints/index.html", {'choices': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'footprints/index.html'

    def get(self, request):
        queryset = Choice.objects.all()
        return Response({'choice': queryset})


class list_all_footprints(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'footprints/tutorial_list.html'

    def get(self, request):
        queryset = Choice.objects.all()
        return Response({'choices': queryset})


@api_view(['GET'])
def lifestyle_list(request):
    lifestyles = Lifestyle.objects.all()
    lifestyle_serializer = LifestyleSerializer(lifestyles, many=True)
    return JsonResponse(lifestyle_serializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def choice_list(request):
    if request.method == 'GET':
        choices = Choice.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            choices = choices.filter(name__icontains=name)

        choices_serializer = ChoiceSerializer(choices, many=True)
        return JsonResponse(choices_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        choice_data = JSONParser().parse(request)
        choice_serializer = ChoiceSerializer(data=choice_data)
        if choice_serializer.is_valid():
            choice_serializer.save()
            return JsonResponse(choice_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(choice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Choice.objects.all().delete()
        return JsonResponse({'message': '{} Choices were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def choice_detail(request, id):
    try:
        choice = Choice.objects.get(id=id)
    except Choice.DoesNotExist:
        return JsonResponse({'message': 'The choice does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        choice_serializer = ChoiceSerializer(choice)
        return JsonResponse(choice_serializer.data)

    elif request.method == 'PUT':
        choice_data = JSONParser().parse(request)
        choice_serializer = ChoiceSerializer(choice, data=choice_data)
        if choice_serializer.is_valid():
            choice_serializer.save()
            return JsonResponse(choice_serializer.data)
        return JsonResponse(choice_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        choice_data = JSONParser().parse(request)
        choice_serializer = ChoiceSerializer(choice, data=choice_data, partial=True)
        if choice_serializer.is_valid():
            choice_serializer.save()
            return JsonResponse(choice_serializer.data)
        return JsonResponse(choice_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        choice.delete()
        return JsonResponse({'message': 'Choice was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
