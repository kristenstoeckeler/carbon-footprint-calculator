from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Choice
from .serializers import ChoiceSerializer
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
    template_name = 'footprints/footprint_list.html'

    def get(self, request):
        queryset = Choice.objects.all()
        return Response({'choices': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def footprint_list(request):
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


@api_view(['GET', 'PUT', 'DELETE'])
def footprint_detail(request, pk):
    try:
        choice = Choice.objects.get(pk=pk)
    except Choice.DoesNotExist:
        return JsonResponse({'message': 'The choice does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        choice_serializer = ChoiceSerializer(choice)
        return JsonResponse(choice_serializer.data)

    elif request.method == 'PUT':
        choice_data = JSONParser().parse(request)
        choice_serializer = ChoiceSerializer(choice, data=choice_data)
        if choice_serializer.is_valid():
            choice_serializer.save()
            return JsonResponse(choice_serializer.data)
        return JsonResponse(choice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        choice.delete()
        return JsonResponse({'message': 'Choice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def footprint_list_published(request):
    choices = Choice.objects.filter(carbon__gt=0)  # Assuming published means carbon > 0

    if request.method == 'GET':
        choices_serializer = ChoiceSerializer(choices, many=True)
        return JsonResponse(choices_serializer.data, safe=False)
        footprint_data = JSONParser().parse(request)
        footprint_serializer = FootprintSerializer(data=footprint_data)
        if footprint_serializer.is_valid():
            footprint_serializer.save()
            return JsonResponse(footprint_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(footprint_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Footprint.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Footprints were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def footprint_detail(request, pk):
    try:
        footprint = Footprint.objects.get(pk=pk)
    except Footprint.DoesNotExist:
        return JsonResponse({'message': 'The footprint does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        footprint_serializer = FootprintSerializer(footprint)
        return JsonResponse(footprint_serializer.data)

    elif request.method == 'PUT':
        footprint_data = JSONParser().parse(request)
        footprint_serializer = FootprintSerializer(footprint, data=footprint_data)
        if footprint_serializer.is_valid():
            footprint_serializer.save()
            return JsonResponse(footprint_serializer.data)
        return JsonResponse(footprint_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        footprint.delete()
        return JsonResponse({'message': 'Footprint was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def footprint_list_published(request):
    footprints = Footprint.objects.filter(published=True)

    if request.method == 'GET':
        footprints_serializer = FootprintSerializer(footprints, many=True)
        return JsonResponse(footprints_serializer.data, safe=False)

# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Choice, Lifestyle, UserChoice


# def index(request):
#     return JsonResponse({"message": "Welcome to Footprints API"})


# def footprint_list(request):
#     choices = Choice.objects.all().values()
#     return JsonResponse(list(choices), safe=False)


# def footprint_detail(request, pk):
#     try:
#         choice = Choice.objects.get(id=pk)
#         return JsonResponse({
#             "id": choice.id,
#             "name": choice.name,
#             "carbon": choice.carbon,
#             "lifestyle": choice.lifestyle.name
#         })
#     except Choice.DoesNotExist:
#         return JsonResponse({"error": "Not found"}, status=404)


# def footprint_list_published(request):
#     # Assuming all choices are "published" for now
#     choices = Choice.objects.all().values()
#     return JsonResponse(list(choices), safe=False)
