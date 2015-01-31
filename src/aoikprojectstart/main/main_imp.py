# coding: utf-8
from __future__ import absolute_import
from aoikargutil import ensure_spec
from aoikexcutil import get_traceback_stxt
from aoikimportutil import load_obj_local_or_remote
from aoikprojectstart.main.argpsr import parser_make
from aoikprojectstart.main.argpsr_const import ARG_DBG_MSG_K
from aoikprojectstart.main.argpsr_const import ARG_FUNC_URI_K
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_K
from aoikprojectstart.main.argpsr_const import ARG_NEGATIVE_MUL2_K
from aoikprojectstart.main.argpsr_const import ARG_OUTPUT_K
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_K
from aoikprojectstart.main.argpsr_const import ARG_POSITIVE_MUL2_K
from aoikprojectstart.main.argpsr_const import ARG_SPEC
from aoikprojectstart.main.argpsr_const import ARG_VER_ON_K
from aoikprojectstart.main.main_const import FUNC_DYN_MOD_NAME
from aoikprojectstart.main.main_const import MAIN_RET_V_EXC_LEAK_ER
from aoikprojectstart.main.main_const import MAIN_RET_V_FUNC_CALL_ER
from aoikprojectstart.main.main_const import MAIN_RET_V_FUNC_LOAD_ER
from aoikprojectstart.main.main_const import MAIN_RET_V_KBINT_OK
from aoikprojectstart.main.main_const import MAIN_RET_V_OK
from aoikprojectstart.main.main_const import MAIN_RET_V_VER_SHOW_OK
from aoikprojectstart.version import __version__
import sys

#/
def main_imp():
    #/
    parser = parser_make()

    #/
    args_obj = parser.parse_args()

    #/
    ensure_spec(parser, ARG_SPEC)

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
    output_on = getattr(args_obj, ARG_OUTPUT_K)

    #/
    neg_val = getattr(args_obj, ARG_NEGATIVE_K)

    #/
    pos_val = getattr(args_obj, ARG_POSITIVE_K)

    #/
    func_uri = getattr(args_obj, ARG_FUNC_URI_K)

    #/
    if neg_val is not None:
        #/
        print('#/ Negative\n%s' % neg_val)

        #/
        if getattr(args_obj, ARG_NEGATIVE_MUL2_K):
            #/
            print('#/ Multiply by 2')

            neg_val *= 2

        #/
        out_txt = str(neg_val)
    #/
    elif pos_val is not None:
        #/
        print('#/ Positive\n%s' % pos_val)

        #/
        if getattr(args_obj, ARG_POSITIVE_MUL2_K):
            #/
            print('#/ Multiply by 2')

            pos_val *= 2

        #/
        out_txt = str(pos_val)
    #/
    elif func_uri is not None:
        #/
        print('#/ Function |%s|' % func_uri)

        #/
        try:
            #/
            func = load_obj_local_or_remote(func_uri,
                mod_name=FUNC_DYN_MOD_NAME,
            )
        #/
        except Exception:
            #/
            msg = '#/ Error\nFailed loading func.\nFunc URI is |{}|.\n'.format(func_uri)

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
            func_res = func()

            #/
            out_txt = str(func_res)
        #/
        except Exception:
            #/
            msg = '#/ Error\nFailed calling func.\nFunc URI is |{}|.\n'.format(func_uri)

            #/
            sys.stderr.write(msg)

            #/
            if dbg_msg_on:
                tb_msg = get_traceback_stxt()

                sys.stderr.write('---\n{}---\n'.format(tb_msg))

            #/
            return MAIN_RET_V_FUNC_CALL_ER
    #/
    else:
        #/ ensured by 2kqbBro
        assert 0

    #/
    if output_on:
        #/
        print('#/ Result')
        print(out_txt)

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
