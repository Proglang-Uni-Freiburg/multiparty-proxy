# $ANTLR 3.5.3 C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g 2025-07-19 08:40:23

import sys
from antlr3 import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__94=94
T__95=95
T__96=96
T__97=97
T__98=98
T__99=99
T__100=100
T__101=101
T__102=102
T__103=103
ANDKW=4
ARGUMENT=5
ARGUMENTLIST=6
ASKW=7
ATKW=8
BYKW=9
CATCHESKW=10
CHOICEKW=11
COMMENT=12
CONTINUEKW=13
DIGIT=14
DOKW=15
EMPTY_ANNOTATION=16
EMPTY_ARGUMENT_LIST=17
EMPTY_LOCAL_CATCHES=18
EMPTY_LOCAL_THROW=19
EMPTY_MESSAGE_OP=20
EMPTY_MODULE_NAME=21
EMPTY_PARAMETER_DECL_LIST=22
EMPTY_SCOPE_NAME=23
EXTIDENTIFIER=24
FROMKW=25
GLOBALCHOICE=26
GLOBALCONTINUE=27
GLOBALDO=28
GLOBALINTERACTIONSEQUENCE=29
GLOBALINTERRUPT=30
GLOBALINTERRUPTIBLE=31
GLOBALKW=32
GLOBALMESSAGETRANSFER=33
GLOBALPARALLEL=34
GLOBALPROTOCOLBLOCK=35
GLOBALPROTOCOLDECL=36
GLOBALPROTOCOLDEF=37
GLOBALPROTOCOLINSTANCE=38
GLOBALRECURSION=39
IDENTIFIER=40
IMPORTKW=41
IMPORTMEMBER=42
IMPORTMODULE=43
INSTANTIATESKW=44
INTERRUPTIBLEKW=45
KIND_MESSAGE_SIGNATURE=46
KIND_PAYLOAD_TYPE=47
LETTER=48
LINE_COMMENT=49
LOCALCATCH=50
LOCALCHOICE=51
LOCALCONTINUE=52
LOCALDO=53
LOCALINTERACTIONSEQUENCE=54
LOCALINTERRUPT=55
LOCALINTERRUPTIBLE=56
LOCALKW=57
LOCALMESSAGETRANSFER=58
LOCALPARALLEL=59
LOCALPROTOCOLBLOCK=60
LOCALPROTOCOLDECL=61
LOCALPROTOCOLDEF=62
LOCALPROTOCOLINSTANCE=63
LOCALRECEIVE=64
LOCALRECURSION=65
LOCALSEND=66
LOCALTHROW=67
MESSAGESIGNATURE=68
MODULE=69
MODULEDECL=70
MODULEKW=71
ORKW=72
PARAMETERDECL=73
PARAMETERDECLLIST=74
PARKW=75
PAYLOAD=76
PAYLOADELEMENT=77
PAYLOADTYPEDECL=78
PROTOCOLKW=79
RECKW=80
ROLEDECL=81
ROLEDECLLIST=82
ROLEINSTANTIATION=83
ROLEINSTANTIATIONLIST=84
ROLEKW=85
SIGKW=86
SYMBOL=87
THROWSKW=88
TOKW=89
TYPEKW=90
UNDERSCORE=91
WHITESPACE=92
WITHKW=93

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 94: "T__94", 95: "T__95", 96: "T__96", 97: "T__97", 98: "T__98", 
    99: "T__99", 100: "T__100", 101: "T__101", 102: "T__102", 103: "T__103", 
    4: "ANDKW", 5: "ARGUMENT", 6: "ARGUMENTLIST", 7: "ASKW", 8: "ATKW", 
    9: "BYKW", 10: "CATCHESKW", 11: "CHOICEKW", 12: "COMMENT", 13: "CONTINUEKW", 
    14: "DIGIT", 15: "DOKW", 16: "EMPTY_ANNOTATION", 17: "EMPTY_ARGUMENT_LIST", 
    18: "EMPTY_LOCAL_CATCHES", 19: "EMPTY_LOCAL_THROW", 20: "EMPTY_MESSAGE_OP", 
    21: "EMPTY_MODULE_NAME", 22: "EMPTY_PARAMETER_DECL_LIST", 23: "EMPTY_SCOPE_NAME", 
    24: "EXTIDENTIFIER", 25: "FROMKW", 26: "GLOBALCHOICE", 27: "GLOBALCONTINUE", 
    28: "GLOBALDO", 29: "GLOBALINTERACTIONSEQUENCE", 30: "GLOBALINTERRUPT", 
    31: "GLOBALINTERRUPTIBLE", 32: "GLOBALKW", 33: "GLOBALMESSAGETRANSFER", 
    34: "GLOBALPARALLEL", 35: "GLOBALPROTOCOLBLOCK", 36: "GLOBALPROTOCOLDECL", 
    37: "GLOBALPROTOCOLDEF", 38: "GLOBALPROTOCOLINSTANCE", 39: "GLOBALRECURSION", 
    40: "IDENTIFIER", 41: "IMPORTKW", 42: "IMPORTMEMBER", 43: "IMPORTMODULE", 
    44: "INSTANTIATESKW", 45: "INTERRUPTIBLEKW", 46: "KIND_MESSAGE_SIGNATURE", 
    47: "KIND_PAYLOAD_TYPE", 48: "LETTER", 49: "LINE_COMMENT", 50: "LOCALCATCH", 
    51: "LOCALCHOICE", 52: "LOCALCONTINUE", 53: "LOCALDO", 54: "LOCALINTERACTIONSEQUENCE", 
    55: "LOCALINTERRUPT", 56: "LOCALINTERRUPTIBLE", 57: "LOCALKW", 58: "LOCALMESSAGETRANSFER", 
    59: "LOCALPARALLEL", 60: "LOCALPROTOCOLBLOCK", 61: "LOCALPROTOCOLDECL", 
    62: "LOCALPROTOCOLDEF", 63: "LOCALPROTOCOLINSTANCE", 64: "LOCALRECEIVE", 
    65: "LOCALRECURSION", 66: "LOCALSEND", 67: "LOCALTHROW", 68: "MESSAGESIGNATURE", 
    69: "MODULE", 70: "MODULEDECL", 71: "MODULEKW", 72: "ORKW", 73: "PARAMETERDECL", 
    74: "PARAMETERDECLLIST", 75: "PARKW", 76: "PAYLOAD", 77: "PAYLOADELEMENT", 
    78: "PAYLOADTYPEDECL", 79: "PROTOCOLKW", 80: "RECKW", 81: "ROLEDECL", 
    82: "ROLEDECLLIST", 83: "ROLEINSTANTIATION", 84: "ROLEINSTANTIATIONLIST", 
    85: "ROLEKW", 86: "SIGKW", 87: "SYMBOL", 88: "THROWSKW", 89: "TOKW", 
    90: "TYPEKW", 91: "UNDERSCORE", 92: "WHITESPACE", 93: "WITHKW"
}


