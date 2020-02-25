# code uitleg

In deze map vind men 2 .py bestanden. Eén daarvan dient op de raspberry pi uitgevoert te worden. en één daarvan dient op de server uitgevoert te worden (op de server waar de frontend en backend op staat).

## Qr+Lora.py
Deze code dient op te draaien op de raspberry pi.Hieronder leg ik de code uit: 
 * Lijn 1 tot 62: Dit is initialisatie code. Hier zullen we all de gpio poorten een funtie geven, de camera instellen, de keys instellen van de the tings network. Deze keys heb je nodig om je raspberry pi te koppelen aan het apparaat dat je online hebt aangemaakt.
 * Lijn 63 tot 76 : Deze functie zorgt ervoor als men op een knop drukt dat er een foto word genomen.
 * Lijn 78 tot 142: Hier zullen we de foto scannen op een QR-code als de code gelezen is zal het deze code doorsturen via de LoRa module.
 * Lijn 147 tot 156: Dit is de main part of de code. Dit houd in dat dit een loop is dat heel de tijd word herhaalt zolang er niks gebeurd. Als men op een knop drukt zal er een interupt in werking komen die de rest van de   bovenstaande code zal activeren.

## mqttserver.py
Deze code dient op te draaien op de server kant (waar de frontend en backend op draait) .Hieronder leg ik de code uit: 
 * Lijn 1 tot 7: Dit zijn de initialisatie codes. Hier connecteren we onze code met de MQTT server doormiddel van de app_id en de acces key te definieren.
 * Lijn 9 tot 19: Dit deel van de code word uitgevoert wanneer er nieuwe data op de MQTT server komt. In deze code zorgt men ervoor dat we de bruikbare data uit de message kunnen filteren. Dan gaat hij met deze data naar de backend schrijven.
 * Lijn 22 tot 36: In dit deel van de code zal het programma meerendeels blijven. Hier wacht men namelijk op nieuwe data in de MQTT server. Als er nieuwe data binnenkomt zal de functie uplink_callback worden opgeroepen (lijn 9 tot 19)
