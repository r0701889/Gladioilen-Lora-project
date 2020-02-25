# Toekomst plannen
## Inleiding
In dit project is +/- 70 uur werk gestoken. Het deel waat ik het meeste tijd heb aan gestoken is de QR-code te lezen en het versturen als individuele bytes. Daarna heb ik ook heel wat nieuwe kennis moeten opzoeken over LoRa en de MQTT server omdat ik hier nog geen ervaring mee heb gehad. Hierdoor zijn niet al de features van het project af geraakt.

## Feedback 
Wat nog een goede feature is voor deze opdracht is dat het lampje niet alleen groen kleurt als de data is verzonden naar de LoRa gateway. Hiermee weet men niet of de data wel effectief in de database is geraakt. Men kan een validator zetten op The Tings Network zodat hij feedback geeft of de data wel effectief is geraakt op de MQTT server. Als men ook wilt weten of de data in de database is gezet zal men dit moeten aanpassen op de backend waar de data naartoe word gestuurt.

## visuele weergaven
Wat het project ook nog beter kan maken is het implementeren van een schermpje. Dit scherm zal dienen om bijvoorbeeld de inhoud van de QR-code weer te geven. Zodat je zeker weet dat het scannen van de QR-code gelukt is. Of het weergeven van je naam in plaats van de inhoud van de QR code. 

## locale database
Een locale database is ook handig om fouten te vermeiden. Als het verzenden naar de MQTT server of de data te posten in de database mislukt is dit project ook niet meer nuttig. Zo een locale database kan dit probleem oplossen. Zelfs als het nooit word gepost in de database heeft de raspberry pi dan nog een locale database draaien waar al de data zal in worden geschreven. Zo heeft men een backup van dit project.
 
