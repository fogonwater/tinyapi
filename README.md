## tinyapi

A tiny, tiny project to demonstrate Flask-RESTful.

There are two styles of GET call. 
```
/dice/<num_sides>
/dice/<num_sides>/<num_rolls>
```

Roll one six-sided dice.
```
http://127.0.0.1:5000/dice/6
```

Roll three six-sided die.
```
http://127.0.0.1:5000/dice/6/3
```

Flask-RESTful : https://flask-restful.readthedocs.org/en/0.3.1/index.html
