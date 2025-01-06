# This implementation uses the API 'ForniteApi.io'
import requests
import os 
import json

class FortniteApiIo():
    base_url = 'https://fortniteapi.io'
    headers = {
        "Authorization": os.getenv('FORTNITE_API_IO_KEY') # Get API Key
    }
    
    def get_list_of_current_loot(self):
        # Hardcoded because there doesn't seem a way to find the weapons enabled for Battle Royale in the API
        # TODO: Find a way to get the weapons that are in BR
        
        # This includes all weapons and utility items, like shockwave grenades, bushes, oni mask, mini shields, etc.
        loot = ["Rifle de asalto holotornado", 
                "Rifle de asalto de furia", 
                "Escopeta de corredera Sentinel", 
                "Escopeta automática de doble disparo", 
                "Escopeta Oni",
                "Subfusil de precisión velado",
                "Subfusil de descarga de fuego",
                "Pistola con silenciador",
                "Rifle de caza", 
                "Máscara de oni del vacío", 
                "Máscara de oni de fuego", 
                "Gustambo de agua",
                "Gustambo de viento",
                "Espada tifón",
                "Granada de arbusto",
                "Búnker portatil",
                "Granada de impulso",
                "Granada de racimo",
                "Pezqueñin",
                "Pescao",
                "Pez de escudo",
                "Vendajes",
                "Botiquín",
                "Mini escudo",
                "Escudo grande",
                "Salpicón saludable",
                "Bidón de gasolina",
                "Caña de pescar"
            ]
        
        return loot
        
    def get_list_of_current_pois(self):
        # lang=es means the language of the returned POI's name is in Spanish. 
        # for english you use "lang=en". See other languages available in fortniteapi.io documentation
        response = requests.get(FortniteApiIo.base_url + '/v2/game/poi?lang=es', 
                                headers = FortniteApiIo.headers)
        
        if response.status_code == 200:
            # Use .content to access to all the content that we receive from our request
            # If we just use response we will get only <Response [Status Code]>
            # Decode the response.content from bytes into string, then convert that string into a dictionary
            json_data = json.loads(response.content.decode('utf-8'))
            locations = [] 
            
            for location in json_data.get("list"):
                location_name = location['name']
                locations.append(location_name)
                
            return locations
        else: 
            print("ERROR")