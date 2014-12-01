# standard libraries
pass
# third party libraries
pass
# first party libraries
pass

class DoteDict(dict):
    """ An autovivificious dictionary with attribute access to keys.  Makes a nice structure for trees.

        There are a plethora of dictionary replacements that allow attribute access, and since the addition of the 
        collections module, it's been possible to get an autovivicious dictionary with a one liner using defaultdict.  

        This class subclasses the vanilla Python dict class.  It allows attribute access to dict keys that are valid
        attribute names.  Traditional key-based lookup still works as expected.  The class is designed to be a drop-in
        replacement for dict.  Currently, all dict methods are supported using traditional key-lookup.  Some dict methods
        act wonky with attribute access (notably __del__).  The update method, however, does work as expected.

        You don't need this, but you want it.

        >>> DoteDict({'a': 1, 'b': 2})
        {'a': 1, 'b': 2}
        >>> d = DoteDict()
        >>> d.a.b = 1
        >>> d
        {'a': {'b': 1}}
        >>> d.a
        {'b': 1}
        >>> d.a.b
        1
        >>> d['a']['b']
        1

        >>> d = DoteDict({'a': {'b': {'c': 1}}})
        >>> d.a
        {'b': {'c': 1}}
        >>> d.a.b.c
        1
        >>> d.a.b.c = 3
        >>> d
        {'a': {'b': {'c': 3}}}
        >>> d.a = 1
        >>> d
        {'a': 1}
        
        >>> d = DoteDict()
        >>> d._3 = 'c'
        >>> print d
        {'_3': 'c'}

        >>> d = DoteDict({'c': 3})
        >>> d.update({'a': {'b': {'c': 2}}})
        >>> d
        {'a': {'b': {'c': 2}}, 'c': 3}
        >>> d.a.b.c
        2

        >>> e = DoteDict({'b': 2, 'c': 3})
        >>> d = {'a': 1, 'e': e}
        >>> e['b'] = None
        >>> d
        {'a': 1, 'e': {'c': 3, 'b': None}}

    """
    
    def __init__(self, *args, **kwargs):
        super(TreeDict, self).__init__(*args, **kwargs)
        self.__treeify(self)

    def __treeify(self, obj):
        t = type(obj)
        if issubclass(t, dict):
            if not issubclass(t, TreeDict):
                obj = TreeDict(obj)
            else:
                for k, v in obj.iteritems():
                    obj[k] = self.__treeify(v)
        elif issubclass(t, (list, tuple)):
            obj = list(obj)
            for i in xrange(len(obj)):
                obj[i] = self.__treeify(obj[i])
            obj = t(obj)
        return obj

    def __missing__(self, key):
        self[key] = TreeDict()
        return self[key]

    def __getattr__(self, attribute):
        return self[attribute]

    def __setattr__(self, attribute, value):
        self[attribute] = self.__treeify(value)

    def update(self, other):
        other = TreeDict(other)
        super(TreeDict, self).update(other)

if __name__ == '__main__':
    import doctest
    doctest.testmod()