#!/bin/bash

file=".github/styles/config/vocabularies/Base/accept.txt"
{ grep '^[[:upper:]]' $file | sort -u; \
  grep '^\['          $file | sort -u; \
  grep '^[[:lower:]]' $file | sort -u; } > tmp && mv tmp $file
