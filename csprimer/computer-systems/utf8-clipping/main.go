package main

import (
	"errors"
	"fmt"
	"strings"
)

func truncate(s string, limit int) (string, error) {
	if len(s) <= limit {
		return s, nil
	}

	cut := limit

	for cut > 0 && limit-cut != 4 {
		ch := s[cut]
		t := ch & 0xC0

		// start of the sequence
		if t != 0x80 {
			break
		}

		cut--
	}

	if s[cut] == 0x80 || limit-cut == 4 {
		return "", errors.New("malfored utf-8 input")
	}

	return s[:cut], nil
}

func main() {
	// target := strings.Repeat("0", 300)
	// target := "cafe\u0301"
	// target := "\U0001F1Fa\U0001F1E6"
	target := strings.Repeat("a", 240) +
		"\U0001F468\u200d\U0001F469\u200d\U0001F467\u200d\U0001F466"

	res, err := truncate(target, 255)
	if err != nil {
		fmt.Println(err.Error())
	} else {
		fmt.Printf("in len = %d\nout len = %d\ntruncated str = %q\n", len(target), len(res), res)
	}
}
