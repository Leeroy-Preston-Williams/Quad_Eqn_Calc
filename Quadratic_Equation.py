'''
	@Author:	Leeroy P. Williams
	@Version:	1
	@Code_Base:	Python3x
	@Desc:		Solve quadratic equations using the CLI
'''

import argparse
from math import sqrt

parser = argparse.ArgumentParser(description='calculates the roots of a quadratic equation')

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
group.add_argument('-q', '--quiet', action='store_true', help='reduce output verbosity')

parser.add_argument('a', type=int, help='the coefficient of x^2')
parser.add_argument('b', type=int, help='the coefficient of x')
parser.add_argument('c', type=int, help='the constant')

args = parser.parse_args()

x1 = ((-args.b + sqrt(args.b**2 - 4 * args.a * args.c)) / (2 * args.a))
x2 = ((-args.b - sqrt(args.b**2 - 4 * args.a * args.c)) / (2 * args.a))

print('\nEqn:    %sx^2 + %sx + %s:\n' % (args.a, args.b, args.c))
if args.quiet:
    print('x is equal to {} and {}'.format(x1, x2))
elif args.verbose:
    print('The roots of the quadratic equation are {} and {}.'.format(x1, x2))
else:
    print('x = {}; {}'.format(x1, x2))