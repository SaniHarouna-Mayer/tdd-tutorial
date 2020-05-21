Hands on task
------------------------
1. your mission is to write a function called ``is_current(item:dict)``
1. it takes a dict like object and returns true if the item in the object is current and 
   False if it is finished or if it hasn't happened yet
1. Examples of such things are in the file ``currenty_things.yml``. The function
   should work when any one of these is handed to it
1. There are at least two approaches to doing this (see below).  For the purpose
   of this exercise please write two test, one that does it each way, to get a 
   feeling for the advantages and disadvantages of each 
    1. use pytest.parameterize to explicitly give the all the different possible 
       types of currenty things
    1. read the yml file and pass all the objects in there to the function to 
       test them one at a time.  Note, that in more advanced usage this could be 
       done using a pytest.fixture decorator
