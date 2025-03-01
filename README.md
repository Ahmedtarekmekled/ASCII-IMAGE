# 🖼️ Image Processing Toolkit

A collection of Python utilities for image processing and ASCII art generation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

## 📋 Overview

This toolkit provides powerful yet simple tools for image processing:

- **Image Converter** (`process.py`): Batch converts images to grayscale JPG format
- **ASCII Art Generator** (`generate_ascii.py`): Transforms images into ASCII art with customizable parameters

## ✨ Example

Here's an example of the ASCII art transformation:

<table>
  <tr>
    <td><b>Original Image</b></td>
    <td><b>ASCII Art Output</b></td>
  </tr>
  <tr>
    <td>
      <img src="example/sample.jpg" width="400" alt="Sample original image">
    </td>
    <td>
      <pre>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>i>iI:::::::::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>!!:,:::::::::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>;:::::::::::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>;:::::::::::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ii>>>>>>!I:::::::::::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>i!ii<>i>ii~)+i~ii>i!,:::::::::::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>i+x|~vXuU}!vwYjQ}~u}i>;,,,:::::::::::::::::::
>>>>>>>>>>>>>>>>>>>>i!i!{JXpqQZwwqZtZmZqmCYQL0Q){j_,,,,:::::::::::::::
>>>>>>>>>>>>>>>>>>i>1f)_[wppwOqpZwqqppZZOOOZddwqZOxI:i<,,:::::::::::::
>>>>>>>>>>>>>>>>><{jUddOYLmpk0wbZZpqbhmpqmwdbqpqQn|xYz(-~:,:::::::::::
>>>>>>>>>>>>>>>>>zdhqwwwwmOZbwphpdqphbdhkkbkdkdmOOppZQOOu?;,::::::::::
>>>>>>>>>>>>>>>i<[cwdddqmmwqbqqbbqdbhhaao**hahkdkhhkkkqUf}>;::::::::::
>>>>>>>>>>>>>>~1fzQOO0OmqdbbdbpZqkkkhaoo*MM#*ahhhhhhhkpZQCri,:::::::::
>>>>>>>>>>>>>><[\c0wwqqqqdkkdpmkoohh*M&#aoMWM#oahhhhhhkqUj{+;,::::::::
>>>>>>>>>>>>>>+tzOqOLJUJQwkkhpq*#ak8@BBB*oaMM#*ohhhkkdqwwQu(!,::::::::
>>>>>>>>>>>>>>>i?cqbdqZQLCObohddh#ooW8WMohoW#ooaahhkkbdqwZYf<,::::::::
>>>>>>>>>>>>>>>>~)tLOJJQ0QQQOphbdhooaoao*oM#*oaaahhhhhhhhd0/;:::::::::
>>>>>>>>>>>>>>>>>ii[fYZqZOOQZqhhbakhkaao*aaaahhhhhhhaaaabZX[::::::::::
>>>>>>>>>>>>>>>>>i-nzCJYzcrcqpZOZddbo*hbhhhkkkbbpddq00mwOx<;::::::::::
>>>>>>>>>>>>>>>>>>>ii>~~<itqqZ0OqZOmkkbkpbdwwqpbabqZUf-II;:,::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>xYU\uadwwwkbwhpmdpmO0xr0ddpLz+,,::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>i>>!_wdhqCZbqbdqwbbq0Yii+{t1il::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>!rQtwr]u\CXj\)zLwC~iiiI,::::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><)>zv<!!<~!iii>[}i>>>i!:,::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ii\Y]i>>i>>>>>ii>>>>>>iI:,::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>>>iiiiii~Xt>ii>>>>>>>>>>>>>>>>i;:;::::::::::
>>>>>>>>>>>>>>>>>>>>>>>iii><_----])UY}?]_>>>>>>>>>>>>>>>>>i>l:,:::::::
>>>>>>>>>>>>>>>>>>iii>~-[{))){}[}}/qO/((?>>>>>>>>>>>>>>>>>>>>iI,::,:::
>>>>>>>>>>>>>>>>i~?}(\\|(1[?-[)()1)rn(->>>>>>>>>>>>>>>>>>>>>>>iiiil;,:
>>>>>>>>>>>>>>i~fcvnr/1]?]fxXQQJvxt)}][?>>>>>>>>>>>>>>>>>>>>>>>>i!!iI!
>>>>>>>>>>>>i>_rCLXcrt1??jLLCJJXnt()[)\{<>>>>>>>>>>>>>>>>>>>>>>>iii>>>
>>>>>>>>>>>~1rzUCCXcnj\1]|){)tff(}?(f}_>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>itLLCCCCUcvrf())(|\|({?-tZr}~>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>i?ULCCCCUzcujf|((){}[]?_CC+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>ifLCCCCCXcvjf((()]????xw1i>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>i(LCCCCLYcnjf((({???-|kxi>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>i{LCLCCUYcxjt(()]???-LU<i>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
+<<>>>>>>>>i]JLUzzzurf\(){}???-fZ?i>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
]??_~~>>>>>i?XXccvxf\()1}????-/m1i>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
???]]?_+<>>i[cvuxf|(){[??????\dti>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      </pre>
    </td>
  </tr>
</table>

## 🚀 Features

- **Image Converter:**
  - Batch processing of multiple images
  - Automatic grayscale conversion
  - Format standardization to JPG
  - Error handling with detailed reporting

- **ASCII Art Generator:**
  - Adjustable width and height
  - Two grayscale character sets (70 or 10 levels)
  - Aspect ratio preservation option
  - Custom output file naming
  - Intelligent brightness mapping

## 📦 Installation

### Prerequisites

- Python 3.6+
- Pillow (PIL Fork)
- NumPy

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Ahmedtarekmekled/ASCII-IMAGE.git
cd ASCII-IMAGE
```

2. Install required packages:
```bash
pip install pillow numpy
```

3. Create required directories:
```bash
mkdir img converted
```

## 💻 Usage

### Image Converter

Convert all images in the `img` folder to grayscale JPG:

```bash
python process.py
```

### ASCII Art Generator

Transform an image into ASCII art with various options:

```bash
python generate_ascii.py [image_path] [options]
```

#### Options:

| Option | Description | Default |
|--------|-------------|---------|
| `-w, --width` | Width of ASCII output | 200 |
| `-he, --height` | Height of ASCII output | 100 |
| `-s, --scale` | Grayscale scale (70 or 10 characters) | 70 |
| `-a, --aspect` | Maintain aspect ratio | False |
| `-o, --output` | Custom output filename | input_name.txt |

#### Examples:

```bash
# Basic usage
python generate_ascii.py img/photo.jpg

# Custom dimensions
python generate_ascii.py img/photo.jpg -w 100 -he 50

# Simple character set
python generate_ascii.py img/photo.jpg -s 10

# Preserve aspect ratio
python generate_ascii.py img/photo.jpg -a

# Custom output file
python generate_ascii.py img/photo.jpg -o my_ascii_art.txt
```

## 🖥️ How It Works

### Image Converter

The converter processes each image through these steps:
1. Opens the original image
2. Converts to grayscale (L mode)
3. Saves as JPG in the output directory
4. Handles errors gracefully with detailed reporting

### ASCII Art Generator

The ASCII generator follows this process:
1. Loads and resizes the input image
2. Maps each pixel's brightness to a corresponding ASCII character
3. Builds the ASCII representation line by line
4. Outputs to console or saves to a text file

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📬 Contact

Ahmed Tarek Mekled - [@GitHub](https://github.com/Ahmedtarekmekled)

Project Link: [https://github.com/Ahmedtarekmekled/ASCII-IMAGE](https://github.com/Ahmedtarekmekled/ASCII-IMAGE)
