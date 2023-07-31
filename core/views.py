from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings

import requests

from .models import *
from .forms import SubmitEmbed
from .serializer import EmbedSerializer, CartItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# https://docs.embed.ly/v1.0/docs/oembed
def users(request):

    # Connecting API
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    # Convert reponse data into json
    users = response.json()

    print(users)
    context = {'users': users}
    return render(request, 'core/users.html', context)


def todos(request):

   # get the list of todos
   response = requests.get('https://jsonplaceholder.typicode.com/todos/')

   # transfor the response to json objects
   todos = response.json()

   context = {"todos": todos}
   print(todos)

   return render(request, "core/todo.html", context)


def save_embed(request):

    if request.method == 'POST':
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            response = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
            json = response.json()
            serializer = EmbedSerializer(data=json)
            #obj = serializers.ShiftSerializer(shift)
            if serializer.is_valid():
                embed = serializer.save()
                return render(request, 'core/embeds.html', {'embed': embed})
            else:
                return HttpResponse("Error")
    else:
        form = SubmitEmbed()
    return render(request, 'core/embeds.html', {'form': form})


# Response Common Model
# curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/cart-items/ -d "{\"product_name\":\"name\",\"product_price\":\"41\",\"product_quantity\":\"1\"}"
# curl -X GET http://127.0.0.1:8000/api/cart-items/
# curl -X GET http://127.0.0.1:8000/api/cart-items/1
# curl -X PATCH http://127.0.0.1:8000/api/cart-items/1 -H 'Content-Type: application/json' -d '{"product_quantity":6}'
# curl -X "DELETE" http://127.0.0.1:8000/api/cart-items/1
"""
{
"product_name": "name",
"product_price": 34,
"product_quantity": 3
}
"""
class CartItemViews(APIView):

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = CartItem.objects.get(id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


def decimal_test(request, id):
    test_object = get_object_or_404(Test, id=id)
    #test = Test.objects.filter(id=id)
    context = {"test_object": test_object}

    return render(request, "test.html", context)



import http.client
import mimetypes
from codecs import encode

def send_request():
    """
    conn = http.client.HTTPSConnection("4com.manas.com.tr")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=username;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("atlasyazilim"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=password;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("123654a"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=lang;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("tr"))
    dataList.append(encode('--' + boundary + '--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/login?ajax=true", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data2 = res.headers
    print(data2)
    print(data.decode("utf-8"))
    """
    import http.client
    import json

    conn = http.client.HTTPSConnection("4com.manas.com.tr")
    payload = json.dumps({
        "username": "atlasyazilim",
        "password": "123654a"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'laravel_session=eyJpdiI6IlJsRFJ0MktBSUc0QUgyOXdnMVhMYUlSWlBORUVcLzdiQThza1VOa3g3NlRjPSIsInZhbHVlIjoiVVFGSE1kZmROb1MxRkY1N1E2aERrWHRrNEhLYjZIRWRqZFAyclNaTmVwSGhDcWJCNFg3bUhmd2lMZ0V2eTJoVDFQVDRWSUJ3RjJ0Y2hma1JPR3prQXc9PSIsIm1hYyI6IjJkNmFkMWE3OGQ4ZWY4NmE3MGQ4OTE2ZDdmNTBmYThkYTM2NDI1MGQ3MzQ1ZTAwYmYzODMyNzYxMWI1YzQ3YjQifQ%3D%3D'
    }
    conn.request("POST", "/login?ajax=true", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    #print(res.headers)


if __name__ == '__main__':
    send_request()
