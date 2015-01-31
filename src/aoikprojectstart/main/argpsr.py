# coding: utf-8
from __future__ import absolute_import
from aoikargutil import bool_0or1
from aoikargutil import int_gt0
from aoikargutil import int_lt0
from aoikprojectstart.main.argpsr_const import ARG_DBG_MSG_D
from aoikprojectstart.main.argpsr_const import ARG_DBG_MSG_F
from aoikprojectstart.main.argpsr_const import ARG_DBG_MSG_H
from aoikprojectstart.main.argpsr_const import ARG_DBG_MSG_K
from aoikprojectstart.main.argpsr_const import ARG_DBG_MSG_V
from aoikprojectstart.main.argpsr_const import ARG_FUNC_URI_F
from aoikprojectstart.main.argpsr_const import ARG_FUNC_URI_H
from aoikprojectstart.main.argpsr_const import ARG_FUNC_URI_K
from aoikprojectstart.main.argpsr_const import ARG_FUNC_URI_V
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_F
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_H
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_K
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_MUL2_A
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_MUL2_F
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_MUL2_H
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_MUL2_K
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_V
from aoikprojectstart.main.argpsr_const import ARG_OUTPUT_A
from aoikprojectstart.main.argpsr_const import ARG_OUTPUT_F
from aoikprojectstart.main.argpsr_const import ARG_OUTPUT_H
from aoikprojectstart.main.argpsr_const import ARG_OUTPUT_K
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_F
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_H
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_K
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_MUL2_A
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_MUL2_F
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_MUL2_H
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_MUL2_K
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_V
from aoikprojectstart.main.argpsr_const import ARG_VER_ON_A
from aoikprojectstart.main.argpsr_const import ARG_VER_ON_F
from aoikprojectstart.main.argpsr_const import ARG_VER_ON_H
from aoikprojectstart.main.argpsr_const import ARG_VER_ON_K
from argparse import ArgumentParser

#/
def parser_make():
    #/
    parser = ArgumentParser(add_help=True)

    #/
    parser.add_argument(
        ARG_NEGATIVE_F,
        dest=ARG_NEGATIVE_K,
        type=int_lt0,
        metavar=ARG_NEGATIVE_V,
        help=ARG_NEGATIVE_H,
    )

    #/
    parser.add_argument(
        ARG_NEGATIVE_MUL2_F,
        dest=ARG_NEGATIVE_MUL2_K,
        action=ARG_NEGATIVE_MUL2_A,
        help=ARG_NEGATIVE_MUL2_H,
    )

    #/
    parser.add_argument(
        ARG_POSITIVE_F,
        dest=ARG_POSITIVE_K,
        type=int_gt0,
        metavar=ARG_POSITIVE_V,
        help=ARG_POSITIVE_H,
    )

    #/
    parser.add_argument(
        ARG_POSITIVE_MUL2_F,
        dest=ARG_POSITIVE_MUL2_K,
        action=ARG_POSITIVE_MUL2_A,
        help=ARG_POSITIVE_MUL2_H,
    )

    #/
    parser.add_argument(
        ARG_FUNC_URI_F,
        dest=ARG_FUNC_URI_K,
        metavar=ARG_FUNC_URI_V,
        help=ARG_FUNC_URI_H,
    )

    #/
    parser.add_argument(
        ARG_OUTPUT_F,
        dest=ARG_OUTPUT_K,
        action=ARG_OUTPUT_A,
        help=ARG_OUTPUT_H,
    )

    #/
    parser.add_argument(
        ARG_DBG_MSG_F,
        dest=ARG_DBG_MSG_K,
        type=bool_0or1,
        nargs='?',
        const=True,
        default=ARG_DBG_MSG_D,
        metavar=ARG_DBG_MSG_V,
        help=ARG_DBG_MSG_H,
    )

    #/
    parser.add_argument(
        ARG_VER_ON_F,
        dest=ARG_VER_ON_K,
        action=ARG_VER_ON_A,
        help=ARG_VER_ON_H,
    )

    #/
    return parser
