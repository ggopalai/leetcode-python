package main

func getSum(a int, b int) int {

	// recursively add the carry and the addition res
	for b != 0 {
		// simulating addition with bits - 1 ^ 0 = 1, 1 ^ 1 = 0, 0 ^ 0 = 0
		t := a ^ b

		// handle the carries
		b = (a & b) << 1

		a = t
	}
	return a
}
