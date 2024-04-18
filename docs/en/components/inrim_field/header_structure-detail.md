### Header structure/detail
1. Prepare the header form
2. Prepare the form to use to manage the rows
3. Update the header form by adding the following components:  
    ![struttura_testata_dettaglio](../../../img/componenti/inrim_field/struttra_testata_dettaglio.png "struttura_testata_dettaglio")  

In the [columns](../layout/columns.md#it-does-not-require-additional-configurations-if-necessary-use-the-standard-configurations) add a [button to add](../base/button.md#button) the rows in the table  
Add one [Search Area](../data/search_area.md#search-area) to define the default relationship between the two forms  
As regards the Search Area, it is important that:  
- The query property is →**query** {'parent':''}
- The basic logic (json logic):  
```
  "logic": [
    {
      "name": "all",
      "trigger": {
        "type": "json",
        "json": {
          "var": "form.rec_name"
        }
      },
      "actions": [
        {
          "name": "eval query",
          "type": "value",
          "value": "query={\"cat\":[\n    \" {'$and':[{'parent':'\",\n       
                          {\"var\":\"form.rec_name\"},\n    \"'}]}\"\n]}"
        }
      ]
    }
  ]
```

 Finally add the [table that will contain the rows, also activating copy and delete](../data/table.md#table) 

[Return home](../../index.md)
