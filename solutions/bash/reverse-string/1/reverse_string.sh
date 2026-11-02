#!/usr/bin/env bash

length="$1" # $@ would take arguments >1
result=""

main() {
  for ((i = ${#length} - 1; i >= 0; i--)); do
    # Bash's substring expansion: ${var:offset:length}
    result+="${length:i:1}"
  done
  echo "$result"
}

main "$@"
