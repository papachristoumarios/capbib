# :book: capbib: Bibliography Transformations made easier with NLP

Transform BibTeX bibliographic references to match your journal discipline.
For example, many journals require noun capitalization in titles and curly brackets in proper nouns.
capbib uses Natural Language Processing to solve this issue.
It facilitates spaCy's POS (Part-Of-Speech) tagger to apply the transformations.

The available POS tags are described [here](https://spacy.io/usage/linguistic-features).



## Installation

```bash
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

Consider this bibliographical reference:

```
@book{kernighan2006c,
  title={The C programming language},
  author={Kernighan, Brian W and Ritchie, Dennis M},
  year={2006}
}
```

After the above preprocessing, the result becomes

```
@book{kernighan2006c,
  title={The {C} Programming Language},
  author={Kernighan, Brian W and Ritchie, Dennis M},
  year={2006}
}
```

Note that in the `-c` argument you can pile more commands. In `-c UC` capbib converts the tokens to uppercase and adds curly braces.  



## Usage

To see what is available type in
```
capbib.py -h
```

To show the list of available options:

```bash
usage: capbib.py [-h] [--pos POS] [--field FIELD] [-c C] [--model MODEL]

optional arguments:
  -h, --help     show this help message and exit
  --pos POS      Part of speech to mutate (e.g. NOUN)
  --field FIELD  Field to mutate (e.g. title)
  -c C           Command to mutate U : To uppercase, L : To lowercase, T : To
                 title, C : Add curly brackets, P : Add parentheses, S : Add
                 square brackets
  --model MODEL  Model to use (e.g. en_core_web_sm)
```

You can define multiple conversion schemes and include them in bash scripts or Makefiles for additional flexibility.
