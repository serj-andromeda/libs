#! /usr/bin/env gorun
package main

import "fmt"



func main() {
	fg := make (map[string]string)
	bg := make (map[string]string)
	fg["BrightGreen"] = "\033[92m"
	bg["BrightWhite"] = "\033[107m"
	fmt.Println(
	fg["BrightGreen"]+
	bg["BrightWhite"]+
	"Green text on white background in golang version still without module itself"+
	"\033[0m")
}