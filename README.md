# :book: capbib: Bibliography Transformations made easier

Transform BibTeX bibliographic references to match your journal discipline.
For example, many journals require noun capitalization in titles and curly brackets in proper nouns.
capbib uses Natural Language Processing to solve this issue.
It facilitates spaCy's POS (Part-Of-Speech) tagger to apply the transformations.

The available POS tags are described [here](https://spacy.io/usage/linguistic-features).

## Installation

```
pip3 install -r requirements.txt
python3 -m spacy download en_core_web_sm # Can be extended to other languages as well
python3 setup.py install
```

## Example

Suppose that you need title capitalization and curly brackets in proper nouns.

```bash
<myref.bib capbib.py --pos NOUN -c T --field title |
capbib.py --pos PROPN --field title -c C >myref_capbib.bib
```

Note that in the `-c` argument you can pile more commands.
For example `-c UC` converts to uppercase and adds curly braces.  

## Usage

To see what is available type in
```
capbib.py -h
```
