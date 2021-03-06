# Python Avatar Generator
I needed an avatar for my github profile but instead of taking a picture of my face - like a normal person - I built this. It takes an arbitrary string eg. my name - which was used for my current github avatar - and generates an image.

## Getting Started
How to download and use the project to start generating images.

### Prerequisites
Python 3 and a working installation of the *pillow* module. Note: I've only tested this project on MacOS but I can't see why it wouldn't work exactly the same on Windows/ Linux.

### Installation / Usage
To use simply download *app.py* and run from the command line like this:
```
$ python3 app.py <string> <output file> 
```
Note: app.py must be in the same directory as map.json

### Example
The following is an example of what an avatar may look like:
<br />
<img src="sample.png" alt="Example Avatar" width="200px" height="200px">
<br />
It was generated with the string "sample" using the following command:
```
$ python3 app.py sample sample.png
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
