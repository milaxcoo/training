package main


func main() {
	FordFuckus := Car{
		Color: "red",
		Age: 10,
		Sale: false,
	}
	_ = FordFuckus // to fix "car declared and not used" error

	ToyotaCorowa := Car{
		Color: "blue",
		Age: 5,
		Sale: true,
	}
	_ = ToyotaCorowa // to fix "car declared and not used" error

	FordFuckus.isSale()
	ToyotaCorowa.isSale()


}

type Car struct {
	Color string
	Age int
	Users int
	Sale bool
}

func (car Car) isSale() string {
	if car.Sale && car.Users < 5 {
		fmt.Println("LETS GOOO")
	} else {
		fmt.Println("NAH EWWW")
	}

	return ""
}