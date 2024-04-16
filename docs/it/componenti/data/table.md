### Table
configurabile sezione **Api → Custom Properties**  
**action_name→** il nome (**rec_name**) dell’ azione da utilizzare per popolare la tabella  
**action_url→** url dell azione  **/action/{action.rec_name}**  
**model→** il model (form.rec_name) collegato alla tabella   
**show_owner→** default "**no**" , se diverso da no viene visualizzato la colonna **owner_full_name** nella tabella   
**hide_select_chk →** default "**no**", se diverso da no viene nascosta la colonna **checkbox** nella tabella   
**list_metadata_show →** si può aggiungere un elenco di [campi metadati](../../base.md#metadati) separati da virgola, Se si e’ in presenza di una tabella nestata (form testata dettaglio) usare il campo **parent**  
**dom →** default **iptilp**, configurazione del [dom di datatable](https://datatables.net/reference/option/dom "dom di datatable")  
**Query →** default **{}**   
**calculateServer →** inserire il nome di un metodo che viene eseguito in fase di submit del form, utilizzare solo si tratta di una tabella integrata in form  testata detttaglio  

<table>
  <tr >
	<td valign=top>
		<font size = 1>"action_url": "/action/list_people_list_users",<br>
		"model": "people_list_users",<br>
		"show_owner": "no",<br>
		"hide_select_chk": "no",<br>
		"list_metadata_show": "parent",<br>
		"dom": "iptilp",<br>
		"query": "{}",<br>
		"action_name": "list_people_list_users",<br>
		"calculateServer": "eval_user_list"<br>
		"modal": "yes",<br>
		"copy_url":  action_url_copy,<br>
		"remove_url":  action_url_remove <br> <br>
		Action_url_copy, action_url_remove devono essere url nel formato:
		/action/action_name <br> <br>
		Dove <b>action_name</b> e’ il campo name della action che e’ possibile 
		Copiare nella sezione <a href = https://docs.google.com/document/d/1eSXA8a7Gd9tm-iV7kv4eN7dPhJgc4OInUUwxjZ6DXpY/edit#bookmark=id.ci2ew347c7uv>Azioni</a href> per l’azione desiderata, copia e/o elimina</font>
	</td>
	<td>
  	<img src="../../../img/componenti/data/table_img1.png" alt="Panel">
	</td>
  </tr>
</table>
