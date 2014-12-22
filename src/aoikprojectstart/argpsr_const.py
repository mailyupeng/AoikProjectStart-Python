# coding: utf-8
from __future__ import absolute_import
import itertools

#/
ARG_HELP_ON_F = '-h'
ARG_HELP_ON_F2 = '--help'

#/
ARG_NEGATIVE_F = '-n'
ARG_NEGATIVE_K = '3vQDwCX'
ARG_NEGATIVE_V = 'N'
ARG_NEGATIVE_H = 'Take a negative integer.'

#/
ARG_NEGATIVE_MUL2_F = '--nn'
ARG_NEGATIVE_MUL2_K = '3nG5kHh'
ARG_NEGATIVE_MUL2_A = 'store_true'
ARG_NEGATIVE_MUL2_H = 'Multiply the negative integer by 2.'

#/
ARG_POSITIVE_F = '-p'
ARG_POSITIVE_K = '2zaQfqH'
ARG_POSITIVE_V = 'N'
ARG_POSITIVE_H = 'Take a positive integer.'

#/
ARG_POSITIVE_MUL2_F = '--pp'
ARG_POSITIVE_MUL2_K = '2fHbd9Y'
ARG_POSITIVE_MUL2_A = 'store_true'
ARG_POSITIVE_MUL2_H = 'Multiply the positive integer by 2.'

#/
ARG_FUNC_URI_F = '-f'
ARG_FUNC_URI_K = '3cInTiI'
ARG_FUNC_URI_V = 'FUNC_URI'
ARG_FUNC_URI_H = 'Function to call.'

#/
ARG_OUTPUT_F = '-o'
ARG_OUTPUT_K = '2evtADm'
ARG_OUTPUT_A = 'store_true'
ARG_OUTPUT_H = 'Print to stdout.'

#/
ARG_DBG_MSG_F = '-V'
ARG_DBG_MSG_K = '3qRcvOd'
ARG_DBG_MSG_D = True
ARG_DBG_MSG_V = '1|0'
ARG_DBG_MSG_H = """Debug messages on/off. Default is {}."""\
    .format('on' if ARG_DBG_MSG_D else 'off')

#/
ARG_VER_ON_F = '--ver'
ARG_VER_ON_K = '3nBeT8W'
ARG_VER_ON_A = 'store_true'
ARG_VER_ON_H = 'Show version.'

#/
## |EXC| means mutual exclusive
ARG_EXC_PAIR_S = list(itertools.combinations([
    ARG_VER_ON_F,
    ARG_NEGATIVE_F,
    ARG_POSITIVE_F,
], 2))

#/
## |REQ_ONE| means requires one of them
ARG_REQ_ONE_S = [
    ARG_HELP_ON_F,
    ARG_HELP_ON_F2,
    ARG_VER_ON_F,
    ARG_NEGATIVE_F,
    ARG_POSITIVE_F,
]

#/
## |REQ_PAIR| means one requires another
ARG_REQ_PAIR_S = [
    (ARG_NEGATIVE_MUL2_F, ARG_NEGATIVE_F),
    (ARG_POSITIVE_MUL2_F, ARG_POSITIVE_F),
    (ARG_OUTPUT_F, (ARG_NEGATIVE_F, ARG_POSITIVE_F)),
]
