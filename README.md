ckanext patcategories
=====================

How to use
==========

I comandi che possono essere usati per creare e cancellare nuove voci
dei vocabolari presenti; i comandi vanno lanciati dalla cartella del
plugin "ckanext-patform",

start from the directory ckanext-patform 
(eg. 
```bash
cd /where/is/ckan/ckanext-patform )
```

to add a term in the vocabulary
```bash
paster pat add-term <vocab_name> <new_term> -c <path to config file>
```
to remove a term from the vocabulary
```bash
paster pat remove-term <vocab_name> <term_to_remove> -c <path to config file>
```

Example
=======
```
paster pat add-term category_vocab Mobilita -c /etc/ckan.ini
````

The terms cad be added to this different vocabularies:
- category_vocab (Categories)
- holders_vocab (Holders)
- coverage_vocab (Geographical coverage)

