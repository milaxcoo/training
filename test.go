
	package main

	import (
		"errors"
		"fmt"
		"math/rand"
		"slices"
	)

	//func main() {
		countCows := rand.Intn(100)
		ending, err := getEnd(countCows)
		if err != nil {
			fmt.Println(err)
			return
		}
		//using getEnd function
		fmt.Printf("У нас %d коров%s", countCows, ending)
	}

	func getEnd(countCows int) (string, error) {
		
		sliceBetweenTwoFour := []int{2, 3, 4}

		switch {
		case slices.Index(sliceBetweenTwoFour, countCows%10) != -1 && (countCows >= 11 || countCows <= 20):
			return "ы", nil
		case countCows%10 == 1 && countCows != 11:
			return "а", nil
		default:
			return "", errors.New("invalid countCows value")
		}
	}

	var err1 = errors.New("Russian language detected...")
	var err2 = errors.New("Number of cows is not found")
	var err3 = errors.New("They are not cows")
	var err4 = errors.New("They are bulls")
	var err5 = errors.New("Error is not found")
	

	
	