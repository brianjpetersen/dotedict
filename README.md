dotedict
========

An autovivificious dictionary with attribute access to keys.  Makes a nice structure for trees.

There are a plethora of dictionary replacements that allow attribute access, and since the addition of the 
collections module, it's been possible to get an autovivicious dictionary with a one liner using defaultdict.  

This class subclasses the vanilla Python dict class.  It allows attribute access to dict keys that are valid
attribute names.  Traditional key-based lookup still works as expected.  The class is designed to be a drop-in
replacement for dict.  Currently, all dict methods are supported using traditional key-lookup.  Some dict methods
act wonky with attribute access (notably __del__).  The update method, however, does work as expected.

You don't need this, but you want it.

