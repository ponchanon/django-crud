from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_data(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_data(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PATCH'])
def update_data(request,id):
    item = Item.objects.get(id=id)
    serializer = ItemSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_data(request,id):
    try:
        item = Item.objects.get(id=id)
        serialized_data = ItemSerializer(item).data
        serialized_data['id'] = item.id
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
    item.delete()
    return Response(serialized_data, status=200)