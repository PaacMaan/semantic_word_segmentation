# French word segmentation

Usually when extracting text from open source OCRs like Tesseract, we're most likely to encounter linked words duo to OCR quality extraction. 

For example :
instead of extracting **"Très bon service"**, one might get sudenlly **"Très bonservice"**. So when doing feature engineering with BOW, TFIDF or even word2vec models, the algorithm will consider that **"bonservice"** as a unique feature, while it is not.

To deal with this problem, I built a module dealing with semantic word segmentation without any predefined corpus.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install frwordsegment.

```bash
pip install foobar
```

## Usage

```python
from wordseg import segment_token

# suppose that a french spellchecker detect this token as misspelled
token = "soitmoinscompliqué"

# apply segmentation function on the given token
result = segment_token(token)

# show results
print("raw token is {}".format(token)) # "soitmoinscompliqué"
print("processed token is {}".format(result)) # "soit moins compliqué"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)