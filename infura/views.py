from django.shortcuts import render
import requests
from .serializer import *
from .models import *

def infura_initial(request):

    context = {
        'title': 'Infura',
        'description': 'Infura is a decentralized platform for decentralized applications.',
    }

    data = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}

    response = requests.post('https://mainnet.infura.io/v3/f908fbfae9834e459066c0f049ddbd4b', headers={'Content-Type': 'application/json'}, json=data)
    result = response.json()
    json = response.json()
    #InfuraInitial.objects.create(**json)
    serializer = InfuraInitialSerializer(data=result)
    if serializer.is_valid():
        infura_basic = serializer.save() # Create a new object and save it to the database
        context['infura_basic'] = infura_basic
        data_result = infura_basic.result
        data_id = infura_basic.id
        data_jsonrpc = infura_basic.jsonrpc
    context['block_number'] = result['result']

    return render(request, 'infura/infura_initial.html', context)