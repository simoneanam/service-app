# Actions
### Cambiare il testo della funzione ‘Nuovo’ per il form IPA Request

Dal menu **Config**  selezionare  **Azioni Apps**

![Change the text of the 'New' function for the IPA Request form](../../img/project_structure/change_the_text_img1.png)

Usare il pulsante **Filtri** e aggiungere la regola:  **Model = “nome model”**  es con **IPA Request
Model == IPA Request**  

![Change the text of the 'New' function for the IPA Request form](../../img/project_structure/change_the_text_img2.png)

Cliccare sull’elemento che si vuole modificare:   in questo caso il Title **“Nuovo”**  


scrivere il nuovo testo, ad es. aggiungere le parentesi quadre, **[ Nuovo ]**  
e cliccare sul pulsante **Submit**  

![Change the text of the 'New' function for the IPA Request form](../../img/project_structure/change_the_text_img3.png)


Risultato:  

![Change the text of the 'New' function for the IPA Request form](../../img/project_structure/change_the_text_img4.png)

### Filtri Data nelle azioni
E’ possibile inserire filtri data calcolati nelle azioni utilizzando un sistema di meta comandi:  

Solo date:  

**_date_today-10**  → 10 giorni dopo oggi:  
- Se oggi e’ il 10-10-2021  
- Il risultato sarà →  2021-10-20T00:00:00   

**_date_today-n-4** → 4 giorni prima di oggi:   
- Se oggi e’ il 10-10-2021  
- Il risultato sarà →  2021-10-06T00:00:00  

Nel caso le date nel form siano di tipo **DateTime** nella query va considerato today  
Come data ultimo secondo  23:59:59  

Ad esempio se si vuole fare un filtro “oggi”  al 20/20/2021 con un campo DateTime nel form
La query deve considerare da mezzanotte ad oggi ultimo secondo:
2021-10-20T00:00:00 <-> 2021-10-20T23:59:59

**_date_today-10**  → 10 giorni dopo oggi:  
- Se oggi e’ il 10-10-2021  
- Il risultato sarà →  2021-10-20T00:00:00  

**_date_today-10-max**  → 10 giorni dopo oggi:  
- Se oggi e’ il 10-10-2021  
- Il risultato sarà →  2021-10-20T23:59:59  
E’ possibile usare anche il max con i giorni in negativo cioè’ con la notazione **“n”.**  

[torna alla home](../index.md)