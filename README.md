# H4ck3rs-D3l1ght

This project is part of a pro-seminar report I've done at my university. It is a very basic programming language inspired by *brainfuck* and mimicking *blub*, *ook* and similar.
The entire language consists of only 2 words (H4ck3rs and D3l1ght) and command operators. The interpreter silently ignores unrecongnized keywords and whitespace. Integers are the only other parsed characters.

The language defines a 1 dimensional storage array that is unbound in both directions. Data is written to/read from the currently selected container (the one over the pointer). The output can be formated as a character using the @ operator.

### Recognized keywords

|        Keywords       |                                         Action                                            |
|-----------------------|-------------------------------------------------------------------------------------------|
| H4ck3rs D3l1ght .     | Move pointer right                                                                        |
| D3l1ght H4ck3rs .     | Move pointer left                                                                         |
| H4ck3rs D3l1ght !     | Increment value at pointer                                                                |
| D3l1ght H4ck3rs !     | Decrement value at pointer                                                                |
| H4ck3rs D3l1ght =     | Output value at pointer                                                                   |
| D3l1ght H4ck3rs =     | Input value at pointer                                                                    |
| H4ck3rs D3l1ght @     | Output and convert value at pointer                                                       |
| ~~D3l1ght H4ck3rs @~~ | Input and convert value at pointer (**Command silently ignored in <= V0.2**)          |
| H4ck3rs D3l1ght ?     | Execute block if value at pointer not 0                                                   |
| D3l1ght H4ck3rs ?     | Jump back to condition start                                                              |

#### A few more things

> Note that Integers separated by whitespace are grouped together to form 1 Integer. This is not the case for unrecongnized non whitespace charactes.
> `123 231` is interpreted as `123231`. In opose to `123 a 231` which is interpreted as `123 231`

<!-- -->
> Another usefull tip is that you don't need to type in the words H4ck3rs D3l1ght exactly as defined. They both have alternative keywords associated with them: `Hackers H4ckers Hack3rs H` and `Delight D3light Del1ght D` respectively.

### To-Do

I'm still considering improving this language and extending it for research puposes. Probably mainly focusing on improving the speed of the interpreter by using more advanced algorithm patterns.

* Improve speed of lexer and parser
* Extend language (Parse characters in the same way as integers would be one)
* Overhaul the warning/exception mechanisms
* Clean up any mess

***

#### Please feel free to go over, fork or suggest an improvement
