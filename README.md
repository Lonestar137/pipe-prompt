# About

pipe-prompt is a CLI tool that spawns and interactive menu from std input.  This means you can pass the contents of a file or a command into this utility and parse the output interactively.  Additionally, you can place delimited fields to change the behavior 
of the menu.  For exampl, you can add `@#cmd: ls -la {row_data} #@` to any line of standard input to run the `ls -la` command and all other text on that line will be passed as an argument to the command.

## Requirements

- Python Version >= 3.5

## How to

1. To use pipe-prompt simply use the pipe character '|' after a command which outputs standard text, i.e.  cat somefile.txt or echo "hello world" | pipe-prompt.  
2. To enable vim keybinds: `-v` or `--vim`

## Known issues

## Philosophy

1. Make your application do one thing and do it well: Write your application to perform a specific task, and make sure it does that task well. Avoid adding unnecessary features that would make the application more complex.

2. Use simple, plain-text input and output: Use plain-text input and output for your application, rather than a proprietary format. This allows other programs and scripts to easily interact with your application, and it also makes it easy for users to read and modify the data.

3. Use command-line arguments for input and configuration: Use command-line arguments for input and configuration, rather than prompting the user for input or using a configuration file. This allows users to easily automate and script their use of your application.

4. Make the application easy to test: Write your application in a way that makes it easy to test. For example, use dependency injection to make it easy to replace components with mock objects, and make sure your code is well-factored and modular so that individual components can be tested in isolation.

5. Make the application easy to extend: Write your application in a way that makes it easy for other developers to extend and customize it. For example, use a plugin architecture or make it easy to subclass key components.

6. Follow the best practices for writing maintainable code, such as using version control, automated testing, and documentation.  
