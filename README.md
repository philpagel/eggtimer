# Egg time

This is a simple app for making perfect boiled eggs. Enter the eggs weight and
starting temperature as well as the desired target temperature and get the
perfect boiling time. You can read up on the background on my
[blog](http://techbotch.org/blog/how-to-boil-an-egg/index.html#how-to-boil-an-egg)
– sorry only in German right now. If you are intersted in the derivation of the
equations behind this, please go to Charles D. H. Williams'
[page](https://newton.ex.ac.uk/teaching/CDHW/egg/).


## command line usage

You can run this from the command line like this:

    ./eggtime.py

And this are the options you can set:

      -m, --mass INTEGER       Egg mass [g]
      -s, --t0 INTEGER         Starting temperature [°C]
      -t, --t1 INTEGER         Target temperature [°C]
      -e, --elevation INTEGER  Elevation over sea level [m]
      --help                   Show this message and exit.


## Flask application

For the graphically inclined, there is also a FLASK app that wraps the functionality 
for online use. Start it with

    flask run

And point your favorite browser to the URL that flask tells you to use.

## run with docker

To run the flask app as a docker container, use the supplied `compose.yaml` file:

    docker compose up


## Target temperatures

I like softboiled eggs with a target temperature of 70°C. I did not work out a
full table of temperatures and resulting texture. And accurately describing egg
texture is somewhat tricky anyway. I recommend working backwards from what you
already know: Start with the boiling time you used so far, weigh an egg and boil
it for that time. Now you have a starting point and you can easily adjust your
time from there and get highly consistent results for any size egg in the
future.

Maybe I will put together a table at some point.
