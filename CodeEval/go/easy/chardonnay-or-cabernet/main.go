// Code Eval- Chardonnay or cabernet 
// https://www.codeeval.com/open_challenges/211/submit package main
package main
import(
    "fmt"
    "log"
    "bufio"
    "os"
    "strings"
)
func main() {
    file, err := os.Open(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        test := strings.Split(scanner.Text(), " | ")
	wines := strings.Split(test[0], " ")
	keyword := test[1]
	solution := ""
	for _, wine := range wines {
	    for index, letter := range keyword{
		if strings.Count(keyword, string(rune(letter))) > 1{
		    if strings.Count(wine, string(rune(letter))) < strings.Count(keyword, string(rune(letter))){break}
		}
		if !strings.ContainsRune(wine, letter){break}
		if len(keyword)-1 == index{
		    solution = solution + wine + " "
		}
	    }
	}
	if solution == ""{solution = "False"}
	fmt.Println(solution)
    }
}