class ScribbleLexer(Lexer):

    grammarFileName = "C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )






    # $ANTLR start "ANDKW"
    def mANDKW(self, ):
        try:
            _type = ANDKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:7:7: ( 'and' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:7:9: 'and'
            pass 
            self.match("and")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ANDKW"



    # $ANTLR start "ARGUMENT"
    def mARGUMENT(self, ):
        try:
            _type = ARGUMENT
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:8:10: ( 'argument' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:8:12: 'argument'
            pass 
            self.match("argument")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARGUMENT"



    # $ANTLR start "ARGUMENTLIST"
    def mARGUMENTLIST(self, ):
        try:
            _type = ARGUMENTLIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:9:14: ( 'argument-list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:9:16: 'argument-list'
            pass 
            self.match("argument-list")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARGUMENTLIST"



    # $ANTLR start "ASKW"
    def mASKW(self, ):
        try:
            _type = ASKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:10:6: ( 'as' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:10:8: 'as'
            pass 
            self.match("as")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ASKW"



    # $ANTLR start "ATKW"
    def mATKW(self, ):
        try:
            _type = ATKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:11:6: ( 'at' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:11:8: 'at'
            pass 
            self.match("at")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ATKW"



    # $ANTLR start "BYKW"
    def mBYKW(self, ):
        try:
            _type = BYKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:12:6: ( 'by' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:12:8: 'by'
            pass 
            self.match("by")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BYKW"



    # $ANTLR start "CATCHESKW"
    def mCATCHESKW(self, ):
        try:
            _type = CATCHESKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:13:11: ( 'catches' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:13:13: 'catches'
            pass 
            self.match("catches")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CATCHESKW"



    # $ANTLR start "CHOICEKW"
    def mCHOICEKW(self, ):
        try:
            _type = CHOICEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:14:10: ( 'choice' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:14:12: 'choice'
            pass 
            self.match("choice")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CHOICEKW"



    # $ANTLR start "CONTINUEKW"
    def mCONTINUEKW(self, ):
        try:
            _type = CONTINUEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:15:12: ( 'continue' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:15:14: 'continue'
            pass 
            self.match("continue")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONTINUEKW"



    # $ANTLR start "DOKW"
    def mDOKW(self, ):
        try:
            _type = DOKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:16:6: ( 'do' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:16:8: 'do'
            pass 
            self.match("do")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOKW"



    # $ANTLR start "EMPTY_ANNOTATION"
    def mEMPTY_ANNOTATION(self, ):
        try:
            _type = EMPTY_ANNOTATION
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:17:18: ( '__empty_annotation' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:17:20: '__empty_annotation'
            pass 
            self.match("__empty_annotation")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EMPTY_ANNOTATION"



    # $ANTLR start "EMPTY_ARGUMENT_LIST"
    def mEMPTY_ARGUMENT_LIST(self, ):
        try:
            _type = EMPTY_ARGUMENT_LIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:18:21: ( '__empty_argument_list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:18:23: '__empty_argument_list'
            pass 
            self.match("__empty_argument_list")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EMPTY_ARGUMENT_LIST"



    # $ANTLR start "EMPTY_LOCAL_CATCHES"
    def mEMPTY_LOCAL_CATCHES(self, ):
        try:
            _type = EMPTY_LOCAL_CATCHES
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:19:21: ( '__empty_local_catch' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:19:23: '__empty_local_catch'
            pass 
            self.match("__empty_local_catch")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EMPTY_LOCAL_CATCHES"



    # $ANTLR start "EMPTY_LOCAL_THROW"
    def mEMPTY_LOCAL_THROW(self, ):
        try:
            _type = EMPTY_LOCAL_THROW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:20:19: ( '__empty_local_throw' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:20:21: '__empty_local_throw'
            pass 
            self.match("__empty_local_throw")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EMPTY_LOCAL_THROW"



    # $ANTLR start "EMPTY_MESSAGE_OP"
    def mEMPTY_MESSAGE_OP(self, ):
        try:
            _type = EMPTY_MESSAGE_OP
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:21:18: ( '__empty_message_op' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:21:20: '__empty_message_op'
            pass 
            self.match("__empty_message_op")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EMPTY_MESSAGE_OP"



    # $ANTLR start "EMPTY_MODULE_NAME"
    def mEMPTY_MODULE_NAME(self, ):
        try:
            _type = EMPTY_MODULE_NAME
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:22:19: ( '__empty_module_name' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:22:21: '__empty_module_name'
            pass 
            self.match("__empty_module_name")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EMPTY_MODULE_NAME"



    # $ANTLR start "EMPTY_PARAMETER_DECL_LIST"
    def mEMPTY_PARAMETER_DECL_LIST(self, ):
        try:
            _type = EMPTY_PARAMETER_DECL_LIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:23:27: ( '__empty_parameter_decl_list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:23:29: '__empty_parameter_decl_list'
            pass 
            self.match("__empty_parameter_decl_list")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EMPTY_PARAMETER_DECL_LIST"



    # $ANTLR start "EMPTY_SCOPE_NAME"
    def mEMPTY_SCOPE_NAME(self, ):
        try:
            _type = EMPTY_SCOPE_NAME
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:24:18: ( '__empty_scope_name' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:24:20: '__empty_scope_name'
            pass 
            self.match("__empty_scope_name")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EMPTY_SCOPE_NAME"



    # $ANTLR start "FROMKW"
    def mFROMKW(self, ):
        try:
            _type = FROMKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:25:8: ( 'from' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:25:10: 'from'
            pass 
            self.match("from")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FROMKW"



    # $ANTLR start "GLOBALCHOICE"
    def mGLOBALCHOICE(self, ):
        try:
            _type = GLOBALCHOICE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:26:14: ( 'global-choice' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:26:16: 'global-choice'
            pass 
            self.match("global-choice")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALCHOICE"



    # $ANTLR start "GLOBALCONTINUE"
    def mGLOBALCONTINUE(self, ):
        try:
            _type = GLOBALCONTINUE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:27:16: ( 'global-continue' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:27:18: 'global-continue'
            pass 
            self.match("global-continue")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALCONTINUE"



    # $ANTLR start "GLOBALDO"
    def mGLOBALDO(self, ):
        try:
            _type = GLOBALDO
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:28:10: ( 'global-do' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:28:12: 'global-do'
            pass 
            self.match("global-do")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALDO"



    # $ANTLR start "GLOBALINTERACTIONSEQUENCE"
    def mGLOBALINTERACTIONSEQUENCE(self, ):
        try:
            _type = GLOBALINTERACTIONSEQUENCE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:29:27: ( 'global-interaction-sequence' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:29:29: 'global-interaction-sequence'
            pass 
            self.match("global-interaction-sequence")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALINTERACTIONSEQUENCE"



    # $ANTLR start "GLOBALINTERRUPT"
    def mGLOBALINTERRUPT(self, ):
        try:
            _type = GLOBALINTERRUPT
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:30:17: ( 'global-interrupt' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:30:19: 'global-interrupt'
            pass 
            self.match("global-interrupt")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALINTERRUPT"



    # $ANTLR start "GLOBALINTERRUPTIBLE"
    def mGLOBALINTERRUPTIBLE(self, ):
        try:
            _type = GLOBALINTERRUPTIBLE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:31:21: ( 'global-interruptible' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:31:23: 'global-interruptible'
            pass 
            self.match("global-interruptible")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALINTERRUPTIBLE"



    # $ANTLR start "GLOBALKW"
    def mGLOBALKW(self, ):
        try:
            _type = GLOBALKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:32:10: ( 'global' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:32:12: 'global'
            pass 
            self.match("global")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALKW"



    # $ANTLR start "GLOBALMESSAGETRANSFER"
    def mGLOBALMESSAGETRANSFER(self, ):
        try:
            _type = GLOBALMESSAGETRANSFER
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:33:23: ( 'global-message-transfer' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:33:25: 'global-message-transfer'
            pass 
            self.match("global-message-transfer")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALMESSAGETRANSFER"



    # $ANTLR start "GLOBALPARALLEL"
    def mGLOBALPARALLEL(self, ):
        try:
            _type = GLOBALPARALLEL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:34:16: ( 'global-parallel' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:34:18: 'global-parallel'
            pass 
            self.match("global-parallel")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALPARALLEL"



    # $ANTLR start "GLOBALPROTOCOLBLOCK"
    def mGLOBALPROTOCOLBLOCK(self, ):
        try:
            _type = GLOBALPROTOCOLBLOCK
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:35:21: ( 'global-protocol-block' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:35:23: 'global-protocol-block'
            pass 
            self.match("global-protocol-block")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALPROTOCOLBLOCK"



    # $ANTLR start "GLOBALPROTOCOLDECL"
    def mGLOBALPROTOCOLDECL(self, ):
        try:
            _type = GLOBALPROTOCOLDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:36:20: ( 'global-protocol-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:36:22: 'global-protocol-decl'
            pass 
            self.match("global-protocol-decl")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALPROTOCOLDECL"



    # $ANTLR start "GLOBALPROTOCOLDEF"
    def mGLOBALPROTOCOLDEF(self, ):
        try:
            _type = GLOBALPROTOCOLDEF
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:37:19: ( 'global-protocol-def' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:37:21: 'global-protocol-def'
            pass 
            self.match("global-protocol-def")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALPROTOCOLDEF"



    # $ANTLR start "GLOBALPROTOCOLINSTANCE"
    def mGLOBALPROTOCOLINSTANCE(self, ):
        try:
            _type = GLOBALPROTOCOLINSTANCE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:38:24: ( 'global-protocol-instance' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:38:26: 'global-protocol-instance'
            pass 
            self.match("global-protocol-instance")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALPROTOCOLINSTANCE"



    # $ANTLR start "GLOBALRECURSION"
    def mGLOBALRECURSION(self, ):
        try:
            _type = GLOBALRECURSION
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:39:17: ( 'global-recursion' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:39:19: 'global-recursion'
            pass 
            self.match("global-recursion")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBALRECURSION"



    # $ANTLR start "IMPORTKW"
    def mIMPORTKW(self, ):
        try:
            _type = IMPORTKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:40:10: ( 'import' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:40:12: 'import'
            pass 
            self.match("import")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IMPORTKW"



    # $ANTLR start "IMPORTMEMBER"
    def mIMPORTMEMBER(self, ):
        try:
            _type = IMPORTMEMBER
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:41:14: ( 'import-member' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:41:16: 'import-member'
            pass 
            self.match("import-member")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IMPORTMEMBER"



    # $ANTLR start "IMPORTMODULE"
    def mIMPORTMODULE(self, ):
        try:
            _type = IMPORTMODULE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:42:14: ( 'import-module' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:42:16: 'import-module'
            pass 
            self.match("import-module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IMPORTMODULE"



    # $ANTLR start "INSTANTIATESKW"
    def mINSTANTIATESKW(self, ):
        try:
            _type = INSTANTIATESKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:43:16: ( 'instantiates' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:43:18: 'instantiates'
            pass 
            self.match("instantiates")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INSTANTIATESKW"



    # $ANTLR start "INTERRUPTIBLEKW"
    def mINTERRUPTIBLEKW(self, ):
        try:
            _type = INTERRUPTIBLEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:44:17: ( 'interruptible' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:44:19: 'interruptible'
            pass 
            self.match("interruptible")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INTERRUPTIBLEKW"



    # $ANTLR start "KIND_MESSAGE_SIGNATURE"
    def mKIND_MESSAGE_SIGNATURE(self, ):
        try:
            _type = KIND_MESSAGE_SIGNATURE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:45:24: ( 'KIND_MESSAGE_SIGNATURE' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:45:26: 'KIND_MESSAGE_SIGNATURE'
            pass 
            self.match("KIND_MESSAGE_SIGNATURE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KIND_MESSAGE_SIGNATURE"



    # $ANTLR start "KIND_PAYLOAD_TYPE"
    def mKIND_PAYLOAD_TYPE(self, ):
        try:
            _type = KIND_PAYLOAD_TYPE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:46:19: ( 'KIND_PAYLOAD_TYPE' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:46:21: 'KIND_PAYLOAD_TYPE'
            pass 
            self.match("KIND_PAYLOAD_TYPE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KIND_PAYLOAD_TYPE"



    # $ANTLR start "LOCALCATCH"
    def mLOCALCATCH(self, ):
        try:
            _type = LOCALCATCH
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:47:12: ( 'local-catch' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:47:14: 'local-catch'
            pass 
            self.match("local-catch")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALCATCH"



    # $ANTLR start "LOCALCHOICE"
    def mLOCALCHOICE(self, ):
        try:
            _type = LOCALCHOICE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:48:13: ( 'local-choice' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:48:15: 'local-choice'
            pass 
            self.match("local-choice")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALCHOICE"



    # $ANTLR start "LOCALCONTINUE"
    def mLOCALCONTINUE(self, ):
        try:
            _type = LOCALCONTINUE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:49:15: ( 'local-continue' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:49:17: 'local-continue'
            pass 
            self.match("local-continue")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALCONTINUE"



    # $ANTLR start "LOCALDO"
    def mLOCALDO(self, ):
        try:
            _type = LOCALDO
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:50:9: ( 'local-do' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:50:11: 'local-do'
            pass 
            self.match("local-do")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALDO"



    # $ANTLR start "LOCALINTERACTIONSEQUENCE"
    def mLOCALINTERACTIONSEQUENCE(self, ):
        try:
            _type = LOCALINTERACTIONSEQUENCE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:51:26: ( 'local-interaction-sequence' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:51:28: 'local-interaction-sequence'
            pass 
            self.match("local-interaction-sequence")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALINTERACTIONSEQUENCE"



    # $ANTLR start "LOCALINTERRUPT"
    def mLOCALINTERRUPT(self, ):
        try:
            _type = LOCALINTERRUPT
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:52:16: ( 'local-interrupt' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:52:18: 'local-interrupt'
            pass 
            self.match("local-interrupt")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALINTERRUPT"



    # $ANTLR start "LOCALINTERRUPTIBLE"
    def mLOCALINTERRUPTIBLE(self, ):
        try:
            _type = LOCALINTERRUPTIBLE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:53:20: ( 'local-interruptible' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:53:22: 'local-interruptible'
            pass 
            self.match("local-interruptible")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALINTERRUPTIBLE"



    # $ANTLR start "LOCALKW"
    def mLOCALKW(self, ):
        try:
            _type = LOCALKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:54:9: ( 'local' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:54:11: 'local'
            pass 
            self.match("local")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALKW"



    # $ANTLR start "LOCALMESSAGETRANSFER"
    def mLOCALMESSAGETRANSFER(self, ):
        try:
            _type = LOCALMESSAGETRANSFER
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:55:22: ( 'local-message-transfer' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:55:24: 'local-message-transfer'
            pass 
            self.match("local-message-transfer")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALMESSAGETRANSFER"



    # $ANTLR start "LOCALPARALLEL"
    def mLOCALPARALLEL(self, ):
        try:
            _type = LOCALPARALLEL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:56:15: ( 'local-parallel' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:56:17: 'local-parallel'
            pass 
            self.match("local-parallel")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALPARALLEL"



    # $ANTLR start "LOCALPROTOCOLBLOCK"
    def mLOCALPROTOCOLBLOCK(self, ):
        try:
            _type = LOCALPROTOCOLBLOCK
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:57:20: ( 'local-protocol-block' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:57:22: 'local-protocol-block'
            pass 
            self.match("local-protocol-block")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALPROTOCOLBLOCK"



    # $ANTLR start "LOCALPROTOCOLDECL"
    def mLOCALPROTOCOLDECL(self, ):
        try:
            _type = LOCALPROTOCOLDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:58:19: ( 'local-protocol-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:58:21: 'local-protocol-decl'
            pass 
            self.match("local-protocol-decl")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALPROTOCOLDECL"



    # $ANTLR start "LOCALPROTOCOLDEF"
    def mLOCALPROTOCOLDEF(self, ):
        try:
            _type = LOCALPROTOCOLDEF
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:59:18: ( 'local-protocol-def' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:59:20: 'local-protocol-def'
            pass 
            self.match("local-protocol-def")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALPROTOCOLDEF"



    # $ANTLR start "LOCALPROTOCOLINSTANCE"
    def mLOCALPROTOCOLINSTANCE(self, ):
        try:
            _type = LOCALPROTOCOLINSTANCE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:60:23: ( 'local-protocol-instance' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:60:25: 'local-protocol-instance'
            pass 
            self.match("local-protocol-instance")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALPROTOCOLINSTANCE"



    # $ANTLR start "LOCALRECEIVE"
    def mLOCALRECEIVE(self, ):
        try:
            _type = LOCALRECEIVE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:61:14: ( 'local-receive' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:61:16: 'local-receive'
            pass 
            self.match("local-receive")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALRECEIVE"



    # $ANTLR start "LOCALRECURSION"
    def mLOCALRECURSION(self, ):
        try:
            _type = LOCALRECURSION
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:62:16: ( 'local-recursion' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:62:18: 'local-recursion'
            pass 
            self.match("local-recursion")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALRECURSION"



    # $ANTLR start "LOCALSEND"
    def mLOCALSEND(self, ):
        try:
            _type = LOCALSEND
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:63:11: ( 'local-send' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:63:13: 'local-send'
            pass 
            self.match("local-send")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALSEND"



    # $ANTLR start "LOCALTHROW"
    def mLOCALTHROW(self, ):
        try:
            _type = LOCALTHROW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:64:12: ( 'local-throw' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:64:14: 'local-throw'
            pass 
            self.match("local-throw")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOCALTHROW"



    # $ANTLR start "MESSAGESIGNATURE"
    def mMESSAGESIGNATURE(self, ):
        try:
            _type = MESSAGESIGNATURE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:65:18: ( 'message-signature' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:65:20: 'message-signature'
            pass 
            self.match("message-signature")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MESSAGESIGNATURE"



    # $ANTLR start "MODULE"
    def mMODULE(self, ):
        try:
            _type = MODULE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:66:8: ( 'modul' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:66:10: 'modul'
            pass 
            self.match("modul")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MODULE"



    # $ANTLR start "MODULEDECL"
    def mMODULEDECL(self, ):
        try:
            _type = MODULEDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:67:12: ( 'module-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:67:14: 'module-decl'
            pass 
            self.match("module-decl")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MODULEDECL"



    # $ANTLR start "MODULEKW"
    def mMODULEKW(self, ):
        try:
            _type = MODULEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:68:10: ( 'module' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:68:12: 'module'
            pass 
            self.match("module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MODULEKW"



    # $ANTLR start "ORKW"
    def mORKW(self, ):
        try:
            _type = ORKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:69:6: ( 'or' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:69:8: 'or'
            pass 
            self.match("or")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ORKW"



    # $ANTLR start "PARAMETERDECL"
    def mPARAMETERDECL(self, ):
        try:
            _type = PARAMETERDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:70:15: ( 'parameter-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:70:17: 'parameter-decl'
            pass 
            self.match("parameter-decl")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PARAMETERDECL"



    # $ANTLR start "PARAMETERDECLLIST"
    def mPARAMETERDECLLIST(self, ):
        try:
            _type = PARAMETERDECLLIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:71:19: ( 'parameter-decl-list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:71:21: 'parameter-decl-list'
            pass 
            self.match("parameter-decl-list")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PARAMETERDECLLIST"



    # $ANTLR start "PARKW"
    def mPARKW(self, ):
        try:
            _type = PARKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:72:7: ( 'par' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:72:9: 'par'
            pass 
            self.match("par")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PARKW"



    # $ANTLR start "PAYLOAD"
    def mPAYLOAD(self, ):
        try:
            _type = PAYLOAD
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:73:9: ( 'payload' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:73:11: 'payload'
            pass 
            self.match("payload")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PAYLOAD"



    # $ANTLR start "PAYLOADELEMENT"
    def mPAYLOADELEMENT(self, ):
        try:
            _type = PAYLOADELEMENT
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:74:16: ( 'payloadelement' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:74:18: 'payloadelement'
            pass 
            self.match("payloadelement")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PAYLOADELEMENT"



    # $ANTLR start "PAYLOADTYPEDECL"
    def mPAYLOADTYPEDECL(self, ):
        try:
            _type = PAYLOADTYPEDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:75:17: ( 'payload-type-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:75:19: 'payload-type-decl'
            pass 
            self.match("payload-type-decl")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PAYLOADTYPEDECL"



    # $ANTLR start "PROTOCOLKW"
    def mPROTOCOLKW(self, ):
        try:
            _type = PROTOCOLKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:76:12: ( 'protocol' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:76:14: 'protocol'
            pass 
            self.match("protocol")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROTOCOLKW"



    # $ANTLR start "RECKW"
    def mRECKW(self, ):
        try:
            _type = RECKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:77:7: ( 'rec' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:77:9: 'rec'
            pass 
            self.match("rec")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RECKW"



    # $ANTLR start "ROLEDECL"
    def mROLEDECL(self, ):
        try:
            _type = ROLEDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:78:10: ( 'role-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:78:12: 'role-decl'
            pass 
            self.match("role-decl")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROLEDECL"



    # $ANTLR start "ROLEDECLLIST"
    def mROLEDECLLIST(self, ):
        try:
            _type = ROLEDECLLIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:79:14: ( 'role-decl-list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:79:16: 'role-decl-list'
            pass 
            self.match("role-decl-list")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROLEDECLLIST"



    # $ANTLR start "ROLEINSTANTIATION"
    def mROLEINSTANTIATION(self, ):
        try:
            _type = ROLEINSTANTIATION
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:80:19: ( 'role-instantiation' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:80:21: 'role-instantiation'
            pass 
            self.match("role-instantiation")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROLEINSTANTIATION"



    # $ANTLR start "ROLEINSTANTIATIONLIST"
    def mROLEINSTANTIATIONLIST(self, ):
        try:
            _type = ROLEINSTANTIATIONLIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:81:23: ( 'role-instantiation-list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:81:25: 'role-instantiation-list'
            pass 
            self.match("role-instantiation-list")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROLEINSTANTIATIONLIST"



    # $ANTLR start "ROLEKW"
    def mROLEKW(self, ):
        try:
            _type = ROLEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:82:8: ( 'role' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:82:10: 'role'
            pass 
            self.match("role")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROLEKW"



    # $ANTLR start "SIGKW"
    def mSIGKW(self, ):
        try:
            _type = SIGKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:83:7: ( 'sig' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:83:9: 'sig'
            pass 
            self.match("sig")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SIGKW"



    # $ANTLR start "THROWSKW"
    def mTHROWSKW(self, ):
        try:
            _type = THROWSKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:84:10: ( 'throws' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:84:12: 'throws'
            pass 
            self.match("throws")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "THROWSKW"



    # $ANTLR start "TOKW"
    def mTOKW(self, ):
        try:
            _type = TOKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:85:6: ( 'to' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:85:8: 'to'
            pass 
            self.match("to")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TOKW"



    # $ANTLR start "TYPEKW"
    def mTYPEKW(self, ):
        try:
            _type = TYPEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:86:8: ( 'type' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:86:10: 'type'
            pass 
            self.match("type")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPEKW"



    # $ANTLR start "WITHKW"
    def mWITHKW(self, ):
        try:
            _type = WITHKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:87:8: ( 'with' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:87:10: 'with'
            pass 
            self.match("with")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WITHKW"



    # $ANTLR start "T__94"
    def mT__94(self, ):
        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:88:7: ( '(' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:88:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__94"



    # $ANTLR start "T__95"
    def mT__95(self, ):
        try:
            _type = T__95
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:89:7: ( ')' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:89:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__95"



    # $ANTLR start "T__96"
    def mT__96(self, ):
        try:
            _type = T__96
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:90:7: ( ',' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:90:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__96"



    # $ANTLR start "T__97"
    def mT__97(self, ):
        try:
            _type = T__97
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:91:7: ( '.' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:91:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__97"



    # $ANTLR start "T__98"
    def mT__98(self, ):
        try:
            _type = T__98
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:92:7: ( ':' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:92:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__98"



    # $ANTLR start "T__99"
    def mT__99(self, ):
        try:
            _type = T__99
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:93:7: ( ';' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:93:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__99"



    # $ANTLR start "T__100"
    def mT__100(self, ):
        try:
            _type = T__100
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:94:8: ( '<' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:94:10: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__100"



    # $ANTLR start "T__101"
    def mT__101(self, ):
        try:
            _type = T__101
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:95:8: ( '>' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:95:10: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__101"



    # $ANTLR start "T__102"
    def mT__102(self, ):
        try:
            _type = T__102
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:96:8: ( '{' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:96:10: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__102"



    # $ANTLR start "T__103"
    def mT__103(self, ):
        try:
            _type = T__103
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:97:8: ( '}' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:97:10: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__103"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):
        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:145:11: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:146:2: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:146:2: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 in {9, 10, 12, 13, 32}) :
                    alt1 = 1


                if alt1 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:
                    pass 
                    if self.input.LA(1) in {9, 10, 12, 13, 32}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1


            #action start
             
            _channel = HIDDEN;
            	
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:151:8: ( '/*' ( . )* '*/' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:152:2: '/*' ( . )* '*/'
            pass 
            self.match("/*")


            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:152:7: ( . )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 42) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 47) :
                        alt2 = 2
                    elif ((0 <= LA2_1 <= 46) or (48 <= LA2_1 <= 65535) or LA2_1 in {}) :
                        alt2 = 1


                elif ((0 <= LA2_0 <= 41) or (43 <= LA2_0 <= 65535) or LA2_0 in {}) :
                    alt2 = 1


                if alt2 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:152:7: .
                    pass 
                    self.matchAny()


                else:
                    break #loop2


            self.match("*/")


            #action start
             
            _channel=HIDDEN;
            	
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):
        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:155:13: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:156:2: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("//")


            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:156:7: (~ ( '\\n' | '\\r' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 9) or (14 <= LA3_0 <= 65535) or LA3_0 in {11, 12}) :
                    alt3 = 1


                if alt3 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (14 <= self.input.LA(1) <= 65535) or self.input.LA(1) in {11, 12}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop3


            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:156:21: ( '\\r' )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 13) :
                alt4 = 1
            if alt4 == 1:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:156:21: '\\r'
                pass 
                self.match(13)




            self.match(10)

            #action start
             
            _channel=HIDDEN;
            	
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "IDENTIFIER"
    def mIDENTIFIER(self, ):
        try:
            _type = IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:168:11: ( ( LETTER | UNDERSCORE ) ( LETTER | DIGIT | UNDERSCORE )* )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:169:2: ( LETTER | UNDERSCORE ) ( LETTER | DIGIT | UNDERSCORE )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:169:24: ( LETTER | DIGIT | UNDERSCORE )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 90) or (97 <= LA5_0 <= 122) or LA5_0 in {95}) :
                    alt5 = 1


                if alt5 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop5




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IDENTIFIER"



    # $ANTLR start "SYMBOL"
    def mSYMBOL(self, ):
        try:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:169:16: ( '{' | '}' | '(' | ')' | '[' | ']' | ':' | '/' | '\\\\' | '.' | '\\#' | '&' | '?' | '!' | UNDERSCORE )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:
            pass 
            if self.input.LA(1) in {33, 35, 38, 40, 41, 46, 47, 58, 63, 91, 92, 93, 95, 123, 125}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "SYMBOL"



    # $ANTLR start "EXTIDENTIFIER"
    def mEXTIDENTIFIER(self, ):
        try:
            _type = EXTIDENTIFIER
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:177:14: ( '\\\"' ( LETTER | UNDERSCORE ) ( LETTER | DIGIT | SYMBOL )* '\\\"' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:178:2: '\\\"' ( LETTER | UNDERSCORE ) ( LETTER | DIGIT | SYMBOL )* '\\\"'
            pass 
            self.match(34)

            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:178:29: ( LETTER | DIGIT | SYMBOL )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((46 <= LA6_0 <= 58) or (65 <= LA6_0 <= 93) or (97 <= LA6_0 <= 123) or LA6_0 in {33, 35, 38, 40, 41, 63, 95, 125}) :
                    alt6 = 1


                if alt6 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:
                    pass 
                    if (46 <= self.input.LA(1) <= 58) or (65 <= self.input.LA(1) <= 93) or (97 <= self.input.LA(1) <= 123) or self.input.LA(1) in {33, 35, 38, 40, 41, 63, 95, 125}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop6


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EXTIDENTIFIER"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):
        try:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:181:16: ( 'a' .. 'z' | 'A' .. 'Z' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):
        try:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:185:15: ( '0' .. '9' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:
            pass 
            if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "UNDERSCORE"
    def mUNDERSCORE(self, ):
        try:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:189:20: ( '_' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:190:2: '_'
            pass 
            self.match(95)




        finally:
            pass

    # $ANTLR end "UNDERSCORE"



    def mTokens(self):
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:8: ( ANDKW | ARGUMENT | ARGUMENTLIST | ASKW | ATKW | BYKW | CATCHESKW | CHOICEKW | CONTINUEKW | DOKW | EMPTY_ANNOTATION | EMPTY_ARGUMENT_LIST | EMPTY_LOCAL_CATCHES | EMPTY_LOCAL_THROW | EMPTY_MESSAGE_OP | EMPTY_MODULE_NAME | EMPTY_PARAMETER_DECL_LIST | EMPTY_SCOPE_NAME | FROMKW | GLOBALCHOICE | GLOBALCONTINUE | GLOBALDO | GLOBALINTERACTIONSEQUENCE | GLOBALINTERRUPT | GLOBALINTERRUPTIBLE | GLOBALKW | GLOBALMESSAGETRANSFER | GLOBALPARALLEL | GLOBALPROTOCOLBLOCK | GLOBALPROTOCOLDECL | GLOBALPROTOCOLDEF | GLOBALPROTOCOLINSTANCE | GLOBALRECURSION | IMPORTKW | IMPORTMEMBER | IMPORTMODULE | INSTANTIATESKW | INTERRUPTIBLEKW | KIND_MESSAGE_SIGNATURE | KIND_PAYLOAD_TYPE | LOCALCATCH | LOCALCHOICE | LOCALCONTINUE | LOCALDO | LOCALINTERACTIONSEQUENCE | LOCALINTERRUPT | LOCALINTERRUPTIBLE | LOCALKW | LOCALMESSAGETRANSFER | LOCALPARALLEL | LOCALPROTOCOLBLOCK | LOCALPROTOCOLDECL | LOCALPROTOCOLDEF | LOCALPROTOCOLINSTANCE | LOCALRECEIVE | LOCALRECURSION | LOCALSEND | LOCALTHROW | MESSAGESIGNATURE | MODULE | MODULEDECL | MODULEKW | ORKW | PARAMETERDECL | PARAMETERDECLLIST | PARKW | PAYLOAD | PAYLOADELEMENT | PAYLOADTYPEDECL | PROTOCOLKW | RECKW | ROLEDECL | ROLEDECLLIST | ROLEINSTANTIATION | ROLEINSTANTIATIONLIST | ROLEKW | SIGKW | THROWSKW | TOKW | TYPEKW | WITHKW | T__94 | T__95 | T__96 | T__97 | T__98 | T__99 | T__100 | T__101 | T__102 | T__103 | WHITESPACE | COMMENT | LINE_COMMENT | IDENTIFIER | EXTIDENTIFIER )
        alt7 = 96
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:10: ANDKW
            pass 
            self.mANDKW()



        elif alt7 == 2:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:16: ARGUMENT
            pass 
            self.mARGUMENT()



        elif alt7 == 3:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:25: ARGUMENTLIST
            pass 
            self.mARGUMENTLIST()



        elif alt7 == 4:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:38: ASKW
            pass 
            self.mASKW()



        elif alt7 == 5:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:43: ATKW
            pass 
            self.mATKW()



        elif alt7 == 6:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:48: BYKW
            pass 
            self.mBYKW()



        elif alt7 == 7:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:53: CATCHESKW
            pass 
            self.mCATCHESKW()



        elif alt7 == 8:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:63: CHOICEKW
            pass 
            self.mCHOICEKW()



        elif alt7 == 9:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:72: CONTINUEKW
            pass 
            self.mCONTINUEKW()



        elif alt7 == 10:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:83: DOKW
            pass 
            self.mDOKW()



        elif alt7 == 11:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:88: EMPTY_ANNOTATION
            pass 
            self.mEMPTY_ANNOTATION()



        elif alt7 == 12:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:105: EMPTY_ARGUMENT_LIST
            pass 
            self.mEMPTY_ARGUMENT_LIST()



        elif alt7 == 13:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:125: EMPTY_LOCAL_CATCHES
            pass 
            self.mEMPTY_LOCAL_CATCHES()



        elif alt7 == 14:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:145: EMPTY_LOCAL_THROW
            pass 
            self.mEMPTY_LOCAL_THROW()



        elif alt7 == 15:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:163: EMPTY_MESSAGE_OP
            pass 
            self.mEMPTY_MESSAGE_OP()



        elif alt7 == 16:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:180: EMPTY_MODULE_NAME
            pass 
            self.mEMPTY_MODULE_NAME()



        elif alt7 == 17:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:198: EMPTY_PARAMETER_DECL_LIST
            pass 
            self.mEMPTY_PARAMETER_DECL_LIST()



        elif alt7 == 18:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:224: EMPTY_SCOPE_NAME
            pass 
            self.mEMPTY_SCOPE_NAME()



        elif alt7 == 19:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:241: FROMKW
            pass 
            self.mFROMKW()



        elif alt7 == 20:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:248: GLOBALCHOICE
            pass 
            self.mGLOBALCHOICE()



        elif alt7 == 21:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:261: GLOBALCONTINUE
            pass 
            self.mGLOBALCONTINUE()



        elif alt7 == 22:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:276: GLOBALDO
            pass 
            self.mGLOBALDO()



        elif alt7 == 23:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:285: GLOBALINTERACTIONSEQUENCE
            pass 
            self.mGLOBALINTERACTIONSEQUENCE()



        elif alt7 == 24:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:311: GLOBALINTERRUPT
            pass 
            self.mGLOBALINTERRUPT()



        elif alt7 == 25:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:327: GLOBALINTERRUPTIBLE
            pass 
            self.mGLOBALINTERRUPTIBLE()



        elif alt7 == 26:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:347: GLOBALKW
            pass 
            self.mGLOBALKW()



        elif alt7 == 27:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:356: GLOBALMESSAGETRANSFER
            pass 
            self.mGLOBALMESSAGETRANSFER()



        elif alt7 == 28:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:378: GLOBALPARALLEL
            pass 
            self.mGLOBALPARALLEL()



        elif alt7 == 29:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:393: GLOBALPROTOCOLBLOCK
            pass 
            self.mGLOBALPROTOCOLBLOCK()



        elif alt7 == 30:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:413: GLOBALPROTOCOLDECL
            pass 
            self.mGLOBALPROTOCOLDECL()



        elif alt7 == 31:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:432: GLOBALPROTOCOLDEF
            pass 
            self.mGLOBALPROTOCOLDEF()



        elif alt7 == 32:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:450: GLOBALPROTOCOLINSTANCE
            pass 
            self.mGLOBALPROTOCOLINSTANCE()



        elif alt7 == 33:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:473: GLOBALRECURSION
            pass 
            self.mGLOBALRECURSION()



        elif alt7 == 34:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:489: IMPORTKW
            pass 
            self.mIMPORTKW()



        elif alt7 == 35:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:498: IMPORTMEMBER
            pass 
            self.mIMPORTMEMBER()



        elif alt7 == 36:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:511: IMPORTMODULE
            pass 
            self.mIMPORTMODULE()



        elif alt7 == 37:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:524: INSTANTIATESKW
            pass 
            self.mINSTANTIATESKW()



        elif alt7 == 38:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:539: INTERRUPTIBLEKW
            pass 
            self.mINTERRUPTIBLEKW()



        elif alt7 == 39:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:555: KIND_MESSAGE_SIGNATURE
            pass 
            self.mKIND_MESSAGE_SIGNATURE()



        elif alt7 == 40:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:578: KIND_PAYLOAD_TYPE
            pass 
            self.mKIND_PAYLOAD_TYPE()



        elif alt7 == 41:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:596: LOCALCATCH
            pass 
            self.mLOCALCATCH()



        elif alt7 == 42:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:607: LOCALCHOICE
            pass 
            self.mLOCALCHOICE()



        elif alt7 == 43:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:619: LOCALCONTINUE
            pass 
            self.mLOCALCONTINUE()



        elif alt7 == 44:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:633: LOCALDO
            pass 
            self.mLOCALDO()



        elif alt7 == 45:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:641: LOCALINTERACTIONSEQUENCE
            pass 
            self.mLOCALINTERACTIONSEQUENCE()



        elif alt7 == 46:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:666: LOCALINTERRUPT
            pass 
            self.mLOCALINTERRUPT()



        elif alt7 == 47:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:681: LOCALINTERRUPTIBLE
            pass 
            self.mLOCALINTERRUPTIBLE()



        elif alt7 == 48:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:700: LOCALKW
            pass 
            self.mLOCALKW()



        elif alt7 == 49:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:708: LOCALMESSAGETRANSFER
            pass 
            self.mLOCALMESSAGETRANSFER()



        elif alt7 == 50:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:729: LOCALPARALLEL
            pass 
            self.mLOCALPARALLEL()



        elif alt7 == 51:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:743: LOCALPROTOCOLBLOCK
            pass 
            self.mLOCALPROTOCOLBLOCK()



        elif alt7 == 52:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:762: LOCALPROTOCOLDECL
            pass 
            self.mLOCALPROTOCOLDECL()



        elif alt7 == 53:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:780: LOCALPROTOCOLDEF
            pass 
            self.mLOCALPROTOCOLDEF()



        elif alt7 == 54:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:797: LOCALPROTOCOLINSTANCE
            pass 
            self.mLOCALPROTOCOLINSTANCE()



        elif alt7 == 55:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:819: LOCALRECEIVE
            pass 
            self.mLOCALRECEIVE()



        elif alt7 == 56:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:832: LOCALRECURSION
            pass 
            self.mLOCALRECURSION()



        elif alt7 == 57:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:847: LOCALSEND
            pass 
            self.mLOCALSEND()



        elif alt7 == 58:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:857: LOCALTHROW
            pass 
            self.mLOCALTHROW()



        elif alt7 == 59:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:868: MESSAGESIGNATURE
            pass 
            self.mMESSAGESIGNATURE()



        elif alt7 == 60:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:885: MODULE
            pass 
            self.mMODULE()



        elif alt7 == 61:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:892: MODULEDECL
            pass 
            self.mMODULEDECL()



        elif alt7 == 62:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:903: MODULEKW
            pass 
            self.mMODULEKW()



        elif alt7 == 63:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:912: ORKW
            pass 
            self.mORKW()



        elif alt7 == 64:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:917: PARAMETERDECL
            pass 
            self.mPARAMETERDECL()



        elif alt7 == 65:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:931: PARAMETERDECLLIST
            pass 
            self.mPARAMETERDECLLIST()



        elif alt7 == 66:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:949: PARKW
            pass 
            self.mPARKW()



        elif alt7 == 67:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:955: PAYLOAD
            pass 
            self.mPAYLOAD()



        elif alt7 == 68:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:963: PAYLOADELEMENT
            pass 
            self.mPAYLOADELEMENT()



        elif alt7 == 69:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:978: PAYLOADTYPEDECL
            pass 
            self.mPAYLOADTYPEDECL()



        elif alt7 == 70:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:994: PROTOCOLKW
            pass 
            self.mPROTOCOLKW()



        elif alt7 == 71:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1005: RECKW
            pass 
            self.mRECKW()



        elif alt7 == 72:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1011: ROLEDECL
            pass 
            self.mROLEDECL()



        elif alt7 == 73:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1020: ROLEDECLLIST
            pass 
            self.mROLEDECLLIST()



        elif alt7 == 74:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1033: ROLEINSTANTIATION
            pass 
            self.mROLEINSTANTIATION()



        elif alt7 == 75:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1051: ROLEINSTANTIATIONLIST
            pass 
            self.mROLEINSTANTIATIONLIST()



        elif alt7 == 76:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1073: ROLEKW
            pass 
            self.mROLEKW()



        elif alt7 == 77:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1080: SIGKW
            pass 
            self.mSIGKW()



        elif alt7 == 78:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1086: THROWSKW
            pass 
            self.mTHROWSKW()



        elif alt7 == 79:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1095: TOKW
            pass 
            self.mTOKW()



        elif alt7 == 80:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1100: TYPEKW
            pass 
            self.mTYPEKW()



        elif alt7 == 81:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1107: WITHKW
            pass 
            self.mWITHKW()



        elif alt7 == 82:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1114: T__94
            pass 
            self.mT__94()



        elif alt7 == 83:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1120: T__95
            pass 
            self.mT__95()



        elif alt7 == 84:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1126: T__96
            pass 
            self.mT__96()



        elif alt7 == 85:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1132: T__97
            pass 
            self.mT__97()



        elif alt7 == 86:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1138: T__98
            pass 
            self.mT__98()



        elif alt7 == 87:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1144: T__99
            pass 
            self.mT__99()



        elif alt7 == 88:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1150: T__100
            pass 
            self.mT__100()



        elif alt7 == 89:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1157: T__101
            pass 
            self.mT__101()



        elif alt7 == 90:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1164: T__102
            pass 
            self.mT__102()



        elif alt7 == 91:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1171: T__103
            pass 
            self.mT__103()



        elif alt7 == 92:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1178: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt7 == 93:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1189: COMMENT
            pass 
            self.mCOMMENT()



        elif alt7 == 94:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1197: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()



        elif alt7 == 95:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1210: IDENTIFIER
            pass 
            self.mIDENTIFIER()



        elif alt7 == 96:
            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:1:1221: EXTIDENTIFIER
            pass 
            self.mEXTIDENTIFIER()








    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        "\1\uffff\21\36\16\uffff\2\36\1\100\1\101\1\102\3\36\1\106\11\36"
        "\1\121\6\36\1\131\2\36\2\uffff\1\134\1\36\3\uffff\3\36\1\uffff\12"
        "\36\1\uffff\1\154\2\36\1\157\1\36\1\161\1\36\1\uffff\2\36\1\uffff"
        "\5\36\1\172\11\36\1\uffff\2\36\1\uffff\1\u0087\1\uffff\1\36\1\u0089"
        "\1\u008a\5\36\1\uffff\5\36\1\u0097\1\36\1\u009a\3\36\2\uffff\1\36"
        "\2\uffff\2\36\1\u00a3\2\36\1\u00a7\1\u00a9\4\36\2\uffff\1\36\1\u00b8"
        "\1\uffff\3\36\2\uffff\1\u00be\1\36\1\u00c0\1\uffff\2\36\4\uffff"
        "\4\36\10\uffff\1\36\2\uffff\1\36\1\u00d9\1\36\3\uffff\1\u00de\1"
        "\uffff\1\u00df\1\36\7\uffff\4\36\10\uffff\2\36\2\uffff\1\u00f5\5"
        "\uffff\5\36\7\uffff\4\36\3\uffff\2\36\1\uffff\1\u010c\1\uffff\7"
        "\36\2\uffff\4\36\5\uffff\1\36\3\uffff\7\36\2\uffff\4\36\3\uffff"
        "\1\36\1\uffff\7\36\2\uffff\1\u013d\3\36\4\uffff\1\36\1\uffff\7\36"
        "\4\uffff\1\u014f\2\36\3\uffff\1\36\1\uffff\7\36\3\uffff\2\36\2\uffff"
        "\1\u0166\1\u0167\1\uffff\10\36\2\uffff\2\36\1\u0176\5\uffff\10\36"
        "\1\u0184\1\uffff\2\36\6\uffff\10\36\5\uffff\1\36\1\u0196\2\uffff"
        "\1\u019a\3\36\1\u019e\2\36\1\u01a1\1\uffff\1\36\3\uffff\1\u01a6"
        "\1\uffff\1\36\1\u01a8\1\u01a9\1\uffff\1\u01aa\1\36\3\uffff\1\36"
        "\2\uffff\1\36\3\uffff\2\36\1\u01b0\2\36\1\uffff\1\36\1\u01b4\1\36"
        "\1\uffff\3\36\1\u01b9\1\uffff"
        )

    DFA7_eof = DFA.unpack(
        "\u01ba\uffff"
        )

    DFA7_min = DFA.unpack(
        "\1\11\1\156\1\171\1\141\1\157\1\137\1\162\1\154\1\155\1\111\1\157"
        "\1\145\1\162\1\141\1\145\1\151\1\150\1\151\13\uffff\1\52\2\uffff"
        "\1\144\1\147\3\60\1\164\1\157\1\156\1\60\1\145\2\157\1\160\1\163"
        "\1\116\1\143\1\163\1\144\1\60\1\162\1\157\1\143\1\154\1\147\1\162"
        "\1\60\1\160\1\164\2\uffff\1\60\1\165\3\uffff\1\143\1\151\1\164\1"
        "\uffff\2\155\1\142\1\157\1\164\1\145\1\104\1\141\1\163\1\165\1\uffff"
        "\1\60\1\154\1\164\1\60\1\145\1\60\1\157\1\uffff\1\145\1\150\1\uffff"
        "\1\155\1\150\1\143\1\151\1\160\1\60\1\141\1\162\1\141\1\162\1\137"
        "\1\154\1\141\1\154\1\155\1\uffff\2\157\1\uffff\1\55\1\uffff\1\167"
        "\2\60\3\145\1\156\1\164\1\uffff\1\154\1\164\1\156\1\162\1\115\1"
        "\55\1\147\1\60\1\145\1\141\1\143\1\144\1\uffff\1\163\2\uffff\1\156"
        "\1\163\1\60\1\165\1\171\2\55\1\164\1\165\1\105\1\101\1\143\1\uffff"
        "\1\145\1\55\1\uffff\1\164\1\144\1\157\1\145\1\156\1\60\1\164\1\60"
        "\1\uffff\1\145\1\137\1\143\1\uffff\1\155\1\uffff\1\151\1\160\1\123"
        "\1\131\1\141\1\uffff\1\156\1\uffff\1\141\1\145\2\uffff\1\55\2\uffff"
        "\1\145\1\55\1\154\1\143\1\163\1\uffff\1\55\1\uffff\1\60\1\141\1"
        "\150\1\uffff\1\156\1\uffff\1\141\1\uffff\1\145\1\141\1\164\1\123"
        "\1\114\3\uffff\1\164\1\uffff\1\157\1\143\1\uffff\1\162\1\154\2\uffff"
        "\1\60\1\154\1\164\3\uffff\1\156\1\157\1\145\1\141\1\143\2\uffff"
        "\1\164\1\uffff\1\157\2\uffff\1\164\1\151\1\101\1\117\1\145\1\164"
        "\1\145\1\55\1\145\1\uffff\1\55\1\141\1\156\1\147\1\143\1\163\1\144"
        "\1\162\1\157\1\145\1\164\1\145\1\142\1\107\1\101\1\162\1\157\2\uffff"
        "\1\144\1\155\2\uffff\1\156\1\157\1\165\1\141\1\163\1\165\1\141\1"
        "\160\1\162\1\157\1\163\1\154\1\105\1\104\1\141\1\143\2\145\2\164"
        "\1\155\1\154\1\141\1\154\1\155\1\145\1\141\1\143\1\60\1\145\2\137"
        "\1\uffff\1\165\1\157\1\143\1\156\1\151\1\141\1\145\1\137\1\147\2"
        "\145\1\137\1\uffff\1\165\1\157\1\uffff\1\60\1\123\1\124\1\160\2"
        "\154\1\164\1\141\1\164\1\156\1\143\1\145\1\137\1\164\1\156\1\160"
        "\1\154\1\uffff\1\111\1\131\1\164\2\55\1\60\1\164\1\151\1\164\1\141"
        "\1\150\1\137\1\156\1\145\1\141\1\164\1\55\1\107\1\120\1\151\1\142"
        "\3\uffff\1\151\1\157\1\137\1\164\1\162\1\157\1\141\1\162\1\155\1"
        "\151\1\142\1\116\1\105\3\uffff\1\145\1\uffff\1\157\1\156\1\154\1"
        "\143\1\157\1\160\1\155\1\137\1\145\3\uffff\1\145\1\uffff\1\101\1"
        "\60\1\143\1\156\1\60\1\151\1\150\1\167\1\60\1\145\1\144\1\60\1\143"
        "\1\124\3\uffff\1\55\1\uffff\1\163\2\60\1\uffff\1\60\1\145\3\uffff"
        "\1\125\2\uffff\1\164\3\uffff\1\143\1\122\1\60\1\154\1\105\1\uffff"
        "\1\137\1\60\1\154\1\uffff\1\151\1\163\1\164\1\60\1\uffff"
        )

    DFA7_max = DFA.unpack(
        "\1\175\1\164\1\171\2\157\1\137\1\162\1\154\1\156\1\111\2\157\2\162"
        "\1\157\1\151\1\171\1\151\13\uffff\1\57\2\uffff\1\144\1\147\3\172"
        "\1\164\1\157\1\156\1\172\1\145\2\157\1\160\1\164\1\116\1\143\1\163"
        "\1\144\1\172\1\171\1\157\1\143\1\154\1\147\1\162\1\172\1\160\1\164"
        "\2\uffff\1\172\1\165\3\uffff\1\143\1\151\1\164\1\uffff\2\155\1\142"
        "\1\157\1\164\1\145\1\104\1\141\1\163\1\165\1\uffff\1\172\1\154\1"
        "\164\1\172\1\145\1\172\1\157\1\uffff\1\145\1\150\1\uffff\1\155\1"
        "\150\1\143\1\151\1\160\1\172\1\141\1\162\1\141\1\162\1\137\1\154"
        "\1\141\1\154\1\155\1\uffff\2\157\1\uffff\1\172\1\uffff\1\167\2\172"
        "\3\145\1\156\1\164\1\uffff\1\154\1\164\1\156\1\162\1\120\1\172\1"
        "\147\1\172\1\145\1\141\1\143\1\151\1\uffff\1\163\2\uffff\1\156\1"
        "\163\1\172\1\165\1\171\2\172\1\164\1\165\1\105\1\101\1\164\1\uffff"
        "\1\145\1\172\1\uffff\1\164\1\144\1\157\1\145\1\156\1\172\1\164\1"
        "\172\1\uffff\1\145\1\137\1\162\1\uffff\1\155\1\uffff\1\151\1\160"
        "\1\123\1\131\1\157\1\uffff\1\156\1\uffff\1\162\1\145\2\uffff\1\55"
        "\2\uffff\1\145\1\172\1\154\1\143\1\163\1\uffff\1\172\1\uffff\1\172"
        "\1\163\1\157\1\uffff\1\156\1\uffff\1\162\1\uffff\1\157\1\141\1\164"
        "\1\123\1\114\3\uffff\1\164\1\uffff\1\157\1\143\1\uffff\1\162\1\154"
        "\2\uffff\1\172\1\154\1\164\3\uffff\1\162\2\157\1\141\1\143\2\uffff"
        "\1\164\1\uffff\1\157\2\uffff\1\164\1\151\1\101\1\117\1\145\1\164"
        "\1\165\1\55\1\145\1\uffff\1\55\1\141\1\156\1\147\1\143\1\163\1\144"
        "\1\162\1\157\1\145\1\164\1\145\1\142\1\107\1\101\1\162\1\157\2\uffff"
        "\1\144\1\155\2\uffff\1\156\1\157\1\165\1\141\1\163\1\165\1\141\1"
        "\160\1\162\1\157\1\163\1\154\1\105\1\104\1\162\1\143\2\145\2\164"
        "\1\155\1\154\1\141\1\154\1\155\1\145\1\162\1\143\1\172\1\145\2\137"
        "\1\uffff\1\165\1\157\1\143\1\156\1\151\1\141\1\145\1\137\1\147\2"
        "\145\1\137\1\uffff\1\165\1\157\1\uffff\1\172\1\123\1\124\1\160\2"
        "\154\1\164\1\141\1\164\1\156\1\164\1\145\1\137\1\164\1\156\1\160"
        "\1\154\1\uffff\1\111\1\131\1\164\2\55\1\172\1\164\1\151\1\164\1"
        "\141\1\150\1\137\1\156\1\145\1\141\1\164\1\55\1\107\1\120\2\151"
        "\3\uffff\1\151\1\157\1\137\1\164\1\162\1\157\1\141\1\162\1\155\2"
        "\151\1\116\1\105\3\uffff\1\145\1\uffff\1\157\1\156\1\154\1\143\1"
        "\157\1\160\1\155\1\137\1\145\3\uffff\1\145\1\uffff\1\101\1\172\1"
        "\146\1\156\1\172\1\151\1\150\1\167\1\172\1\145\1\144\1\172\1\146"
        "\1\124\3\uffff\1\55\1\uffff\1\163\2\172\1\uffff\1\172\1\145\3\uffff"
        "\1\125\2\uffff\1\164\3\uffff\1\143\1\122\1\172\1\154\1\105\1\uffff"
        "\1\137\1\172\1\154\1\uffff\1\151\1\163\1\164\1\172\1\uffff"
        )

    DFA7_accept = DFA.unpack(
        "\22\uffff\1\122\1\123\1\124\1\125\1\126\1\127\1\130\1\131\1\132"
        "\1\133\1\134\1\uffff\1\137\1\140\34\uffff\1\135\1\136\2\uffff\1"
        "\4\1\5\1\6\3\uffff\1\12\12\uffff\1\77\7\uffff\1\117\2\uffff\1\1"
        "\17\uffff\1\102\2\uffff\1\107\1\uffff\1\115\10\uffff\1\23\14\uffff"
        "\1\114\1\uffff\1\120\1\121\14\uffff\1\60\2\uffff\1\74\10\uffff\1"
        "\10\3\uffff\1\32\1\uffff\1\42\5\uffff\1\54\1\uffff\1\61\2\uffff"
        "\1\71\1\72\1\uffff\1\75\1\76\5\uffff\1\116\1\uffff\1\7\3\uffff\1"
        "\26\1\uffff\1\33\1\uffff\1\41\5\uffff\1\51\1\52\1\53\1\uffff\1\62"
        "\2\uffff\1\73\2\uffff\1\105\1\103\3\uffff\1\3\1\2\1\11\5\uffff\1"
        "\24\1\25\1\uffff\1\34\1\uffff\1\43\1\44\11\uffff\1\106\21\uffff"
        "\1\67\1\70\2\uffff\1\111\1\110\40\uffff\1\55\14\uffff\1\27\2\uffff"
        "\1\45\21\uffff\1\46\25\uffff\1\101\1\100\1\104\15\uffff\1\57\1\56"
        "\1\63\1\uffff\1\66\11\uffff\1\31\1\30\1\35\1\uffff\1\40\16\uffff"
        "\1\50\1\64\1\65\1\uffff\1\13\3\uffff\1\17\2\uffff\1\22\1\36\1\37"
        "\1\uffff\1\113\1\112\1\uffff\1\15\1\16\1\20\5\uffff\1\14\3\uffff"
        "\1\47\4\uffff\1\21"
        )

    DFA7_special = DFA.unpack(
        "\u01ba\uffff"
        )


    DFA7_transition = [
        DFA.unpack("\2\34\1\uffff\2\34\22\uffff\1\34\1\uffff\1\37\5\uffff"
        "\1\22\1\23\2\uffff\1\24\1\uffff\1\25\1\35\12\uffff\1\26\1\27\1\30"
        "\1\uffff\1\31\2\uffff\12\36\1\11\17\36\4\uffff\1\5\1\uffff\1\1\1"
        "\2\1\3\1\4\1\36\1\6\1\7\1\36\1\10\2\36\1\12\1\13\1\36\1\14\1\15"
        "\1\36\1\16\1\17\1\20\2\36\1\21\3\36\1\32\1\uffff\1\33"),
        DFA.unpack("\1\40\3\uffff\1\41\1\42\1\43"),
        DFA.unpack("\1\44"),
        DFA.unpack("\1\45\6\uffff\1\46\6\uffff\1\47"),
        DFA.unpack("\1\50"),
        DFA.unpack("\1\51"),
        DFA.unpack("\1\52"),
        DFA.unpack("\1\53"),
        DFA.unpack("\1\54\1\55"),
        DFA.unpack("\1\56"),
        DFA.unpack("\1\57"),
        DFA.unpack("\1\60\11\uffff\1\61"),
        DFA.unpack("\1\62"),
        DFA.unpack("\1\63\20\uffff\1\64"),
        DFA.unpack("\1\65\11\uffff\1\66"),
        DFA.unpack("\1\67"),
        DFA.unpack("\1\70\6\uffff\1\71\11\uffff\1\72"),
        DFA.unpack("\1\73"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\74\4\uffff\1\75"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\76"),
        DFA.unpack("\1\77"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\103"),
        DFA.unpack("\1\104"),
        DFA.unpack("\1\105"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\107"),
        DFA.unpack("\1\110"),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112"),
        DFA.unpack("\1\113\1\114"),
        DFA.unpack("\1\115"),
        DFA.unpack("\1\116"),
        DFA.unpack("\1\117"),
        DFA.unpack("\1\120"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\122\6\uffff\1\123"),
        DFA.unpack("\1\124"),
        DFA.unpack("\1\125"),
        DFA.unpack("\1\126"),
        DFA.unpack("\1\127"),
        DFA.unpack("\1\130"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\132"),
        DFA.unpack("\1\133"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\135"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\136"),
        DFA.unpack("\1\137"),
        DFA.unpack("\1\140"),
        DFA.unpack(""),
        DFA.unpack("\1\141"),
        DFA.unpack("\1\142"),
        DFA.unpack("\1\143"),
        DFA.unpack("\1\144"),
        DFA.unpack("\1\145"),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147"),
        DFA.unpack("\1\150"),
        DFA.unpack("\1\151"),
        DFA.unpack("\1\152"),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\1\153\31\36"),
        DFA.unpack("\1\155"),
        DFA.unpack("\1\156"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\160"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\162"),
        DFA.unpack(""),
        DFA.unpack("\1\163"),
        DFA.unpack("\1\164"),
        DFA.unpack(""),
        DFA.unpack("\1\165"),
        DFA.unpack("\1\166"),
        DFA.unpack("\1\167"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\171"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\1\177"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\u0081"),
        DFA.unpack("\1\u0082"),
        DFA.unpack("\1\u0083"),
        DFA.unpack(""),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\1\u0085"),
        DFA.unpack(""),
        DFA.unpack("\1\u0086\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36\1"
        "\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack("\1\u0088"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u008b"),
        DFA.unpack("\1\u008c"),
        DFA.unpack("\1\u008d"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\1\u008f"),
        DFA.unpack(""),
        DFA.unpack("\1\u0090"),
        DFA.unpack("\1\u0091"),
        DFA.unpack("\1\u0092"),
        DFA.unpack("\1\u0093"),
        DFA.unpack("\1\u0094\2\uffff\1\u0095"),
        DFA.unpack("\1\u0096\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36\1"
        "\uffff\32\36"),
        DFA.unpack("\1\u0098"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\4\36\1\u0099"
        "\25\36"),
        DFA.unpack("\1\u009b"),
        DFA.unpack("\1\u009c"),
        DFA.unpack("\1\u009d"),
        DFA.unpack("\1\u009e\4\uffff\1\u009f"),
        DFA.unpack(""),
        DFA.unpack("\1\u00a0"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00a1"),
        DFA.unpack("\1\u00a2"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u00a4"),
        DFA.unpack("\1\u00a5"),
        DFA.unpack("\1\u00a6\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36\1"
        "\uffff\32\36"),
        DFA.unpack("\1\u00a8\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36\1"
        "\uffff\32\36"),
        DFA.unpack("\1\u00aa"),
        DFA.unpack("\1\u00ab"),
        DFA.unpack("\1\u00ac"),
        DFA.unpack("\1\u00ad"),
        DFA.unpack("\1\u00ae\1\u00af\4\uffff\1\u00b0\3\uffff\1\u00b1\2\uffff"
        "\1\u00b2\1\uffff\1\u00b3\1\u00b4\1\u00b5"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b6"),
        DFA.unpack("\1\u00b7\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36\1"
        "\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b9"),
        DFA.unpack("\1\u00ba"),
        DFA.unpack("\1\u00bb"),
        DFA.unpack("\1\u00bc"),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u00bf"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c1"),
        DFA.unpack("\1\u00c2"),
        DFA.unpack("\1\u00c3\1\u00c4\4\uffff\1\u00c5\3\uffff\1\u00c6\2\uffff"
        "\1\u00c7\1\uffff\1\u00c8"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c9"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ca"),
        DFA.unpack("\1\u00cb"),
        DFA.unpack("\1\u00cc"),
        DFA.unpack("\1\u00cd"),
        DFA.unpack("\1\u00ce\6\uffff\1\u00cf\6\uffff\1\u00d0"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d1"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d2\20\uffff\1\u00d3"),
        DFA.unpack("\1\u00d4"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00d5"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00d6"),
        DFA.unpack("\1\u00d8\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36\1"
        "\uffff\4\36\1\u00d7\25\36"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\1\u00dc"),
        DFA.unpack(""),
        DFA.unpack("\1\u00dd\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36\1"
        "\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u00e0\12\uffff\1\u00e1\1\u00e2\2\uffff\1\u00e3\2"
        "\uffff\1\u00e4"),
        DFA.unpack("\1\u00e5\6\uffff\1\u00e6"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e7"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e8\20\uffff\1\u00e9"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ea\11\uffff\1\u00eb"),
        DFA.unpack("\1\u00ec"),
        DFA.unpack("\1\u00ed"),
        DFA.unpack("\1\u00ee"),
        DFA.unpack("\1\u00ef"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f0"),
        DFA.unpack(""),
        DFA.unpack("\1\u00f1"),
        DFA.unpack("\1\u00f2"),
        DFA.unpack(""),
        DFA.unpack("\1\u00f3"),
        DFA.unpack("\1\u00f4"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u00f6"),
        DFA.unpack("\1\u00f7"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f8\3\uffff\1\u00f9"),
        DFA.unpack("\1\u00fa"),
        DFA.unpack("\1\u00fb\11\uffff\1\u00fc"),
        DFA.unpack("\1\u00fd"),
        DFA.unpack("\1\u00fe"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00ff"),
        DFA.unpack(""),
        DFA.unpack("\1\u0100"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0101"),
        DFA.unpack("\1\u0102"),
        DFA.unpack("\1\u0103"),
        DFA.unpack("\1\u0104"),
        DFA.unpack("\1\u0105"),
        DFA.unpack("\1\u0106"),
        DFA.unpack("\1\u0107\17\uffff\1\u0108"),
        DFA.unpack("\1\u0109"),
        DFA.unpack("\1\u010a"),
        DFA.unpack(""),
        DFA.unpack("\1\u010b"),
        DFA.unpack("\1\u010d"),
        DFA.unpack("\1\u010e"),
        DFA.unpack("\1\u010f"),
        DFA.unpack("\1\u0110"),
        DFA.unpack("\1\u0111"),
        DFA.unpack("\1\u0112"),
        DFA.unpack("\1\u0113"),
        DFA.unpack("\1\u0114"),
        DFA.unpack("\1\u0115"),
        DFA.unpack("\1\u0116"),
        DFA.unpack("\1\u0117"),
        DFA.unpack("\1\u0118"),
        DFA.unpack("\1\u0119"),
        DFA.unpack("\1\u011a"),
        DFA.unpack("\1\u011b"),
        DFA.unpack("\1\u011c"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u011d"),
        DFA.unpack("\1\u011e"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u011f"),
        DFA.unpack("\1\u0120"),
        DFA.unpack("\1\u0121"),
        DFA.unpack("\1\u0122"),
        DFA.unpack("\1\u0123"),
        DFA.unpack("\1\u0124"),
        DFA.unpack("\1\u0125"),
        DFA.unpack("\1\u0126"),
        DFA.unpack("\1\u0127"),
        DFA.unpack("\1\u0128"),
        DFA.unpack("\1\u0129"),
        DFA.unpack("\1\u012a"),
        DFA.unpack("\1\u012b"),
        DFA.unpack("\1\u012c"),
        DFA.unpack("\1\u012d\20\uffff\1\u012e"),
        DFA.unpack("\1\u012f"),
        DFA.unpack("\1\u0130"),
        DFA.unpack("\1\u0131"),
        DFA.unpack("\1\u0132"),
        DFA.unpack("\1\u0133"),
        DFA.unpack("\1\u0134"),
        DFA.unpack("\1\u0135"),
        DFA.unpack("\1\u0136"),
        DFA.unpack("\1\u0137"),
        DFA.unpack("\1\u0138"),
        DFA.unpack("\1\u0139"),
        DFA.unpack("\1\u013a\20\uffff\1\u013b"),
        DFA.unpack("\1\u013c"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u013e"),
        DFA.unpack("\1\u013f"),
        DFA.unpack("\1\u0140"),
        DFA.unpack(""),
        DFA.unpack("\1\u0141"),
        DFA.unpack("\1\u0142"),
        DFA.unpack("\1\u0143"),
        DFA.unpack("\1\u0144"),
        DFA.unpack("\1\u0145"),
        DFA.unpack("\1\u0146"),
        DFA.unpack("\1\u0147"),
        DFA.unpack("\1\u0148"),
        DFA.unpack("\1\u0149"),
        DFA.unpack("\1\u014a"),
        DFA.unpack("\1\u014b"),
        DFA.unpack("\1\u014c"),
        DFA.unpack(""),
        DFA.unpack("\1\u014d"),
        DFA.unpack("\1\u014e"),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u0150"),
        DFA.unpack("\1\u0151"),
        DFA.unpack("\1\u0152"),
        DFA.unpack("\1\u0153"),
        DFA.unpack("\1\u0154"),
        DFA.unpack("\1\u0155"),
        DFA.unpack("\1\u0156"),
        DFA.unpack("\1\u0157"),
        DFA.unpack("\1\u0158"),
        DFA.unpack("\1\u0159\20\uffff\1\u015a"),
        DFA.unpack("\1\u015b"),
        DFA.unpack("\1\u015c"),
        DFA.unpack("\1\u015d"),
        DFA.unpack("\1\u015e"),
        DFA.unpack("\1\u015f"),
        DFA.unpack("\1\u0160"),
        DFA.unpack(""),
        DFA.unpack("\1\u0161"),
        DFA.unpack("\1\u0162"),
        DFA.unpack("\1\u0163"),
        DFA.unpack("\1\u0164"),
        DFA.unpack("\1\u0165"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u0168"),
        DFA.unpack("\1\u0169"),
        DFA.unpack("\1\u016a"),
        DFA.unpack("\1\u016b"),
        DFA.unpack("\1\u016c"),
        DFA.unpack("\1\u016d"),
        DFA.unpack("\1\u016e"),
        DFA.unpack("\1\u016f"),
        DFA.unpack("\1\u0170"),
        DFA.unpack("\1\u0171"),
        DFA.unpack("\1\u0172"),
        DFA.unpack("\1\u0173"),
        DFA.unpack("\1\u0174"),
        DFA.unpack("\1\u0175"),
        DFA.unpack("\1\u0177\1\uffff\1\u0178\4\uffff\1\u0179"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u017a"),
        DFA.unpack("\1\u017b"),
        DFA.unpack("\1\u017c"),
        DFA.unpack("\1\u017d"),
        DFA.unpack("\1\u017e"),
        DFA.unpack("\1\u017f"),
        DFA.unpack("\1\u0180"),
        DFA.unpack("\1\u0181"),
        DFA.unpack("\1\u0182"),
        DFA.unpack("\1\u0183"),
        DFA.unpack("\1\u0185\1\uffff\1\u0186\4\uffff\1\u0187"),
        DFA.unpack("\1\u0188"),
        DFA.unpack("\1\u0189"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u018a"),
        DFA.unpack(""),
        DFA.unpack("\1\u018b"),
        DFA.unpack("\1\u018c"),
        DFA.unpack("\1\u018d"),
        DFA.unpack("\1\u018e"),
        DFA.unpack("\1\u018f"),
        DFA.unpack("\1\u0190"),
        DFA.unpack("\1\u0191"),
        DFA.unpack("\1\u0192"),
        DFA.unpack("\1\u0193"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0194"),
        DFA.unpack(""),
        DFA.unpack("\1\u0195"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u0197\2\uffff\1\u0198"),
        DFA.unpack("\1\u0199"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u019b"),
        DFA.unpack("\1\u019c"),
        DFA.unpack("\1\u019d"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u019f"),
        DFA.unpack("\1\u01a0"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u01a2\2\uffff\1\u01a3"),
        DFA.unpack("\1\u01a4"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01a5"),
        DFA.unpack(""),
        DFA.unpack("\1\u01a7"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u01ab"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01ac"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01ad"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01ae"),
        DFA.unpack("\1\u01af"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u01b1"),
        DFA.unpack("\1\u01b2"),
        DFA.unpack(""),
        DFA.unpack("\1\u01b3"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u01b5"),
        DFA.unpack(""),
        DFA.unpack("\1\u01b6"),
        DFA.unpack("\1\u01b7"),
        DFA.unpack("\1\u01b8"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(ScribbleLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
