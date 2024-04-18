# Resources and Report Forms
### Multiple relationship on resource data form or form

Suppose we have two related resource forms so:  
Resource A has a one-to-many relationship with Resource B  
So on a form we want to insert two select fields connected to Resource A and Resource B  
So that when the value in the select of Resource A changes, the data in Resource B is updated consistently.  

Create a new named resource  
- Title : Resource A
- Name: resource_a
- Fields:
    - **Field Name**: no changes
    - **Field Text**: Name: Label, Property Name:  label  

Create a new named resource  
- Title : Resource B
- Name: resource_b
- Fields:
    - **Field Name**: no changes
    - **Field Text**: Name: Label, Property Name:  label
    - **Model List**: 
        - **Data Source Type**:  Resource
        - **Resource**: Resource A
        - **Validation**: Required check  

At this point we have created the relationship between the resources, and it is possible to load the data.  
Now let's continue by creating a new Form  
- **Title** : Form Resources Rel
- **Name**: form_resources_rel
- **Fields**:
    - **Field Name**: no changes
    - **Model List**: 
        - **Data Source Type**:  Resource
        - **Property Name**:  resource_a
        - **Resource**: Resource A
        - **Validation**: Required check
    - **Model List**: 
        - **Data Source Type**:  Resource
        - **Resource**: Resource B
        - **API->​​Custom Properties**: key: domain, value: {}
        - **Logic -> Advanced Logic**:
            - **Logic Name**: make domain  
                **Trigger ->JSON Logic**:
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
        - **Actions**:
            - **Action Name**: Set Value
            - **Type**: Value
            - **Value (Javascript)**: domain  

Save so now we move on to loading the data onto the form **Rel. Resources Form** and we can see that when the value of changes **Resource A** the options ofResource Bare modified.  
Through logic **make domain** it is possible to create even very complex queries if necessary.

[Return home](../index.md)