# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    _isalnum.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marsoare <marsoare@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/08 09:06:57 by marsoare          #+#    #+#              #
#    Updated: 2024/12/08 09:19:47 by marsoare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from _isalpha import _isalpha
from _isdigit import _isdigit

def _isalnum(c) -> bool:
	return (_isdigit(c) or _isalpha(c))
