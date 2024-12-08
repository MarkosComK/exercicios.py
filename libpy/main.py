# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marsoare <marsoare@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/08 08:39:40 by marsoare          #+#    #+#              #
#    Updated: 2024/12/08 09:54:35 by marsoare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from header import *

def test_ascii(function):
	i = 0
	while (i <= 177):
		print("char: " + chr(i), function(chr(i)))
		i += 1

def test_digit(function):
	i = -9
	while (i <= 9):
		print(f'value: {i}, {function(i)}')
		i += 1

def __main__():
	name = ['M', 'a', 'r', 'k', 'o', 's']
	x = name[:]
	x[0] = 'a'
	print(x)
	print(name)

__main__()
