from tools_views import *
import json
from webservice.models import Boardgames
import base64
import urllib2
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addGame(request):
    if request.method == "POST":
        try:
            newgame = json.loads(request.body)

            game = Boardgames()

            game.name = newgame['name']
            game.max_player = newgame['max_player']
            game.min_player = newgame['min_player']

            if 'sub_name' in newgame:
                game.sub_name = newgame['sub_name']
            if 'date_buy' in newgame:
                game.date_buy = newgame['date_buy']
            if 'price' in newgame:
                game.price = newgame['price']

            if 'image_url' in newgame:
                image_content = urllib2.urlopen(newgame['image_url']).read()
                game.image = "data:image/jpeg;base64," + base64.b64encode(image_content)

            if 'image' in newgame:
                game.image = newgame['image']

            game.save()

            return send_response(True)
        except:
            return send_response("Erreur lors de la sauvegarde.", 500)
