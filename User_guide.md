# User guide
## Hoe gebruik ik dit project ?
Dit project is bedoelt om als backup systeem te werken voor het oorsprongelijke project. Het is minder geavanceerd dan het main project, meer info hierover kan men vinden in de README.md file.

Dit systeem is niet moeilijk te gebruiken. Elke werknemer die zich komt aan/af melden zal op de knop "aanmelden of afmelden" moeten drukken. Vervolgens zal er een lichtje 3x beginnen knipperen. Dit is de tijd dat men heeft om de QR-code klaar te houden voor de camera. Houd de QR-code tussen de 15 en 20 centimeter van de camera zodat de camera een duidelijke foto kan nemen. Vervolgens zal het RGB led groen schijnen als de QR-code met succes is gelezen en de waarden van de QR-code is doorgestuurd naar de LoRa gateway.  Indien de RGB led rood kleurt is er iets mis gegaan. Met zal namelijk dan nog eens op de knop moeten drukken en heel dit proces nogmaals uitvoeren.

## Hoe komt de data in de database ?
Elke keer men op een knop drukt en een QR-code scant zal de waarden van deze QR-code worden omgezet in individuele bytes, manelijk ascii bytes. De waarden van de QR-code stelt de persoonlijke id voor van de werknemer. Deze bytes zullen dan via het LoRa netwerk een voor een worden doorgestuurt. De MQTT server neemt deze bytes en zet deze om in één base64 string. Dit omdat het performanter is op de server. Dan komt de mqttserver.py code in actie. Deze zorgt ervoor dat de base64 string omgezet word in text formaat. Deze text formaat zal dan ook in de database worden geschreven.
