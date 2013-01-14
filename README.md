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

Change the shortcut:

```json
"keys": ["ctrl+shift+@"]
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

## Contributors

None

## Licence

The MIT License

Copyright (c) 2012 Washington Botelho

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Donate

You can do it via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=X8HEP2878NDEG&item_name=Sublime%20Assignment). Thanks! (:

