/*
Trong một bể cá, có nhiều con cá A, B, C,... Mỗi con cá bắt đầu từ một vị trí ban đầu
và di chuyển với một vận tốc nhất định. Nếu vận tốc là số dương thì cá di chuyển về phía phải,

	nếu vận tốc là số âm thì cá di chuyển về phía trái.
	Khi hai con cá gặp nhau (tại cùng vị trí), con cá có vận tốc lớn hơn sẽ
	nuốt con cá có vận tốc nhỏ hơn. Nếu vận tốc bằng nhau, cả hai con cá đều bị loại bỏ.
*/

package main

import (
	"container/list"
	"fmt"
)

func survivingFish(fishList []Fish) []Fish {
	leftQueue := list.New()
	rightQueue := list.New()

	for _, fish := range fishList {
		if fish.Velocity > 0 {
			rightQueue.PushBack(fish)
		} else {
			for rightQueue.Len() > 0 && rightQueue.Back().Value.(Fish).Velocity < abs(fish.Velocity) {
				rightQueue.Remove(rightQueue.Back())
			}
			if rightQueue.Len() > 0 && rightQueue.Back().Value.(Fish).Velocity == abs(fish.Velocity) {
				rightQueue.Remove(rightQueue.Back())
			} else if rightQueue.Len() == 0 {
				leftQueue.PushBack(fish)
			}
		}
	}

	survivors := []Fish{}
	for e := leftQueue.Front(); e != nil; e = e.Next() {
		survivors = append(survivors, e.Value.(Fish))
	}
	for e := rightQueue.Front(); e != nil; e = e.Next() {
		survivors = append(survivors, e.Value.(Fish))
	}

	return survivors
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func testSurvivingFish() {
	fishList := []Fish{{0, 2}, {3, -1}, {5, 4}, {6, -2}}
	result := survivingFish(fishList)
	fmt.Println("Surviving fish:")
	for _, fish := range result {
		fmt.Printf("Position: %d, Velocity: %d\n", fish.Position, fish.Velocity)
	}
}
