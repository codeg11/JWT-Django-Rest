# JWT-Django-Rest

Instalar el requirements.txt desde pip

La token se genera por medio de la libreria de django-restFramework-jwt

las urls de la libreria son 
<ul>
  <li>'api-token-auth/'</li>
    <li>'api-token-refresh/'</li>
   <li> 'api-token-verify/'</li>
   <li> 'api/v1/'</li>
  
 </ul>
 
 y las urls para hacer el test de las vistas para ya sea registrar un usuario o un modelo (en este caso un modelo llamada producto), el cual contiene los permisos para saber si un usario esta logeado o no
 
<img src="https://i.imgur.com/betFSZe.png">

si quieres hacer alguna peticion por postman con la JWT seria de la siguiente manera 

<img src="https://i.imgur.com/YHrqoxn.png">

la url http://127.0.0.1:8000/api/v1/hello_world

tiene la vista de:

<img src="https://i.imgur.com/QIDHpGl.png">
