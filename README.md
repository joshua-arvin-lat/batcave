cave
====

The CAVE is part of the Busy Administrator's Toolbox. It allows tagging of files and folders to help organize and search files effectively.

Busy Administrator's Toolbox ~ Central Authorized Variable Environment
* linux and unix tagging for files and folders
* tag files and folders using symlinks
* support for nested tags
* list objects with specified tag
* list tags of target object
* search tagged files and folders recursively
* tag autocompletion
* colored output
* add cave location to path then enter the batcave to get started

### Usage

~~~
  # add cave location to path (edit bash profile)
  $ batcave location

  # enter environment
  $ `batcave enter`
  [batcave] $ # use tools, tag -h
  
  # create tag named favorites and reset tag autocompletion
  [batcave] $ `tag create -t favorites`
  [batcave] $ tag add -o awesomefile -t <tab to autocomplete>
  
  # exit environment
  [batcave] $ `batcave exit`
  
  $ # back to normal
~~~

### Create Tags
~~~
  `tag create -t tag1`
  `tag create -t tag2/subtag`
  `tag create -t tag1 tag2 tag2/subtag`
~~~

### Adding tags to files and folders
~~~
  tag add -o file1 -t tag1
  tag add -o file1 file2 -t tag1
  tag add -o file1 folder1 -t tag1
  tag add -o folder1 -t tag1
  tag add -o file1 -t tag1 tag2
  tag add -o file1 file2 -t tag2/subtag
~~~

### Removings tags from files and folders
~~~
  tag remove -o file1 -t tag1
  tag remove -o file1 file2 -t tag1
  tag remove -o file1 folder1 -t tag1
  tag remove -o folder1 -t tag1
  tag remove -o file1 -t tag1 tag2
  tag remove -o file1 file2 -t tag2/subtag
~~~

### Listing tags
~~~
  tag list
  tag list -f tag1
  tag list -f tag1 --no-cache
  tag list --detailed | grep -v '0  '
  tag list --detailed -f tag8
  tag list --detailed -f tag1/tag1c --exact --paths-only
~~~

### Listing objects and tags
~~~
  tag list-objects -f tag1/tag1b
  tag list-objects -f tag3 --recursive
  tag list-tags -o object1
  cd `tag list-objects -f scripts | grep '.sh' | dir`
~~~

### Moving tags and objects
~~~
  tag move -t tag2 tag1/tag2
  tag move-object -o loc1 loc2
  tag move-object -o file1 dir1/file2
~~~

### Searching
~~~
  search "query"
  search "query" -t tag1
  search "query" -t tag1/tag2
~~~