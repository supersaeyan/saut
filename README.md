# saut
Search As You Type

A small Django project with fuzzy search / autocomplete search implementation such that:
  1. Substring match can occur anywhere in the strings
  2. a) Matches found closer to the beginning are ranked higher
     b) Matches that are more frequently used words, are ranked higher
     c) Matches that are shorter in length, rank higher, i.e exact matches rank #1
