# Design 
### Generale

Il sistema di design dei form e di conseguenza dei model si basa su Formio.Js.  
Per l’elenco dei componenti disponibili che si possono inserire sui form si faccia riferimento al [documento dedicato](../index.md#L9)

Quando si crea un nuovo elemento Form/Risorsa si possono configurare alcuni dati di base:  

![General](../../img/project_structure/general.png)

**Titolo:** Titolo dell’ elemento, sarà visualizzato come intestazione della Card e di base nei nomi dei menu di default  
**Name:** E’ il nome univoco del form, utilizzato nel database come indice per cercare l’elemento stesso.  
**Sys:** Se impostato a Si identifica l’elemento come un elemento di sistema, ne viene creato un menù a tendina, non sarà visibile nelle cards e sarà accessibile solo dagli Admins  
**Model:** 
- Si → default→ viene generata una tabella nel database in modo dinamico dove salvare i dati e vengono generate in automatico le azioni di default  
- No → il form non prevede mai salvataggio di dati  
- TODO → **nome di un model** →  l’elemento è un’interfaccia diversa da quella base per il model selezionato con numero di campi inferiore o disposti in modo diverso ma che legge i dati dalla tabella del database del modello selezionato,  non crea la tabella nel database , ma crea le azioni di default 

**Display as:** TODO per ora solo FORM  
**Vedi Pulsante 'Abbandona'**:   Si → visualizza il **Abbandona** nel form, No → non lo visualizza  
**Gestisci onchange Globale:** se ci sono logiche nei componenti impostare a “Si” in modo che il form alla modifica di ogni campo elabori le logiche  

Sotto le configurazioni di base ci sono i tab:  
**Builder:** → E’ l’area che implementa **Formio.js** builder e rende disponibile i componenti drag&drop per disegnare gli elementi 

**Layout di Stampa** → E’ l’area che permette di disegnare un layout stampabile del form.  
Mette a disposizione un componente WYSIWYG tipo Word semplificato ed è possibile inserire all’interno placeholder che verranno valorizzati con i dati del **Form**  
I placeholder del form vanno inseriti con notazione [Jinja2 Templating](https://jinja.palletsprojects.com/en/3.0.x/templates/)

Tutti i form sono salvati nella tabella **Component** del database.  
In base al tipo di menu, il campo type del record Component creato dal builder imposta il valore specifico:

1. **Form** → Component.type = “form”  
2. **Risorse** → Component.type = ”resource”  
3. **Layout** → Component.type = ”layout” (Wip)  

[torna alla home](../index.md)

