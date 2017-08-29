**Create a contact**
----
* **URL**

  api/v1/contacts/

* **Method:**

  `POST`
  
*  **URL Params**

   None
 
* **Data Params**

  ```
  {
    "name": "Steve",
    "email": "steve@mail.com",
    "age": 35,
    "state": "SC",
    "position": "Developer"
  }
  ```

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{ id : 12 }`
 
* **Error Response:**

  None


**Create a segmentation**
----
* **URL**

  api/v1/segmentations/

* **Method:**

  `POST`
  
*  **URL Params**

   None
 
* **Data Params**

  ```
  {
    "query": {
      "AND": [
         {
             "column": "age",
             "operator": ">",
             "value": 10,
             "type": "numeric"
         },
         {
             "column": "state",
             "operator": "=",
             "value": "SC",
             "type": "text"
         }    
      ]    
    }
  }
  ```

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{ id : 12 }`
 
* **Error Response:**

  None

**Search contacts by segmentation**
----
* **URL**

  api/v1/segmentations/{segmentation_id}/contacts/

* **Method:**

  `GET`
  
*  **URL Params**

   None
 
* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    ````
    [
      {
        "name": "Steve",
        "email": "steve@mail.com",
        "age": 35,
        "state": "SC",
        "position": "Developer"
      }
    ]
    ```
 
* **Error Response:**

  None
