# ForestFireSimulator
This is a small project to develop my skills with python. This program takes in a density of the forest and a chance that the fire will
catch and spread and uses this information to simulate a forest fire. This program comes with a console-based display, but a GUI-based application could be developed or this could be used as a without a display and as a back-end to collect data.

Block.java is the most basic element in this program. The Block is just an empty space in the forest.

Tree.java is a tree to be held in the forest. A Tree has three states: unchanged, on fire, and destroyed. The toString method returns a 
string representation of the current state of the tree.

Forest.java holds a two dimensional array of Blocks and Trees. Forest objects have the ability to create a new forest, ignite a random or
a specific tree, and spread the fire to all viable trees through updateFire, or change the forest through one event through incrementFire
(such as igniting or destroying a tree).

FireSimulator.java holds the forest object and simulates the forest fire. It takes in a display method to display the forest, as well as
methods to get the density and ignition chance from the user. A FireSimulator then uses these methods to simulate the forest fire and 
returns the percentage of trees burned.

ConsoleSimulator.java implements the FireSimulator. It defines a text-based display method, a method to get the density of the forest,
and a method to get the ignition chance from the user. The ConsoleSimulator then allows the user to simulate different forest fires as
many times as they desire.
