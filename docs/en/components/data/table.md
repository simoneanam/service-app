### Table:  
configurable section **Api → Custom Properties**  
**action_name→** the name (**rec_name**) of the action to use to populate the table
**action_url→** URL of the action  **/action/{action.rec_name}**  
**model→** the model (form.rec_name) linked to the table  
**show_owner→** default **"no"** , if different from no the column is displayed **owner_full_name** in the table  
**hide_select_chk →** default **"no"**, if different from no the column is hidden **checkbox** in the table  
**list_metadata_show→** you can add a list of [metadata fields](../../base.md#metadata) separated by comma, If you have a nested table (detail header form) use the field **parent**  
**dom→** default **content**,configuration of [dom in the datatable](https://datatables.net/reference/option/dom "dom")  
**Query →** default **{}**   
**calculateServer →** enter the name of a method that is executed when submitting the form, use only it is a table integrated into the detailed header form 

<table>
 <tr >
   <td valign=top>
       <font size = 1>
       "action_url": "/action/list_people_list_users",<br>
      "model": "people_list_users",<br>
      "show_owner": "no",<br>
      "hide_select_chk": "no",<br>
      "list_metadata_show": "parent",<br>
      "home": "iptilp",<br>
      "query": "{}",<br>
      "action_name": "list_people_list_users",<br>
      "calculateServer": "eval_user_list",<br>
      "modal": "yes",<br>
      "copy_url":  action_url_copy ,<br>
      "remove_url":  action_url_remove <br><br>
      Action_url_copy, action_url_remove must be urls in the format:/action/action_name<br><br>
      Where <b>action_name</b> it is the name field of the action that is possible Copy into the section <a href=https://docs.google.com/document/d/1eSXA8a7Gd9tm-iV7kv4eN7dPhJgc4OInUUwxjZ6DXpY/edit#bookmark=id.ci2ew347c7uv> Actions</a> for the desired action, copy and/or delete</font>
   </td>
   <td>
   <img src="../../../img/componenti/data/table_img1.png" alt="Panel">
   </td>
 </tr>
</table>

