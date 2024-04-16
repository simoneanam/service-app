# Form Builder Components

All components in the builder are or are derived from the default components of [Formio.js](https://formio.github.io/formio.js/app/builder)  
The system integrates this tool for creating Drag&Drop forms and makes them available to the user in the form of an App with [graphics adhering to AGID guidelines](https://italia.github.io/bootstrap-italia/docs/come-iniziare/introduzione/)  
Not all the features of Formio.js have been managed but only those useful for the purpose of the project.  
As regards the basic functionality of the project, see [general documentation of the application](https://docs.google.com/document/d/1eSXA8a7Gd9tm-iV7kv4eN7dPhJgc4OInUUwxjZ6DXpY/edit#)  

## **Metadata**  
Metadata is data present in each model (form) and is automatically enhanced when creating/modifying a form record.
The list of metadata is as follows:  
**id, rec_name, owner_uid, owner_name, owner_sector, owner_sector_id, owner_function, update_datetime,create_datetime,owner_function_type, sys, demo, deleted, list_order, owner_personal_type, owner_job_title**

# Basic functionality of all components:
### The following properties are managed in the components:  
**Display:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Custom CSS Class →** classes can be used [Bootstrap 4](https://italia.github.io/bootstrap-italia/1.x/docs/utilities/colori/)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hidden →** set the field hidden or not  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Disabled  →** disables the field and makes it read-only and does not save the data.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Table View →** displays the field in the list view or not  
**Validation:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Required →** makes the field mandatory in the form  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Unique →** checks that the field value is unique in the db, renders the field mandatory in the form  
**Api:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Property Name → is the name of the field in the database  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Custom Properties →** this configuration depends on the type of functionality adds the field; Yessee the specific documentation of the components  
**Conditional:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Advanced Conditions [Json-logic](logic.md#Guide)  
**Logic:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Json-logic](logic.md#Guide)  
### <font color="#FA8072">In the components the following properties are **<font color = "#ff6063">not</font>** managed:</font>

**Display:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label Position  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initial Focus   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hide Label 

**Validation:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Validate On  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Error Label  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Custom Error Message  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Custom Validation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JSONLogic-Validation  

**API:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Field Tags  
**Conditional:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Simple  

### Icons 
Regarding the icons and images available in the interfaces, refer to [official AGID guide](https://italia.github.io/bootstrap-italia/docs/utilities/icone/).
