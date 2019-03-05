# Project description 

Our firm has been contracted to help a mathematician take his amazing
one-million dollar idea to market.  Our client specializes in the field of
complex dynamics, which, frankly, is well above my pay grade, but so is
programming to him.  He has a passion for mathematics education and wants to
take his programs to the K-12 system to teach middle and high-school students
all about the beauty of complex numbers and repeated, tedious calculations.  I
didn't have the heart to tell him that there are already dozens of websites
doing what he wants to do for free; if his inability to use Google keeps us in
steady work, who am I to set him straight?

He has created two prototype programs intended for high school math students.
He quickly realized that creating user-friendly software is perhaps more
difficult than understanding complex dynamics.  This is where we come in.

Our contract is to adapt his programs into a complete *Programming Systems
Product*.  We must also make it usable by non-programmers, which means that
instead of controlling the program by changing hard-coded data within the
source code it must accept configuration files from the command-line and
adjust its runtime behavior accordingly.

Now, I realize that asking a user to create configuration files and run a
program from the command-line is no longer considered user-friendly in the
21st century.  We have two teams working on this project: one team will be
creating a GUI which is what the students will ultimately interact with.  This
GUI will drive the core program that you will create.  Your responsibility is
to make sure that your piece of the Program System adheres to the
configuration file format that the GUI team has defined, as well as the
command-line interface they are expecting.




# Running the programs

Presently, these programs are very simple and self-contained.  They are run
them directly from the command line:

    python src/mandelbrot.py [FRACTAL_NAME]
    python src/julia.py [FRACTAL_NAME]

`FRACTAL_NAME` is the name of a fractal image this program is capable of
producing.  When run without this argument the program lists the names of
fractals it can produce and exits.

If you use PyCharm, create a **Run configuration** to launch the program in
this manner.

Next sprint this program will be made to accept the name of a fractal
configuration file from the command-line so that one does not need to hack the
source code each time they want to produce a new image.  The GUI team has
translated the hardcoded fractal configurations into the sample configuration
files you will find in the `data/` directory.  You may disregard these files
in the first sprint of this project.



# Interactive Mandelbrot Viewer

It is not strictly necessary for you to understand the math behind these
fractals in order to refactor this program.  The mystery of how so much
complexity can arise from iterating a simple formula is what gives it it's
appeal.

However, you will feel much more confident about this if you understand at
least a little bit about what's going on.  To this end I have provided an
interactive Mandelbrot program called `src/interactive.py`.

* Left-Clicking on its Canvas will paint a square region using the same
  algorithm that the `src/mandelbrot.py` program uses, except this program will
  print the values of the Z paramter at each iteration.

* Right-Clicking the Canvas paints the entire image.

Readaing its code and watching its output may help you better understand how
your program produces its images.

**Important:** `src/interactive.py` is provided for your amusement/benefit.
It is *not* a part of the assignment, and you *are not* required to improve it.




# Hints

UsefulJS does a nice explanation of how the Mandelbrot set works and how the
Julia set is related to it:

http://usefuljs.net/fractals/docs/julia_mandelbrot.html

The points *inside* the cardioid are the points *within* the Mandlebrot set.
These are the coordinates on the imaginary plane corresponding to Z values
which fail to become greater than 2+0i after repeated iterations.



# Online fractal visualizers

You can compare your program's output with other Mandlebrot and Julia set
visualizers.

* https://atopon.org/mandel/
* https://sciencedemos.org.uk/mandelbrot.php (note: this program produces
  images which are upside down relative to our program)
* http://bl.ocks.org/syntagmatic/3736720
* http://usefuljs.net/fractals/



## Write a helper program to compare pictures

You can find ideas for new fractal configurations by exploring the Mandelbrot
and Julia sets online.  You will it helpful to write a small helper program
which converts these websites' `(minX, minY), (maxX, maxY)` coordinates into
our program's `(centerX, centerY) + axisLength` scheme.  This will also let
you compare your program's output with other working programs.




# Other fun links

* FractInt: A classic MS-DOS program (which is *still* under development!)
  whose users have made interesting discoveries within the Mandelbrot set and
  other related fractals over the years
    - [FractInt Homepage](https://www.fractint.org/)


* GNU XaoS: A free and open source fractal explorer for Linux, Windows and Mac
    - [GNU XaoS Homepage](http://matek.hu/xaos/doku.php)


* Eyecandy: Turn your computer into an expensive lava lamp.  Contains links to
  other programs you can use to explore fractals and other interesting
  patterns of pixels.
    - [Eyecandy Homepage](http://eyecandyarchive.com/)
