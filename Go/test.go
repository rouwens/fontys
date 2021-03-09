package main

import (
	"fmt"
)

func main() {
	fmt.Println("Vul een getal in dat groter is dan 10")
	var test string
	fmt.Scanln(&test)

	var getal = 10

	if test >= getal {
		fmt.Println("Dit klopt")
	} else {
		fmt.Println("Dit klopt niet")
	}
}
