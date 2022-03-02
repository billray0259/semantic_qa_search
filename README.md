# Usage Guide

* Give this project a star

## Ask me for the embeddings so you don't have to run the model yourself

## If you want to run the OpenAI model yourself (and pay for it)
* get an OpenAI API key
* make a folder in this directory called data
  * make a subfolder called cs514
  * make a text file called urls.txt in data/cs514
    * paste this into the text file:
```
https://people.cs.umass.edu/~mcgregor/514S22/lecture1.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture2.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture3.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture4.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture5.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture6.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture7.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture8.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture9.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture10.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture11.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture12.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture13.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture14.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture15.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture16.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture17.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture18.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture19.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture20.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture21.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture22.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture23.pdf
https://people.cs.umass.edu/~mcgregor/514S22/lecture24.pdf
```
* pip install requirements.txt
* run pdf_to_text.ipynb to download the PDFs and extract the text from the PDF documents
* run document_encoder.ipynb ONCE (it costs money) to encode the documents and save the embeddings

## Now that you have the embeddings
* open search_engine.ipynb and modify the last cell
* set query = "some question you want to search the slides for"

## Things to know
* Getting the document embeddings with ada costs about $0.45, getting them with curie costs about $3.50, and davincie costs about $35
* Getting the query embeddings costs much less. So much less I'm not even sure how much it costs.