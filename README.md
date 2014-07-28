# Sublime Assignment - An Assignment Plugin

[![Build Status](https://img.shields.io/travis/wbotelhos/sublime-assignment/master.svg)](https://travis-ci.org/wbotelhos/sublime-assignment "Travis CI")
[![Code Climate](https://codeclimate.com/github/wbotelhos/sublime-assignment.png)](https://codeclimate.com/github/wbotelhos/sublime-assignment "Code Climate")
[![Support Sublime Assignment](http://img.shields.io/gittip/wbotelhos.svg)](https://www.gittip.com/wbotelhos "Git Tip")

Sublime assignment is a plugin that changes your lines assignment to an inline style.

## Version

```
@version  0.1.0
@since    2012-01-12
@author   Washington Botelho
@doc      wbotelhos.com/sublime-assignment
```
## Dependencies

+ assignment.py
+ Default (YOUR_OS).sublime-keymap
+ Main.sublime-menu

## Installation

### Mac OSX

```bash
cd /Users/$USER/Library/Application Support/Sublime Text 2/Packages
git clone https://github.com/wbotelhos/sublime-assignment Assignment
```

### Linux

```bash
cd ~/.config/sublime-text-2/Packages
git clone https://github.com/wbotelhos/sublime-assignment Assignment
```

### Windows

```bash
cd %APPDATA%/Sublime Text 2/Packages
git clone https://github.com/wbotelhos/sublime-assignment Assignment
```

## Options

Copy the content of keymap here and append it to your *User/Default (YOUR_OS).sublime-keymap*.

```json
{ "keys": ["ctrl+shift+@"], "command": "assignment" }
```

## Usage

1) Select the lines you want to extract to an inline assignment:

```ruby
@article = article
@comment = comment
@user    = user
```

2) Press your shortcut keys or follow the menu *Tools > Assignment > Assign.

3) Result:

```ruby
@article, @comment, @user = article, comment, user
```

## Features

1) You don't need to select all lines, just one character of each line is enough:

```ruby
@article = ar(ticle
@comment = comment
@user    =) user
```

Will becames:

```ruby
(@article = article
@comment = comment
@user    = user)
```

2) If you select lines that is not an assignment, than it will be ignored:

```ruby
@article = article

puts 'Not an assign!'

@comment = comment
```

Result:

```ruby
@article, @comment = article, comment

puts 'Not an assign!'
```

Take care, if you have a logical assignment like:

```ruby
@article = article
@comment = Comment.new if @comment.nil?
```

It will be result in a bad assignment:

```ruby
@article, @comment = article, Comment.new if @comment.nil?
```

So, avoid to select things that is not a variable assignment.

3) If you have repeated assignment, it will generates a warning:

```ruby
@article = article
@comment = comment
@article = article
```

Result:

```ruby
# WARNING: duplicate assignments: {'article': '2 times'}
@article, @comment, @article = article, comment, article
```

## Licence

The MIT License

## Donate

You can do it via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=X8HEP2878NDEG&item_name=Sublime%20Assignment). Thanks! (:
