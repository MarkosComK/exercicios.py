# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marsoare <marsoare@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/08 08:39:40 by marsoare          #+#    #+#              #
#    Updated: 2024/12/08 08:50:46 by marsoare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from _isalpha import _isalpha

def test_ascii(function):
	i = 0
	while (i <= 177):
		print("char: " + chr(i), function(chr(i)))
		i += 1

def __main__():
	test_ascii(_isalpha)

__main__()
