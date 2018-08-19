Simple "Hello World" application to allow users to store date of births and check how far the next birthday is.

Tech stack used - 

App - Flask (python)
* Other options considered - Sinatra (ruby)


Storage - Redis
* Tested by running locally on instance, but we can use a central server or service like Elasticache
* Didn't use a relational database because our dataset has only name and date of birth, and a key-value store works great.