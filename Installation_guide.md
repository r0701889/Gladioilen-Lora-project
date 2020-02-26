# Installation guide
## Mijn log terminal
De log terminal is een raspberry pi met zijn nodige componenten dat ervoor zorgt dat de mensen zich hier kunnen aan-/afmelden. Wanneer iemand zich komt melden zal er via het LoRa netwerk een registratie naar de database  worden verstuurd.
  - Raspberry pi (in mijn geval heb ik een raspberry pi 3b+ gebruikt)
  - Jumper kabels
  - RGB led
  - Led naar keuze
  - 2 Knoppen
  - 3 Weerstanden 220 ohm
  - 2 Pull down weerstanden 10k ohm
  - Adafruit RFM9x LoRa Radio
  - Raspberry pi camera

![Fritzing_40](https://user-images.githubusercontent.com/38457884/75234731-626c7f80-57bb-11ea-82a4-980ed84fb3ce.png)

## LoRa netwerk
Het grote voordeel van LoRa is dat het tot grote afstanden kan verbinden. Aan de andere kant heeft het LoRa netwerk ook een groot nadeel. Het is niet geschikt voor grote bestanden te versturen. Voor dit project is het duidelijk geschikt. Men moet alleen de Id van de Qr-code versturen wat uit niet meer dan 7 bytes bestaat. 
