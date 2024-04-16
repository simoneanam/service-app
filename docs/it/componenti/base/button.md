### Button
Pulsante Azione config sezione **Api → Custom Properties**  
**btn_action_type** → “post”(default)  
**url_action →** url dell’azione che si vuole eseguire   
**leftIcon**  o **rightIcon** → opzionale [impostare un icona](../../base.md#Icone)

Nel caso si voglia utilizzare il pulsante per aggiungere un record in una tabella integrata
aggiungere le seguenti proprieta’
    **todo**: new_row,  
    **default_fields**: {"rec_name":"parent"},  
    **open_modal**: y  → apre il form in una modale  

Oppure nel caso si voglia aprire un form modale, **modalEdit**: y  
Oppure nel caso si voglia esportare dati di una collezzione:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**export**: y  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**url_action**: /client/export/{nome_model}/{type} - type = xls,csv,json  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**body**: {"query": {"$and": [{"active": true}]}}

![button](../../../img/componenti/base/button_img1.png "button")
