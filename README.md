# application_blocking


task  schedular

general-->  run whether user is logged on r not
            give tick (do not store password)
            tick run with highest privileges
            tick hidden
            

Triggers --> Daily
             Repeat task everyday 5 min
             duration infinitely
             tick ennabled
 
 Action--> script - python exe location
           add  -  filelocation
           
           
settings-->
            allow task to be run on demand
            stop the task
            if the running task does not end when requested force it to stop
            
            run a new instance in parallel
