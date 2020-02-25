# code uitleg

In deze map vind men 2 .py bestanden. Eén daarvan dient op de raspberry pi uitgevoert te worden. en één daarvan dient op de server uitgevoert te worden (op de server waar de frontend en backend op staat).

## Qr+Lora.py
Deze code dient op te draaien op de raspberry pi. wat er juist gebeurt in deze code: 
 * lijn 1 tot 62: Dit is initialisatie code. Hier zullen we all de gpio poorten een funtie geven, de camera instellen, de keys instellen van de the tings network. Deze keys heb je nodig om je raspberry pi te koppelen aan het apparaat dat je online hebt aangemaakt.
 * lijn 63 tot 76 : Deze functie zorgt ervoor als men op een knop drukt dat er een foto word genomen.
 * lijn 78 tot 142: Hier zullen we de foto scannen op een QR-code als de code gelezen is zal het deze code doorsturen via de LoRa module.
 * lijn 147 tot 156: Dit is de main part of de code. Dit houd in dat dit een loop is dat heel de tijd word herhaalt zolang er niks gebeurd. Als men op een knop drukt zal er een interupt in werking komen die de rest van de   bovenstaande code zal activeren.

## mqttserver.py
      Deze code zal draaien op de server kant.
         * 
