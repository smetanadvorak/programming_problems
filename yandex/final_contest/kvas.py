with open('input.txt', 'r') as f:
	b, c = map(int, f.readline().split())
	r, d = map(int, f.readline().split())


banknote_value = 1000000
bottles_bought = 0
while banknote_value * b + c >= r:
    if c < r:
        required_b = r // banknote_value
        if required_b * banknote_value + c < r:
            required_b += 1
            if (required_b <= b) and (d >= required_b * banknote_value - r):
                b -= required_b
                d -= required_b*banknote_value - r
                c += required_b*banknote_value - r
                bottles_bought += 1
            else:
                break
        else:
            if (required_b <= b):
                b -= required_b
                c -= r - required_b * banknote_value
                d += r - required_b * banknote_value
                bottles_bought += 1
            else:
                break

    else:
        c -= r
        d += r
        bottles_bought += 1

with open('ouput.txt', 'w') as f:
    f.write(str(bottles_bought))
