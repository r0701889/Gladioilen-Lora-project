# Gladioilen-LoRa-project

# Inleiding
Gladiolen had ons gevraagd om een applicatie te maken waarmee werknemers zich kunnen inchecken en uitchecken. De werknemers zouden dan zo geld kunnen inzamelen voor hun organisatie. De vraag was om via een android applicatie zo een systeem te maken dat verbind met een database op de server en dat alle data keurig wordt bijgehouden. De android toestellen zouden met 4G verbinden met de server. Als je als werknemer komt werken is het de bedoeling dat je je persoonlijke QR-code komt scannen. Deze Qr-code heeft een persoonlijke ID dat aan jou gelinkt is. Zo weten we wie er zicht heeft komen aanm/af melden

Het project waar ik aan heb gewerkt is een back-up systeem van dit project. Op de meeste festivals is er geen wifi en zit iedereen op 4G te surfen met het internet. Er is dus een kans dat de 4G op bepaalde momenten niet zal werken. Daar heb ik namelijk een oplossing voor gevonden. Aan de raspberry pi is een camera bevestigd die de Qr-code zal scannen van de werknemer. Met een LoRa netwerk heb ik ervoor gezorgd dat de database nog steeds word aangevuld met data van de werknemers. Dit zonder directe wifi of 4G. 

# Instalation guide
## Mijn log terminal
De log terminal is een raspberry pi met zijn nodige componenten dat ervoor zorgt dat de mensen zich hier kunnen aan/af melden. Wanneer iemand zich komt melden zal er via het LoRa netwerk naar de database de registratie worden verstuurd.
  * Raspberry pi (in mijn geval heb ik een raspberry pi 3b+ gebruikt)
  * Jumper kabels
  * RGB led
  * Led naar keuze
  * 2 Knoppen
  * 3 Weerstanden 220 ohm
  * 2 Pull down weerstanden 10k ohm
  * Adafruit RFM9x LoRa Radio
  * Raspberry pi camera

![Fritzing_40](https://user-images.githubusercontent.com/38457884/75234731-626c7f80-57bb-11ea-82a4-980ed84fb3ce.png)

## LoRa netwerk
Het grote voordeel van LoRa is dat het tot grote afstanden kan verbinden. Aan de andere kant heeft het LoRa netwerk ook een groot nadeel. Het is niet geschikt voor grote bestanden te versturen. Voor dit project is het duidelijk geschikt. Men moet alleen de Id van de Qr-code versturen wat uit niet meer dan 7 bytes bestaat. Er bestaan 2 soorten LoRa gateways: indoor gateways en outdoor gateways. De indoor gateways zal ongeveer een bereik hebben van 500m. Als je voor een outdoor zal gaan kan het bereik gaan van 1 tot 10 km. Dit hangt af van de sterkte van de gateway.
Voor mijn project heb ik een indoor gateway gebruikt omdat ik in de testfase de gateway altijd dicht bij had staan. Via deze link (http://bit.ly/2vhDSL4) heb ik de LoRa gateway geconfigureerd met het internet. Zo kan het LoRa netwerk connecteren met de servers die verbonden zijn aan het internet. 


## De server kant
Nadat de raspberry pi zijn data heeft verzonden naar de LoRa gateway heeft de gateway deze data op een MQTT server gezet. Dit is een server waar alle data bijeenkomt van het LoRa netwerk. Voor de data af de MQTT server te halen heb ik een script geschreven die op de server van gladiolen zal draaien. Het script zal continu kijken of er geen niewe waarden is binnen gekomen op de MQTT server. Als er een nieuwe waarden is toegekomen zal hij deze data af de server halen. Deze data staat op de server in base64 code. Dit om het zo performant mogelijk te maken voor de MQTT server. In mijn script dat op onze server staat te draaien zal ik de base64 code omzetten naar text formaat. Nu ik bruikbare data heb kan ik deze poushen naar de backend. Deze backend is reeds geschreven voor ons hoofdproject. In de readme staat uitgelecht wat het oorspronkelijke project is. In het oorspronkelijke project hebben ze een backend gemaakt die ik ook gebruik. 

