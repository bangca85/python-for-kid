/*
Trong một bể cá, có nhiều con cá A, B, C,... Mỗi con cá bắt đầu từ một vị trí ban đầu
và di chuyển với một vận tốc nhất định. Nếu vận tốc là số dương thì cá di chuyển về phía phải,

	nếu vận tốc là số âm thì cá di chuyển về phía trái.
	Khi hai con cá gặp nhau (tại cùng vị trí), con cá có vận tốc lớn hơn sẽ
	nuốt con cá có vận tốc nhỏ hơn. Nếu vận tốc bằng nhau, cả hai con cá đều bị loại bỏ.
*/
package problems

import (
	"fmt"
	"math"
)

type Fish struct {
	Position int
	Velocity int
}

func survivingFish2(fishList []Fish) []Fish {
	stack := []Fish{}

	for _, fish := range fishList {
		alive := true
		for alive && fish.Velocity < 0 && len(stack) > 0 && stack[len(stack)-1].Velocity > 0 {
			topFish := stack[len(stack)-1]
			if int(math.Abs(float64(topFish.Velocity))) > int(math.Abs(float64(fish.Velocity))) {
				alive = false
			} else if int(math.Abs(float64(topFish.Velocity))) < int(math.Abs(float64(fish.Velocity))) {
				stack = stack[:len(stack)-1]
			} else {
				stack = stack[:len(stack)-1]
				alive = false
			}
		}
		if alive {
			stack = append(stack, fish)
		}
	}
	return stack
}

func survivingFishLeftToRight(fishList []Fish) []Fish {
	survivors := []Fish{}

	for _, fish := range fishList {
		for len(survivors) > 0 && fish.Velocity < 0 && survivors[len(survivors)-1].Velocity > 0 {
			topFish := survivors[len(survivors)-1]
			if int(math.Abs(float64(topFish.Velocity))) > int(math.Abs(float64(fish.Velocity))) {
				fish = Fish{} // Fish is eliminated
				break
			} else if int(math.Abs(float64(topFish.Velocity))) < int(math.Abs(float64(fish.Velocity))) {
				survivors = survivors[:len(survivors)-1] // Eliminate the top fish
			} else {
				survivors = survivors[:len(survivors)-1] // Both fish are eliminated
				fish = Fish{}
				break
			}
		}
		if (Fish{} != fish) {
			survivors = append(survivors, fish)
		}
	}
	return survivors
}

func testSurvivingFish2() {
	fishList := []Fish{{0, 2}, {3, -1}, {5, 4}, {6, -2}}
	result := survivingFish2(fishList)
	fmt.Println("Surviving fish:")
	for _, fish := range result {
		fmt.Printf("Position: %d, Velocity: %d\n", fish.Position, fish.Velocity)
	}
}
