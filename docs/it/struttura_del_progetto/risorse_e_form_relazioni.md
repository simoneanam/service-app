# Risorse e Form Relazioni
### Relazione multipla su form di dati risorse o form

Supponiamo di avere due form di risorse correlati per cui:

Risorsa A ha una relazione uno a molti con Risorsa B

Quindi su un form vogliamo inserire due campi select collegati alla Risorsa A e alla Risorsa B
In modo che quando cambia il valore nella select della Risorsa A i dati nella Risorsa B vengano aggiornati in modo coerente.

Creare una nuova risorsa con nome   
- Title : Risorsa A  
- Name: risorsa_a
Campi:  
    - **Field Name**: nessuna modifica  
    - **Field Text**: Name: Label, Property Name:  label  

Creare una nuova risorsa con nome   
- Title : Risorsa B  
- Name: risorsa_b  
- Campi:  
    - **Field Name**: nessuna modifica  
    - **Field Text**: Name: Label, Property Name:  label  
    - **Model List**:  
        - **Data Source Type**:  Resource  
        - **Resource**: Risorsa A  
        - **Validation**: Required check  

A questo punto abbiamo creato la relazione tra le risorse, ed ‘ possibile caricare i dati.  
Ora proseguiamo creando un nuovo Form  
- **Title**: Form Risorse Rel  
- **Name**: form_risorse_rel  
- **Campi**:  
    - **Field Name**: nessuna modifica  
    - **Model List**:   
        - **Data Source Type**:  Resource  
        - **Property Name**:  resource_a  
        - **Resource**: Risorsa A  
        - **Validation**: Required check  
    - **Model List**:   
        - **Data Source Type**:  Resource  
        - **Resource**: Risorsa B  
        - **API->​​Custom Properties**: key: domain, value: {}  
        - **Logic -> Advanced Logic**:  
            - **Logic Name**: make domain  
                **Trigger ->JSON Logic:** 
                 ```
                       {
                        "cat": [
                            "{'resource_a':'",
                            {
                            "var": "form.resource_a"
                            },
                            "'}"
                        ]
                       }
                     ```
        - **Actions**: note
            - **Action Name**: Set Value
            - **Type**: Value
            - **Value (Javascript)**: domain note

Salva quindi ora ci spostiamo a caricare i dati sul form **Form Risorse Rel** e possiamo notare che quando cambia il valore di **Risorsa A** le opzioni di **Risorsa B** vengono modificate.  
Attraverso la logica **make domain** è possibile creare query anche molto complesse se fosse necessario.  

[torna alla home](../index.md)

