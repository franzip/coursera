# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct.get(key, set()) for key in keylist]

def list2dict(L, keylist): return {key:val for (key, val) in zip(keylist, L)}

def listrange2dict(L): return list2dict(L, range(len(L)))
