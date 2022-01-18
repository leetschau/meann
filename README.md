# Manager of Ebook Annotations

`meann` saves/loads your ebook annotations into/from plain-text json file,
therefore you can manage your ebook annotations in version control system.

## Book Repo Structure

* books.json
* one or more anno-<abbr>.json, each records annotations in one book/article

Attributes of each item (book) in books.json:

* ISBN
* type: book/article
* homepage: URL string of the official webpage of the book/article
* ofn: origin file name of the file, such as: `Streaming systems-Tyler Akidau(2018).pdf`
* abbr: abbreviations of the book/article, such as `SICP` for
  "Structure and Interpretation of Computer Programs", etc
* md5: md5 string of the "original" ebook file, such as `Streaming systems-Tyler Akidau(2018).pdf`.

## Usage

```
pipx install reav
git clone <your-ebbok-annotation-repo>
cd <your-ebbok-annotation-repo>
reav save ...
git commit ...
git push
```

## API

* Load annotations: `load anno-<abbr>.json <ofn>.pdf [<abbr>-MMdd.pdf]`, 
  parse annotations in `anno-<abbr>.json` and merge them into `<ofn>.pdf`,
  write the "annotated" pdf into a new PDF file. When the last argument is not specified,
  the file name is `<abbr>-MMdd.pdf`, where `MMdd` is the current month and day;
* Save annotations: `save <abbr>-MMdd.pdf [anno-<abbr>.json]`,
  export annotations from `<abbr>-MMdd.pdf` to a JSON file, the default value is
  `anno-<abbr>.json` when not specified.

