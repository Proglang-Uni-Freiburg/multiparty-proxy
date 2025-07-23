# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g 2025-07-20 16:22:21

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
LOCALKW=9
ASKW=13
TOKW=15
UNDERSCORE=89
LOCALSEND=73
MODULEDECL=30
ROLEKW=10
LOCALRECEIVE=74
GLOBALPROTOCOLDECL=45
GLOBALKW=8
WITHKW=24
WHITESPACE=85
DOKW=28
BYKW=25
GLOBALMESSAGETRANSFER=50
LOCALINTERRUPTIBLE=68
PARKW=21
GLOBALPROTOCOLBLOCK=48
KIND_MESSAGE_SIGNATURE=83
GLOBALDO=57
LOCALINTERACTIONSEQUENCE=62
LINE_COMMENT=87
SYMBOL=92
GLOBALPARALLEL=54
EMPTY_MODULE_NAME=79
EMPTY_ARGUMENT_LIST=78
MESSAGESIGNATURE=36
TYPEKW=6
COMMENT=86
LOCALPARALLEL=67
GLOBALPROTOCOLINSTANCE=47
ARGUMENT=40
EMPTY_LOCAL_CATCHES=82
IMPORTMODULE=31
LOCALPROTOCOLINSTANCE=60
GLOBALINTERRUPTIBLE=55
GLOBALCHOICE=51
THROWSKW=26
PAYLOADELEMENT=42
SIGKW=11
CHOICEKW=16
LOCALRECURSION=65
INSTANTIATESKW=12
MODULEKW=4
RECKW=19
T__100=100
ROLEDECLLIST=37
T__102=102
LETTER=88
T__94=94
T__101=101
INTERRUPTIBLEKW=23
PAYLOAD=41
EMPTY_SCOPE_NAME=80
FROMKW=14
PROTOCOLKW=7
LOCALCONTINUE=66
PARAMETERDECL=35
EMPTY_LOCAL_THROW=81
T__99=99
PARAMETERDECLLIST=34
LOCALTHROW=71
T__95=95
T__96=96
T__97=97
GLOBALRECURSION=52
T__98=98
ROLEINSTANTIATION=44
IMPORTKW=5
ORKW=18
GLOBALINTERACTIONSEQUENCE=49
MODULE=29
GLOBALCONTINUE=53
EXTIDENTIFIER=93
CATCHESKW=27
PAYLOADTYPEDECL=33
KIND_PAYLOAD_TYPE=84
ROLEINSTANTIATIONLIST=43
ATKW=17
ARGUMENTLIST=39
LOCALCHOICE=64
LOCALPROTOCOLDEF=59
LOCALMESSAGETRANSFER=63
CONTINUEKW=20
ANDKW=22
IDENTIFIER=91
EOF=-1
LOCALPROTOCOLDECL=58
GLOBALINTERRUPT=56
LOCALPROTOCOLBLOCK=61
LOCALDO=70
GLOBALPROTOCOLDEF=46
EMPTY_PARAMETER_DECL_LIST=77
ROLEDECL=38
EMPTY_MESSAGE_OP=75
DIGIT=90
LOCALINTERRUPT=69
EMPTY_ANNOTATION=76
IMPORTMEMBER=32
T__103=103
LOCALCATCH=72


