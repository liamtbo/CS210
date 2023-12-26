  >>> search('ALPHA', ['ALPHA', 'BETA', 'GAMMA']) == MATCH
  True

  >>> search('BE', ['ALPHA', 'BETA', 'GAMMA']) == PREFIX
  True

  >>> search("FOX", ['ALPHA', 'BETA', 'GAMMA']) == NOPE
  True

  >>> search("ZZZZ", ['ALPHA', 'BETA', 'GAMMA']) == NOPE
  True