from scipy import stats

#compute the n!/(n-m)!*m!
def combinum(n, m):
	n1 = n - m + 1;
	ns = 1
	while(n1 <= n):
		ns *= n1
		n1 += 1
	n1 = 1
	nm = 1
	while(n1<=m):
		nm *= n1
		n1 += 1

	return ns/nm

#p**x * (1-p)**(n-x) * combinum(n, x)
def binomdist(x, n, p):
	return pow(p, x)*pow(1-p, n-x)*combinum(n, x)

#caculate the accumlated possibility of binary distribution
def main():
	P = [0.4, 0.33, 0.25]
	N = [40, 80, 160]

	for n in N:
	    for p in P: 
	        k = int((n*2)/3)+1

	        r = 0
	        for x in range(k, n+1):
	            #r += stats.binom.pmf(x, n, p)
	            r += binomdist(x, n, p)

	        print("[%3d, %3d, %.2f] %.1e" % (n, k, p, r))


if __name__ == '__main__':
	main()
	
