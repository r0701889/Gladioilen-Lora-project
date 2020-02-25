# Gladioilen-Lora-project

# Inleiding
Gladiolen had ons gevraagd om een applicatie te maken waarmee werknemers zich kunnen inchecken en uitchecken. De werknemers zouden dan zo geld kunnen inzamelen voor hun organisatie. De vraag was om via een android applicatie zo een systeem te maken dat verbind met een database op de server en dat alle data keurig wordt bijgehouden. De android toestellen zouden met 4G verbinden met de server. Als je als werknemer komt werken is het de bedoeling dat je je persoonlijke QR-code komt scannen. Deze Qr-code heeft een persoonlijke ID dat aan jou gelinkt is. Zo weten we wie er zicht heeft komen aanm/af melden

Het project waar ik aan heb gewerkt is een back-up systeem van dit project. Op de meeste festivals is er geen wifi en zit iedereen op 4G te surfen met het internet. Er is dus een kans dat de 4G op bepaalde momenten niet zal werken. Daar heb ik namelijk een oplossing voor gevonden. Aan de raspberry pi is een camera bevestigd die de Qr-code zal scannen van de werknemer. Met een Lora netwerk heb ik ervoor gezorgd dat de database nog steeds word aangevuld met data van de werknemers. Dit zonder directe wifi of 4G. 

# Mijn log terminal
De log terminal is een raspberry pi met zijn nodige componenten dat ervoor zorgt dat de mensen zich hier kunnen aan/af melden. Wanneer iemand zich komt melden zal er via het LoRa netwerk naar de database de registratie worden verstuurd.
  - Raspberry pi (in mijn geval heb ik een raspberry pi 3b+ gebruikt)
  - Jumper kabels
  - RGB led
  - Led naar keuze
  - 2 Knoppen
  - 3 Weerstanden 220 ohm
  - 2 Pull down weerstanden 10k ohm
  - Adafruit RFM9x LoRa Radio
  - Raspberry pi camera
  
  
