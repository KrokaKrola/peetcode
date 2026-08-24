package main

import (
	"fmt"
	"math"
)

const MaxStrElements = 6

func conseal(s string) float64 {
	var res uint64 = 0x7FF8000000000000

	if len(s) >= MaxStrElements {
		s = s[:MaxStrElements]
	}

	for i := 0; i < len(s); i++ {
		res |= uint64(s[i]) << (i * 8)
	}

	return math.Float64frombits(res)
}

func reveal(n float64) string {
	consealedBits := math.Float64bits(n) & 0xFFFFFFFFFFFF
	res := []byte{}

	for consealedBits != 0 {
		ch := consealedBits & 0xFF
		res = append(res, byte(ch))
		consealedBits >>= 8
	}

	return string(res)
}

func main() {
	targets := []string{"😀", "hello!", "hi"}

	for _, target := range targets {
		res := conseal(target)

		revealed := reveal(res)

		if target != revealed {
			fmt.Println("target=", target, "revealed=", revealed)
			panic("target != revealed")
		}
	}
}
