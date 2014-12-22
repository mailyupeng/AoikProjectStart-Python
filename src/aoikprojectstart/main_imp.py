# coding: utf-8
from __future__ import absolute_import
from aoikargutil import ensure_exc_pairs
from aoikargutil import ensure_req_one
from aoikargutil import ensure_req_pairs
from aoikexcutil import get_traceback_stxt
from aoikimportutil import load_obj_local_or_remote
from aoikprojectstart.argpsr import parser_make
from aoikprojectstart.argpsr_const import ARG_DBG_MSG_K
from aoikprojectstart.argpsr_const import ARG_EXC_PAIR_S
from aoikprojectstart.argpsr_const import ARG_FUNC_URI_K
from aoikprojectstart.argpsr_const import ARG_NEGATIVE_K
from aoikprojectstart.argpsr_const import ARG_NEGATIVE_MUL2_K
from aoikprojectstart.argpsr_const import ARG_OUTPUT_K
from aoikprojectstart.argpsr_const import ARG_POSITIVE_K
from aoikprojectstart.argpsr_const import ARG_POSITIVE_MUL2_K
from aoikprojectstart.argpsr_const import ARG_REQ_ONE_S
from aoikprojectstart.argpsr_const import ARG_REQ_PAIR_S
from aoikprojectstart.argpsr_const import ARG_VER_ON_K
from aoikprojectstart.main_const import FUNC_DYN_MOD_NAME
from aoikprojectstart.main_const import MAIN_RET_V_EXC_LEAK_ER
from aoikprojectstart.main_const import MAIN_RET_V_FUNC_CALL_ER
from aoikprojectstart.main_const import MAIN_RET_V_FUNC_LOAD_ER
from aoikprojectstart.main_const import MAIN_RET_V_KBINT_OK
from aoikprojectstart.main_const import MAIN_RET_V_OK
from aoikprojectstart.main_const import MAIN_RET_V_VER_SHOW_OK
from aoikprojectstart.version import __version__
import sys

#/
def main_imp():
    #/
    parser = parser_make()

    #/
    args_obj = parser.parse_args()

    #/
    ensure_exc_pairs(parser, ARG_EXC_PAIR_S)

    #/ 2kqbBro
    ensure_req_one(parser, ARG_REQ_ONE_S)

    #/
    ensure_req_pairs(parser, ARG_REQ_PAIR_S)

    #/
    dbg_msg_on = getattr(args_obj, ARG_DBG_MSG_K)

    #/
    ver_on = getattr(args_obj, ARG_VER_ON_K)

    #/
    if ver_on:
        #/
        print(__version__)

        #/
        return MAIN_RET_V_VER_SHOW_OK

    #/
    neg_val = getattr(args_obj, ARG_NEGATIVE_K)

    #/
    pos_val = getattr(args_obj, ARG_POSITIVE_K)

    #/
    if neg_val:
        #/
        print('#/ Negative')

        #/
        if getattr(args_obj, ARG_NEGATIVE_MUL2_K):
            #/
            print('#/ Multiply by 2')

            neg_val *= 2

        #/
        out_val = neg_val
    #/
    elif pos_val:
        #/
        print('#/ Positive')

        #/
        if getattr(args_obj, ARG_POSITIVE_MUL2_K):
            #/
            print('#/ Multiply by 2')

            pos_val *= 2

        #/
        out_val = pos_val
    #/
    else:
        assert False
        ## ensured by 2kqbBro

    #/
    if getattr(args_obj, ARG_OUTPUT_K):
        print('#/ Output')
        print(out_val)

    #/
    func_uri = getattr(args_obj, ARG_FUNC_URI_K)

    if func_uri is None:
        return MAIN_RET_V_OK

    #/
    #assert func_uri is not None

    try:
        #/
        func = load_obj_local_or_remote(func_uri,
            mod_name=FUNC_DYN_MOD_NAME,
        )

    #/
    except Exception:
        #/
        msg = '#/ Error\nFailed loading func.\nFunc uri is |{}|.\n'.format(func_uri)

        #/
        sys.stderr.write(msg)

        #/
        if dbg_msg_on:
            tb_msg = get_traceback_stxt()

            sys.stderr.write('---\n{}---\n'.format(tb_msg))

        #/
        return MAIN_RET_V_FUNC_LOAD_ER

    #/
    try:
        #/
        res = func()

        #/
        print('#/ Result')
        print(res)

    #/
    except Exception:
        #/
        msg = '#/ Error\nFailed calling func.\nFunc uri is |{}|.\n'.format(func_uri)

        #/
        sys.stderr.write(msg)

        #/
        if dbg_msg_on:
            tb_msg = get_traceback_stxt()

            sys.stderr.write('---\n{}---\n'.format(tb_msg))

        #/
        return MAIN_RET_V_FUNC_CALL_ER

    #/
    return MAIN_RET_V_OK

#/
def main():
    #/
    try:
        #/
        return main_imp()
    #/
    except KeyboardInterrupt:
        #/
        return MAIN_RET_V_KBINT_OK
    #/
    except Exception:
        #/
        tb_msg = get_traceback_stxt()

        sys.stderr.write('#/ Uncaught exception\n---\n{}---\n'.format(tb_msg))

        #/
        return MAIN_RET_V_EXC_LEAK_ER