class ScribbleLexer(Lexer):

    grammarFileName = "C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(ScribbleLexer, self).__init__(input, state)


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






    # $ANTLR start "MODULEKW"
    def mMODULEKW(self, ):

        try:
            _type = MODULEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:7:10: ( 'module' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:7:12: 'module'
            pass 
            self.match("module")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MODULEKW"



    # $ANTLR start "IMPORTKW"
    def mIMPORTKW(self, ):

        try:
            _type = IMPORTKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:8:10: ( 'import' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:8:12: 'import'
            pass 
            self.match("import")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IMPORTKW"



    # $ANTLR start "TYPEKW"
    def mTYPEKW(self, ):

        try:
            _type = TYPEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:9:8: ( 'type' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:9:10: 'type'
            pass 
            self.match("type")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TYPEKW"



    # $ANTLR start "PROTOCOLKW"
    def mPROTOCOLKW(self, ):

        try:
            _type = PROTOCOLKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:10:12: ( 'protocol' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:10:14: 'protocol'
            pass 
            self.match("protocol")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROTOCOLKW"



    # $ANTLR start "GLOBALKW"
    def mGLOBALKW(self, ):

        try:
            _type = GLOBALKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:11:10: ( 'global' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:11:12: 'global'
            pass 
            self.match("global")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALKW"



    # $ANTLR start "LOCALKW"
    def mLOCALKW(self, ):

        try:
            _type = LOCALKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:12:9: ( 'local' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:12:11: 'local'
            pass 
            self.match("local")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALKW"



    # $ANTLR start "ROLEKW"
    def mROLEKW(self, ):

        try:
            _type = ROLEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:13:8: ( 'role' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:13:10: 'role'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:14:7: ( 'sig' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:14:9: 'sig'
            pass 
            self.match("sig")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SIGKW"



    # $ANTLR start "INSTANTIATESKW"
    def mINSTANTIATESKW(self, ):

        try:
            _type = INSTANTIATESKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:15:16: ( 'instantiates' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:15:18: 'instantiates'
            pass 
            self.match("instantiates")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INSTANTIATESKW"



    # $ANTLR start "ASKW"
    def mASKW(self, ):

        try:
            _type = ASKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:16:6: ( 'as' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:16:8: 'as'
            pass 
            self.match("as")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASKW"



    # $ANTLR start "FROMKW"
    def mFROMKW(self, ):

        try:
            _type = FROMKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:17:8: ( 'from' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:17:10: 'from'
            pass 
            self.match("from")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FROMKW"



    # $ANTLR start "TOKW"
    def mTOKW(self, ):

        try:
            _type = TOKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:18:6: ( 'to' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:18:8: 'to'
            pass 
            self.match("to")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TOKW"



    # $ANTLR start "CHOICEKW"
    def mCHOICEKW(self, ):

        try:
            _type = CHOICEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:19:10: ( 'choice' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:19:12: 'choice'
            pass 
            self.match("choice")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CHOICEKW"



    # $ANTLR start "ATKW"
    def mATKW(self, ):

        try:
            _type = ATKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:20:6: ( 'at' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:20:8: 'at'
            pass 
            self.match("at")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ATKW"



    # $ANTLR start "ORKW"
    def mORKW(self, ):

        try:
            _type = ORKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:21:6: ( 'or' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:21:8: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ORKW"



    # $ANTLR start "RECKW"
    def mRECKW(self, ):

        try:
            _type = RECKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:22:7: ( 'rec' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:22:9: 'rec'
            pass 
            self.match("rec")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RECKW"



    # $ANTLR start "CONTINUEKW"
    def mCONTINUEKW(self, ):

        try:
            _type = CONTINUEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:23:12: ( 'continue' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:23:14: 'continue'
            pass 
            self.match("continue")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONTINUEKW"



    # $ANTLR start "PARKW"
    def mPARKW(self, ):

        try:
            _type = PARKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:24:7: ( 'par' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:24:9: 'par'
            pass 
            self.match("par")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PARKW"



    # $ANTLR start "ANDKW"
    def mANDKW(self, ):

        try:
            _type = ANDKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:25:7: ( 'and' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:25:9: 'and'
            pass 
            self.match("and")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ANDKW"



    # $ANTLR start "INTERRUPTIBLEKW"
    def mINTERRUPTIBLEKW(self, ):

        try:
            _type = INTERRUPTIBLEKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:26:17: ( 'interruptible' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:26:19: 'interruptible'
            pass 
            self.match("interruptible")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTERRUPTIBLEKW"



    # $ANTLR start "WITHKW"
    def mWITHKW(self, ):

        try:
            _type = WITHKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:27:8: ( 'with' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:27:10: 'with'
            pass 
            self.match("with")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WITHKW"



    # $ANTLR start "BYKW"
    def mBYKW(self, ):

        try:
            _type = BYKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:28:6: ( 'by' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:28:8: 'by'
            pass 
            self.match("by")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BYKW"



    # $ANTLR start "THROWSKW"
    def mTHROWSKW(self, ):

        try:
            _type = THROWSKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:29:10: ( 'throws' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:29:12: 'throws'
            pass 
            self.match("throws")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THROWSKW"



    # $ANTLR start "CATCHESKW"
    def mCATCHESKW(self, ):

        try:
            _type = CATCHESKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:30:11: ( 'catches' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:30:13: 'catches'
            pass 
            self.match("catches")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CATCHESKW"



    # $ANTLR start "DOKW"
    def mDOKW(self, ):

        try:
            _type = DOKW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:31:6: ( 'do' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:31:8: 'do'
            pass 
            self.match("do")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOKW"



    # $ANTLR start "MODULE"
    def mMODULE(self, ):

        try:
            _type = MODULE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:32:8: ( 'modul' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:32:10: 'modul'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:33:12: ( 'module-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:33:14: 'module-decl'
            pass 
            self.match("module-decl")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MODULEDECL"



    # $ANTLR start "IMPORTMODULE"
    def mIMPORTMODULE(self, ):

        try:
            _type = IMPORTMODULE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:34:14: ( 'import-module' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:34:16: 'import-module'
            pass 
            self.match("import-module")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IMPORTMODULE"



    # $ANTLR start "IMPORTMEMBER"
    def mIMPORTMEMBER(self, ):

        try:
            _type = IMPORTMEMBER
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:35:14: ( 'import-member' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:35:16: 'import-member'
            pass 
            self.match("import-member")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IMPORTMEMBER"



    # $ANTLR start "PAYLOADTYPEDECL"
    def mPAYLOADTYPEDECL(self, ):

        try:
            _type = PAYLOADTYPEDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:36:17: ( 'payload-type-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:36:19: 'payload-type-decl'
            pass 
            self.match("payload-type-decl")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PAYLOADTYPEDECL"



    # $ANTLR start "PARAMETERDECLLIST"
    def mPARAMETERDECLLIST(self, ):

        try:
            _type = PARAMETERDECLLIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:37:19: ( 'parameter-decl-list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:37:21: 'parameter-decl-list'
            pass 
            self.match("parameter-decl-list")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PARAMETERDECLLIST"



    # $ANTLR start "PARAMETERDECL"
    def mPARAMETERDECL(self, ):

        try:
            _type = PARAMETERDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:38:15: ( 'parameter-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:38:17: 'parameter-decl'
            pass 
            self.match("parameter-decl")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PARAMETERDECL"



    # $ANTLR start "MESSAGESIGNATURE"
    def mMESSAGESIGNATURE(self, ):

        try:
            _type = MESSAGESIGNATURE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:39:18: ( 'message-signature' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:39:20: 'message-signature'
            pass 
            self.match("message-signature")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MESSAGESIGNATURE"



    # $ANTLR start "ROLEDECLLIST"
    def mROLEDECLLIST(self, ):

        try:
            _type = ROLEDECLLIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:40:14: ( 'role-decl-list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:40:16: 'role-decl-list'
            pass 
            self.match("role-decl-list")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROLEDECLLIST"



    # $ANTLR start "ROLEDECL"
    def mROLEDECL(self, ):

        try:
            _type = ROLEDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:41:10: ( 'role-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:41:12: 'role-decl'
            pass 
            self.match("role-decl")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROLEDECL"



    # $ANTLR start "ARGUMENTLIST"
    def mARGUMENTLIST(self, ):

        try:
            _type = ARGUMENTLIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:42:14: ( 'argument-list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:42:16: 'argument-list'
            pass 
            self.match("argument-list")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ARGUMENTLIST"



    # $ANTLR start "ARGUMENT"
    def mARGUMENT(self, ):

        try:
            _type = ARGUMENT
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:43:10: ( 'argument' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:43:12: 'argument'
            pass 
            self.match("argument")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ARGUMENT"



    # $ANTLR start "PAYLOAD"
    def mPAYLOAD(self, ):

        try:
            _type = PAYLOAD
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:44:9: ( 'payload' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:44:11: 'payload'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:45:16: ( 'payloadelement' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:45:18: 'payloadelement'
            pass 
            self.match("payloadelement")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PAYLOADELEMENT"



    # $ANTLR start "ROLEINSTANTIATIONLIST"
    def mROLEINSTANTIATIONLIST(self, ):

        try:
            _type = ROLEINSTANTIATIONLIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:46:23: ( 'role-instantiation-list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:46:25: 'role-instantiation-list'
            pass 
            self.match("role-instantiation-list")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROLEINSTANTIATIONLIST"



    # $ANTLR start "ROLEINSTANTIATION"
    def mROLEINSTANTIATION(self, ):

        try:
            _type = ROLEINSTANTIATION
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:47:19: ( 'role-instantiation' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:47:21: 'role-instantiation'
            pass 
            self.match("role-instantiation")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROLEINSTANTIATION"



    # $ANTLR start "GLOBALPROTOCOLDECL"
    def mGLOBALPROTOCOLDECL(self, ):

        try:
            _type = GLOBALPROTOCOLDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:48:20: ( 'global-protocol-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:48:22: 'global-protocol-decl'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:49:19: ( 'global-protocol-def' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:49:21: 'global-protocol-def'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:50:24: ( 'global-protocol-instance' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:50:26: 'global-protocol-instance'
            pass 
            self.match("global-protocol-instance")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALPROTOCOLINSTANCE"



    # $ANTLR start "GLOBALPROTOCOLBLOCK"
    def mGLOBALPROTOCOLBLOCK(self, ):

        try:
            _type = GLOBALPROTOCOLBLOCK
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:51:21: ( 'global-protocol-block' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:51:23: 'global-protocol-block'
            pass 
            self.match("global-protocol-block")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALPROTOCOLBLOCK"



    # $ANTLR start "GLOBALINTERACTIONSEQUENCE"
    def mGLOBALINTERACTIONSEQUENCE(self, ):

        try:
            _type = GLOBALINTERACTIONSEQUENCE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:52:27: ( 'global-interaction-sequence' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:52:29: 'global-interaction-sequence'
            pass 
            self.match("global-interaction-sequence")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALINTERACTIONSEQUENCE"



    # $ANTLR start "GLOBALMESSAGETRANSFER"
    def mGLOBALMESSAGETRANSFER(self, ):

        try:
            _type = GLOBALMESSAGETRANSFER
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:53:23: ( 'global-message-transfer' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:53:25: 'global-message-transfer'
            pass 
            self.match("global-message-transfer")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALMESSAGETRANSFER"



    # $ANTLR start "GLOBALCHOICE"
    def mGLOBALCHOICE(self, ):

        try:
            _type = GLOBALCHOICE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:54:14: ( 'global-choice' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:54:16: 'global-choice'
            pass 
            self.match("global-choice")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALCHOICE"



    # $ANTLR start "GLOBALRECURSION"
    def mGLOBALRECURSION(self, ):

        try:
            _type = GLOBALRECURSION
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:55:17: ( 'global-recursion' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:55:19: 'global-recursion'
            pass 
            self.match("global-recursion")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALRECURSION"



    # $ANTLR start "GLOBALCONTINUE"
    def mGLOBALCONTINUE(self, ):

        try:
            _type = GLOBALCONTINUE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:56:16: ( 'global-continue' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:56:18: 'global-continue'
            pass 
            self.match("global-continue")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALCONTINUE"



    # $ANTLR start "GLOBALPARALLEL"
    def mGLOBALPARALLEL(self, ):

        try:
            _type = GLOBALPARALLEL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:57:16: ( 'global-parallel' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:57:18: 'global-parallel'
            pass 
            self.match("global-parallel")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALPARALLEL"



    # $ANTLR start "GLOBALINTERRUPTIBLE"
    def mGLOBALINTERRUPTIBLE(self, ):

        try:
            _type = GLOBALINTERRUPTIBLE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:58:21: ( 'global-interruptible' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:58:23: 'global-interruptible'
            pass 
            self.match("global-interruptible")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALINTERRUPTIBLE"



    # $ANTLR start "GLOBALINTERRUPT"
    def mGLOBALINTERRUPT(self, ):

        try:
            _type = GLOBALINTERRUPT
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:59:17: ( 'global-interrupt' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:59:19: 'global-interrupt'
            pass 
            self.match("global-interrupt")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALINTERRUPT"



    # $ANTLR start "GLOBALDO"
    def mGLOBALDO(self, ):

        try:
            _type = GLOBALDO
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:60:10: ( 'global-do' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:60:12: 'global-do'
            pass 
            self.match("global-do")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBALDO"



    # $ANTLR start "LOCALPROTOCOLDECL"
    def mLOCALPROTOCOLDECL(self, ):

        try:
            _type = LOCALPROTOCOLDECL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:61:19: ( 'local-protocol-decl' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:61:21: 'local-protocol-decl'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:62:18: ( 'local-protocol-def' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:62:20: 'local-protocol-def'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:63:23: ( 'local-protocol-instance' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:63:25: 'local-protocol-instance'
            pass 
            self.match("local-protocol-instance")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALPROTOCOLINSTANCE"



    # $ANTLR start "LOCALPROTOCOLBLOCK"
    def mLOCALPROTOCOLBLOCK(self, ):

        try:
            _type = LOCALPROTOCOLBLOCK
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:64:20: ( 'local-protocol-block' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:64:22: 'local-protocol-block'
            pass 
            self.match("local-protocol-block")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALPROTOCOLBLOCK"



    # $ANTLR start "LOCALINTERACTIONSEQUENCE"
    def mLOCALINTERACTIONSEQUENCE(self, ):

        try:
            _type = LOCALINTERACTIONSEQUENCE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:65:26: ( 'local-interaction-sequence' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:65:28: 'local-interaction-sequence'
            pass 
            self.match("local-interaction-sequence")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALINTERACTIONSEQUENCE"



    # $ANTLR start "LOCALMESSAGETRANSFER"
    def mLOCALMESSAGETRANSFER(self, ):

        try:
            _type = LOCALMESSAGETRANSFER
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:66:22: ( 'local-message-transfer' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:66:24: 'local-message-transfer'
            pass 
            self.match("local-message-transfer")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALMESSAGETRANSFER"



    # $ANTLR start "LOCALCHOICE"
    def mLOCALCHOICE(self, ):

        try:
            _type = LOCALCHOICE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:67:13: ( 'local-choice' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:67:15: 'local-choice'
            pass 
            self.match("local-choice")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALCHOICE"



    # $ANTLR start "LOCALRECURSION"
    def mLOCALRECURSION(self, ):

        try:
            _type = LOCALRECURSION
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:68:16: ( 'local-recursion' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:68:18: 'local-recursion'
            pass 
            self.match("local-recursion")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALRECURSION"



    # $ANTLR start "LOCALCONTINUE"
    def mLOCALCONTINUE(self, ):

        try:
            _type = LOCALCONTINUE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:69:15: ( 'local-continue' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:69:17: 'local-continue'
            pass 
            self.match("local-continue")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALCONTINUE"



    # $ANTLR start "LOCALPARALLEL"
    def mLOCALPARALLEL(self, ):

        try:
            _type = LOCALPARALLEL
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:70:15: ( 'local-parallel' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:70:17: 'local-parallel'
            pass 
            self.match("local-parallel")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALPARALLEL"



    # $ANTLR start "LOCALINTERRUPTIBLE"
    def mLOCALINTERRUPTIBLE(self, ):

        try:
            _type = LOCALINTERRUPTIBLE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:71:20: ( 'local-interruptible' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:71:22: 'local-interruptible'
            pass 
            self.match("local-interruptible")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALINTERRUPTIBLE"



    # $ANTLR start "LOCALINTERRUPT"
    def mLOCALINTERRUPT(self, ):

        try:
            _type = LOCALINTERRUPT
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:72:16: ( 'local-interrupt' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:72:18: 'local-interrupt'
            pass 
            self.match("local-interrupt")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALINTERRUPT"



    # $ANTLR start "LOCALDO"
    def mLOCALDO(self, ):

        try:
            _type = LOCALDO
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:73:9: ( 'local-do' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:73:11: 'local-do'
            pass 
            self.match("local-do")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALDO"



    # $ANTLR start "LOCALTHROW"
    def mLOCALTHROW(self, ):

        try:
            _type = LOCALTHROW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:74:12: ( 'local-throw' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:74:14: 'local-throw'
            pass 
            self.match("local-throw")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALTHROW"



    # $ANTLR start "LOCALCATCH"
    def mLOCALCATCH(self, ):

        try:
            _type = LOCALCATCH
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:75:12: ( 'local-catch' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:75:14: 'local-catch'
            pass 
            self.match("local-catch")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALCATCH"



    # $ANTLR start "LOCALSEND"
    def mLOCALSEND(self, ):

        try:
            _type = LOCALSEND
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:76:11: ( 'local-send' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:76:13: 'local-send'
            pass 
            self.match("local-send")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALSEND"



    # $ANTLR start "LOCALRECEIVE"
    def mLOCALRECEIVE(self, ):

        try:
            _type = LOCALRECEIVE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:77:14: ( 'local-receive' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:77:16: 'local-receive'
            pass 
            self.match("local-receive")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOCALRECEIVE"



    # $ANTLR start "EMPTY_MESSAGE_OP"
    def mEMPTY_MESSAGE_OP(self, ):

        try:
            _type = EMPTY_MESSAGE_OP
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:78:18: ( '__empty_message_op' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:78:20: '__empty_message_op'
            pass 
            self.match("__empty_message_op")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY_MESSAGE_OP"



    # $ANTLR start "EMPTY_ANNOTATION"
    def mEMPTY_ANNOTATION(self, ):

        try:
            _type = EMPTY_ANNOTATION
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:79:18: ( '__empty_annotation' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:79:20: '__empty_annotation'
            pass 
            self.match("__empty_annotation")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY_ANNOTATION"



    # $ANTLR start "EMPTY_PARAMETER_DECL_LIST"
    def mEMPTY_PARAMETER_DECL_LIST(self, ):

        try:
            _type = EMPTY_PARAMETER_DECL_LIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:80:27: ( '__empty_parameter_decl_list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:80:29: '__empty_parameter_decl_list'
            pass 
            self.match("__empty_parameter_decl_list")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY_PARAMETER_DECL_LIST"



    # $ANTLR start "EMPTY_ARGUMENT_LIST"
    def mEMPTY_ARGUMENT_LIST(self, ):

        try:
            _type = EMPTY_ARGUMENT_LIST
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:81:21: ( '__empty_argument_list' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:81:23: '__empty_argument_list'
            pass 
            self.match("__empty_argument_list")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY_ARGUMENT_LIST"



    # $ANTLR start "EMPTY_MODULE_NAME"
    def mEMPTY_MODULE_NAME(self, ):

        try:
            _type = EMPTY_MODULE_NAME
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:82:19: ( '__empty_module_name' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:82:21: '__empty_module_name'
            pass 
            self.match("__empty_module_name")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY_MODULE_NAME"



    # $ANTLR start "EMPTY_SCOPE_NAME"
    def mEMPTY_SCOPE_NAME(self, ):

        try:
            _type = EMPTY_SCOPE_NAME
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:83:18: ( '__empty_scope_name' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:83:20: '__empty_scope_name'
            pass 
            self.match("__empty_scope_name")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY_SCOPE_NAME"



    # $ANTLR start "EMPTY_LOCAL_THROW"
    def mEMPTY_LOCAL_THROW(self, ):

        try:
            _type = EMPTY_LOCAL_THROW
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:84:19: ( '__empty_local_throw' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:84:21: '__empty_local_throw'
            pass 
            self.match("__empty_local_throw")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY_LOCAL_THROW"



    # $ANTLR start "EMPTY_LOCAL_CATCHES"
    def mEMPTY_LOCAL_CATCHES(self, ):

        try:
            _type = EMPTY_LOCAL_CATCHES
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:85:21: ( '__empty_local_catch' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:85:23: '__empty_local_catch'
            pass 
            self.match("__empty_local_catch")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY_LOCAL_CATCHES"



    # $ANTLR start "KIND_MESSAGE_SIGNATURE"
    def mKIND_MESSAGE_SIGNATURE(self, ):

        try:
            _type = KIND_MESSAGE_SIGNATURE
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:86:24: ( 'KIND_MESSAGE_SIGNATURE' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:86:26: 'KIND_MESSAGE_SIGNATURE'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:87:19: ( 'KIND_PAYLOAD_TYPE' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:87:21: 'KIND_PAYLOAD_TYPE'
            pass 
            self.match("KIND_PAYLOAD_TYPE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "KIND_PAYLOAD_TYPE"



    # $ANTLR start "T__94"
    def mT__94(self, ):

        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:88:7: ( '.' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:88:9: '.'
            pass 
            self.match(46)



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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:89:7: ( ';' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:89:9: ';'
            pass 
            self.match(59)



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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:90:7: ( '<' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:90:9: '<'
            pass 
            self.match(60)



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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:91:7: ( '>' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:91:9: '>'
            pass 
            self.match(62)



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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:92:7: ( '(' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:92:9: '('
            pass 
            self.match(40)



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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:93:7: ( ')' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:93:9: ')'
            pass 
            self.match(41)



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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:94:8: ( ',' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:94:10: ','
            pass 
            self.match(44)



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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:95:8: ( ':' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:95:10: ':'
            pass 
            self.match(58)



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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:96:8: ( '{' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:96:10: '{'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:97:8: ( '}' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:97:10: '}'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:138:11: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:139:2: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:139:2: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((9 <= LA1_0 <= 10) or (12 <= LA1_0 <= 13) or LA1_0 == 32) :
                    alt1 = 1


                if alt1 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:148:8: ( '/*' ( . )* '*/' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:149:2: '/*' ( . )* '*/'
            pass 
            self.match("/*")
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:149:7: ( . )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 42) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 47) :
                        alt2 = 2
                    elif ((0 <= LA2_1 <= 46) or (48 <= LA2_1 <= 65535)) :
                        alt2 = 1


                elif ((0 <= LA2_0 <= 41) or (43 <= LA2_0 <= 65535)) :
                    alt2 = 1


                if alt2 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:149:7: .
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:155:13: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:156:2: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("//")
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:156:7: (~ ( '\\n' | '\\r' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 9) or (11 <= LA3_0 <= 12) or (14 <= LA3_0 <= 65535)) :
                    alt3 = 1


                if alt3 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:156:7: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:156:21: ( '\\r' )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 13) :
                alt4 = 1
            if alt4 == 1:
                # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:156:21: '\\r'
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:165:11: ( ( LETTER | UNDERSCORE ) ( LETTER | DIGIT | UNDERSCORE )* )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:166:2: ( LETTER | UNDERSCORE ) ( LETTER | DIGIT | UNDERSCORE )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:166:24: ( LETTER | DIGIT | UNDERSCORE )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 90) or LA5_0 == 95 or (97 <= LA5_0 <= 122)) :
                    alt5 = 1


                if alt5 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
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
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:169:16: ( '{' | '}' | '(' | ')' | '[' | ']' | ':' | '/' | '\\\\' | '.' | '\\#' | '&' | '?' | '!' | UNDERSCORE )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:
            pass 
            if self.input.LA(1) == 33 or self.input.LA(1) == 35 or self.input.LA(1) == 38 or (40 <= self.input.LA(1) <= 41) or (46 <= self.input.LA(1) <= 47) or self.input.LA(1) == 58 or self.input.LA(1) == 63 or (91 <= self.input.LA(1) <= 93) or self.input.LA(1) == 95 or self.input.LA(1) == 123 or self.input.LA(1) == 125:
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

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:177:14: ( '\\\"' ( LETTER | UNDERSCORE ) ( LETTER | DIGIT | SYMBOL )* '\\\"' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:178:2: '\\\"' ( LETTER | UNDERSCORE ) ( LETTER | DIGIT | SYMBOL )* '\\\"'
            pass 
            self.match(34)
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:178:29: ( LETTER | DIGIT | SYMBOL )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 33 or LA6_0 == 35 or LA6_0 == 38 or (40 <= LA6_0 <= 41) or (46 <= LA6_0 <= 58) or LA6_0 == 63 or (65 <= LA6_0 <= 93) or LA6_0 == 95 or (97 <= LA6_0 <= 123) or LA6_0 == 125) :
                    alt6 = 1


                if alt6 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:
                    pass 
                    if self.input.LA(1) == 33 or self.input.LA(1) == 35 or self.input.LA(1) == 38 or (40 <= self.input.LA(1) <= 41) or (46 <= self.input.LA(1) <= 58) or self.input.LA(1) == 63 or (65 <= self.input.LA(1) <= 93) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 123) or self.input.LA(1) == 125:
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
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:181:16: ( 'a' .. 'z' | 'A' .. 'Z' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
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
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:185:15: ( '0' .. '9' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:186:2: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "UNDERSCORE"
    def mUNDERSCORE(self, ):

        try:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:189:20: ( '_' )
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:190:2: '_'
            pass 
            self.match(95)




        finally:

            pass

    # $ANTLR end "UNDERSCORE"



    def mTokens(self):
        # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:8: ( MODULEKW | IMPORTKW | TYPEKW | PROTOCOLKW | GLOBALKW | LOCALKW | ROLEKW | SIGKW | INSTANTIATESKW | ASKW | FROMKW | TOKW | CHOICEKW | ATKW | ORKW | RECKW | CONTINUEKW | PARKW | ANDKW | INTERRUPTIBLEKW | WITHKW | BYKW | THROWSKW | CATCHESKW | DOKW | MODULE | MODULEDECL | IMPORTMODULE | IMPORTMEMBER | PAYLOADTYPEDECL | PARAMETERDECLLIST | PARAMETERDECL | MESSAGESIGNATURE | ROLEDECLLIST | ROLEDECL | ARGUMENTLIST | ARGUMENT | PAYLOAD | PAYLOADELEMENT | ROLEINSTANTIATIONLIST | ROLEINSTANTIATION | GLOBALPROTOCOLDECL | GLOBALPROTOCOLDEF | GLOBALPROTOCOLINSTANCE | GLOBALPROTOCOLBLOCK | GLOBALINTERACTIONSEQUENCE | GLOBALMESSAGETRANSFER | GLOBALCHOICE | GLOBALRECURSION | GLOBALCONTINUE | GLOBALPARALLEL | GLOBALINTERRUPTIBLE | GLOBALINTERRUPT | GLOBALDO | LOCALPROTOCOLDECL | LOCALPROTOCOLDEF | LOCALPROTOCOLINSTANCE | LOCALPROTOCOLBLOCK | LOCALINTERACTIONSEQUENCE | LOCALMESSAGETRANSFER | LOCALCHOICE | LOCALRECURSION | LOCALCONTINUE | LOCALPARALLEL | LOCALINTERRUPTIBLE | LOCALINTERRUPT | LOCALDO | LOCALTHROW | LOCALCATCH | LOCALSEND | LOCALRECEIVE | EMPTY_MESSAGE_OP | EMPTY_ANNOTATION | EMPTY_PARAMETER_DECL_LIST | EMPTY_ARGUMENT_LIST | EMPTY_MODULE_NAME | EMPTY_SCOPE_NAME | EMPTY_LOCAL_THROW | EMPTY_LOCAL_CATCHES | KIND_MESSAGE_SIGNATURE | KIND_PAYLOAD_TYPE | T__94 | T__95 | T__96 | T__97 | T__98 | T__99 | T__100 | T__101 | T__102 | T__103 | WHITESPACE | COMMENT | LINE_COMMENT | IDENTIFIER | EXTIDENTIFIER )
        alt7 = 96
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:10: MODULEKW
            pass 
            self.mMODULEKW()


        elif alt7 == 2:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:19: IMPORTKW
            pass 
            self.mIMPORTKW()


        elif alt7 == 3:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:28: TYPEKW
            pass 
            self.mTYPEKW()


        elif alt7 == 4:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:35: PROTOCOLKW
            pass 
            self.mPROTOCOLKW()


        elif alt7 == 5:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:46: GLOBALKW
            pass 
            self.mGLOBALKW()


        elif alt7 == 6:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:55: LOCALKW
            pass 
            self.mLOCALKW()


        elif alt7 == 7:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:63: ROLEKW
            pass 
            self.mROLEKW()


        elif alt7 == 8:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:70: SIGKW
            pass 
            self.mSIGKW()


        elif alt7 == 9:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:76: INSTANTIATESKW
            pass 
            self.mINSTANTIATESKW()


        elif alt7 == 10:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:91: ASKW
            pass 
            self.mASKW()


        elif alt7 == 11:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:96: FROMKW
            pass 
            self.mFROMKW()


        elif alt7 == 12:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:103: TOKW
            pass 
            self.mTOKW()


        elif alt7 == 13:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:108: CHOICEKW
            pass 
            self.mCHOICEKW()


        elif alt7 == 14:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:117: ATKW
            pass 
            self.mATKW()


        elif alt7 == 15:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:122: ORKW
            pass 
            self.mORKW()


        elif alt7 == 16:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:127: RECKW
            pass 
            self.mRECKW()


        elif alt7 == 17:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:133: CONTINUEKW
            pass 
            self.mCONTINUEKW()


        elif alt7 == 18:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:144: PARKW
            pass 
            self.mPARKW()


        elif alt7 == 19:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:150: ANDKW
            pass 
            self.mANDKW()


        elif alt7 == 20:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:156: INTERRUPTIBLEKW
            pass 
            self.mINTERRUPTIBLEKW()


        elif alt7 == 21:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:172: WITHKW
            pass 
            self.mWITHKW()


        elif alt7 == 22:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:179: BYKW
            pass 
            self.mBYKW()


        elif alt7 == 23:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:184: THROWSKW
            pass 
            self.mTHROWSKW()


        elif alt7 == 24:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:193: CATCHESKW
            pass 
            self.mCATCHESKW()


        elif alt7 == 25:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:203: DOKW
            pass 
            self.mDOKW()


        elif alt7 == 26:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:208: MODULE
            pass 
            self.mMODULE()


        elif alt7 == 27:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:215: MODULEDECL
            pass 
            self.mMODULEDECL()


        elif alt7 == 28:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:226: IMPORTMODULE
            pass 
            self.mIMPORTMODULE()


        elif alt7 == 29:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:239: IMPORTMEMBER
            pass 
            self.mIMPORTMEMBER()


        elif alt7 == 30:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:252: PAYLOADTYPEDECL
            pass 
            self.mPAYLOADTYPEDECL()


        elif alt7 == 31:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:268: PARAMETERDECLLIST
            pass 
            self.mPARAMETERDECLLIST()


        elif alt7 == 32:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:286: PARAMETERDECL
            pass 
            self.mPARAMETERDECL()


        elif alt7 == 33:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:300: MESSAGESIGNATURE
            pass 
            self.mMESSAGESIGNATURE()


        elif alt7 == 34:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:317: ROLEDECLLIST
            pass 
            self.mROLEDECLLIST()


        elif alt7 == 35:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:330: ROLEDECL
            pass 
            self.mROLEDECL()


        elif alt7 == 36:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:339: ARGUMENTLIST
            pass 
            self.mARGUMENTLIST()


        elif alt7 == 37:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:352: ARGUMENT
            pass 
            self.mARGUMENT()


        elif alt7 == 38:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:361: PAYLOAD
            pass 
            self.mPAYLOAD()


        elif alt7 == 39:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:369: PAYLOADELEMENT
            pass 
            self.mPAYLOADELEMENT()


        elif alt7 == 40:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:384: ROLEINSTANTIATIONLIST
            pass 
            self.mROLEINSTANTIATIONLIST()


        elif alt7 == 41:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:406: ROLEINSTANTIATION
            pass 
            self.mROLEINSTANTIATION()


        elif alt7 == 42:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:424: GLOBALPROTOCOLDECL
            pass 
            self.mGLOBALPROTOCOLDECL()


        elif alt7 == 43:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:443: GLOBALPROTOCOLDEF
            pass 
            self.mGLOBALPROTOCOLDEF()


        elif alt7 == 44:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:461: GLOBALPROTOCOLINSTANCE
            pass 
            self.mGLOBALPROTOCOLINSTANCE()


        elif alt7 == 45:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:484: GLOBALPROTOCOLBLOCK
            pass 
            self.mGLOBALPROTOCOLBLOCK()


        elif alt7 == 46:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:504: GLOBALINTERACTIONSEQUENCE
            pass 
            self.mGLOBALINTERACTIONSEQUENCE()


        elif alt7 == 47:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:530: GLOBALMESSAGETRANSFER
            pass 
            self.mGLOBALMESSAGETRANSFER()


        elif alt7 == 48:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:552: GLOBALCHOICE
            pass 
            self.mGLOBALCHOICE()


        elif alt7 == 49:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:565: GLOBALRECURSION
            pass 
            self.mGLOBALRECURSION()


        elif alt7 == 50:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:581: GLOBALCONTINUE
            pass 
            self.mGLOBALCONTINUE()


        elif alt7 == 51:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:596: GLOBALPARALLEL
            pass 
            self.mGLOBALPARALLEL()


        elif alt7 == 52:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:611: GLOBALINTERRUPTIBLE
            pass 
            self.mGLOBALINTERRUPTIBLE()


        elif alt7 == 53:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:631: GLOBALINTERRUPT
            pass 
            self.mGLOBALINTERRUPT()


        elif alt7 == 54:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:647: GLOBALDO
            pass 
            self.mGLOBALDO()


        elif alt7 == 55:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:656: LOCALPROTOCOLDECL
            pass 
            self.mLOCALPROTOCOLDECL()


        elif alt7 == 56:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:674: LOCALPROTOCOLDEF
            pass 
            self.mLOCALPROTOCOLDEF()


        elif alt7 == 57:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:691: LOCALPROTOCOLINSTANCE
            pass 
            self.mLOCALPROTOCOLINSTANCE()


        elif alt7 == 58:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:713: LOCALPROTOCOLBLOCK
            pass 
            self.mLOCALPROTOCOLBLOCK()


        elif alt7 == 59:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:732: LOCALINTERACTIONSEQUENCE
            pass 
            self.mLOCALINTERACTIONSEQUENCE()


        elif alt7 == 60:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:757: LOCALMESSAGETRANSFER
            pass 
            self.mLOCALMESSAGETRANSFER()


        elif alt7 == 61:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:778: LOCALCHOICE
            pass 
            self.mLOCALCHOICE()


        elif alt7 == 62:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:790: LOCALRECURSION
            pass 
            self.mLOCALRECURSION()


        elif alt7 == 63:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:805: LOCALCONTINUE
            pass 
            self.mLOCALCONTINUE()


        elif alt7 == 64:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:819: LOCALPARALLEL
            pass 
            self.mLOCALPARALLEL()


        elif alt7 == 65:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:833: LOCALINTERRUPTIBLE
            pass 
            self.mLOCALINTERRUPTIBLE()


        elif alt7 == 66:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:852: LOCALINTERRUPT
            pass 
            self.mLOCALINTERRUPT()


        elif alt7 == 67:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:867: LOCALDO
            pass 
            self.mLOCALDO()


        elif alt7 == 68:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:875: LOCALTHROW
            pass 
            self.mLOCALTHROW()


        elif alt7 == 69:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:886: LOCALCATCH
            pass 
            self.mLOCALCATCH()


        elif alt7 == 70:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:897: LOCALSEND
            pass 
            self.mLOCALSEND()


        elif alt7 == 71:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:907: LOCALRECEIVE
            pass 
            self.mLOCALRECEIVE()


        elif alt7 == 72:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:920: EMPTY_MESSAGE_OP
            pass 
            self.mEMPTY_MESSAGE_OP()


        elif alt7 == 73:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:937: EMPTY_ANNOTATION
            pass 
            self.mEMPTY_ANNOTATION()


        elif alt7 == 74:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:954: EMPTY_PARAMETER_DECL_LIST
            pass 
            self.mEMPTY_PARAMETER_DECL_LIST()


        elif alt7 == 75:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:980: EMPTY_ARGUMENT_LIST
            pass 
            self.mEMPTY_ARGUMENT_LIST()


        elif alt7 == 76:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1000: EMPTY_MODULE_NAME
            pass 
            self.mEMPTY_MODULE_NAME()


        elif alt7 == 77:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1018: EMPTY_SCOPE_NAME
            pass 
            self.mEMPTY_SCOPE_NAME()


        elif alt7 == 78:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1035: EMPTY_LOCAL_THROW
            pass 
            self.mEMPTY_LOCAL_THROW()


        elif alt7 == 79:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1053: EMPTY_LOCAL_CATCHES
            pass 
            self.mEMPTY_LOCAL_CATCHES()


        elif alt7 == 80:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1073: KIND_MESSAGE_SIGNATURE
            pass 
            self.mKIND_MESSAGE_SIGNATURE()


        elif alt7 == 81:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1096: KIND_PAYLOAD_TYPE
            pass 
            self.mKIND_PAYLOAD_TYPE()


        elif alt7 == 82:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1114: T__94
            pass 
            self.mT__94()


        elif alt7 == 83:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1120: T__95
            pass 
            self.mT__95()


        elif alt7 == 84:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1126: T__96
            pass 
            self.mT__96()


        elif alt7 == 85:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1132: T__97
            pass 
            self.mT__97()


        elif alt7 == 86:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1138: T__98
            pass 
            self.mT__98()


        elif alt7 == 87:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1144: T__99
            pass 
            self.mT__99()


        elif alt7 == 88:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1150: T__100
            pass 
            self.mT__100()


        elif alt7 == 89:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1157: T__101
            pass 
            self.mT__101()


        elif alt7 == 90:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1164: T__102
            pass 
            self.mT__102()


        elif alt7 == 91:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1171: T__103
            pass 
            self.mT__103()


        elif alt7 == 92:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1178: WHITESPACE
            pass 
            self.mWHITESPACE()


        elif alt7 == 93:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1189: COMMENT
            pass 
            self.mCOMMENT()


        elif alt7 == 94:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1197: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt7 == 95:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1210: IDENTIFIER
            pass 
            self.mIDENTIFIER()


        elif alt7 == 96:
            # C:\\Tools\\myPythonScrib\\scribble-python\\scribble\\Scribble.g:1:1221: EXTIDENTIFIER
            pass 
            self.mEXTIDENTIFIER()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        "\1\uffff\21\36\16\uffff\5\36\1\104\10\36\1\116\1\117\6\36\1\126"
        "\1\36\1\130\1\131\2\36\2\uffff\6\36\1\uffff\2\36\1\145\4\36\1\152"
        "\1\153\2\uffff\1\154\5\36\1\uffff\1\36\2\uffff\7\36\1\172\3\36"
        "\1\uffff\3\36\1\u0082\3\uffff\1\36\1\u0084\3\36\1\u0088\2\36\1"
        "\u008c\4\36\1\uffff\5\36\1\u0097\2\uffff\1\36\1\uffff\3\36\1\uffff"
        "\2\36\1\u00a2\1\uffff\1\36\1\u00a5\2\36\1\u00a8\3\36\1\u00ad\4"
        "\uffff\1\36\1\u00b9\5\36\2\uffff\1\36\2\uffff\2\36\1\uffff\2\36"
        "\1\u00c7\14\uffff\1\36\1\uffff\1\36\1\u00d9\3\36\2\uffff\2\36\1"
        "\u00e1\1\36\1\uffff\1\36\20\uffff\1\u00ef\1\u00f0\1\uffff\3\36"
        "\2\uffff\2\36\1\uffff\2\36\10\uffff\1\u0103\4\uffff\11\36\1\uffff"
        "\1\36\11\uffff\13\36\1\uffff\1\36\5\uffff\11\36\1\u0133\1\36\1"
        "\uffff\1\36\6\uffff\11\36\1\uffff\1\u0146\1\uffff\1\36\6\uffff"
        "\11\36\1\uffff\1\u0158\1\u0159\5\uffff\11\36\6\uffff\1\u016f\1"
        "\uffff\12\36\1\uffff\1\u017f\6\uffff\12\36\7\uffff\11\36\1\u0199"
        "\3\uffff\1\u019d\1\u019e\1\36\1\u01a0\2\36\1\u01a3\3\36\6\uffff"
        "\1\u01a7\1\uffff\2\36\1\uffff\1\u01aa\1\u01ab\1\36\1\uffff\2\36"
        "\2\uffff\1\36\1\u01b0\2\36\1\uffff\1\36\1\u01b4\1\36\1\uffff\3"
        "\36\1\u01b9\1\uffff"
        )

    DFA7_eof = DFA.unpack(
        "\u01ba\uffff"
        )

    DFA7_min = DFA.unpack(
        "\1\11\1\145\1\155\1\150\1\141\1\154\1\157\1\145\1\151\1\156\1"
        "\162\1\141\1\162\1\151\1\171\1\157\1\137\1\111\13\uffff\1\52\2"
        "\uffff\1\144\1\163\1\160\1\163\1\160\1\60\1\162\1\157\1\162\1\157"
        "\1\143\1\154\1\143\1\147\2\60\1\144\1\147\2\157\1\156\1\164\1\60"
        "\1\164\2\60\1\145\1\116\2\uffff\1\165\1\163\1\157\1\164\2\145\1"
        "\uffff\1\157\1\164\1\60\1\154\1\142\1\141\1\145\2\60\2\uffff\1"
        "\60\1\165\1\155\1\151\1\164\1\143\1\uffff\1\150\2\uffff\1\155\1"
        "\104\1\154\1\141\1\162\1\141\1\162\1\60\1\167\1\157\1\155\1\uffff"
        "\1\157\1\141\1\154\1\55\3\uffff\1\155\1\60\1\143\1\151\1\150\1"
        "\60\1\160\1\137\1\60\1\147\1\164\1\156\1\162\1\uffff\1\163\1\143"
        "\1\145\1\141\1\154\1\55\1\144\1\uffff\1\145\1\uffff\1\145\1\156"
        "\1\145\1\uffff\1\164\1\115\1\55\1\uffff\1\145\1\55\1\164\1\165"
        "\1\60\1\157\1\164\1\144\1\55\1\143\1\uffff\1\145\2\156\1\60\1\165"
        "\1\163\1\171\1\105\1\101\2\uffff\1\55\1\155\1\uffff\1\151\1\160"
        "\1\uffff\1\154\1\145\1\55\1\143\1\uffff\1\141\1\156\1\uffff\1\141"
        "\1\145\3\uffff\1\143\1\163\1\164\1\uffff\1\145\1\60\1\137\1\123"
        "\1\131\1\uffff\1\145\1\141\1\164\1\60\1\162\1\uffff\1\154\1\uffff"
        "\1\141\1\156\1\uffff\1\150\2\uffff\1\157\1\uffff\1\164\3\uffff"
        "\1\143\1\154\1\164\1\55\1\60\1\uffff\1\141\1\123\1\114\2\uffff"
        "\1\164\1\151\1\uffff\1\55\1\145\1\157\1\uffff\1\164\2\uffff\1\164"
        "\2\145\1\55\1\141\3\uffff\1\145\1\156\1\141\1\143\1\157\1\101\1"
        "\117\1\145\1\142\1\144\1\155\1\164\1\145\1\157\1\162\4\uffff\1"
        "\156\1\163\1\144\1\156\1\147\1\162\1\157\1\143\1\107\1\101\1\163"
        "\1\154\2\145\1\157\1\162\1\143\1\141\1\164\1\163\1\165\1\157\1"
        "\165\1\141\1\160\1\141\1\105\1\104\1\60\1\145\1\143\1\156\1\143"
        "\1\141\1\157\1\uffff\1\165\1\151\1\141\1\154\1\164\2\155\1\145"
        "\1\154\2\137\1\uffff\1\60\1\154\1\164\1\157\1\uffff\1\165\1\154"
        "\1\160\1\141\1\147\1\145\1\141\2\145\2\137\1\123\1\124\1\uffff"
        "\1\55\1\60\1\154\1\160\1\55\2\164\1\145\1\137\1\164\1\156\1\164"
        "\1\156\1\143\1\111\1\131\3\uffff\1\55\1\164\1\142\2\151\1\137\1"
        "\156\1\151\1\164\1\145\1\141\1\150\1\141\1\107\1\120\1\142\1\151"
        "\1\145\4\uffff\2\157\1\141\1\157\1\137\1\162\1\155\1\162\1\164"
        "\1\116\1\105\1\145\4\uffff\1\143\1\156\1\160\1\155\1\156\1\154"
        "\1\137\1\145\1\157\1\143\1\101\1\60\1\143\2\uffff\1\55\1\60\1\145"
        "\1\60\1\151\1\144\1\60\1\167\1\150\1\124\6\uffff\1\60\1\uffff\1"
        "\163\1\145\1\uffff\2\60\1\125\1\uffff\1\164\1\143\2\uffff\1\122"
        "\1\60\1\154\1\105\1\uffff\1\137\1\60\1\154\1\uffff\1\151\1\163"
        "\1\164\1\60\1\uffff"
        )

    DFA7_max = DFA.unpack(
        "\1\175\1\157\1\156\1\171\1\162\1\154\2\157\1\151\1\164\1\162\1"
        "\157\1\162\1\151\1\171\1\157\1\137\1\111\13\uffff\1\57\2\uffff"
        "\1\144\1\163\1\160\1\164\1\160\1\172\1\162\1\157\1\171\1\157\1"
        "\143\1\154\1\143\1\147\2\172\1\144\1\147\2\157\1\156\1\164\1\172"
        "\1\164\2\172\1\145\1\116\2\uffff\1\165\1\163\1\157\1\164\2\145"
        "\1\uffff\1\157\1\164\1\172\1\154\1\142\1\141\1\145\2\172\2\uffff"
        "\1\172\1\165\1\155\1\151\1\164\1\143\1\uffff\1\150\2\uffff\1\155"
        "\1\104\1\154\1\141\1\162\1\141\1\162\1\172\1\167\1\157\1\155\1"
        "\uffff\1\157\1\141\1\154\1\172\3\uffff\1\155\1\172\1\143\1\151"
        "\1\150\1\172\1\160\1\137\1\172\1\147\1\164\1\156\1\162\1\uffff"
        "\1\163\1\143\1\145\1\141\1\154\1\172\1\151\1\uffff\1\145\1\uffff"
        "\1\145\1\156\1\145\1\uffff\1\164\1\120\1\172\1\uffff\1\145\1\172"
        "\1\164\1\165\1\172\1\157\1\164\1\144\1\172\1\164\1\uffff\1\145"
        "\2\156\1\172\1\165\1\163\1\171\1\105\1\101\2\uffff\1\55\1\155\1"
        "\uffff\1\151\1\160\1\uffff\1\154\1\145\1\172\1\162\1\uffff\1\162"
        "\1\156\1\uffff\1\157\1\145\3\uffff\1\143\1\163\1\164\1\uffff\1"
        "\145\1\172\1\137\1\123\1\131\1\uffff\1\157\1\141\1\164\1\172\1"
        "\162\1\uffff\1\154\1\uffff\1\162\1\156\1\uffff\1\157\2\uffff\1"
        "\157\1\uffff\1\164\3\uffff\1\143\1\154\1\164\2\172\1\uffff\1\163"
        "\1\123\1\114\2\uffff\1\164\1\151\1\uffff\1\55\1\145\1\157\1\uffff"
        "\1\164\2\uffff\1\164\1\145\1\165\1\55\1\141\3\uffff\1\157\1\162"
        "\1\141\1\143\1\157\1\101\1\117\1\145\1\142\1\144\1\155\1\164\1"
        "\145\1\157\1\162\4\uffff\1\156\1\163\1\144\1\156\1\147\1\162\1"
        "\157\1\143\1\107\1\101\1\163\1\154\2\145\1\157\1\162\1\143\1\162"
        "\1\164\1\163\1\165\1\157\1\165\1\141\1\160\1\141\1\105\1\104\1"
        "\172\1\145\1\143\1\156\1\143\1\162\1\157\1\uffff\1\165\1\151\1"
        "\141\1\154\1\164\2\155\1\145\1\154\2\137\1\uffff\1\172\1\154\1"
        "\164\1\157\1\uffff\1\165\1\154\1\160\1\141\1\147\1\145\1\141\2"
        "\145\2\137\1\123\1\124\1\uffff\1\55\1\172\1\154\1\160\1\55\2\164"
        "\1\145\1\137\1\164\1\156\1\164\1\156\1\164\1\111\1\131\3\uffff"
        "\1\55\1\164\3\151\1\137\1\156\1\151\1\164\1\145\1\141\1\150\1\141"
        "\1\107\1\120\2\151\1\145\4\uffff\2\157\1\141\1\157\1\137\1\162"
        "\1\155\1\162\1\164\1\116\1\105\1\145\4\uffff\1\146\1\156\1\160"
        "\1\155\1\156\1\154\1\137\1\145\1\157\1\143\1\101\1\172\1\146\2"
        "\uffff\1\55\1\172\1\145\1\172\1\151\1\144\1\172\1\167\1\150\1\124"
        "\6\uffff\1\172\1\uffff\1\163\1\145\1\uffff\2\172\1\125\1\uffff"
        "\1\164\1\143\2\uffff\1\122\1\172\1\154\1\105\1\uffff\1\137\1\172"
        "\1\154\1\uffff\1\151\1\163\1\164\1\172\1\uffff"
        )

    DFA7_accept = DFA.unpack(
        "\22\uffff\1\122\1\123\1\124\1\125\1\126\1\127\1\130\1\131\1\132"
        "\1\133\1\134\1\uffff\1\137\1\140\34\uffff\1\135\1\136\6\uffff\1"
        "\14\11\uffff\1\12\1\16\6\uffff\1\17\1\uffff\1\26\1\31\13\uffff"
        "\1\22\4\uffff\1\20\1\10\1\23\15\uffff\1\3\7\uffff\1\7\1\uffff\1"
        "\13\3\uffff\1\25\3\uffff\1\32\12\uffff\1\6\11\uffff\1\33\1\1\2"
        "\uffff\1\2\2\uffff\1\27\4\uffff\1\5\2\uffff\1\74\2\uffff\1\103"
        "\1\104\1\106\3\uffff\1\15\5\uffff\1\41\5\uffff\1\36\1\uffff\1\46"
        "\2\uffff\1\57\1\uffff\1\61\1\66\1\uffff\1\100\1\uffff\1\75\1\77"
        "\1\105\5\uffff\1\30\3\uffff\1\34\1\35\2\uffff\1\4\3\uffff\1\63"
        "\1\uffff\1\60\1\62\5\uffff\1\44\1\45\1\21\17\uffff\1\76\1\107\1"
        "\42\1\43\43\uffff\1\73\13\uffff\1\11\4\uffff\1\56\15\uffff\1\24"
        "\20\uffff\1\37\1\40\1\47\22\uffff\1\71\1\72\1\101\1\102\14\uffff"
        "\1\54\1\55\1\64\1\65\15\uffff\1\67\1\70\12\uffff\1\121\1\52\1\53"
        "\1\50\1\51\1\110\1\uffff\1\111\2\uffff\1\115\3\uffff\1\114\2\uffff"
        "\1\116\1\117\4\uffff\1\113\3\uffff\1\120\4\uffff\1\112"
        )

    DFA7_special = DFA.unpack(
        "\u01ba\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack("\2\34\1\uffff\2\34\22\uffff\1\34\1\uffff\1\37\5\uffff"
        "\1\26\1\27\2\uffff\1\30\1\uffff\1\22\1\35\12\uffff\1\31\1\23\1"
        "\24\1\uffff\1\25\2\uffff\12\36\1\21\17\36\4\uffff\1\20\1\uffff"
        "\1\11\1\16\1\13\1\17\1\36\1\12\1\5\1\36\1\2\2\36\1\6\1\1\1\36\1"
        "\14\1\4\1\36\1\7\1\10\1\3\2\36\1\15\3\36\1\32\1\uffff\1\33"),
        DFA.unpack("\1\41\11\uffff\1\40"),
        DFA.unpack("\1\42\1\43"),
        DFA.unpack("\1\46\6\uffff\1\45\11\uffff\1\44"),
        DFA.unpack("\1\50\20\uffff\1\47"),
        DFA.unpack("\1\51"),
        DFA.unpack("\1\52"),
        DFA.unpack("\1\54\11\uffff\1\53"),
        DFA.unpack("\1\55"),
        DFA.unpack("\1\60\3\uffff\1\61\1\56\1\57"),
        DFA.unpack("\1\62"),
        DFA.unpack("\1\65\6\uffff\1\63\6\uffff\1\64"),
        DFA.unpack("\1\66"),
        DFA.unpack("\1\67"),
        DFA.unpack("\1\70"),
        DFA.unpack("\1\71"),
        DFA.unpack("\1\72"),
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
        DFA.unpack("\1\100"),
        DFA.unpack("\1\101\1\102"),
        DFA.unpack("\1\103"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\105"),
        DFA.unpack("\1\106"),
        DFA.unpack("\1\107\6\uffff\1\110"),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112"),
        DFA.unpack("\1\113"),
        DFA.unpack("\1\114"),
        DFA.unpack("\1\115"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\120"),
        DFA.unpack("\1\121"),
        DFA.unpack("\1\122"),
        DFA.unpack("\1\123"),
        DFA.unpack("\1\124"),
        DFA.unpack("\1\125"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\127"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\132"),
        DFA.unpack("\1\133"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\134"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack("\1\137"),
        DFA.unpack("\1\140"),
        DFA.unpack("\1\141"),
        DFA.unpack(""),
        DFA.unpack("\1\142"),
        DFA.unpack("\1\143"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\1\144\31"
        "\36"),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147"),
        DFA.unpack("\1\150"),
        DFA.unpack("\1\151"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\155"),
        DFA.unpack("\1\156"),
        DFA.unpack("\1\157"),
        DFA.unpack("\1\160"),
        DFA.unpack("\1\161"),
        DFA.unpack(""),
        DFA.unpack("\1\162"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\163"),
        DFA.unpack("\1\164"),
        DFA.unpack("\1\165"),
        DFA.unpack("\1\166"),
        DFA.unpack("\1\167"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\171"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack(""),
        DFA.unpack("\1\176"),
        DFA.unpack("\1\177"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\u0081\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36"
        "\1\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0083"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u0085"),
        DFA.unpack("\1\u0086"),
        DFA.unpack("\1\u0087"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u0089"),
        DFA.unpack("\1\u008a"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\4\36\1\u008b"
        "\25\36"),
        DFA.unpack("\1\u008d"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u0090"),
        DFA.unpack(""),
        DFA.unpack("\1\u0091"),
        DFA.unpack("\1\u0092"),
        DFA.unpack("\1\u0093"),
        DFA.unpack("\1\u0094"),
        DFA.unpack("\1\u0095"),
        DFA.unpack("\1\u0096\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36"
        "\1\uffff\32\36"),
        DFA.unpack("\1\u0098\4\uffff\1\u0099"),
        DFA.unpack(""),
        DFA.unpack("\1\u009a"),
        DFA.unpack(""),
        DFA.unpack("\1\u009b"),
        DFA.unpack("\1\u009c"),
        DFA.unpack("\1\u009d"),
        DFA.unpack(""),
        DFA.unpack("\1\u009e"),
        DFA.unpack("\1\u009f\2\uffff\1\u00a0"),
        DFA.unpack("\1\u00a1\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36"
        "\1\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack("\1\u00a3"),
        DFA.unpack("\1\u00a4\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36"
        "\1\uffff\32\36"),
        DFA.unpack("\1\u00a6"),
        DFA.unpack("\1\u00a7"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u00a9"),
        DFA.unpack("\1\u00aa"),
        DFA.unpack("\1\u00ab"),
        DFA.unpack("\1\u00ac\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36"
        "\1\uffff\32\36"),
        DFA.unpack("\1\u00b1\1\u00b3\4\uffff\1\u00af\3\uffff\1\u00b0\2"
        "\uffff\1\u00ae\1\uffff\1\u00b2\1\u00b5\1\u00b4"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b6"),
        DFA.unpack("\1\u00b7"),
        DFA.unpack("\1\u00b8"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u00ba"),
        DFA.unpack("\1\u00bb"),
        DFA.unpack("\1\u00bc"),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\1\u00be"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00bf"),
        DFA.unpack("\1\u00c0"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c1"),
        DFA.unpack("\1\u00c2"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c3"),
        DFA.unpack("\1\u00c4"),
        DFA.unpack("\1\u00c5\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36"
        "\1\uffff\4\36\1\u00c6\25\36"),
        DFA.unpack("\1\u00cb\1\u00cd\4\uffff\1\u00c9\3\uffff\1\u00ca\2"
        "\uffff\1\u00c8\1\uffff\1\u00cc"),
        DFA.unpack(""),
        DFA.unpack("\1\u00cf\20\uffff\1\u00ce"),
        DFA.unpack("\1\u00d0"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d3\6\uffff\1\u00d1\6\uffff\1\u00d2"),
        DFA.unpack("\1\u00d4"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00d5"),
        DFA.unpack("\1\u00d6"),
        DFA.unpack("\1\u00d7"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d8"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\1\u00dc"),
        DFA.unpack(""),
        DFA.unpack("\1\u00de\11\uffff\1\u00dd"),
        DFA.unpack("\1\u00df"),
        DFA.unpack("\1\u00e0"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u00e2"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e3"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e5\20\uffff\1\u00e4"),
        DFA.unpack("\1\u00e6"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e7\6\uffff\1\u00e8"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00e9"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ea"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00eb"),
        DFA.unpack("\1\u00ec"),
        DFA.unpack("\1\u00ed"),
        DFA.unpack("\1\u00ee\2\uffff\12\36\7\uffff\32\36\4\uffff\1\36"
        "\1\uffff\32\36"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack("\1\u00f2\12\uffff\1\u00f5\1\u00f1\2\uffff\1\u00f3"
        "\2\uffff\1\u00f4"),
        DFA.unpack("\1\u00f6"),
        DFA.unpack("\1\u00f7"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f8"),
        DFA.unpack("\1\u00f9"),
        DFA.unpack(""),
        DFA.unpack("\1\u00fa"),
        DFA.unpack("\1\u00fb"),
        DFA.unpack("\1\u00fc"),
        DFA.unpack(""),
        DFA.unpack("\1\u00fd"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00fe"),
        DFA.unpack("\1\u00ff"),
        DFA.unpack("\1\u0101\17\uffff\1\u0100"),
        DFA.unpack("\1\u0102"),
        DFA.unpack("\1\u0104"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0105\11\uffff\1\u0106"),
        DFA.unpack("\1\u0107\3\uffff\1\u0108"),
        DFA.unpack("\1\u0109"),
        DFA.unpack("\1\u010a"),
        DFA.unpack("\1\u010b"),
        DFA.unpack("\1\u010c"),
        DFA.unpack("\1\u010d"),
        DFA.unpack("\1\u010e"),
        DFA.unpack("\1\u010f"),
        DFA.unpack("\1\u0110"),
        DFA.unpack("\1\u0111"),
        DFA.unpack("\1\u0112"),
        DFA.unpack("\1\u0113"),
        DFA.unpack("\1\u0114"),
        DFA.unpack("\1\u0115"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0116"),
        DFA.unpack("\1\u0117"),
        DFA.unpack("\1\u0118"),
        DFA.unpack("\1\u0119"),
        DFA.unpack("\1\u011a"),
        DFA.unpack("\1\u011b"),
        DFA.unpack("\1\u011c"),
        DFA.unpack("\1\u011d"),
        DFA.unpack("\1\u011e"),
        DFA.unpack("\1\u011f"),
        DFA.unpack("\1\u0120"),
        DFA.unpack("\1\u0121"),
        DFA.unpack("\1\u0122"),
        DFA.unpack("\1\u0123"),
        DFA.unpack("\1\u0124"),
        DFA.unpack("\1\u0125"),
        DFA.unpack("\1\u0126"),
        DFA.unpack("\1\u0127\20\uffff\1\u0128"),
        DFA.unpack("\1\u0129"),
        DFA.unpack("\1\u012a"),
        DFA.unpack("\1\u012b"),
        DFA.unpack("\1\u012c"),
        DFA.unpack("\1\u012d"),
        DFA.unpack("\1\u012e"),
        DFA.unpack("\1\u012f"),
        DFA.unpack("\1\u0130"),
        DFA.unpack("\1\u0131"),
        DFA.unpack("\1\u0132"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u0134"),
        DFA.unpack("\1\u0135"),
        DFA.unpack("\1\u0136"),
        DFA.unpack("\1\u0137"),
        DFA.unpack("\1\u0138\20\uffff\1\u0139"),
        DFA.unpack("\1\u013a"),
        DFA.unpack(""),
        DFA.unpack("\1\u013b"),
        DFA.unpack("\1\u013c"),
        DFA.unpack("\1\u013d"),
        DFA.unpack("\1\u013e"),
        DFA.unpack("\1\u013f"),
        DFA.unpack("\1\u0140"),
        DFA.unpack("\1\u0141"),
        DFA.unpack("\1\u0142"),
        DFA.unpack("\1\u0143"),
        DFA.unpack("\1\u0144"),
        DFA.unpack("\1\u0145"),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u0147"),
        DFA.unpack("\1\u0148"),
        DFA.unpack("\1\u0149"),
        DFA.unpack(""),
        DFA.unpack("\1\u014a"),
        DFA.unpack("\1\u014b"),
        DFA.unpack("\1\u014c"),
        DFA.unpack("\1\u014d"),
        DFA.unpack("\1\u014e"),
        DFA.unpack("\1\u014f"),
        DFA.unpack("\1\u0150"),
        DFA.unpack("\1\u0151"),
        DFA.unpack("\1\u0152"),
        DFA.unpack("\1\u0153"),
        DFA.unpack("\1\u0154"),
        DFA.unpack("\1\u0155"),
        DFA.unpack("\1\u0156"),
        DFA.unpack(""),
        DFA.unpack("\1\u0157"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u015a"),
        DFA.unpack("\1\u015b"),
        DFA.unpack("\1\u015c"),
        DFA.unpack("\1\u015d"),
        DFA.unpack("\1\u015e"),
        DFA.unpack("\1\u015f"),
        DFA.unpack("\1\u0160"),
        DFA.unpack("\1\u0161"),
        DFA.unpack("\1\u0162"),
        DFA.unpack("\1\u0163"),
        DFA.unpack("\1\u0164"),
        DFA.unpack("\1\u0166\20\uffff\1\u0165"),
        DFA.unpack("\1\u0167"),
        DFA.unpack("\1\u0168"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0169"),
        DFA.unpack("\1\u016a"),
        DFA.unpack("\1\u016d\1\uffff\1\u016b\4\uffff\1\u016c"),
        DFA.unpack("\1\u016e"),
        DFA.unpack("\1\u0170"),
        DFA.unpack("\1\u0171"),
        DFA.unpack("\1\u0172"),
        DFA.unpack("\1\u0173"),
        DFA.unpack("\1\u0174"),
        DFA.unpack("\1\u0175"),
        DFA.unpack("\1\u0176"),
        DFA.unpack("\1\u0177"),
        DFA.unpack("\1\u0178"),
        DFA.unpack("\1\u0179"),
        DFA.unpack("\1\u017a"),
        DFA.unpack("\1\u017d\1\uffff\1\u017b\4\uffff\1\u017c"),
        DFA.unpack("\1\u017e"),
        DFA.unpack("\1\u0180"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0181"),
        DFA.unpack("\1\u0182"),
        DFA.unpack("\1\u0183"),
        DFA.unpack("\1\u0184"),
        DFA.unpack("\1\u0185"),
        DFA.unpack("\1\u0186"),
        DFA.unpack("\1\u0187"),
        DFA.unpack("\1\u0188"),
        DFA.unpack("\1\u0189"),
        DFA.unpack("\1\u018a"),
        DFA.unpack("\1\u018b"),
        DFA.unpack("\1\u018c"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u018d\2\uffff\1\u018e"),
        DFA.unpack("\1\u018f"),
        DFA.unpack("\1\u0190"),
        DFA.unpack("\1\u0191"),
        DFA.unpack("\1\u0192"),
        DFA.unpack("\1\u0193"),
        DFA.unpack("\1\u0194"),
        DFA.unpack("\1\u0195"),
        DFA.unpack("\1\u0196"),
        DFA.unpack("\1\u0197"),
        DFA.unpack("\1\u0198"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u019a\2\uffff\1\u019b"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u019c"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u019f"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u01a1"),
        DFA.unpack("\1\u01a2"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u01a4"),
        DFA.unpack("\1\u01a5"),
        DFA.unpack("\1\u01a6"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack(""),
        DFA.unpack("\1\u01a8"),
        DFA.unpack("\1\u01a9"),
        DFA.unpack(""),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\12\36\7\uffff\32\36\4\uffff\1\36\1\uffff\32\36"),
        DFA.unpack("\1\u01ac"),
        DFA.unpack(""),
        DFA.unpack("\1\u01ad"),
        DFA.unpack("\1\u01ae"),
        DFA.unpack(""),
        DFA.unpack(""),
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
