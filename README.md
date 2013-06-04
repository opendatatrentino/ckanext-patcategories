ckanext patcategories
=====================

How to use
==========

I comandi che possono essere usati per creare e cancellare nuove voci
dei vocabolari presenti; i comandi vanno lanciati dalla cartella del
plugin "ckanext-patform",

start from the directory ckanext-patform (eg. cd /where/is/ckan/ckanext-patform )

to add a term in the vocabulary
paster pat add-term <vocab_name> <new_term> -c <path to config file>

to remove a term from the vocabulary
paster pat remove-term <vocab_name> <term_to_remove> -c <path to config
file>


Example
=======

paster pat add-term category_vocab Mobilita -c
/etc/ckan.ini

I vocabolari ai quali si possono aggiungere termini sono:
category_vocab (Categories)
holders_vocab (Holders)
coverage_vocab (Geographical coverage)

