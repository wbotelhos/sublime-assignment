# Sublime Assignment - An Assignment Plugin

Sublime assignment is a plugin that changes your lines assignment to an inline style.

## Version

```
@version        0.1.0
@since          2012-01-12
@author         Washington Botelho
@twitter        twitter.com/wbotelhos
```

## Required Files

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
cd %APPDATA%/Sublime Text 2/Packages/
git clone https://github.com/wbotelhos/sublime-assignment Assignment
```

Copy the content of keymap here and append it to your *User/Default (YOUR_OS).sublime-keymap*.

## Options

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

2) Press your shortcut keys or follow the menu *Edit > Assignment.

3) Result:

```ruby
@article, @comment, @user = article, comment, user
```
# Features

1) You don't need to select all line, just one character of a line you select it all:

```ruby
@article = ar(ticle
@comment = comment
@user    =) user
```

Will select:

```ruby
(@article = article
@comment = comment
@user    = user)
```

2) If you select lines that is not an assignment, than it will be ignored:

```ruby
@article = article

if @comment.nil?
  puts 'Comment is nil!'
end

@comment = comment
```

Result:

```ruby
@article, @comment = article, comment

if @comment.nil?
  puts 'Comment is nil!'
end
```

Take care, if you have a logical assignment like:

```ruby
@article = article
@comment = Comment.new if @comment.nil?
```

It will be result a bad assignment:

```ruby
@article, @comment = article, Comment.new if @comment.nil?
```

Then, avoid to select things that is not a variable assignment.

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
