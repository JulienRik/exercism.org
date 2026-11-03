#!/usr/bin/env bash

# ${1:-you}	unset or empty
# ${1-you}	unset only (an empty value is kept)

#(Unrelated habit: name="$1" is conventional even though an assignment doesn't word-split. In most other contexts, unquoted $1 would.)

echo "One for ${1:-you}, one for me."
